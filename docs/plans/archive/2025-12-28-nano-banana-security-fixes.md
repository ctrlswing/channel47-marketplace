# Nano Banana Security & Quality Fixes Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix critical security vulnerabilities, remove unused code, and resolve version/documentation inconsistencies in the nano-banana plugin.

**Architecture:** This plan addresses security hardening (API key sanitization, path validation, file size limits), code cleanup (unused functions/enums), and documentation fixes (version sync, CHANGELOG corrections).

**Tech Stack:** Python 3.x, FastMCP, httpx, Pydantic, pytest

---

## Task 1: Fix Version Mismatch (Critical)

**Files:**
- Modify: `plugins/nano-banana/.claude-plugin/plugin.json:3`

**Step 1: Update plugin.json version to match CHANGELOG**

Current version in plugin.json is "1.0.0" but CHANGELOG shows "1.1.0" as current.

```json
{
  "name": "nano-banana",
  "version": "1.1.0",
  "description": "AI-powered image generation using Google's Nano Banana Pro (Gemini 3 Pro Image) and Nano Banana (Gemini 2.5 Flash Image) with professional 4K quality, smart model selection, and Google Search grounding",
  "author": {
    "name": "Jackson",
    "url": "https://channel47.dev"
  },
  "homepage": "https://channel47.dev/plugins/nano-banana",
  "repository": "https://github.com/ctrlswing/channel47-marketplace",
  "license": "MIT",
  "keywords": [
    "image-generation",
    "ai-art",
    "gemini",
    "nano-banana",
    "4k",
    "google",
    "mcp",
    "creative"
  ],
  "mcpServers": "./.mcp.json"
}
```

**Step 2: Verify version is updated**

Run: `cat plugins/nano-banana/.claude-plugin/plugin.json | grep version`
Expected: `"version": "1.1.0",`

**Step 3: Commit version fix**

```bash
git add plugins/nano-banana/.claude-plugin/plugin.json
git commit -m "fix(nano-banana): sync plugin.json version to 1.1.0"
```

---

## Task 2: Sanitize API Key from Error Responses (Critical)

**Files:**
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:1-30` (add import)
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:354-362`
- Create: `plugins/nano-banana/tests/test_security.py`

**Step 1: Write failing test for API key sanitization**

Create test file:

```python
# File: plugins/nano-banana/tests/test_security.py
import pytest
import re
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
```

**Step 2: Run test to verify it fails**

Run: `cd plugins/nano-banana && pytest tests/test_security.py::test_sanitize_api_key_from_url -v`
Expected: FAIL with "ImportError: cannot import name 'sanitize_error_response'"

**Step 3: Add re import at top of nanobanana_mcp.py**

Modify line 1-30 section to add:

```python
import re
```

After the existing imports (around line 33).

**Step 4: Implement sanitize_error_response function**

Add after `get_api_key()` function (around line 189):

```python
def sanitize_error_response(error_text: str, max_length: int = 500) -> str:
    """
    Sanitize error responses to prevent API key leakage.

    Args:
        error_text: Raw error text from API
        max_length: Maximum length to return (default 500)

    Returns:
        Sanitized and truncated error text
    """
    if not error_text:
        return ""

    # Remove API keys from URLs (matches key=... patterns)
    sanitized = re.sub(r'key=[^&\s]+', 'key=REDACTED', error_text)

    # Truncate to max length
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length] + "\n[TRUNCATED]"

    return sanitized
```

**Step 5: Run tests to verify they pass**

Run: `cd plugins/nano-banana && pytest tests/test_security.py -v`
Expected: All 3 tests PASS

**Step 6: Apply sanitization to error responses in generate_image**

Modify lines 354-362:

```python
            if response.status_code != 200:
                error_detail = sanitize_error_response(response.text)
                return json.dumps({
                    "success": False,
                    "error": f"API request failed with status {response.status_code}",
                    "details": error_detail,
                    "model_used": model,
                    "selection_reason": selection_reason
                }, indent=2)
```

**Step 7: Apply sanitization to other error responses**

Find and update all other places where `response.text` is included in error messages:
- Line 473: `list_files` error handling
- Line 579: `upload_file` start upload error
- Line 604: `upload_file` upload error
- Line 671: `delete_file` error handling

For each, replace `response.text` with `sanitize_error_response(response.text)`.

