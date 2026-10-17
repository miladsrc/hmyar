#!/usr/bin/env python3
"""Scan tracked text files for secret-like content. Run before committing."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from validate_memory import check_secrets

if __name__ == "__main__":
    ok = check_secrets()
    print("check_secrets: " + ("OK" if ok else "FAILED"))
    sys.exit(0 if ok else 1)
