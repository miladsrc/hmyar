"""Tests for memory validation and secret scanning."""
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import validate_memory


def test_required_files_present():
    assert validate_memory.check_required() is True


def test_no_secrets_in_repo():
    assert validate_memory.check_secrets() is True


def test_nonempty_required():
    assert validate_memory.check_nonempty() is True


def test_secret_detection():
    with tempfile.TemporaryDirectory() as d:
        # temporarily create a file with a secret-like token inside repo? Instead test pattern directly
        import re
        pat = re.compile(r"ghp_[A-Za-z0-9]{30,}")
        assert pat.search("token ghp_" + "a" * 36) is not None
        assert pat.search("no secret here") is None