**Step 8: Run all tests**

Run: `cd plugins/nano-banana && pytest tests/ -v`
Expected: All tests PASS

**Step 9: Commit API key sanitization**

```bash
git add plugins/nano-banana/src/nanobanana_mcp.py plugins/nano-banana/tests/test_security.py
git commit -m "fix(nano-banana): sanitize API keys from error responses"
```

---

## Task 3: Add Path Traversal Protection (Critical)

**Files:**
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:250-262`
- Modify: `plugins/nano-banana/tests/test_security.py`

**Step 1: Write failing test for path validation**

Add to `tests/test_security.py`:

```python
import tempfile
from pathlib import Path
from nanobanana_mcp import save_image


def test_save_image_prevents_traversal():
    """Test that path traversal is prevented."""
    # Attempt to write outside safe directories
    with pytest.raises(ValueError, match="Invalid output path"):
        save_image(b"test", "/etc/passwd")

    with pytest.raises(ValueError, match="Invalid output path"):
        save_image(b"test", "../../../etc/passwd")


def test_save_image_allows_home_directory():
    """Test that writing to home directory is allowed."""
    with tempfile.TemporaryDirectory() as tmpdir:
        home_path = Path.home() / "test_image.png"
        # This should succeed without raising
        # (we'll clean it up in the test)
        try:
            result = save_image(b"test", str(home_path))
            assert Path(result).exists()
        finally:
            if home_path.exists():
                home_path.unlink()


def test_save_image_allows_cwd():
    """Test that writing to current directory is allowed."""
    import os
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        result = save_image(b"test", "test_image.png")
        assert Path(result).exists()
```

**Step 2: Run test to verify it fails**

Run: `cd plugins/nano-banana && pytest tests/test_security.py::test_save_image_prevents_traversal -v`
Expected: FAIL (no ValueError raised)

**Step 3: Implement path validation in save_image**

Modify the `save_image` function (lines 250-262):

```python
def save_image(image_data: bytes, output_path: str) -> str:
    """
    Save image data to file with path validation.

    Args:
        image_data: Image bytes to save
        output_path: Destination path (must be within home or cwd)

    Returns:
        Absolute path to saved file

    Raises:
        ValueError: If path is invalid or attempts traversal
    """
    path = Path(output_path).expanduser().resolve()

    # Validate path is within safe directories
    safe_dirs = [Path.home(), Path.cwd()]
    is_safe = False

    for safe_dir in safe_dirs:
        try:
            # Check if path is relative to safe directory
            path.relative_to(safe_dir)
            is_safe = True
            break
        except ValueError:
            # Not relative to this safe directory, try next
            continue

    if not is_safe:
        raise ValueError(
            f"Invalid output path: must be within home directory or current working directory. "
            f"Attempted: {path}"
        )

    # Create parent directories if needed
    path.parent.mkdir(parents=True, exist_ok=True)

    # Add extension if missing
    if not path.suffix:
        path = path.with_suffix('.png')

    path.write_bytes(image_data)
    return str(path)
```

**Step 4: Run tests to verify they pass**

Run: `cd plugins/nano-banana && pytest tests/test_security.py -v`
Expected: All tests PASS

**Step 5: Commit path validation**

```bash
git add plugins/nano-banana/src/nanobanana_mcp.py plugins/nano-banana/tests/test_security.py
git commit -m "fix(nano-banana): add path traversal protection to save_image"
```

---

## Task 4: Add File Size Validation (High Priority)

**Files:**
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:35-37` (add constant)
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:523-629` (upload_file function)
- Modify: `plugins/nano-banana/tests/test_security.py`

**Step 1: Write failing test for file size limits**

Add to `tests/test_security.py`:

```python
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
```

**Step 2: Run test to verify it fails**

Run: `cd plugins/nano-banana && pytest tests/test_security.py::test_upload_file_rejects_large_files -v`
Expected: FAIL with "ImportError: cannot import name 'validate_file_size'"

**Step 3: Add MAX_FILE_SIZE constant**

Add after other constants (around line 37):

```python
# File upload limits
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB
```

**Step 4: Implement validate_file_size helper**

Add after `sanitize_error_response()` function:

```python
def validate_file_size(file_size: int, max_size: int = MAX_FILE_SIZE) -> None:
    """
    Validate file size is within limits.

    Args:
        file_size: Size in bytes
        max_size: Maximum allowed size (default: MAX_FILE_SIZE)

    Raises:
        ValueError: If file exceeds size limit
    """
    if file_size > max_size:
        raise ValueError(
            f"File too large: {file_size:,} bytes "
            f"(maximum: {max_size:,} bytes / {max_size // (1024*1024)}MB)"
        )
