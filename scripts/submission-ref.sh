#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ] || [ $# -gt 2 ]; then
  echo "usage: $0 owner/repo [git_dir]" >&2
  exit 1
fi

repo="$1"
git_dir="${2:-.}"
sha="$(git -C "$git_dir" rev-parse HEAD)"

printf 'submission_ref=%s@%s\n' "$repo" "$sha"
printf 'commit_url=https://github.com/%s/commit/%s\n' "$repo" "$sha"
