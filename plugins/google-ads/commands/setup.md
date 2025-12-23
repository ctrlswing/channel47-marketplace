---
description: Interactive guide for setting up Google Ads API credentials
---

# Google Ads Setup Wizard

This command guides you through configuring OAuth credentials for the Google Ads plugin.

## What You'll Need

This setup wizard will help you configure these 5 environment variables:

1. **GOOGLE_ADS_DEVELOPER_TOKEN** - Your Google Ads API developer token (from Google Ads API Center)
2. **GOOGLE_ADS_LOGIN_CUSTOMER_ID** - Your MCC (Manager) account ID (10 digits)
3. **GOOGLE_ADS_CLIENT_ID** - OAuth 2.0 client ID (from Google Cloud Console)
4. **GOOGLE_ADS_CLIENT_SECRET** - OAuth 2.0 client secret (from Google Cloud Console)
5. **GOOGLE_ADS_REFRESH_TOKEN** - OAuth refresh token (generated during this setup)

These will be saved to your Claude Code settings file (`~/.claude/settings.json` or project-specific).

---

## Phase 1: Prerequisites Check

First, let me verify your environment:

**Checking Python version...**

Run: `python3 --version`

Expected: Python 3.10 or higher

If Python not found or version too old:
- Install Python 3.10+ from https://python.org
- Restart Claude Code after installation (exit, run `claude`, then `/resume`)

**Checking plugin dependencies...**

Run: `pip show google-ads mcp pydantic 2>/dev/null | grep Name`

If any missing:
```bash
pip install -r ${CLAUDE_PLUGIN_ROOT}/requirements.txt
```

Expected: All dependencies installed successfully

**Checking setup scripts...**

Run: `ls ${CLAUDE_PLUGIN_ROOT}/scripts/*.py`

Expected: Shows generate_refresh_token.py and test_auth.py

---

## Phase 2: Google Cloud Project Setup

I'll walk you through setting up your Google Cloud project and OAuth credentials.

### Have you created a Google Cloud project?

**If NO:**
1. Go to https://console.cloud.google.com/
2. Click "Select a project" → "New Project"
3. Name it (e.g., "Google Ads API")
4. Click "Create"

**If YES:** ✓ Great, let's continue.

### Have you enabled the Google Ads API?

**If NO:**
1. In Google Cloud Console, go to "APIs & Services" → "Library"
2. Search for "Google Ads API"
3. Click on it and press "Enable"
4. Wait for enablement to complete

**If YES:** ✓ API is ready.

### Step 1: Configure OAuth Consent Screen (Required First)

Before creating credentials, you must configure the consent screen.

**Navigation - Use Direct URL (Recommended):**
1. Go directly to: https://console.cloud.google.com/apis/credentials/consent
2. This ensures you're on the correct page for consent screen configuration

**Alternative Navigation:**
1. Google Cloud Console → "APIs & Services" → "OAuth consent screen"
2. NOTE: If you see "OAuth Overview" with charts, you're on the wrong page - use direct URL above

---

**If you've already configured and published the consent screen:**
✓ Skip to Step 2

**If not configured yet:**

1. On the OAuth consent screen page, select **User Type: External**
2. Click "Create"
3. Fill in required fields:
   - **App name:** "Google Ads MCP" (or your preference)
   - **User support email:** your email
   - **Developer contact:** your email
4. Click "Save and Continue" through:
   - Scopes screen (no changes needed)
   - Test users screen (no changes needed)
5. You should now see a summary page

---

### Publishing Your OAuth App (Optional but Recommended)

**About Publishing Status:**

Your OAuth app can be in two modes:
- **Testing Mode** (default): Refresh tokens expire after 7 days
- **Production Mode** (published): Refresh tokens work indefinitely

**Should you publish?**

✅ **PUBLISH if:** You want permanent tokens without re-authentication
⚠️ **SKIP if:** You're okay regenerating tokens every 7 days (takes ~2 minutes with `/google-ads:setup`)

**How to Publish:**

**Option A: If you can find "PUBLISH APP" button**
1. Look for "Publishing status: Testing" on the consent screen page
2. Click the "PUBLISH APP" button
3. Confirm the dialog
4. Status should change to "In production"

**Option B: If you cannot find publishing controls**
This is a known UI inconsistency in Google Cloud Console.

Try:
1. Direct link: https://console.cloud.google.com/apis/credentials/consent
2. Or: APIs & Services → Credentials → Click your OAuth Client ID → Check for publishing status

**Option C: Skip publishing for now**
- Proceed with setup as-is
- Your tokens will work for 7+ days
- When they expire, re-run `/google-ads:setup` (Phase 5 only, ~2 minutes)
- Token regeneration is much faster than initial setup

---

**What if my tokens expire?**

**Symptoms:**
- Error: "invalid_grant" when using Google Ads tools
- Authentication failures after 7+ days

**Quick Fix (2 minutes):**
1. Run: `/google-ads:setup`
2. Skip to Phase 5 (Generate Refresh Token)
3. Copy new `GOOGLE_ADS_REFRESH_TOKEN` to your settings
4. Restart Claude Code

Note: You don't need to recreate OAuth credentials, just regenerate the token.

---

Respond with 'done' when consent screen is configured (published or not).

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

Run: `test -f "[USER_PROVIDED_PATH]" && echo "File exists" || echo "File not found"`

Expected: "File exists"

**Copying to plugin scripts directory...**

Run: `cp "[USER_PROVIDED_PATH]" ${CLAUDE_PLUGIN_ROOT}/scripts/client_secrets.json`