```

**Step 5: Run test to verify it passes**

Run: `cd plugins/nano-banana && pytest tests/test_security.py::test_upload_file_rejects_large_files -v`
Expected: PASS

**Step 6: Add file size check to upload_file**

Modify the `upload_file` function around line 541:

```python
        file_data = file_path.read_bytes()
        file_size = len(file_data)

        # Validate file size
        try:
            validate_file_size(file_size)
        except ValueError as e:
            return json.dumps({
                "success": False,
                "error": str(e)
            }, indent=2)
```

**Step 7: Run all tests**

Run: `cd plugins/nano-banana && pytest tests/ -v`
Expected: All tests PASS

**Step 8: Commit file size validation**

```bash
git add plugins/nano-banana/src/nanobanana_mcp.py plugins/nano-banana/tests/test_security.py
git commit -m "fix(nano-banana): add file size validation to prevent memory issues"
```

---

## Task 5: Remove Unused Code (High Priority)

**Files:**
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:36` (remove CHARACTER_LIMIT)
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:86-91` (remove MediaResolution)
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:221-232` (remove get_aspect_dimensions)
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:235-247` (remove truncate_response)

**Step 1: Remove CHARACTER_LIMIT constant**

Delete line 36:

```python
# Remove this line:
CHARACTER_LIMIT = 25000
```

**Step 2: Remove MediaResolution enum**

Delete lines 86-91:

```python
# Remove this entire enum:
class MediaResolution(str, Enum):
    """Output resolution settings."""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    AUTO = "AUTO"
```

**Step 3: Remove get_aspect_dimensions function**

Delete lines 221-232:

```python
# Remove this entire function:
def get_aspect_dimensions(aspect_ratio: AspectRatio) -> tuple[int, int]:
    """Get pixel dimensions for aspect ratio."""
    dimensions = {
        AspectRatio.SQUARE: (1024, 1024),
        AspectRatio.LANDSCAPE: (1920, 1080),
        AspectRatio.PORTRAIT: (1080, 1920),
        AspectRatio.CINEMATIC: (2520, 1080),
        AspectRatio.CLASSIC: (1365, 1024),
        AspectRatio.VERTICAL: (1024, 1365),
        AspectRatio.WIDE: (2048, 1024),
    }
    return dimensions.get(aspect_ratio, (1024, 1024))
```

**Step 4: Remove truncate_response function**

Delete lines 235-247:

```python
# Remove this entire function:
def truncate_response(data: str, message: str = "") -> str:
    """Truncate response if it exceeds CHARACTER_LIMIT."""
    if len(data) <= CHARACTER_LIMIT:
        return data

    truncation_notice = (
        f"\n\n[RESPONSE TRUNCATED]\n"
        f"Original size: {len(data):,} characters\n"
        f"Truncated to: {CHARACTER_LIMIT:,} characters\n"
        f"{message}"
    )

    return data[:CHARACTER_LIMIT - len(truncation_notice)] + truncation_notice
```

**Step 5: Verify code still works**

Run: `cd plugins/nano-banana && python -m py_compile src/nanobanana_mcp.py`
Expected: No syntax errors

**Step 6: Run all tests**

Run: `cd plugins/nano-banana && pytest tests/ -v`
Expected: All tests PASS

**Step 7: Commit unused code removal**

```bash
git add plugins/nano-banana/src/nanobanana_mcp.py
git commit -m "refactor(nano-banana): remove unused code (CHARACTER_LIMIT, MediaResolution, get_aspect_dimensions, truncate_response)"
```

---

## Task 6: Fix CHANGELOG Inconsistencies (Medium Priority)

**Files:**
- Modify: `plugins/nano-banana/CHANGELOG.md:28-30`

**Step 1: Remove quick_generate from 1.0.0 additions**

The CHANGELOG says `quick_generate` was added in 1.0.0, but according to the context, it was removed. However, examining the actual MCP server code, `quick_generate` still exists as an MCP tool. We need to clarify this.

First, verify if quick_generate exists:

Run: `grep -n "quick_generate" plugins/nano-banana/src/nanobanana_mcp.py`
Expected: Should show if the tool exists or not

**Step 2: Update CHANGELOG based on findings**

If `quick_generate` still exists in the code:
- Remove any mention of it being removed
- Keep it in the 1.0.0 additions

If it was actually removed:
- Add to 1.1.0 "Removed" section
- Keep it in 1.0.0 "Added" section for historical accuracy

Modify CHANGELOG.md to clarify status.

**Step 3: Fix version date order**

Current: 1.1.0 is dated 2025-12-28, 1.0.0 is dated 2025-01-01
This is backwards - 1.0.0 should be older than 1.1.0.

Change line 8 or line 17 to fix chronological order:

```markdown
## [1.1.0] - 2025-12-28

