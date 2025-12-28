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


def test_sanitize_api_key_case_insensitive():
    """Test that API keys are redacted regardless of case."""
    error_text = "Error: https://api.example.com?KEY=AIzaSyABC123&Key=XYZ789&key=secret"
    result = sanitize_error_response(error_text)

    assert "AIzaSyABC123" not in result
    assert "XYZ789" not in result
    assert "secret" not in result
    assert result.count("key=REDACTED") == 3  # All three variants


def test_sanitize_in_exception_messages():
    """Test that sanitization works for exception-like strings."""
    exception_msg = "Connection failed: GET https://api.example.com?key=SECRET failed"
    result = sanitize_error_response(exception_msg)

    assert "SECRET" not in result
    assert "key=REDACTED" in result