Expected: File copied successfully

---

## Phase 3: Google Ads Developer Token

### Do you have a Google Ads developer token?

**If NO:**
1. Sign in to your Google Ads **MCC (Manager) account**
2. Click "Tools & Settings" (wrench icon)
3. Under "Setup", click "API Center"
4. Apply for developer token
5. Fill out the application form
6. **Important:** You need at least "Basic" access for production use
7. Wait for approval (can take 1-2 business days)

**If YES:** ✓ Great!

### What is your developer token?

Paste your developer token here:

**[Wait for user input]**

**Validating format...**

Basic validation: Token should be alphanumeric, typically 22 characters

**Stored temporarily:** dev_tok...*** (last 3 chars masked)

---

## Phase 4: MCC Account ID

### What is your MCC (Manager) account ID?

Your MCC account ID is found in Google Ads:
- Top right corner, click on the customer ID
- Look for the Manager account (has sub-accounts beneath it)
- Format: 123-456-7890 or 1234567890

Paste your MCC account ID here:

**[Wait for user input]**

**Validating format...**

Expected: 10 digits (dashes optional)

**Formatted:** [1234567890] (dashes removed)

---

## Phase 5: Generate Refresh Token

Now I'll run the OAuth flow to generate a refresh token.

**About to run:** `python ${CLAUDE_PLUGIN_ROOT}/scripts/generate_refresh_token.py`

This script will:
1. Open a URL for you to authorize the app
2. Redirect you to a URL after authorization
3. Ask you to paste that redirect URL back

**Ready? Let's start the OAuth flow.**

Run: `cd ${CLAUDE_PLUGIN_ROOT}/scripts && python generate_refresh_token.py`

**Follow the instructions in the terminal:**

1. Copy the URL that appears
2. Open it in your browser
3. Sign in with the Google account that has access to your MCC
4. Click "Allow" to grant permissions
5. You'll be redirected to a URL starting with `http://localhost` or `urn:ietf:wg:oauth:2.0:oob`
6. Copy the ENTIRE redirect URL
7. Paste it back into the terminal

**Expected output:**
```
Your refresh token is: 1//0abc123...xyz
```

**Refresh token generated successfully!**

Stored temporarily: 1//...*** (masked)

---

## Phase 6: Configuration Summary

Here's your complete Google Ads configuration:

```
Developer Token:     dev_tok...***
MCC Account ID:      1234567890
Client ID:           123...apps.googleusercontent.com
Client Secret:       GOC...***
Refresh Token:       1//...***
```

**These credentials will be saved to your Claude Code settings.**

---

## Phase 7: Save to Settings

I'll guide you to save these environment variables.

### Where do you want to save these credentials?

**Options:**

1. **User-level** (recommended) - `~/.claude/settings.json`
   - Available to all projects on this machine
   - Best for personal use

2. **Project-level** - `.claude/settings.json`
   - Shared with team via git (⚠️ NOT recommended for secrets)
   - Use this only for non-sensitive project settings

3. **Local project** - `.claude/settings.local.json`
   - This project only, this machine only
   - Not shared via git (gitignored)
   - Good for project-specific secrets

**Your choice:** [Wait for user input: user/project/local]

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

[Wait for user confirmation]

---

## Phase 8: Verification

⚠️ **IMPORTANT: Restart Claude Code now**

Your credentials are saved, but Claude Code needs to restart to load them into the environment.

**Steps to restart:**
1. Exit Claude completely:
   - Press `Ctrl+C` (Linux/Windows) or `Cmd+Q` (Mac)
   - Or type `exit` if in a shell
2. Wait 2-3 seconds for complete shutdown
3. Start Claude again: `claude`
4. Return to this conversation: Type `/resume` and select this conversation

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

1. **Completely exit Claude** (not just this conversation):
   - `Ctrl+C` or `Cmd+Q` to quit the CLI
   - Verify the process is gone: `ps aux | grep claude`
2. **Wait 5 seconds**
3. **Start fresh Claude session**: `claude`
4. **Resume this conversation**: Type `/resume` and select this conversation, then respond with 'restarted'

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

---

**Common Error Messages:**

### Error: "invalid_grant"
**Cause:** Refresh token is invalid or expired
**Fix:**
- Re-run this setup wizard: `/google-ads:setup`
- Make sure OAuth consent screen is "Published" (not "Testing")
- Testing mode tokens expire after 7 days

### Error: "invalid_client"
**Cause:** Client ID or Client Secret is incorrect
**Fix:**
- Double-check these values in Google Cloud Console
- Re-run setup wizard and carefully copy credentials

### Error: "Developer token only approved for test accounts"
**Cause:** Developer token has Test access, not Basic/Standard
**Fix:**
- Go to Google Ads API Center
- Apply for Basic or Standard access
- Wait for approval

### Error: "Permission denied"
**Cause:** Authenticated user doesn't have access to MCC account
**Fix:**
- Verify MCC account ID is correct
- Ensure the Google account you authorized has at least Read-only access to the MCC
- Try authorizing with a different Google account that has access

### Error: "Customer not found"
**Cause:** MCC account ID is incorrect
**Fix:**
- Verify the MCC account ID in Google Ads
- Make sure you're using the Manager account ID, not a sub-account

---

## Support

Need help?
- Documentation: https://channel47.dev/plugins/google-ads
- Re-run setup: `/setup`
- Test credentials: `python ~/.claude/plugins/google-ads/scripts/test_auth.py`