### Changed
- Updated Gemini models to latest state-of-the-art versions:
  - Pro Tier: `gemini-2.0-flash-preview-image-generation` -> `gemini-3-pro-image-preview`
  - Flash Tier: `gemini-2.0-flash-preview-image-generation` -> `gemini-2.5-flash-image`
- Updated documentation to reflect 4K generation capabilities of the new Pro model.

## [1.0.0] - 2025-01-01
```

This order is correct (most recent first).

**Step 4: Verify CHANGELOG formatting**

Run: `cat plugins/nano-banana/CHANGELOG.md`
Expected: Clean, chronological, no contradictions

**Step 5: Commit CHANGELOG fixes**

```bash
git add plugins/nano-banana/CHANGELOG.md
git commit -m "docs(nano-banana): fix CHANGELOG inconsistencies"
```

---

## Task 7: Extract Magic Numbers to Constants (Low Priority)

**Files:**
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:35-40` (add constants)
- Modify: `plugins/nano-banana/src/nanobanana_mcp.py:305-308` (use constants)

**Step 1: Add thinking budget constants**

Add to constants section (around line 40):

```python
# Thinking budget levels for Pro model
THINKING_BUDGET_LOW = 1024
THINKING_BUDGET_HIGH = 8192
```

**Step 2: Replace magic numbers in generate_image**

Modify lines 305-308:

```python
        # Add thinking config if specified
        if params.thinking_level:
            thinking_budget = THINKING_BUDGET_HIGH if params.thinking_level == ThinkingLevel.HIGH else THINKING_BUDGET_LOW
            generation_config["thinkingConfig"] = {
                "thinkingBudget": thinking_budget
            }
```

**Step 3: Verify code compiles**

Run: `cd plugins/nano-banana && python -m py_compile src/nanobanana_mcp.py`
Expected: No errors

**Step 4: Commit magic number extraction**

```bash
git add plugins/nano-banana/src/nanobanana_mcp.py
git commit -m "refactor(nano-banana): extract magic numbers to named constants"
```

---

## Task 8: Create Test Infrastructure (Medium Priority)

**Files:**
- Create: `plugins/nano-banana/tests/__init__.py`
- Create: `plugins/nano-banana/tests/conftest.py`
- Create: `plugins/nano-banana/pytest.ini`

**Step 1: Create tests __init__.py**

```python
# File: plugins/nano-banana/tests/__init__.py
"""Test suite for nano-banana plugin."""
```

**Step 2: Create pytest configuration**

```ini
# File: plugins/nano-banana/pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```

**Step 3: Create conftest.py with fixtures**

```python
# File: plugins/nano-banana/tests/conftest.py
"""Pytest configuration and fixtures for nano-banana tests."""

import pytest
import os
from unittest.mock import Mock, patch


@pytest.fixture
def mock_api_key(monkeypatch):
    """Mock GEMINI_API_KEY environment variable."""
    monkeypatch.setenv("GEMINI_API_KEY", "test-api-key-abc123")
    return "test-api-key-abc123"


@pytest.fixture
def mock_no_api_key(monkeypatch):
    """Remove GEMINI_API_KEY from environment."""
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)


@pytest.fixture
def sample_image_bytes():
    """Sample PNG image bytes for testing."""
    # Minimal valid PNG header
    return b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01'
```

**Step 4: Run tests to verify setup**

Run: `cd plugins/nano-banana && pytest tests/ -v`
Expected: Tests run with proper configuration

**Step 5: Commit test infrastructure**

