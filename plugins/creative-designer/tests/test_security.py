# File: plugins/creative-designer/tests/test_security.py
import pytest
import re
import sys
import tempfile
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from nanobanana_mcp import sanitize_error_response, save_image


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


def test_save_image_prevents_traversal():
    """Test that path traversal is prevented."""
    # Attempt to write outside safe directories
    with pytest.raises(ValueError, match="Invalid output path"):
        save_image(b"test", "/etc/passwd")

    # Try to escape to a system directory using enough traversal
    # This will resolve to /etc/passwd which is outside home/cwd
    import os
    deep_path = "../" * 20 + "etc/passwd"
    with pytest.raises(ValueError, match="Invalid output path"):
        save_image(b"test", deep_path)


def test_save_image_allows_home_directory():
    """Test that writing to home directory is allowed."""
    import shutil

    # Create temp dir inside home for test isolation
    temp_home_dir = Path.home() / ".nano_banana_test_tmp"
    temp_home_dir.mkdir(exist_ok=True)

    try:
        test_file = temp_home_dir / "test_image.png"
        result = save_image(b"test data", str(test_file))
        assert Path(result).exists()
        assert Path(result).read_bytes() == b"test data"
    finally:
        # Clean up
        if temp_home_dir.exists():
            shutil.rmtree(temp_home_dir)


def test_save_image_allows_cwd():
    """Test that writing to current directory is allowed."""
    import os

    # Save current dir
    original_cwd = os.getcwd()

    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            os.chdir(tmpdir)
            result = save_image(b"test data", "test_image.png")
            assert Path(result).exists()
            assert Path(result).read_bytes() == b"test data"
        finally:
            # Restore original directory
            os.chdir(original_cwd)


def test_upload_file_rejects_large_files():
    """Test that files exceeding size limit are rejected."""
    # This test would need actual upload_file function testing
    # For now, we'll test the validation logic separately
    from nanobanana_mcp import validate_file_size

    # 25MB file should be rejected (max is 20MB)
    with pytest.raises(ValueError, match="File too large"):
        validate_file_size(25 * 1024 * 1024)

    # 10MB file should be accepted
    validate_file_size(10 * 1024 * 1024)  # Should not raise


def test_validate_file_size_negative():
    """Test that negative file sizes are rejected."""
    from nanobanana_mcp import validate_file_size

    with pytest.raises(ValueError, match="cannot be negative"):
        validate_file_size(-1)

    with pytest.raises(ValueError, match="cannot be negative"):
        validate_file_size(-1000)


def test_validate_file_size_boundary():
    """Test exact boundary conditions."""
    from nanobanana_mcp import validate_file_size, MAX_FILE_SIZE

    # Exactly at limit - should pass
    validate_file_size(MAX_FILE_SIZE)

    # One byte over - should fail
    with pytest.raises(ValueError, match="File too large"):
        validate_file_size(MAX_FILE_SIZE + 1)

    # Zero bytes - should pass
    validate_file_size(0)
