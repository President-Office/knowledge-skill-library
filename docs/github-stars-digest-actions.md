# GitHub Stars Digest Actions

The starred-project digest runs in GitHub Actions. The local Codex cron is not
part of the runtime path.

## Schedule

- Scheduled run: Monday at `01:00 UTC`, which is Monday at `09:00` in
  `Asia/Shanghai`.
- Manual run: use **Actions -> GitHub Stars Digest -> Run workflow**.

## Permissions and secrets

The workflow uses two different credentials:

1. `STARS_GITHUB_TOKEN` is an Actions secret used only for reading the
   `PeterKZhao` starred endpoint and metadata for private starred repositories.
   It must be a token that can read the user's starred list and the relevant
   private repository metadata.
2. The built-in `GITHUB_TOKEN` is used by checkout, the final push to `main`,
   and the remote-file verification call. Its workflow permission is limited
   to `contents: write`.

Never write either token into the repository, digest, logs, or generated
artifacts.

## Public-report boundary

This repository is public. The action may read private starred repositories,
but it writes only aggregate private-project counts. Private repository names,
URLs, descriptions, releases, commits, Issues, and PRs are intentionally
omitted from `00-inbox/github-stars-digest.md`.

## Update boundary

The action replaces only the section between:

```text
<!-- BEGIN GITHUB_STARS_ACTIONS -->
<!-- END GITHUB_STARS_ACTIONS -->
```

The curated report above that section remains human-owned. If the generated
snapshot has no material change, the workflow does not create a commit.
