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

## Generated report and privacy

This repository is public. The action may read private starred repositories,
but it regenerates the entire `00-inbox/github-stars-digest.md` from the
current API response on each run. Private repository names, URLs,
descriptions, releases, commits, Issues, and PRs are omitted; only private
project counts are included.

Public repositories are automatically grouped using their names, descriptions,
and GitHub topics. These rule-based groups are for navigation, not editorial
recommendations. The generated report includes the complete public starred
repository list so its counts and contents come from the same scan.

The previous hand-curated report is replaced on the first run of this
generator version. The workflow runs focused generator tests before scanning.
If the generated report has no material change, it does not create a commit.
