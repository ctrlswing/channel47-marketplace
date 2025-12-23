# Google Ads Plugin Setup Improvements

**Date:** 2025-12-22
**Author:** Jackson
**Status:** Design Complete

## Problem Statement

User testing of the Google Ads plugin setup flow revealed critical issues that blocked functionality and created unnecessary friction:

### Critical Issues
1. **MCP Server Connection Failures** - Empty env vars in `.mcp.json` overrode values from `settings.json`, preventing the MCP server from connecting after setup
2. **Dependency Version Conflicts** - `mcp~=1.2.0` was incompatible with `fastmcp 2.13.0.2` (requires `mcp>=1.17.0`), causing runtime failures

### UX Friction Points
3. **OAuth Consent Screen Confusion** - Instructions didn't match Google's actual flow (consent screen required before OAuth client creation)
4. **Manual File Path Entry** - Users had to manually type full paths to downloaded OAuth JSON files
5. **No Restart Verification** - No confirmation that Claude Code was actually restarted or that env vars loaded
6. **Unclear Environment Variables** - After removing env vars from `.mcp.json`, no clear documentation of what's required

## Goals

1. **Fix plugin structure issues** that block functionality
2. **Improve setup UX** with hybrid automation (speed + transparency)
3. **Document requirements** clearly in multiple locations
4. **Verify critical steps** to catch common mistakes

## Design

### 1. Plugin Structure Changes

#### 1.1 Remove `.mcp.json` Environment Variables

**Current `.mcp.json`:**
```json
{
  "mcpServers": {
    "google-ads": {
      "command": "python3",
      "args": ["${CLAUDE_PLUGIN_ROOT}/src/google_ads_mcp.py"],
      "env": {
        "GOOGLE_ADS_DEVELOPER_TOKEN": "",
        "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "",
        "GOOGLE_ADS_CLIENT_ID": "",
        "GOOGLE_ADS_CLIENT_SECRET": "",
        "GOOGLE_ADS_REFRESH_TOKEN": ""
      }
    }
  }
}
```

**New `.mcp.json`:**
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

**Rationale:** Empty strings in the `env` section override values from `settings.json`. Removing the section entirely allows proper inheritance from Claude Code's environment.

#### 1.2 Pin Exact Dependency Versions

**Current `requirements.txt`:**
```txt
mcp~=1.2.0
google-ads~=28.0
google-auth~=2.32
google-auth-oauthlib~=1.2
google-auth-httplib2~=0.1
pydantic~=2.8
httpx~=0.27
python-dotenv~=1.0
grpcio~=1.66
protobuf~=5.27
```

**New `requirements.txt`:**
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

**Rationale:** Exact version pinning prevents compatibility issues. The `mcp~=1.2.0` caused a critical failure because `fastmcp 2.13.0.2` requires `mcp>=1.17.0`.

### 2. Environment Variables Documentation

#### 2.1 Create Plugin README

Add `README.md` at plugin root (`plugins/google-ads/README.md`):

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

#### 2.2 Update Setup Command Documentation

Add environment variables reference section at the top of `commands/setup.md` (after description, before Phase 1):

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

**Rationale:** Users see what they're working toward before starting the setup process. README provides permanent reference, setup command shows context during the flow.

### 3. Setup Command UX Improvements

#### 3.1 Auto-Detect OAuth Credentials File

**Location:** Phase 2, after user downloads `client_secrets.json`

**Current flow:**
```markdown
### Where did you save client_secrets.json?

Please provide the full path to your client_secrets.json file:

**[Wait for user input]**
```

**New flow:**
```markdown
### Locating your OAuth credentials file

Let me search for recently downloaded OAuth credential files...

[Search ~/Downloads/, ~/Desktop/, and current directory for client_secret_*.json]

**If 1 file found:**
✓ Found: ~/Downloads/client_secret_1013756079418-k3im53gjmt719n7mau715gvihdkal3ji.apps.googleusercontent.com.json
  Modified: 2 minutes ago

Use this file? [yes/no]

**If multiple files found:**
Found multiple OAuth credential files:
1. ~/Downloads/client_secret_123.json (2 minutes ago)
2. ~/Downloads/client_secret_456.json (3 days ago)
3. ~/Desktop/client_secret_789.json (1 week ago)

Which file should I use? [1/2/3] or provide custom path:

**If none found:**
I didn't find any OAuth credential files in common locations.

Please provide the full path to your client_secrets.json file:
```

**Implementation:** Use `find` with `-mtime` to search common locations, sort by modification time.

#### 3.2 Automatic Settings File Writing

**Location:** Phase 7, saving credentials

**Current flow:**
```markdown
Based on your choice, add these to your settings file:

File to edit: ~/.claude/settings.json

[Shows JSON to copy]

Please manually edit the file and add the JSON above.

After you've saved the settings file, respond with 'done'.
```

**New flow:**
```markdown
I'll add these credentials to ~/.claude/settings.json:

Environment variables to add:
  • GOOGLE_ADS_DEVELOPER_TOKEN: 86M...tkg
  • GOOGLE_ADS_LOGIN_CUSTOMER_ID: 3461276031
  • GOOGLE_ADS_CLIENT_ID: 1013...apps.googleusercontent.com
  • GOOGLE_ADS_CLIENT_SECRET: GOC...LiTi
  • GOOGLE_ADS_REFRESH_TOKEN: 1//0...C4I

Proceed with writing to ~/.claude/settings.json? [yes/no]

[If yes:]
✓ Credentials saved to ~/.claude/settings.json

[If no:]
Cancelled. Here's the JSON to add manually:
[Shows JSON]
```

