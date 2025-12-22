---
description: Interactive guide for setting up Google Ads API credentials
---

# Google Ads Setup Wizard

This command guides you through configuring OAuth credentials for the Google Ads plugin.

## Phase 1: Prerequisites Check

First, let me verify your environment:

**Checking Python version...**

Run: `python3 --version`

Expected: Python 3.10 or higher

If Python not found or version too old:
- Install Python 3.10+ from https://python.org
- Restart Claude Code after installation

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

### Have you created OAuth 2.0 credentials?

**If NO:**
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. If prompted, configure OAuth consent screen:
   - User type: External
   - App name: "Google Ads MCP"
   - User support email: your email
   - Developer contact: your email
   - Click "Save and Continue" through remaining screens
   - **Important:** Publish the app (don't leave in Testing mode or tokens expire in 7 days)
4. Back to Create OAuth client ID:
   - Application type: "Desktop app"
   - Name: "Google Ads MCP Client"
   - Click "Create"
5. **Download JSON** - Click "DOWNLOAD JSON" button
6. Save file as `client_secrets.json`

**If YES:** ✓ You should have a client_secrets.json file.

### Where did you save client_secrets.json?

Please provide the full path to your client_secrets.json file:

**[Wait for user input]**

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

**Based on your choice, add these to your settings file:**

File to edit: `~/.claude/settings.json` (or project/local based on choice)

Add this JSON (merge with existing content if file exists):

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

**Would you like me to open the settings file for you?**

If YES:
Run: `code ~/.claude/settings.json` (or other editor based on availability)

If NO:
"Please manually edit the file at [path] and add the JSON above."

**After you've saved the settings file, respond with 'done'.**

[Wait for user confirmation]

---

## Phase 8: Verification

**Important: Restart Claude Code now for settings to take effect.**

After restarting, let's verify your configuration works:

Run: `cd ${CLAUDE_PLUGIN_ROOT}/scripts && python test_auth.py`

**Expected output:**
```
✓ Authentication successful!
✓ Connected to Google Ads API
✓ MCC Account: [Your MCC Name] (1234567890)
```

**If successful:**
```
🎉 Setup complete! Your Google Ads plugin is ready to use.

Try it out:
- "List my Google Ads accounts"
- "Find negative keyword opportunities for account 1234567890"
```

**If failed:**

Common issues and fixes:

### Error: "invalid_grant"
**Cause:** Refresh token is invalid or expired
**Fix:**
- Re-run this setup wizard: `/setup`
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
