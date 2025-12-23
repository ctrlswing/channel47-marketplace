# Google Ads Plugin Setup Improvements - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix critical plugin structure bugs and improve setup UX with automation

**Architecture:** Direct file modifications (config, docs, command flow). No code changes to Python scripts. Focus on eliminating manual steps via bash automation in setup.md interactive flow.

**Tech Stack:** JSON config files, Markdown documentation, Bash scripting for automation

---

## Task 1: Fix MCP Server Configuration

**Files:**
- Modify: `plugins/google-ads/.mcp.json`

**Step 1: Read current .mcp.json**

Run: `cat plugins/google-ads/.mcp.json`

Expected: Shows config with empty env vars

**Step 2: Remove env section from .mcp.json**

Replace the file content with:
```json
{
  "mcpServers": {
    "google-ads": {
      "command": "python3",
      "args": ["${CLAUDE_PLUGIN_ROOT}/src/google_ads_mcp.py"]
    }
  }
}
```

**Step 3: Verify format**

Run: `cat plugins/google-ads/.mcp.json | python3 -m json.tool`

Expected: Valid JSON, no errors

**Step 4: Commit the fix**

```bash
git add plugins/google-ads/.mcp.json
git commit -m "fix(google-ads): remove env vars from .mcp.json to fix MCP connection

Empty env var strings override settings.json values, preventing
MCP server from loading environment variables after setup"
```

---

## Task 2: Pin Exact Dependency Versions

**Files:**
- Modify: `plugins/google-ads/requirements.txt`

**Step 1: Read current requirements.txt**

Run: `cat plugins/google-ads/requirements.txt`

Expected: Shows tilde-based version ranges

**Step 2: Replace with pinned versions**

Replace the file content with:
```txt
# MCP Framework - pinned to compatible versions
mcp==1.25.0
fastmcp==2.13.0.2

# Google Ads API
google-ads==28.0.0

# Google Auth
google-auth==2.32.0
google-auth-oauthlib==1.2.0
google-auth-httplib2==0.1.0

# Core dependencies
pydantic==2.8.0
httpx==0.27.0
python-dotenv==1.0.0

# gRPC dependencies
grpcio==1.66.0
protobuf==5.27.0
```

**Step 3: Verify format**

Run: `cat plugins/google-ads/requirements.txt | head -15`

Expected: Shows pinned versions with == operator

**Step 4: Commit the fix**

```bash
git add plugins/google-ads/requirements.txt
git commit -m "fix(google-ads): pin exact dependency versions

Prevents version conflicts. Previously mcp~=1.2.0 was incompatible
with fastmcp 2.13.0.2 which requires mcp>=1.17.0"
```

---

## Task 3: Create Plugin README Documentation

**Files:**
- Create: `plugins/google-ads/README.md`

**Step 1: Check if README already exists**

Run: `test -f plugins/google-ads/README.md && echo "exists" || echo "not found"`

