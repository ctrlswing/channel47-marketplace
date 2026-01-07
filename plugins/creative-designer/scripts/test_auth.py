#!/usr/bin/env python3
"""
Test authentication with the Gemini API.

Usage:
    python test_auth.py

This script verifies that your GEMINI_API_KEY is correctly configured
and can communicate with the Gemini API.
"""

import os
import sys
import httpx

GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta"


def test_authentication():
    """Test Gemini API authentication."""
    print("=" * 60)
    print("Nano Banana Pro - Authentication Test")
    print("=" * 60)
    print()

    # Check for API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[FAIL] GEMINI_API_KEY environment variable not set")
        print()
        print("To fix this:")
        print("1. Get your free API key from: https://aistudio.google.com/apikey")
        print("2. Add to ~/.claude/settings.json:")
        print('   "env": { "GEMINI_API_KEY": "your-key-here" }')
        print("3. Restart Claude Code")
        return False

    print(f"[OK] GEMINI_API_KEY found (starts with: {api_key[:8]}...)")
    print()

    # Test API connection
    print("Testing API connection...")
    try:
        response = httpx.get(
            f"{GEMINI_API_BASE}/models",
            params={"key": api_key},
            timeout=30.0
        )

        if response.status_code == 200:
            result = response.json()
            models = result.get("models", [])
            print(f"[OK] Successfully connected to Gemini API")
            print(f"[OK] Found {len(models)} available models")
            print()

            # List image generation capable models
            image_models = [
                m for m in models
                if "image" in m.get("name", "").lower()
                or "image" in str(m.get("supportedGenerationMethods", [])).lower()
            ]
            if image_models:
                print("Image-capable models found:")
                for m in image_models[:5]:
                    print(f"  - {m.get('name', 'unknown')}")
            print()
            print("[SUCCESS] Authentication test passed!")
            return True

        elif response.status_code == 400:
            print(f"[FAIL] Invalid API key format")
            print(f"       Response: {response.text}")
            return False

        elif response.status_code == 403:
            print(f"[FAIL] API key is invalid or has been revoked")
            print(f"       Get a new key from: https://aistudio.google.com/apikey")
            return False

        else:
            print(f"[FAIL] Unexpected response: {response.status_code}")
            print(f"       Response: {response.text}")
            return False

    except httpx.ConnectError:
        print("[FAIL] Could not connect to Gemini API")
        print("       Check your internet connection")
        return False

    except httpx.TimeoutException:
        print("[FAIL] Connection timed out")
        print("       The API might be temporarily unavailable")
        return False

    except Exception as e:
        print(f"[FAIL] Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = test_authentication()
    sys.exit(0 if success else 1)
