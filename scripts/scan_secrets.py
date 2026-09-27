#!/usr/bin/env python3
"""Scan tracked text files for obvious credentials and signing artifacts."""
from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
try:
    files = subprocess.check_output(["git", "-C", str(root), "ls-files", "-co", "--exclude-standard"], text=True).splitlines()
except Exception:
    files = [str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()]
patterns = [
    (re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"), "private key material"),
    (re.compile(r"AuthKey_[A-Za-z0-9]+\.p8"), "App Store Connect key filename"),
    (re.compile(r"(?i)(api[_-]?key|private[_-]?key|secret|password)\s*[:=]\s*['\"][^'\"]{12,}"), "credential assignment"),
    (re.compile(r"(?i)ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}"), "token-like value"),
]
findings = []
for name in files:
    path = root / name
    if path.suffix in {".png", ".jpg", ".jpeg", ".gif", ".zip", ".mobileprovision", ".p12", ".cer", ".ipa"}:
        findings.append((name, 1, "binary/signing artifact"))
        continue
    try:
        text = path.read_text(errors="ignore")
    except Exception:
        continue
    for number, line in enumerate(text.splitlines(), 1):
        for pattern, label in patterns:
            if pattern.search(line) and "placeholder" not in line.lower() and "example" not in line.lower():
                findings.append((name, number, label))
if findings:
    print("Potential secrets or signing artifacts found:")
    for finding in findings:
        print(f"- {finding[0]}:{finding[1]} ({finding[2]})")
    sys.exit(1)
print("Secret scan passed")
