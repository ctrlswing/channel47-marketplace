# File: plugins/nano-banana/tests/test_security.py
import pytest
import re
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from nanobanana_mcp import sanitize_error_response


def test_sanitize_api_key_from_url():
    """Test that API keys in URLs are redacted."""
    error_text = "Error: https://api.example.com?key=AIzaSyABC123XYZ&param=value"
    result = sanitize_error_response(error_text)

    assert "AIzaSyABC123XYZ" not in result
    assert "key=REDACTED" in result
    assert "param=value" in result


def test_sanitize_api_key_from_multiline():
    """Test sanitization across multiple lines."""
    error_text = """
    Request failed:
    URL: https://api.example.com?key=AIzaSyABC123XYZ
    Status: 403
    """
    result = sanitize_error_response(error_text)

    assert "AIzaSyABC123XYZ" not in result
    assert "key=REDACTED" in result


def test_sanitize_truncates_long_errors():
    """Test that error responses are truncated to prevent leakage."""
    error_text = "x" * 10000
    result = sanitize_error_response(error_text)

    assert len(result) <= 500
    assert "[TRUNCATED]" in result or len(result) == 500
