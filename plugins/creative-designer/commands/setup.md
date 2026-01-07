---
description: Interactive wizard to configure Nano Banana Pro API credentials
---

# Nano Banana Pro Setup Wizard

Guide users through configuring the Gemini API for image generation.

## Phase 1: Welcome and Requirements Check

Display welcome message and verify prerequisites:

```
=================================================================
         Nano Banana Pro Setup Wizard
=================================================================

This wizard will help you configure AI-powered image generation
using Google's Gemini API.

What you'll need:
- A Google account (any account works)
- Internet access to Google AI Studio
- About 2 minutes to complete setup

Let's get started!
```

Check if GEMINI_API_KEY is already configured by examining the environment.

## Phase 2: API Key Generation

If no API key exists, guide user to obtain one:

```
STEP 1: Get Your API Key
------------------------

1. Open: https://aistudio.google.com/apikey

2. Sign in with your Google account

3. Click "Create API Key"

4. Select a project (or create new one)

5. Copy the generated API key

The key looks like: AIza...
```

Ask user to paste their API key.

## Phase 3: Validate API Key

Test the provided API key:

1. Make a test request to the Gemini API
2. Verify the key has access to image generation models
3. Report success or failure with actionable feedback

```
Testing API key...

[OK] API key is valid
[OK] Connected to Gemini API
[OK] Image generation models available

Your API key is working correctly!
```

If validation fails:
```
[FAIL] API key validation failed

Common issues:
- Key was copied incorrectly (check for extra spaces)
- Key was deleted or regenerated
- API is temporarily unavailable

Please try again or generate a new key.
```

## Phase 4: Configuration

Provide the settings configuration:

```
STEP 2: Configure Claude Code
-----------------------------

Add this to ~/.claude/settings.json:

{
  "env": {
    "GEMINI_API_KEY": "YOUR_API_KEY_HERE"
  }
}

Replace YOUR_API_KEY_HERE with your actual key.

If the file already has an "env" section, just add the GEMINI_API_KEY line.
```

## Phase 5: Restart Instructions

```
STEP 3: Restart Claude Code
---------------------------

For changes to take effect:

1. Exit Claude Code (Ctrl+C or Cmd+Q)
2. Run: claude
3. Resume your session: /resume

The creative-designer plugin will be ready to use!
```

## Phase 6: Verification

After restart, verify setup:

```
STEP 4: Verify Setup
--------------------

Try generating a test image:

  "Generate an image of a sunset over mountains"

If successful, you'll see the generation result.
If there's an error, the message will explain what to fix.
```

## Phase 7: Quick Reference

Provide quick reference for common usage:

```
=================================================================
                    Setup Complete!
=================================================================

Quick Commands:
--------------
- "Generate an image of..."     - Basic generation
- "Quick sketch of..."          - Fast draft
- "Professional 4K photo of..." - High quality

Model Selection:
---------------
- Flash: Fast (2-3s), 1024px max
- Pro: Quality (5-10s), 4K resolution
- Auto: Smart selection based on prompt

Aspect Ratios:
-------------
- 1:1   - Square (Instagram, profile pics)
- 16:9  - Landscape (YouTube, presentations)
- 9:16  - Portrait (Stories, TikTok)

Need help? Check the README or ask:
  "How do I use creative-designer?"

Happy generating!
=================================================================
```

## Error Recovery

If user encounters issues at any step:

1. Identify the specific error
2. Provide targeted solution
3. Offer to retry or start over
4. Link to full troubleshooting in GETTING_STARTED.md
