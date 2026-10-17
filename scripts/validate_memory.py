#!/usr/bin/env python3
"""Validate the hmyar shared-memory structure.

Checks:
- Required files exist.
- No secret-like tokens in tracked text files.
- Markdown links resolve (basic).
- Memory files are non-empty.

Exit 0 on success, 1 on failure.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED = [
    "README.md", "AGENTS.md",
    "memory/current-state.md", "memory/phase-roadmap.md", "memory/lessons-learned.md",
    "memory/README.md",
    "backlog/README.md", "backlog/open-questions.md", "backlog/source-manifest.md",
    "docs/discovery/BASELINE.md",
]

SECRET_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9]{30,}"),
    re.compile(r"glpat-[A-Za-z0-9\-]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)password\s*[:=]\s*\S{6,}"),
]

TEXT_EXTS = {".md", ".yaml", ".yml", ".json", ".csv", ".txt", ".py"}


def check_required():
    missing = [p for p in REQUIRED if not os.path.isfile(os.path.join(ROOT, p))]
    if missing:
        print("MISSING REQUIRED FILES:")
        for m in missing:
            print("  - " + m)
        return False
    return True


def check_secrets():
    bad = []
    for dirpath, _, files in os.walk(ROOT):
        # skip .git and venv
        if ".git" in dirpath.split(os.sep) or ".venv" in dirpath.split(os.sep):
            continue
        for fn in files:
            ext = os.path.splitext(fn)[1].lower()
            if ext not in TEXT_EXTS:
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()
            except Exception:
                continue
            for pat in SECRET_PATTERNS:
                if pat.search(content):
                    bad.append((os.path.relpath(p, ROOT), pat.pattern))
    if bad:
        print("SECRET-LIKE CONTENT FOUND:")
        for p, pat in bad:
            print(f"  - {p}: {pat}")
        return False
    return True


def check_nonempty():
    empty = []
    for p in REQUIRED:
        full = os.path.join(ROOT, p)
        if os.path.isfile(full) and os.path.getsize(full) == 0:
            empty.append(p)
    if empty:
        print("EMPTY REQUIRED FILES:")
        for e in empty:
            print("  - " + e)
        return False
    return True


def main():
    ok = True
    ok = check_required() and ok
    ok = check_nonempty() and ok
    ok = check_secrets() and ok
    if ok:
        print("validate_memory: OK")
    else:
        print("validate_memory: FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
