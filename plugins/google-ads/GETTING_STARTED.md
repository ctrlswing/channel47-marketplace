# Getting Started with Google Ads Plugin

This guide walks through the complete setup process for the Google Ads plugin.

## Prerequisites

### 1. Google Ads Account
- MCC (Manager) account with access to sub-accounts
- At least Read-only access level

### 2. Google Cloud Project
- Create project at https://console.cloud.google.com/
- Enable Google Ads API
- Create OAuth 2.0 credentials (Desktop app type)
- **Optional but Recommended:** Publish OAuth consent screen to Production mode
  - Testing mode: Tokens expire after 7 days (requires re-authentication)
  - Production mode: Tokens work indefinitely
  - See `/google-ads:setup` wizard for detailed publishing instructions
  - Can't find publish controls? Proceed anyway - tokens work for 7+ days

### 3. Developer Token
- Apply for token in Google Ads: Tools & Settings > Setup > API Center
- Basic or Standard access level required

## Installation

Install the plugin from the channel47 marketplace:

```bash
/plugin install google-ads@channel47
```

## Configuration

Run the interactive setup wizard:

```bash
/setup
```

The wizard will:
1. Check Python and dependencies
2. Guide you through obtaining OAuth credentials
3. Help generate a refresh token
4. Provide configuration for your settings.json

**Manual Setup Alternative:**

If you prefer to configure manually, add these to `~/.claude/settings.json`:

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "your_developer_token",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "1234567890",
    "GOOGLE_ADS_CLIENT_ID": "your_oauth_client_id",
    "GOOGLE_ADS_CLIENT_SECRET": "your_oauth_client_secret",
    "GOOGLE_ADS_REFRESH_TOKEN": "your_refresh_token"
  }
}
```

**Restart Claude Code** after updating settings (exit, run `claude`, then `/resume`).

## Verification

Test your configuration:

```bash
python ~/.claude/plugins/google-ads/scripts/test_auth.py
```

Or simply try:
```
"List my Google Ads accounts"
```

## Usage Examples

### Account Discovery
```
"List all my Google Ads accounts"
"Show me accounts under my MCC"
```

### Negative Keyword Discovery
```
"Find negative keyword opportunities for account 1234567890"
"Analyze search terms for wasted spend in the last 30 days"
"Show me search terms with zero conversions for account 1234567890"
```

### Custom GAQL Queries
```
"Run this GAQL query for account 1234567890:
SELECT campaign.name, metrics.cost_micros, metrics.conversions
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC"
```

### Using the Agent
The negative keyword hunter agent triggers automatically when you mention:
- "negative keywords"
- "wasted spend"
- "search terms analysis"

Or invoke directly:
```
"Run the negative keyword hunter for account 1234567890"
```

## Troubleshooting

### "Missing required environment variables"
- Ensure all 5 environment variables are set in settings.json
- Restart Claude Code after updating settings (exit, run `claude`, then `/resume`)

### "invalid_grant" during authentication
- Your refresh token expired
- Re-run the setup wizard to generate a new token
- Check that OAuth consent screen is "Published" (not "Testing")

### "Developer token only approved for test accounts"
- Apply for Basic or Standard access in Google Ads API Center
- Test accounts have limited functionality

### "Permission denied"
- Verify MCC account ID is correct (10 digits, no dashes)
- Ensure authenticated user has access to the MCC account

## Rate Limits

Google Ads API has rate limits:
- **Basic Access**: 15,000 operations per day
- **Standard Access**: 40 operations per second

The MCP server uses efficient querying patterns to stay within limits.

## Next Steps

- Try the negative keyword hunter on your accounts
- Learn GAQL query patterns for custom analysis
- Set up recurring checks for search term optimization

For more examples and guides, visit [channel47.dev/plugins/google-ads](https://channel47.dev/plugins/google-ads)
