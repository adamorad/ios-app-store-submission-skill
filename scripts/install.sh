#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${IOS_APP_STORE_SKILL_REPO:-https://github.com/adamorad/ios-app-store-submission-skill.git}"
AGENT="${1:-codex}"
case "$AGENT" in
  codex) target="${CODEX_HOME:-$HOME/.codex}/skills/ios-app-store-submission" ;;
  claude) target="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}/ios-app-store-submission" ;;
  project) target="${2:-.}/.agent-skills/ios-app-store-submission" ;;
  *) echo "Usage: $0 [codex|claude|project [project-root]]" >&2; exit 2 ;;
esac

mkdir -p "$(dirname "$target")"
if [[ -d "$target/.git" ]]; then
  git -C "$target" pull --ff-only
else
  if [[ -e "$target" ]]; then
    echo "Refusing to overwrite existing non-git directory: $target" >&2
    exit 1
  fi
  git clone "$REPO_URL" "$target"
fi
echo "Installed ios-app-store-submission at $target"
