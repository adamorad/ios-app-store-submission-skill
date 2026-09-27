#!/usr/bin/env python3
"""Lightweight repository checks that run on any platform."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
required = ["SKILL.md", "README.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md", "INSTRUCTIONS.md"]
missing = [name for name in required if not (root / name).exists()]
if missing:
    print("Missing required files:", ", ".join(missing))
    sys.exit(1)

skill = (root / "SKILL.md").read_text()
if not re.search(r"^---\nname: [^\n]+\ndescription: [^\n]+\n---", skill, re.M):
    print("SKILL.md front matter is invalid")
    sys.exit(1)

readme = (root / "README.md").read_text()
for target in re.findall(r"\[[^]]+\]\(([^)#]+)", readme):
    if target.startswith(("http://", "https://", "mailto:")):
        continue
    if not (root / target).exists():
        print(f"README link target does not exist: {target}")
        sys.exit(1)

for script in (root / "scripts").glob("*.sh"):
    text = script.read_text()
    if "set -" not in text:
        print(f"Shell script should enable strict mode: {script}")
        sys.exit(1)

print("Repository validation passed")