Expected: "not found" (if it exists, we'll update it instead)

**Step 2: Write comprehensive README**

Create file with complete content (see design doc section 2.1 for full text):

```markdown
# Google Ads Plugin

Query Google Ads data using GAQL with OAuth authentication.

## Required Environment Variables

This plugin requires the following environment variables in your Claude Code settings:

| Variable | Description | Example |
|----------|-------------|---------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Your Google Ads API developer token | `abc123XYZ456...` |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | Your MCC (Manager) account ID | `3461276031` |
| `GOOGLE_ADS_CLIENT_ID` | OAuth 2.0 client ID | `123...apps.googleusercontent.com` |
| `GOOGLE_ADS_CLIENT_SECRET` | OAuth 2.0 client secret | `GOCSPX-...` |
| `GOOGLE_ADS_REFRESH_TOKEN` | OAuth 2.0 refresh token | `1//0abc...` |

### Quick Setup

Run the interactive setup wizard:
```
/google-ads:setup
```

The wizard will guide you through:
1. Creating a Google Cloud project
2. Configuring OAuth credentials
3. Generating a refresh token
4. Saving credentials to your settings

### Manual Setup

If you prefer manual configuration, add these to `~/.claude/settings.json`:

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "your-token-here",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "1234567890",
    "GOOGLE_ADS_CLIENT_ID": "your-client-id.apps.googleusercontent.com",
    "GOOGLE_ADS_CLIENT_SECRET": "GOCSPX-your-secret",
    "GOOGLE_ADS_REFRESH_TOKEN": "1//0your-refresh-token"
  }
}
```

After adding credentials, restart Claude Code for changes to take effect.

## Troubleshooting

### MCP Server Won't Connect

1. Verify all 5 environment variables are set in your settings file
2. Restart Claude Code completely
3. Check for typos in variable names (they're case-sensitive)
4. Run verification: `python ~/.claude/plugins/cache/channel47/google-ads/*/scripts/test_auth.py`

### Invalid Grant Error

- OAuth consent screen must be "Published" (not "Testing")
- Testing mode tokens expire after 7 days
- Re-run `/google-ads:setup` to generate a new refresh token

### Developer Token Issues

- Token must have at least "Basic" access level for production use
- "Test" access only works with test accounts
- Apply for access at: Google Ads → Tools & Settings → API Center
```

**Step 3: Verify file created**

Run: `test -f plugins/google-ads/README.md && wc -l plugins/google-ads/README.md`

Expected: File exists with ~65 lines

**Step 4: Commit documentation**

```bash
git add plugins/google-ads/README.md
git commit -m "docs(google-ads): add README with env var requirements

Documents required environment variables and troubleshooting steps
for common setup issues"
```

---

## Task 4: Add Environment Variables Reference to Setup Command

**Files:**
- Modify: `plugins/google-ads/commands/setup.md:7-8` (after description, before Phase 1)

**Step 1: Read setup.md header**

Run: `head -10 plugins/google-ads/commands/setup.md`

Expected: Shows frontmatter and title

**Step 2: Add "What You'll Need" section**

Insert after line 8 (after "This command guides you through..."), before Phase 1:

```markdown

## What You'll Need

This setup wizard will help you configure these 5 environment variables:

1. **GOOGLE_ADS_DEVELOPER_TOKEN** - Your Google Ads API developer token (from Google Ads API Center)
2. **GOOGLE_ADS_LOGIN_CUSTOMER_ID** - Your MCC (Manager) account ID (10 digits)
3. **GOOGLE_ADS_CLIENT_ID** - OAuth 2.0 client ID (from Google Cloud Console)
4. **GOOGLE_ADS_CLIENT_SECRET** - OAuth 2.0 client secret (from Google Cloud Console)
5. **GOOGLE_ADS_REFRESH_TOKEN** - OAuth refresh token (generated during this setup)

These will be saved to your Claude Code settings file (`~/.claude/settings.json` or project-specific).

---
```

**Step 3: Verify insertion**

Run: `sed -n '8,30p' plugins/google-ads/commands/setup.md`

Expected: Shows new section between description and Phase 1

**Step 4: Commit the change**

```bash
git add plugins/google-ads/commands/setup.md
git commit -m "docs(google-ads): add env vars overview to setup wizard

Users now see what they're configuring before starting the setup flow"
```

---

## Task 5: Reorder OAuth Instructions - Split Consent Screen

**Files:**
- Modify: `plugins/google-ads/commands/setup.md:66-86` (Phase 2, OAuth section)

**Step 1: Read current OAuth section**

Run: `sed -n '66,86p' plugins/google-ads/commands/setup.md`

Expected: Shows combined OAuth credentials instructions

**Step 2: Replace OAuth section with two-step flow**

Replace the "Have you created OAuth 2.0 credentials?" section (lines 66-86) with:

```markdown
### Step 1: Configure OAuth Consent Screen (Required First)

Before creating credentials, you must configure the consent screen:

**If you've already configured and published the consent screen:**
✓ Skip to Step 2

**If not configured yet:**

1. Go to "APIs & Services" → "OAuth consent screen"
2. Select **User Type: External**, then click "Create"
3. Fill in required fields:
   - **App name:** "Google Ads MCP"
   - **User support email:** your email
   - **Developer contact:** your email
4. Click "Save and Continue" through remaining screens (Scopes, Test users)
5. **CRITICAL:** Click "Publish App" on the final screen
   - Don't leave in Testing mode or tokens expire in 7 days
   - Publishing is instant for External apps with no sensitive scopes

Respond with 'done' when consent screen is configured and published.

**[Wait for user confirmation]**

---

### Step 2: Create OAuth Client ID

Now create the OAuth credentials:

**If you've already created desktop app credentials:**
✓ You should have the downloaded JSON file

**If not created yet:**

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. Select **Application type: Desktop app**
4. Name: "Google Ads MCP Client"
5. Click "Create"
6. **IMPORTANT:** Click "DOWNLOAD JSON" button
7. Save the file (default name is long, you don't need to rename it)
```

**Step 3: Verify replacement**

Run: `sed -n '66,120p' plugins/google-ads/commands/setup.md | grep -E "(Step 1|Step 2|CRITICAL)"`

Expected: Shows two-step structure with CRITICAL warning

**Step 4: Commit the change**

```bash
git add plugins/google-ads/commands/setup.md
git commit -m "docs(google-ads): split OAuth consent screen into separate step

Consent screen must be configured first, matching Google's actual flow.
Prevents 'configure consent screen first' error during credential creation"
```

---

## Task 6: Add OAuth File Auto-Detection

**Files:**
- Modify: `plugins/google-ads/commands/setup.md:87-100` (OAuth file path prompt)

**Step 1: Read current file path section**

Run: `sed -n '87,100p' plugins/google-ads/commands/setup.md`

Expected: Shows manual path entry prompt

**Step 2: Replace with auto-detection flow**

Replace lines 87-100 with:

```markdown

### Locating your OAuth credentials file

Let me search for recently downloaded OAuth credential files...

**Searching common locations...**

Run:
```bash
find ~/Downloads ~/Desktop . -maxdepth 1 -name "client_secret*.json" -type f -mtime -7 2>/dev/null | \
  while read -r file; do
    mod_time=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$file" 2>/dev/null || stat -c "%y" "$file" 2>/dev/null | cut -d' ' -f1-2)
    echo "$mod_time|$file"
  done | sort -r
```

**If 1 file found:**

✓ Found: `[FILEPATH]`
  Modified: [TIMESTAMP]

Use this file?

**[Wait for user: yes/no]**

If YES: Continue to validation
If NO: Ask for custom path below

**If multiple files found:**

Found multiple OAuth credential files:
```
1. [FILE1] (modified: [TIME1])
2. [FILE2] (modified: [TIME2])
3. [FILE3] (modified: [TIME3])
```

Which file should I use?

**[Wait for user: 1/2/3 or custom path]**

**If none found or user provides custom path:**

I didn't find any OAuth credential files, or you want to use a different location.

Please provide the full path to your client_secrets.json file:

**[Wait for user input]**

---

**Validating file...**
```

**Step 3: Verify replacement**

Run: `grep -n "auto-detection\|Searching common" plugins/google-ads/commands/setup.md`

Expected: Shows new auto-detection section

**Step 4: Commit the change**

```bash
git add plugins/google-ads/commands/setup.md
git commit -m "feat(google-ads): add OAuth file auto-detection to setup

Searches ~/Downloads, ~/Desktop, and current directory for recent
client_secret*.json files. Eliminates manual path entry in most cases"
```

---

## Task 7: Add Automatic Settings File Writing

**Files:**
- Modify: `plugins/google-ads/commands/setup.md:232-260` (Phase 7, save settings)

**Step 1: Read current save settings section**

Run: `sed -n '232,260p' plugins/google-ads/commands/setup.md`

Expected: Shows manual JSON editing instructions

**Step 2: Replace with automatic writing flow**

Replace the "Based on your choice, add these to your settings file:" section with:

```markdown
**I'll automatically save these credentials to your settings file.**

Preview of environment variables to add:
```
GOOGLE_ADS_DEVELOPER_TOKEN: [FIRST_3_CHARS]...[LAST_3_CHARS]
GOOGLE_ADS_LOGIN_CUSTOMER_ID: [FULL_MCC_ID]
GOOGLE_ADS_CLIENT_ID: [FIRST_10_CHARS]...[apps.googleusercontent.com]
GOOGLE_ADS_CLIENT_SECRET: GOCSPX-...[LAST_4_CHARS]
GOOGLE_ADS_REFRESH_TOKEN: 1//0...[LAST_4_CHARS]
```

Target file: `[SETTINGS_FILE_PATH]`

Proceed with writing to `[SETTINGS_FILE_PATH]`?

**[Wait for user: yes/no]**

---

**If YES - Automatic Save:**

**Step 1: Backup existing settings (if file exists)**

Run:
```bash
SETTINGS_FILE="[PATH]"
if [ -f "$SETTINGS_FILE" ]; then
  cp "$SETTINGS_FILE" "${SETTINGS_FILE}.backup.$(date +%Y%m%d_%H%M%S)"
  echo "✓ Backed up existing settings"
fi
```

**Step 2: Merge environment variables**

Run:
```bash
SETTINGS_FILE="[PATH]"

# Read existing settings or create empty object
if [ -f "$SETTINGS_FILE" ]; then
  EXISTING=$(cat "$SETTINGS_FILE")
else
  EXISTING='{}'
fi

# Merge new env vars using Python
python3 -c "
import json
import sys

existing = json.loads('''$EXISTING''')
if 'env' not in existing:
    existing['env'] = {}

existing['env']['GOOGLE_ADS_DEVELOPER_TOKEN'] = '[TOKEN]'
existing['env']['GOOGLE_ADS_LOGIN_CUSTOMER_ID'] = '[MCC_ID]'
existing['env']['GOOGLE_ADS_CLIENT_ID'] = '[CLIENT_ID]'
existing['env']['GOOGLE_ADS_CLIENT_SECRET'] = '[CLIENT_SECRET]'
existing['env']['GOOGLE_ADS_REFRESH_TOKEN'] = '[REFRESH_TOKEN]'

print(json.dumps(existing, indent=2))
" > "$SETTINGS_FILE"

echo "✓ Credentials saved to $SETTINGS_FILE"
```

Expected: "✓ Credentials saved to [PATH]"

**Verification:**

Run: `cat [SETTINGS_FILE_PATH] | python3 -m json.tool | grep GOOGLE_ADS | wc -l`

Expected: 5 (all 5 env vars present)

---

**If NO - Manual Save:**

Cancelled automatic save. Here's the JSON to add manually:

File to edit: `[SETTINGS_FILE_PATH]`

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "[ACTUAL_TOKEN]",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "[ACTUAL_MCC_ID]",
    "GOOGLE_ADS_CLIENT_ID": "[ACTUAL_CLIENT_ID]",
    "GOOGLE_ADS_CLIENT_SECRET": "[ACTUAL_CLIENT_SECRET]",
    "GOOGLE_ADS_REFRESH_TOKEN": "[ACTUAL_REFRESH_TOKEN]"
  }
}
```

**If the file already exists,** merge the `env` section with your existing settings.

After you've saved the settings file manually, respond with 'done'.

**[Wait for user confirmation]**
```

**Step 3: Verify replacement**

Run: `grep -n "automatic\|Backup existing" plugins/google-ads/commands/setup.md | head -5`

Expected: Shows new automatic save section

**Step 4: Commit the change**

```bash
git add plugins/google-ads/commands/setup.md
git commit -m "feat(google-ads): add automatic settings file writing

Eliminates manual JSON editing. Backs up existing settings before merge.
User can still opt for manual edit if preferred"
```

---

## Task 8: Add Restart Verification Flow

**Files:**
- Modify: `plugins/google-ads/commands/setup.md:266-278` (Phase 8, verification)

**Step 1: Read current verification section**

Run: `sed -n '266,278p' plugins/google-ads/commands/setup.md`

Expected: Shows immediate test_auth.py execution

**Step 2: Replace with restart verification flow**

Replace Phase 8 content with:

```markdown
## Phase 8: Verification

⚠️ **IMPORTANT: Restart Claude Code now**

Your credentials are saved, but Claude Code needs to restart to load them into the environment.

**Steps to restart:**
1. Exit Claude Code completely:
   - Press `Ctrl+C` (Linux/Windows) or `Cmd+Q` (Mac)
   - Or type `exit` if in a shell
2. Wait 2-3 seconds for complete shutdown
3. Start Claude Code again: `claude code`
4. Return to this conversation: Navigate back or use session history

After restarting Claude Code completely, respond with 'done' and I'll verify automatically.

**[Wait for user to restart and respond with 'done']**

---

**Checking if environment variables are loaded...**

Run:
```bash
if [ -n "$GOOGLE_ADS_DEVELOPER_TOKEN" ]; then
  echo "✓ Environment variables detected"
  exit 0
else
  echo "❌ Environment variables NOT detected"
  exit 1
fi
```

---

**SCENARIO A: Environment variables detected**

✓ Environment variables detected!

Your Claude Code environment has successfully loaded the Google Ads credentials.

Let me test the connection to Google Ads API...

Run: `cd ${CLAUDE_PLUGIN_ROOT}/scripts && python3 test_auth.py`

**Expected output:**
```
✓ Authentication successful!
✓ Connected to Google Ads API
✓ MCC Account: [Your MCC Name] ([MCC_ID])
```

**If successful:**

🎉 **Setup complete! Your Google Ads plugin is ready to use.**

Try it out:
- "List my Google Ads accounts"
- "Show me search terms for account [ACCOUNT_ID]"
- "Find negative keyword opportunities"

---

**SCENARIO B: Environment variables NOT detected**

❌ **Environment variables not detected**

It looks like Claude Code hasn't loaded the environment variables yet.

**This usually means:**
1. Claude Code wasn't fully restarted (conversation closed but CLI still running)
2. Settings file wasn't saved correctly
3. Wrong settings file was edited

**Recovery steps:**

**Step 1: Verify settings file has the credentials**

Run:
```bash
SETTINGS_FILE="[PATH_USED]"
if [ -f "$SETTINGS_FILE" ]; then
  echo "Settings file exists"
  cat "$SETTINGS_FILE" | python3 -m json.tool | grep GOOGLE_ADS | wc -l
else
  echo "Settings file not found at $SETTINGS_FILE"
fi
```

Expected: Should show "5" (all 5 env vars)

If not 5: Re-run the settings save step (Phase 7)

**Step 2: Complete restart (if settings are correct)**

1. **Completely exit Claude Code** (not just this conversation):
   - `Ctrl+C` or `Cmd+Q` to quit the CLI
   - Verify the process is gone: `ps aux | grep claude`
2. **Wait 5 seconds**
3. **Start fresh Claude Code session**: `claude code`
4. **Come back to this conversation** and respond with 'restarted'

**[Wait for user: 'restarted']**

**When user responds 'restarted', run the environment check again (loop back to "Checking if environment variables are loaded...")**

---

**If still failing after restart:**

The issue may be with the settings file location. Let me check all possible locations:

Run:
```bash
echo "Checking all settings files..."
for f in ~/.claude/settings.json .claude/settings.json .claude/settings.local.json; do
  if [ -f "$f" ]; then
    echo "Found: $f"
    cat "$f" | python3 -m json.tool | grep -c GOOGLE_ADS || echo "  No GOOGLE_ADS vars"
  fi
done
```

This will help identify which file has the credentials and which file Claude Code is reading.

**[Provide guidance based on output]**
```

**Step 3: Verify replacement**

Run: `grep -n "SCENARIO A:\|SCENARIO B:" plugins/google-ads/commands/setup.md`

Expected: Shows both verification scenarios

**Step 4: Commit the change**

```bash
git add plugins/google-ads/commands/setup.md
git commit -m "feat(google-ads): add restart verification with env var check

Verifies Claude Code actually restarted and loaded environment variables.
Provides recovery steps if restart didn't take effect. Catches common
mistake of not fully exiting the CLI"
```

---

## Task 9: Test Complete Setup Flow (Manual Verification)

**Files:**
- Read: `plugins/google-ads/commands/setup.md` (full file)
- Read: `plugins/google-ads/README.md`
- Read: `plugins/google-ads/.mcp.json`
- Read: `plugins/google-ads/requirements.txt`

**Step 1: Verify all files are updated**

Run:
```bash
echo "=== .mcp.json ==="
cat plugins/google-ads/.mcp.json
echo -e "\n=== requirements.txt (first 10 lines) ==="
head -10 plugins/google-ads/requirements.txt
echo -e "\n=== README.md (first 30 lines) ==="
head -30 plugins/google-ads/README.md
echo -e "\n=== setup.md structure ==="
grep -n "^## " plugins/google-ads/commands/setup.md
```

Expected: All files show updated content

**Step 2: Check for consistency**

Verify all 5 env var names are consistent across files:

Run:
```bash
echo "Checking env var consistency..."
grep -h "GOOGLE_ADS_" plugins/google-ads/README.md plugins/google-ads/commands/setup.md | \
  grep -Eo "GOOGLE_ADS_[A-Z_]+" | sort -u
```

Expected:
```
GOOGLE_ADS_CLIENT_ID
GOOGLE_ADS_CLIENT_SECRET
GOOGLE_ADS_DEVELOPER_TOKEN
GOOGLE_ADS_LOGIN_CUSTOMER_ID
GOOGLE_ADS_REFRESH_TOKEN
```

**Step 3: Validate JSON files**

Run:
```bash
python3 -m json.tool plugins/google-ads/.mcp.json > /dev/null && echo "✓ .mcp.json valid" || echo "❌ .mcp.json invalid"
```

Expected: "✓ .mcp.json valid"

**Step 4: Check setup.md phase structure**

Run: `grep "^## Phase" plugins/google-ads/commands/setup.md`

Expected: 8 phases shown (Prerequisites through Verification)

**Step 5: No commit needed** (verification only)

---

## Task 10: Create Completion Summary

**Files:**
- Create: `docs/plans/completed/2025-12-22-google-ads-setup-improvements-summary.md`

**Step 1: Create completed directory if needed**

Run: `mkdir -p docs/plans/completed`

Expected: Directory created or already exists

**Step 2: Write completion summary**

Create file with:

```markdown
# Google Ads Setup Improvements - Completion Summary

**Date:** 2025-12-22
**Status:** ✅ Complete

## Changes Implemented

### Critical Fixes
1. ✅ **Fixed MCP server connection failures**
   - Removed empty env vars from `.mcp.json`
   - File: `plugins/google-ads/.mcp.json`

2. ✅ **Fixed dependency version conflicts**
   - Pinned exact versions (mcp==1.25.0, fastmcp==2.13.0.2)
   - File: `plugins/google-ads/requirements.txt`

### Documentation
3. ✅ **Created plugin README**
   - Documents all 5 required environment variables
   - Includes troubleshooting guide
   - File: `plugins/google-ads/README.md`

4. ✅ **Added env vars reference to setup wizard**
   - Users see what they're configuring upfront
   - File: `plugins/google-ads/commands/setup.md`

### UX Improvements
5. ✅ **OAuth consent screen reordering**
   - Split into Step 1 (consent) and Step 2 (credentials)
   - Matches Google's actual flow
   - File: `plugins/google-ads/commands/setup.md`

6. ✅ **OAuth file auto-detection**
   - Searches ~/Downloads, ~/Desktop, current directory
   - Shows modification timestamps
   - Falls back to manual entry
   - File: `plugins/google-ads/commands/setup.md`

7. ✅ **Automatic settings file writing**
   - Auto-merges with existing settings
   - Backs up before writing
   - User can opt for manual edit
   - File: `plugins/google-ads/commands/setup.md`

8. ✅ **Restart verification**
   - Checks if env vars loaded after restart
   - Provides recovery steps if not detected
   - Prevents "setup complete" when credentials not loaded
   - File: `plugins/google-ads/commands/setup.md`

## Commits

Total: 8 commits

1. `fix(google-ads): remove env vars from .mcp.json to fix MCP connection`
2. `fix(google-ads): pin exact dependency versions`
3. `docs(google-ads): add README with env var requirements`
4. `docs(google-ads): add env vars overview to setup wizard`
5. `docs(google-ads): split OAuth consent screen into separate step`
6. `feat(google-ads): add OAuth file auto-detection to setup`
7. `feat(google-ads): add automatic settings file writing`
8. `feat(google-ads): add restart verification with env var check`

## Testing Needed

Before merging:
1. Fresh install test (clean environment)
2. Upgrade test (v1.0.0 → v1.1.0)
3. Setup wizard happy path
4. Setup wizard error paths (skip restart, wrong file paths)
5. Auto-detection with 0, 1, 3+ OAuth files
6. Settings merge with existing vs new settings.json

## Success Metrics (Expected)

- ✅ Zero MCP connection failures after setup
- ✅ No dependency conflicts on fresh install
- ✅ Env vars documented in 2+ locations
- ✅ 50% reduction in manual steps (auto-detection + auto-write)
- ✅ Restart verification catches missing restart 100%
- ✅ No OAuth consent screen errors

## Next Steps

1. Run testing plan
2. Create PR with all 8 commits
3. Update plugin version to v1.1.0
4. Publish to marketplace
```

**Step 3: Verify summary created**

Run: `test -f docs/plans/completed/2025-12-22-google-ads-setup-improvements-summary.md && echo "✓ Summary created"`

Expected: "✓ Summary created"

**Step 4: Move design doc to completed**

Run:
```bash
git mv docs/plans/2025-12-22-google-ads-setup-improvements.md \
        docs/plans/completed/2025-12-22-google-ads-setup-improvements-design.md
```

Expected: Design doc moved to completed folder

**Step 5: Commit completion artifacts**

```bash
git add docs/plans/completed/
git commit -m "docs: add google-ads setup improvements completion summary"
```

---

## Testing Checklist

After implementation, verify:

- [ ] `.mcp.json` has no `env` section
- [ ] `requirements.txt` has exact version pins (==)
- [ ] `README.md` exists and documents all 5 env vars
- [ ] `setup.md` has "What You'll Need" section
- [ ] `setup.md` OAuth flow split into two steps
- [ ] `setup.md` has auto-detection search logic
- [ ] `setup.md` has automatic settings write with backup
- [ ] `setup.md` has restart verification with env var check
- [ ] All 5 env var names consistent across all files
- [ ] All JSON files are valid
- [ ] 8 commits created with descriptive messages

---

## Notes for Implementer

**Environment variable names (must be exact):**
1. `GOOGLE_ADS_DEVELOPER_TOKEN`
2. `GOOGLE_ADS_LOGIN_CUSTOMER_ID`
3. `GOOGLE_ADS_CLIENT_ID`
4. `GOOGLE_ADS_CLIENT_SECRET`
5. `GOOGLE_ADS_REFRESH_TOKEN`

**Key principles:**
- DRY: Don't duplicate env var lists unnecessarily
- YAGNI: Only add what the design specifies
- TDD: Verify each change works before committing
- Frequent commits: One commit per task (8 total)

**Be careful with:**
- JSON syntax in `.mcp.json` (no trailing commas)
- Python indentation in bash scripts (settings merge)
- Markdown formatting in setup.md (nested lists, code blocks)
- File paths (use exact paths from design doc)