**Implementation:**
1. Read existing `~/.claude/settings.json` (or create if missing)
2. Parse JSON
3. Merge new env vars into existing `env` section (or create section)
4. Write back with proper formatting (2-space indent)
5. Confirm success

#### 3.3 OAuth Consent Screen Reordering

**Location:** Phase 3 (OAuth credentials creation)

**Current flow:**
```markdown
### Have you created OAuth 2.0 credentials?

**If NO:**
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. If prompted, configure OAuth consent screen:
   [Instructions here]
```

**New flow:**
```markdown
### Step 1: Configure OAuth Consent Screen (Required First)

Before creating credentials, you must configure the consent screen:

1. Go to "APIs & Services" → "OAuth consent screen"
2. Select **User Type: External**, then click "Create"
3. Fill in required fields:
   - **App name:** "Google Ads MCP"
   - **User support email:** your email
   - **Developer contact:** your email
4. Click "Save and Continue" through remaining screens
5. **CRITICAL:** Click "Publish App" (don't leave in Testing mode or tokens expire in 7 days)

Respond with 'done' when consent screen is configured and published.

### Step 2: Create OAuth Client ID

Now create the OAuth credentials:

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. Select **Application type: Desktop app**
4. Name: "Google Ads MCP Client"
5. Click "Create"
6. **IMPORTANT:** Click "DOWNLOAD JSON" button
7. Save the file

Where did you save the file? [Auto-detect flow from 3.1]
```

**Rationale:** Matches Google's actual flow. Consent screen is required before OAuth client creation. Making this explicit prevents the "must configure consent screen" error.

### 4. Restart Verification Flow

**Location:** Phase 8 (Verification)

**Current flow:**
```markdown
**Important: Restart Claude Code now for settings to take effect.**

After restarting, let's verify your configuration works:

[Immediately tries to run test_auth.py]
```

**New flow:**
```markdown
⚠️ **IMPORTANT: Restart Claude Code now**

Your credentials are saved, but Claude Code needs to restart to load them.

**Steps:**
1. Exit Claude Code completely (Ctrl+C or Cmd+Q)
2. Start Claude Code again: `claude`
3. Resume this session: `claude /resume`

After restarting and resuming, respond with 'done' and I'll verify automatically.

[Wait for user response]

---

[When user returns with 'done' or 'restarted']

Checking if environment variables are loaded...

[Run check: if [ -z "$GOOGLE_ADS_DEVELOPER_TOKEN" ]; then ...]

**Scenario A: Env vars detected**
✓ Environment variables detected!

Let me test the connection to Google Ads API...

[Run test_auth.py]

🎉 Success! Your Google Ads plugin is ready.

**Scenario B: Env vars NOT detected**
❌ Environment variables not detected

It looks like the restart didn't take effect. Please:

1. Completely exit Claude Code (not just this conversation)
2. Start a fresh Claude Code session
3. Run: `claude /resume` to return here
4. Respond with 'restarted' and I'll check again

If you're certain you restarted, verify credentials are in:
  ~/.claude/settings.json

[Show command to check: cat ~/.claude/settings.json | grep GOOGLE_ADS]
```

**Implementation:**
1. Check for presence of `$GOOGLE_ADS_DEVELOPER_TOKEN` environment variable
2. If present, proceed to verification test
3. If absent, show clear error with recovery instructions
4. Provide `claude /resume` command explicitly

**Rationale:** Catches the common mistake of not restarting or restarting incorrectly. Provides clear recovery path.

## Implementation Plan

### Phase 1: Plugin Structure Fixes (Critical)
1. Update `.mcp.json` - remove `env` section
2. Update `requirements.txt` - pin exact versions
3. Test: Install fresh, verify MCP server connects
4. Test: Verify env var inheritance from settings.json

### Phase 2: Documentation
1. Create `plugins/google-ads/README.md`
2. Update `commands/setup.md` - add env vars reference section
3. Test: Review for clarity and completeness

### Phase 3: Setup Command UX - Auto-Detection
1. Implement OAuth file auto-detection in Phase 2
2. Add search logic for `~/Downloads/`, `~/Desktop/`, `.`
3. Add file picker with timestamps
4. Test with 0, 1, and multiple files

### Phase 4: Setup Command UX - Auto-Writing
1. Implement settings file auto-write in Phase 7
2. Add JSON merge logic (preserve existing settings)
3. Add confirmation prompt before writing
4. Test with existing and new settings files

### Phase 5: Setup Command UX - Flow Improvements
1. Reorder OAuth consent screen instructions (Phase 3)
2. Add restart verification logic (Phase 8)
3. Add env var detection check
4. Add `claude /resume` instructions
5. Test complete flow end-to-end

## Success Criteria

1. **Zero MCP connection failures** after completing setup
2. **No dependency version conflicts** on fresh install
3. **Clear documentation** of required env vars in 2+ locations
4. **Faster setup flow** with auto-detection (fewer manual steps)
5. **Restart verification** catches missing restart 100% of the time
6. **No OAuth consent screen errors** with reordered instructions

## Testing Plan

1. **Fresh install test** on clean environment
2. **Upgrade test** from v1.0.0 to updated version
3. **Happy path** - user follows all instructions correctly
4. **Error paths** - user skips restart, provides wrong paths, etc.
5. **Multiple files** - test auto-detection with 0, 1, 3+ OAuth files
6. **Settings merge** - test with existing vs new settings.json files

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Pinned versions become outdated | Medium | Document version update process, test before bumping |
| Auto-detection misses OAuth file | Low | Always provide manual path fallback |
| Settings auto-write corrupts file | High | Validate JSON before writing, backup existing file |
| Restart verification false negative | Medium | Test thoroughly, provide manual verification command |

## Open Questions

None - design is complete and validated.