```bash
git add plugins/nano-banana/tests/__init__.py plugins/nano-banana/tests/conftest.py plugins/nano-banana/pytest.ini
git commit -m "test(nano-banana): add test infrastructure and fixtures"
```

---

## Task 9: Add Unit Tests for Core Functions (Medium Priority)

**Files:**
- Create: `plugins/nano-banana/tests/test_utils.py`

**Step 1: Create utility function tests**

```python
# File: plugins/nano-banana/tests/test_utils.py
"""Tests for utility functions in nanobanana_mcp."""

import pytest
from nanobanana_mcp import (
    get_api_key,
    select_model,
    sanitize_error_response,
    validate_file_size,
    ModelTier,
    FLASH_MODEL,
    PRO_MODEL,
    MAX_FILE_SIZE
)


class TestGetApiKey:
    """Tests for get_api_key function."""

    def test_get_api_key_success(self, mock_api_key):
        """Test successful API key retrieval."""
        key = get_api_key()
        assert key == "test-api-key-abc123"

    def test_get_api_key_missing(self, mock_no_api_key):
        """Test error when API key is missing."""
        with pytest.raises(ValueError, match="Missing GEMINI_API_KEY"):
            get_api_key()


class TestSelectModel:
    """Tests for select_model function."""

    def test_select_pro_when_requested(self):
        """Test Pro model is selected when explicitly requested."""
        model, reason = select_model("any prompt", ModelTier.PRO)
        assert model == PRO_MODEL
        assert "user requested" in reason.lower()

    def test_select_flash_when_requested(self):
        """Test Flash model is selected when explicitly requested."""
        model, reason = select_model("any prompt", ModelTier.FLASH)
        assert model == FLASH_MODEL
        assert "user requested" in reason.lower()

    def test_auto_select_pro_for_quality_keywords(self):
        """Test Pro model auto-selected for quality keywords."""
        quality_prompts = [
            "create a professional 4k image",
            "photorealistic detailed portrait",
            "premium commercial product photo"
        ]
        for prompt in quality_prompts:
            model, reason = select_model(prompt, ModelTier.AUTO)
            assert model == PRO_MODEL
            assert "auto-selected" in reason.lower()

    def test_auto_select_flash_for_speed_keywords(self):
        """Test Flash model auto-selected for speed keywords."""
        speed_prompts = [
            "quick sketch of a cat",
            "fast draft illustration",
            "simple concept art"
        ]
        for prompt in speed_prompts:
            model, reason = select_model(prompt, ModelTier.AUTO)
            assert model == FLASH_MODEL
            assert "auto-selected" in reason.lower()

    def test_auto_select_flash_default(self):
        """Test Flash model is default for general prompts."""
        model, reason = select_model("a cat sitting", ModelTier.AUTO)
        assert model == FLASH_MODEL
        assert "default" in reason.lower()


class TestSanitizeErrorResponse:
    """Tests for sanitize_error_response function."""

    def test_removes_api_keys_from_urls(self):
        """Test API keys are redacted from URLs."""
        error = "Error at https://api.example.com?key=AIzaSyABC123&param=value"
        result = sanitize_error_response(error)
        assert "AIzaSyABC123" not in result
        assert "key=REDACTED" in result
        assert "param=value" in result

    def test_truncates_long_errors(self):
        """Test long errors are truncated."""
        error = "x" * 1000
        result = sanitize_error_response(error, max_length=100)
        assert len(result) <= 110  # 100 + [TRUNCATED]
        assert "[TRUNCATED]" in result

    def test_handles_empty_string(self):
        """Test empty strings are handled."""
        result = sanitize_error_response("")
        assert result == ""


class TestValidateFileSize:
    """Tests for validate_file_size function."""

    def test_accepts_small_files(self):
        """Test small files are accepted."""
        # Should not raise
        validate_file_size(1024)  # 1KB
        validate_file_size(1024 * 1024)  # 1MB
        validate_file_size(10 * 1024 * 1024)  # 10MB

    def test_rejects_large_files(self):
        """Test files exceeding limit are rejected."""
        with pytest.raises(ValueError, match="File too large"):
            validate_file_size(MAX_FILE_SIZE + 1)

        with pytest.raises(ValueError, match="File too large"):
            validate_file_size(100 * 1024 * 1024)  # 100MB

    def test_accepts_at_limit(self):
        """Test file exactly at limit is accepted."""
        validate_file_size(MAX_FILE_SIZE)  # Should not raise
```

