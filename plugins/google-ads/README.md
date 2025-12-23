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

After adding credentials, restart Claude Code for changes to take effect (exit, run `claude`, then use `/resume` to return to your session).

## Troubleshooting

### MCP Server Won't Connect

1. Verify all 5 environment variables are set in your settings file
2. Restart Claude Code completely (exit with `Ctrl+C`/`Cmd+Q`, run `claude`, then `/resume`)
3. Check for typos in variable names (they're case-sensitive)
4. Run verification: `python ~/.claude/plugins/cache/channel47/google-ads/*/scripts/test_auth.py`

### Invalid Grant Error

**Cause:** Your OAuth refresh token has expired or been revoked.

**Common Scenarios:**
- OAuth app is in "Testing" mode (tokens expire after 7 days)
- Refresh token was manually revoked in Google Cloud Console
- OAuth credentials were deleted/regenerated

**Quick Fix (~2 minutes):**
1. Re-run `/google-ads:setup`
2. Skip to Phase 5 (Generate Refresh Token)
3. Copy new `GOOGLE_ADS_REFRESH_TOKEN` to your settings
4. Restart Claude Code

**Prevent Future Expiration:**
- Publish your OAuth app to "Production" mode (optional)
- See `/google-ads:setup` wizard for publishing instructions
- Direct link: https://console.cloud.google.com/apis/credentials/consent
- Note: If you can't find publish controls, tokens will expire every 7 days

### Developer Token Issues

- Token must have at least "Basic" access level for production use
- "Test" access only works with test accounts
- Apply for access at: Google Ads → Tools & Settings → API Center
