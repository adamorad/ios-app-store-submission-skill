#!/usr/bin/env python3
"""Validate the required scalar fields in the example app config without extra dependencies."""
from pathlib import Path
import re
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else "app-config.yml")
if not path.exists():
    print(f"Config not found: {path}")
    sys.exit(2)
text = path.read_text()
required = {
    "name": r"^\s+name:\s*\"([^\"]+)\"",
    "bundle_id": r"^\s+bundle_id:\s*\"([^\"]+)\"",
    "team_id": r"^\s+team_id:\s*\"([^\"]+)\"",
    "scheme": r"^\s+scheme:\s*\"([^\"]+)\"",
    "marketing_version": r"^\s+marketing_version:\s*\"([^\"]+)\"",
    "build_number": r"^\s+build_number:\s*\"([^\"]+)\"",
}
errors = []
for key, pattern in required.items():
    match = re.search(pattern, text, re.M)
    if not match or not match.group(1).strip():
        errors.append(f"{key} is empty or missing")

bundle = re.search(required["bundle_id"], text, re.M)
if bundle and not re.fullmatch(r"[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+", bundle.group(1)):
    errors.append("bundle_id must use reverse-domain notation")
team = re.search(required["team_id"], text, re.M)
if team and not re.fullmatch(r"[A-Z0-9]{10}", team.group(1)):
    errors.append("team_id should be a 10-character Apple Team ID")
version = re.search(required["marketing_version"], text, re.M)
if version and not re.fullmatch(r"\d+(?:\.\d+){1,2}", version.group(1)):
    errors.append("marketing_version must look like 1.0 or 1.0.0")
build = re.search(required["build_number"], text, re.M)
if build and not build.group(1).isdigit():
    errors.append("build_number must be numeric")

if errors:
    print("Config validation failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"Config validation passed: {path}")