**Step 2: Run tests to verify they pass**

Run: `cd plugins/nano-banana && pytest tests/test_utils.py -v`
Expected: All tests PASS

**Step 3: Commit unit tests**

```bash
git add plugins/nano-banana/tests/test_utils.py
git commit -m "test(nano-banana): add comprehensive unit tests for utility functions"
```

---

## Task 10: Update Documentation for Reference Images (Medium Priority)

**Files:**
- Modify: `plugins/nano-banana/README.md:49-70` (add examples)
- Modify: `plugins/nano-banana/GETTING_STARTED.md:76-112` (add section)
- Modify: `plugins/nano-banana/skills/image-gen/SKILL.md:98-112` (add workflow)

**Step 1: Add reference image examples to README**

Add new section after line 70 in README.md:

```markdown
### With Reference Image
```
"Use this product photo as reference and generate a similar composition with a coffee mug"
```

The plugin supports two ways to provide reference images:
1. Upload a file first using `upload_file`, then use the returned URI
2. Provide base64-encoded image data directly
```

**Step 2: Add reference image section to GETTING_STARTED**

Add new section after line 112:

```markdown
### Reference-Based Generation

Generate images inspired by reference materials:

1. **Upload a reference image:**
```bash
# Upload returns a file URI
"Upload image.png to use as reference"
```

2. **Generate with reference:**
```
"Generate a product photo similar to the uploaded reference, but with a coffee mug instead"
```

The reference image helps maintain consistent style, composition, or branding.
```

**Step 3: Add to skill workflow**

Modify SKILL.md around line 98-112 to add:

```markdown
### Reference Image Usage

When user provides or wants to use a reference:

```
generate_image(
  prompt="Your detailed prompt here",
  reference_file_uri="files/abc123",  # From upload_file
  reference_file_mime_type="image/png",
  ...other params
)
```

Or with base64 data:

```
generate_image(
  prompt="Your detailed prompt here",
  reference_image_base64="iVBORw0KGg...",  # Base64 encoded
  reference_file_mime_type="image/png",
  ...other params
)
```
```

**Step 4: Verify documentation reads well**

Run: `cat plugins/nano-banana/README.md | grep -A 10 "Reference Image"`
Expected: Clear, helpful documentation

**Step 5: Commit documentation updates**

```bash
git add plugins/nano-banana/README.md plugins/nano-banana/GETTING_STARTED.md plugins/nano-banana/skills/image-gen/SKILL.md
git commit -m "docs(nano-banana): add reference image feature documentation"
```

---

## Final Tasks

### Task 11: Run Full Test Suite

**Step 1: Run all tests**

Run: `cd plugins/nano-banana && pytest tests/ -v --tb=short`
Expected: All tests PASS

**Step 2: Check code coverage (if coverage installed)**

Run: `cd plugins/nano-banana && pytest tests/ --cov=src --cov-report=term-missing`
Expected: Reasonable coverage of core functions

### Task 12: Final Verification

**Step 1: Verify all modified files compile**

Run: `cd plugins/nano-banana && python -m py_compile src/nanobanana_mcp.py`
Expected: No errors

**Step 2: Review git log**

Run: `git log --oneline -12`
Expected: Clean commit history with descriptive messages

**Step 3: Verify version consistency**

Run: `grep -h version plugins/nano-banana/.claude-plugin/plugin.json plugins/nano-banana/CHANGELOG.md | head -3`
Expected: All show 1.1.0

---

## Testing Notes

**Required for testing:**
- pytest installed: `pip install pytest pytest-cov`
- Run tests from plugin root: `cd plugins/nano-banana && pytest tests/`

**Manual testing:**
1. Verify API key sanitization works (intentionally trigger error)
2. Test path validation with various paths
3. Test file size rejection with large file
4. Verify all features still work after refactoring

**Integration testing:**
- Test actual image generation if API key available
- Test file upload with real files
- Verify error messages are user-friendly

---

## Success Criteria

- ✅ All critical security issues fixed
- ✅ Version mismatch resolved
- ✅ Unused code removed
- ✅ All tests passing
- ✅ Documentation updated
- ✅ Clean commit history
- ✅ No regressions in functionality
