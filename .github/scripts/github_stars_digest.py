"""Generate a complete, public-safe report from the user's GitHub stars."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from zoneinfo import ZoneInfo


API_VERSION = "2022-11-28"
PAGE_SIZE = 100
BEIJING = ZoneInfo("Asia/Shanghai")
UTC = timezone.utc
CATEGORY_RULES = (
    (
        "AI 与 Agent",
        (
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "generative ai",
            "llm",
            "agent",
            "gpt",
            "mcp",
            "rag",
            "embedding",
            "transformer",
            "neural network",
            "claude",
            "skill",
        ),
    ),
    (
        "金融与量化",
        ("finance", "financial", "trading", "quant", "stock", "investment", "crypto"),
    ),
    (
        "数据与研究",
        ("data", "database", "analytics", "research", "search", "crawler", "knowledge"),
    ),
    (
        "开发工具与基础设施",
        ("developer", "development", "framework", "library", "cli", "api", "vscode", "git"),
    ),
    (
        "学习与资料",
        ("awesome", "book", "course", "tutorial", "guide", "learning", "study", "interview"),
    ),
)
CATEGORY_NAMES = tuple(name for name, _ in CATEGORY_RULES) + ("其他",)


class GitHubApiError(RuntimeError):
    """An API failure that should block a write."""


def env_required(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise GitHubApiError(f"Required environment variable is missing: {name}")
    return value


PRIVATE_NAMES: set[str] = set()


def redacted_path(path: str) -> str:
    result = path
    for name in PRIVATE_NAMES:
        result = result.replace(name, "<private-repository>")
    return result


def api_json(
    path: str,
    *,
    params: dict[str, Any] | None = None,
    accept: str = "application/vnd.github+json",
    allow_not_found: bool = False,
) -> Any:
    query = f"?{urlencode(params)}" if params else ""
    endpoint = f"{path.lstrip('/')}{query}"
    command = [
        "gh",
        "api",
        endpoint,
        "--header",
        f"Accept: {accept}",
        "--header",
        f"X-GitHub-Api-Version: {API_VERSION}",
    ]
    for attempt in range(3):
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=60,
                check=False,
            )
        except subprocess.TimeoutExpired as error:
            if attempt < 2:
                time.sleep(2**attempt)
                continue
            raise GitHubApiError(
                f"GitHub API timed out at {redacted_path(path)} after retries."
            ) from error
        except OSError as error:
            raise GitHubApiError(
                f"Could not run GitHub CLI at {redacted_path(path)}: {error}"
            ) from error
        if result.returncode == 0:
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError as error:
                raise GitHubApiError(
                    f"GitHub API returned invalid JSON at {redacted_path(path)}"
                ) from error

        error_text = result.stderr.strip()
        if allow_not_found and "HTTP 404" in error_text:
            return None
        retryable = any(
            f"HTTP {code}" in error_text for code in (429, 500, 502, 503, 504)
        ) or any(
            message in error_text.lower()
            for message in (
                "unexpected eof",
                "connection reset",
                "tls handshake timeout",
                "timeout awaiting response headers",
            )
        )
        if retryable:
            if attempt < 2:
                time.sleep(2**attempt)
                continue
        raise GitHubApiError(
            f"GitHub API failed at {redacted_path(path)}: {error_text[:240]}"
        )

    raise GitHubApiError(f"GitHub API failed after retries at {redacted_path(path)}")


def load_starred() -> list[dict[str, Any]]:
    starred: list[dict[str, Any]] = []
    page = 1
    while True:
        items = api_json(
            "user/starred",
            params={"page": page, "per_page": PAGE_SIZE},
            accept="application/vnd.github.star+json",
        )
        if not isinstance(items, list):
            raise GitHubApiError("GitHub starred endpoint returned an unexpected payload.")
        for item in items:
            repo = item.get("repo") if isinstance(item, dict) else None
            if not isinstance(repo, dict):
                repo = item if isinstance(item, dict) else {}
            full_name = repo.get("full_name")
            if not full_name:
                continue
            starred.append(
                {
                    "repo": repo,
                    "starred_at": item.get("starred_at")
                    if isinstance(item, dict)
                    else None,
                }
            )
            if repo.get("private"):
                PRIVATE_NAMES.add(full_name)
        if len(items) < PAGE_SIZE:
            return starred
        page += 1


def parse_timestamp(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)
    except ValueError:
        return None


def iso(value: datetime | None) -> str:
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z") if value else ""


def latest_commit(full_name: str) -> dict[str, str]:
    commits = api_json(
        f"repos/{full_name}/commits",
        params={"per_page": 1},
        allow_not_found=True,
    )
    if not commits or not isinstance(commits, list):
        return {}
    commit = commits[0]
    commit_info = commit.get("commit", {})
    author = commit_info.get("author", {}) if isinstance(commit_info, dict) else {}
    message = str(commit_info.get("message", "")).splitlines()[0][:120]
    return {
        "sha": str(commit.get("sha", ""))[:8],
        "date": str(author.get("date", "")),
        "message": message,
    }


def latest_release(full_name: str) -> dict[str, str]:
    release = api_json(
        f"repos/{full_name}/releases/latest",
        allow_not_found=True,
    )
    if not isinstance(release, dict):
        return {}
    return {
        "tag": str(release.get("tag_name", "")),
        "date": str(release.get("published_at") or release.get("created_at") or ""),
    }


def recent_issue_activity(full_name: str, since: datetime) -> tuple[int, int]:
    items = api_json(
        f"repos/{full_name}/issues",
        params={
            "state": "all",
            "since": iso(since),
            "per_page": PAGE_SIZE,
        },
        allow_not_found=True,
    )
    if not isinstance(items, list):
        return 0, 0
    issues = sum(1 for item in items if "pull_request" not in item)
    pull_requests = len(items) - issues
    return issues, pull_requests


def inspect_repository(item: dict[str, Any], window_start: datetime) -> dict[str, Any]:
    repo = item["repo"]
    full_name = str(repo["full_name"])
    private = bool(repo.get("private"))
    starred_at = parse_timestamp(item.get("starred_at"))
    pushed_at = parse_timestamp(repo.get("pushed_at"))
    updated_at = parse_timestamp(repo.get("updated_at"))
    recent_star = bool(starred_at and starred_at >= window_start)
    candidate = bool(
        recent_star
        or (pushed_at and pushed_at >= window_start)
        or (updated_at and updated_at >= window_start)
    )
    commit = latest_commit(full_name) if candidate else {}
    release = latest_release(full_name) if candidate else {}
    issue_count, pr_count = (
        recent_issue_activity(full_name, window_start) if candidate else (0, 0)
    )
    release_at = parse_timestamp(release.get("date"))
    commit_at = parse_timestamp(commit.get("date"))
    recent_activity = bool(
        candidate
        or (release_at and release_at >= window_start)
        or (commit_at and commit_at >= window_start)
        or issue_count
        or pr_count
    )
    return {
        "repo": repo,
        "private": private,
        "starred_at": item.get("starred_at") or "",
        "recent_star": recent_star,
        "recent_activity": recent_activity,
        "commit": commit,
        "release": release,
        "issues": issue_count,
        "pull_requests": pr_count,
    }


def collect_snapshot(now: datetime) -> dict[str, Any]:
    user = api_json("user")
    account = user.get("login") if isinstance(user, dict) else None
    if account != "PeterKZhao":
        raise GitHubApiError(
            f"Expected starred account PeterKZhao, received {account or 'unknown'}."
        )
    starred = load_starred()
    window_start = now.astimezone(UTC) - timedelta(days=7)
    public: list[dict[str, Any]] = []
    private_new = 0
    private_active = 0

    with ThreadPoolExecutor(max_workers=8) as executor:
        inspected = executor.map(
            lambda item: inspect_repository(item, window_start),
            starred,
        )

    for details in inspected:
        repo = details["repo"]
        full_name = str(repo["full_name"])
        if details["private"]:
            if details["recent_star"]:
                private_new += 1
            if details["recent_activity"]:
                private_active += 1
            continue

        public.append(
            {
                "name": full_name,
                "url": repo.get("html_url", f"https://github.com/{full_name}"),
                "description": str(repo.get("description") or "").replace("\n", " ")[:160],
                "language": repo.get("language") or "n/a",
                "stars": int(repo.get("stargazers_count") or 0),
                "topics": repo.get("topics") or [],
                "archived": bool(repo.get("archived")),
                "starred_at": details["starred_at"],
                "recent_star": details["recent_star"],
                "recent_activity": details["recent_activity"],
                "pushed_at": repo.get("pushed_at") or "",
                "commit": details["commit"],
                "release": details["release"],
                "issues": details["issues"],
                "pull_requests": details["pull_requests"],
            }
        )

    public.sort(key=lambda repo: repo.get("name", "").lower())
    new_public = sorted(
        (repo for repo in public if repo["recent_star"]),
        key=lambda repo: repo.get("starred_at", ""),
        reverse=True,
    )
    active_public = sorted(
        (repo for repo in public if repo["recent_activity"]),
        key=lambda repo: (
            repo.get("commit", {}).get("date", ""),
            repo.get("pushed_at", ""),
            repo.get("starred_at", ""),
        ),
        reverse=True,
    )

    return {
        "account": account,
        "checked_at": now.astimezone(BEIJING).strftime("%Y-%m-%d %H:%M:%S %Z"),
        "window_start": window_start.astimezone(BEIJING).strftime("%Y-%m-%d"),
        "total": len(starred),
        "public_total": len(public),
        "private_total": len(starred) - len(public),
        "private_new": private_new,
        "private_active": private_active,
        "new_public": new_public,
        "active_public_total": len(active_public),
        "active_public": active_public[:40],
        "public": public,
    }


def classify_repository(repo: dict[str, Any]) -> str:
    searchable = " ".join(
        [
            str(repo.get("name", "")),
            str(repo.get("description", "")),
            " ".join(str(topic) for topic in repo.get("topics", [])),
        ]
    ).lower()
    for category, keywords in CATEGORY_RULES:
        if any(keyword in searchable for keyword in keywords):
            return category
    return "其他"


def markdown_cell(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def render_report(snapshot: dict[str, Any]) -> str:
    public = snapshot["public"]
    category_groups = {
        category: [repo for repo in public if classify_repository(repo) == category]
        for category in CATEGORY_NAMES
    }
    languages: dict[str, int] = {}
    for repo in public:
        language = str(repo.get("language") or "n/a")
        languages[language] = languages.get(language, 0) + 1

    lines = [
        "# GitHub Stars Digest",
        "",
        f"> 账号：[`{snapshot['account']}`](https://github.com/{snapshot['account']}?tab=stars)",
        f"> 更新时间：{snapshot['checked_at']}",
        f"> 统计窗口：最近 7 天（自 {snapshot['window_start']} 起；时间以 GitHub API 返回值为准）。",
        "",
        "## 总览",
        "",
        f"- Star 总数：{snapshot['total']}（公开 {snapshot['public_total']}，私有 {snapshot['private_total']}）。",
        f"- 最近 7 天新增：公开 {len(snapshot['new_public'])} 个，私有 {snapshot['private_new']} 个（私有名称不公开）。",
        f"- 最近 7 天有活动：公开 {snapshot['active_public_total']} 个，私有 {snapshot['private_active']} 个（私有项目仅统计数量）。",
        "",
        "### 自动分类",
        "",
    ]
    for category, repos in category_groups.items():
        lines.append(f"- {category}：{len(repos)}")
    lines.extend(["", "### 主要语言", ""])
    if languages:
        for language, count in sorted(
            languages.items(), key=lambda item: (-item[1], item[0].lower())
        )[:10]:
            lines.append(f"- {language}：{count}")
    else:
        lines.append("- 无公开项目")

    lines.extend(["", "## 最近新增的公开 Star", ""])
    if snapshot["new_public"]:
        for repo in snapshot["new_public"]:
            starred_at = parse_timestamp(repo.get("starred_at"))
            date = (
                starred_at.astimezone(BEIJING).strftime("%Y-%m-%d")
                if starred_at
                else "日期未知"
            )
            lines.append(f"- {date} [{repo['name']}]({repo['url']})")
    else:
        lines.append("- 无")

    lines.extend(["", "## 最近活动的公开项目", ""])
    if snapshot["active_public"]:
        lines.append(
            f"> 展示最近活动的前 {len(snapshot['active_public'])} 个；符合近 7 天活动条件的共 {snapshot['active_public_total']} 个。"
        )
        lines.append("")
        lines.extend(
            [
                "| 项目 | 最近提交 | 最新 Release | 近 7 天 Issue/PR |",
                "| --- | --- | --- | --- |",
            ]
        )
        for repo in snapshot["active_public"]:
            commit = repo["commit"]
            release = repo["release"]
            commit_text = (
                f"{commit.get('date', '')[:10]} "
                f"`{commit.get('sha', 'n/a')}`"
                if commit
                else "无"
            )
            release_text = (
                f"`{release.get('tag', 'n/a')}` {release.get('date', '')[:10]}"
                if release
                else "无"
            )
            activity = f"{repo['issues']} / {repo['pull_requests']}"
            lines.append(
                f"| [{repo['name']}]({repo['url']}) | {commit_text} | "
                f"{release_text} | {activity} |"
            )
    else:
        lines.append("- 无")

    lines.extend(["", "## 全部公开 Star 仓库", ""])
    lines.append(
        "> 按仓库名称、描述和 GitHub topics 进行规则分类，仅作浏览导航；未匹配到规则的项目归入“其他”。"
    )
    for category, repos in category_groups.items():
        lines.extend(["", f"### {category}（{len(repos)}）", ""])
        if not repos:
            lines.append("- 无")
            continue
        lines.extend(
            [
                "| 仓库 | 描述 | 语言 | Stars | Star 日期 | Topics | 状态 |",
                "| --- | --- | --- | ---: | --- | --- | --- |",
            ]
        )
        for repo in repos:
            starred_at = parse_timestamp(repo.get("starred_at"))
            date = (
                starred_at.astimezone(BEIJING).strftime("%Y-%m-%d")
                if starred_at
                else "未知"
            )
            topics = ", ".join(str(topic) for topic in repo.get("topics", [])) or "—"
            status = "Archived" if repo.get("archived") else "Active"
            lines.append(
                f"| [{repo['name']}]({repo['url']}) | "
                f"{markdown_cell(repo.get('description')) or '—'} | "
                f"{markdown_cell(repo.get('language')) or 'n/a'} | "
                f"{repo.get('stars', 0)} | {date} | "
                f"{markdown_cell(topics)} | {status} |"
            )

    lines.extend(
        [
            "",
            "## 数据来源与口径",
            "",
            "- Star 列表及 Star 时间：GitHub REST API `user/starred`。",
            "- 仓库描述、语言、topics、Stars 数和归档状态：GitHub 仓库元数据。",
            "- 活动信号：最近 7 天内的 Star、仓库更新/推送、提交、Release、Issue 或 PR；仅对候选活跃仓库查询详细记录。",
            "- 私有仓库名称、链接和详细元数据不会写入此公开报告；只输出私有项目总数及近 7 天统计。",
            "- 本报告每次运行均整体重新生成；分类为基于公开仓库元数据的规则分类，不代表人工评价或优先级。",
        ]
    )
    return "\n".join(lines) + "\n"


def normalize_generated_block(block: str) -> str:
    lines = block.replace("\r\n", "\n").splitlines()
    return "\n".join(
        re.sub(
            r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]{2,5}",
            "<normalized>",
            line,
        )
        for line in lines
    )


def replace_report(content: str, generated: str) -> tuple[str, bool]:
    if normalize_generated_block(content) == normalize_generated_block(generated):
        return content, False
    return generated, True


def write_summary(snapshot: dict[str, Any], changed: bool) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    text = "\n".join(
        [
            "## GitHub Stars Digest",
            "",
            f"- Status: {'updated' if changed else 'no change'}",
            f"- Starred checked: {snapshot['total']} "
            f"(public {snapshot['public_total']}, private {snapshot['private_total']})",
            f"- Public activity rows: {snapshot['active_public_total']}",
            f"- Private details: omitted from public report",
        ]
    )
    Path(summary_path).write_text(text + "\n", encoding="utf-8")


def main() -> int:
    if not os.environ.get("GH_TOKEN", "").strip():
        raise GitHubApiError(
            "STARS_GITHUB_TOKEN is not configured; set it as the GH_TOKEN workflow secret."
        )
    repository = env_required("DIGEST_REPOSITORY")
    if repository != "President-Office/knowledge-skill-library":
        raise GitHubApiError(
            f"Unexpected digest repository: {repository}; refusing to write."
        )
    digest_path = Path(env_required("DIGEST_PATH"))
    if not digest_path.is_file():
        raise GitHubApiError(f"Digest file does not exist: {digest_path}")

    now = datetime.now(UTC)
    snapshot = collect_snapshot(now)
    generated = render_report(snapshot)
    current = digest_path.read_text(encoding="utf-8")
    updated, changed = replace_report(current, generated)
    if changed:
        digest_path.write_text(updated, encoding="utf-8")
        print("GitHub Stars Digest: snapshot changed.")
    else:
        print("GitHub Stars Digest: no material snapshot change.")
    write_summary(snapshot, changed)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except GitHubApiError as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        raise SystemExit(1)
