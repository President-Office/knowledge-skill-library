import importlib.util
import json
import unittest
from pathlib import Path
from subprocess import CompletedProcess
from unittest.mock import patch


SCRIPT_PATH = Path(__file__).with_name("github_stars_digest.py")
SPEC = importlib.util.spec_from_file_location("github_stars_digest", SCRIPT_PATH)
assert SPEC and SPEC.loader
digest = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(digest)


class RenderReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.snapshot = {
            "account": "PeterKZhao",
            "checked_at": "2026-10-24 17:00:00 CST",
            "window_start": "2026-10-17",
            "total": 3,
            "public_total": 2,
            "private_total": 1,
            "private_new": 0,
            "private_active": 0,
            "new_public": [],
            "active_public_total": 0,
            "active_public": [],
            "public": [
                {
                    "name": "owner/agent-kit",
                    "url": "https://github.com/owner/agent-kit",
                    "description": "Agent tools | samples",
                    "language": "Python",
                    "stars": 42,
                    "topics": ["agent"],
                    "archived": False,
                    "starred_at": "2026-10-20T00:00:00Z",
                },
                {
                    "name": "owner/quant-notes",
                    "url": "https://github.com/owner/quant-notes",
                    "description": "Quant research",
                    "language": "Python",
                    "stars": 12,
                    "topics": ["finance"],
                    "archived": True,
                    "starred_at": "2026-10-18T00:00:00Z",
                },
            ],
        }

    def test_report_contains_all_public_repositories_and_current_totals(self) -> None:
        report = digest.render_report(self.snapshot)

        self.assertIn("Star 总数：3（公开 2，私有 1）", report)
        self.assertIn("AI 与 Agent：1", report)
        self.assertIn("金融与量化：1", report)
        self.assertIn("[owner/agent-kit]", report)
        self.assertIn("[owner/quant-notes]", report)
        self.assertIn("Agent tools \\| samples", report)
        self.assertIn("Archived", report)
        self.assertNotIn("private-repo", report)
        self.assertNotIn("BEGIN GITHUB_STARS_ACTIONS", report)

    def test_report_replaces_stale_human_content(self) -> None:
        report = digest.render_report(self.snapshot)
        updated, changed = digest.replace_report(
            "# Old report\n\nStale count: 101\n", report
        )

        self.assertTrue(changed)
        self.assertEqual(updated, report)
        self.assertNotIn("Stale count", updated)

    def test_same_day_timestamp_only_change_does_not_create_commit(self) -> None:
        first = digest.render_report(self.snapshot)
        later_snapshot = dict(self.snapshot)
        later_snapshot["checked_at"] = "2026-10-24 17:30:00 CST"
        second = digest.render_report(later_snapshot)

        updated, changed = digest.replace_report(first, second)

        self.assertFalse(changed)
        self.assertEqual(updated, first)


class ApiRetryTests(unittest.TestCase):
    def test_transient_eof_is_retried_before_returning_response(self) -> None:
        transient = CompletedProcess(
            args=["gh", "api"], returncode=1, stdout="", stderr="unexpected EOF"
        )
        success = CompletedProcess(
            args=["gh", "api"], returncode=0, stdout=json.dumps({"ok": True}), stderr=""
        )

        with (
            patch.object(digest.subprocess, "run", side_effect=[transient, success]) as run,
            patch.object(digest.time, "sleep"),
        ):
            response = digest.api_json("user")

        self.assertEqual(response, {"ok": True})
        self.assertEqual(run.call_count, 2)

    def test_timeout_is_retried_and_reported_as_api_error(self) -> None:
        timeout = digest.subprocess.TimeoutExpired(["gh", "api"], timeout=60)

        with (
            patch.object(digest.subprocess, "run", side_effect=timeout) as run,
            patch.object(digest.time, "sleep"),
            self.assertRaisesRegex(digest.GitHubApiError, "timed out"),
        ):
            digest.api_json("user")

        self.assertEqual(run.call_count, 3)


if __name__ == "__main__":
    unittest.main()
