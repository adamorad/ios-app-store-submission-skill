#!/usr/bin/env python3
"""Generate a factual Markdown release report from an iOS project checkout."""
from pathlib import Path
import datetime as dt
import plistlib
import subprocess
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
out = Path(sys.argv[2] if len(sys.argv) > 2 else root / "release-report.md").resolve()

def run(*args):
    try:
        return subprocess.check_output(args, cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "unknown"

plist_path = next(root.rglob("Info.plist"), None)
values = {}
if plist_path:
    try:
        values = plistlib.loads(plist_path.read_bytes())
    except Exception:
        pass
project = next(root.rglob("*.xcworkspace"), None) or next(root.rglob("*.xcodeproj"), None)
lines = [
    "# iOS Release Report",
    "",
    f"Generated: {dt.datetime.now(dt.timezone.utc).isoformat()}",
    "",
    "| Field | Value |",
    "| --- | --- |",
    f"| Project | `{project.relative_to(root) if project else 'unknown'}` |",
    f"| Bundle ID | `{values.get('CFBundleIdentifier', 'unknown')}` |",
    f"| Marketing version | `{values.get('CFBundleShortVersionString', 'unknown')}` |",
    f"| Build number | `{values.get('CFBundleVersion', 'unknown')}` |",
    f"| Git commit | `{run('git', 'rev-parse', 'HEAD')}` |",
    f"| Git branch | `{run('git', 'branch', '--show-current')}` |",
    "",
    "## Human checks still required",
    "",
    "- [ ] Release signing uses Apple Distribution and get-task-allow is false.",
    "- [ ] Privacy answers match the shipped binary, SDKs, backend, and policy.",
    "- [ ] Support and privacy URLs are publicly reachable.",
    "- [ ] The processed build is attached to the intended App Store version.",
    "- [ ] TestFlight testing completed on supported devices.",
    "- [ ] Final App Review submission was explicitly authorized.",
]
out.write_text("\n".join(lines) + "\n")
print(out)
