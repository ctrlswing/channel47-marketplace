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
