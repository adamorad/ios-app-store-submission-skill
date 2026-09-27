#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"
echo "Local release status"
if [[ -d "$HOME/Library/Developer/Xcode/Archives" ]]; then
  find "$HOME/Library/Developer/Xcode/Archives" -type d -name '*.xcarchive' -print | sort | tail -10
else
  echo "No local Xcode Archives directory found."
fi
cat <<'MSG'

App Store Connect status is account-scoped and must be checked in App Store Connect or through an authenticated API client.
Record the exact marketing version, build number, processing state, TestFlight state, and App Review state.
See references/status.md for the safe monitoring workflow.
MSG
