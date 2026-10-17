#!/usr/bin/env python3
"""Check relative markdown links resolve to existing files."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    broken = []
    for dirpath, _, files in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep) or ".venv" in dirpath.split(os.sep):
            continue
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            with open(p, "r", encoding="utf-8", errors="replace") as f:
                text = f.read()
            for m in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", text):
                link = m.group(2).strip()
                if link.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = os.path.normpath(os.path.join(os.path.dirname(p), link.split("#")[0]))
                if not os.path.exists(target):
                    broken.append((os.path.relpath(p, ROOT), link))
    if broken:
        print("BROKEN LINKS:")
        for p, link in broken:
            print(f"  - {p}: {link}")
        sys.exit(1)
    print("check_links: OK")


if __name__ == "__main__":
    main()
