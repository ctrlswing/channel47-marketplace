# Getting Started with Google Ads MCP Server (Node.js)

This guide walks you through setting up the Google Ads MCP Server from scratch.

## Prerequisites

Before you begin, ensure you have:

1. **Node.js 18+** installed ([download](https://nodejs.org/))
2. **A Google Ads account** with API access
3. **A Google Cloud project** with OAuth 2.0 configured
4. **An MCC (Manager) account** if querying multiple accounts

## Step 1: Google Cloud Project Setup

### 1.1 Create or Select a Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Note your project ID

### 1.2 Enable Google Ads API

1. Go to **APIs & Services** > **Library**
2. Search for "Google Ads API"
3. Click **Enable**

### 1.3 Configure OAuth Consent Screen

1. Go to **APIs & Services** > **OAuth consent screen**
2. Select **External** user type (or Internal for Workspace)
3. Fill in required fields:
   - App name: "Google Ads MCP Server"
   - User support email: Your email
   - Developer contact: Your email
4. Add scopes:
   - `https://www.googleapis.com/auth/adwords`
5. Add test users (your Google account email)
6. Save and continue

### 1.4 Create OAuth 2.0 Credentials

1. Go to **APIs & Services** > **Credentials**
2. Click **Create Credentials** > **OAuth client ID**
3. Application type: **Desktop app**
4. Name: "Google Ads MCP Client"
5. Click **Create**
6. Download the JSON file (you'll need `client_id` and `client_secret`)

## Step 2: Get Your Google Ads Developer Token

1. Sign in to [Google Ads](https://ads.google.com/)
2. Go to **Tools & Settings** > **API Center**
3. If you don't have a Developer Token:
   - Apply for one (requires MCC account)
   - Basic access is sufficient for read-only operations
4. Copy your Developer Token

## Step 3: Generate OAuth Refresh Token

You need a refresh token to authenticate without user interaction.

### Option A: Use the Python Helper Script

If you have the Python plugin installed:

```bash
cd plugins/google-ads
python scripts/generate_refresh_token.py
```

### Option B: Manual OAuth Flow

1. Create a file `get_token.js`:

```javascript
import { OAuth2Client } from 'google-auth-library';
import http from 'http';
import url from 'url';

const CLIENT_ID = 'YOUR_CLIENT_ID';
const CLIENT_SECRET = 'YOUR_CLIENT_SECRET';
const REDIRECT_URI = 'http://localhost:8080/oauth2callback';
const SCOPES = ['https://www.googleapis.com/auth/adwords'];

const oauth2Client = new OAuth2Client(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI);

// Generate auth URL
const authUrl = oauth2Client.generateAuthUrl({
  access_type: 'offline',
  scope: SCOPES,
  prompt: 'consent',
});

console.log('Open this URL in your browser:\n');
console.log(authUrl);
console.log('\nWaiting for authorization...');

// Start local server to receive callback
const server = http.createServer(async (req, res) => {
  const queryParams = new url.URL(req.url, 'http://localhost:8080').searchParams;
  const code = queryParams.get('code');

  if (code) {
    try {
      const { tokens } = await oauth2Client.getToken(code);
      console.log('\n--- Your Refresh Token ---');
      console.log(tokens.refresh_token);
      console.log('--------------------------\n');

      res.end('Authorization successful! You can close this window.');
      server.close();
      process.exit(0);
    } catch (error) {
      console.error('Error getting tokens:', error);
      res.end('Error: ' + error.message);
    }
  }
});

server.listen(8080);
```

2. Run it:
```bash
node get_token.js
```

3. Open the URL in your browser and authorize
4. Copy the refresh token from the output

## Step 4: Configure Environment Variables

### Option A: Claude Code Settings

Add to `~/.claude/settings.json`:

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "your_developer_token",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "1234567890",
    "GOOGLE_ADS_CLIENT_ID": "your_client_id.apps.googleusercontent.com",
    "GOOGLE_ADS_CLIENT_SECRET": "GOCSPX-your_client_secret",
    "GOOGLE_ADS_REFRESH_TOKEN": "1//0your_refresh_token"
  }
}
```

### Option B: Project-Level Settings

Add to `.claude/settings.json` in your project:

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "...",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "...",
    "GOOGLE_ADS_CLIENT_ID": "...",
    "GOOGLE_ADS_CLIENT_SECRET": "...",
    "GOOGLE_ADS_REFRESH_TOKEN": "..."
  }
}
```

### Option C: Shell Environment

```bash
export GOOGLE_ADS_DEVELOPER_TOKEN="your_developer_token"
export GOOGLE_ADS_LOGIN_CUSTOMER_ID="1234567890"
export GOOGLE_ADS_CLIENT_ID="your_client_id.apps.googleusercontent.com"
export GOOGLE_ADS_CLIENT_SECRET="GOCSPX-your_client_secret"
export GOOGLE_ADS_REFRESH_TOKEN="1//0your_refresh_token"
```

## Step 5: Install Dependencies

```bash
cd plugins/google-ads-nodejs-mcpb
npm install
```

## Step 6: Test the Server

### Quick Test

```bash
npm start
```

You should see startup logs. The server is now waiting for MCP connections.

### Test with Claude Code

1. Restart Claude Code to load the new MCP server
2. Try a command like:
   - "List my Google Ads accounts"
   - "Show campaign performance for account 1234567890"

## Step 7: Pack as MCPB (Optional)

To distribute as an MCPB bundle:

```bash
npm install -g @anthropic-ai/mcpb
mcpb pack .
```

This creates a `.mcpb` file ready for installation in compatible MCP hosts.

## Troubleshooting

### "Missing required environment variables"

Check that all 5 environment variables are set:
```bash
echo $GOOGLE_ADS_DEVELOPER_TOKEN
echo $GOOGLE_ADS_LOGIN_CUSTOMER_ID
echo $GOOGLE_ADS_CLIENT_ID
echo $GOOGLE_ADS_CLIENT_SECRET
echo $GOOGLE_ADS_REFRESH_TOKEN
```

### "invalid_grant" Error

Your refresh token may have expired or been revoked:
1. Generate a new refresh token (Step 3)
2. Update your settings

### "DEVELOPER_TOKEN_NOT_APPROVED"

Your developer token needs approval:
1. Apply for Basic Access in Google Ads API Center
2. Wait for approval (usually 24-48 hours)

### "CUSTOMER_NOT_FOUND"

Verify the customer ID:
- Must be 10 digits (no dashes)
- Must be accessible from your MCC account
- Use `google_ads_list_accounts` to see available accounts

### "PERMISSION_DENIED"

Check that:
1. Your Google account has access to the Google Ads account
2. The OAuth consent screen is properly configured
3. The `adwords` scope is included

### Query Errors

Common GAQL issues:
- **Incompatible fields**: Some fields can't be selected together
- **Missing WHERE clause**: Date segmentation requires date filter
- **Invalid resource**: Check the resource name spelling

## Rate Limits

| Access Level | Limit |
|--------------|-------|
| Basic | 15,000 operations/day |
| Standard | 40 operations/second |

## Next Steps

1. Explore available GAQL resources in the [README](./README.md)
2. Check out the [GAQL reference](https://developers.google.com/google-ads/api/docs/query/overview)
3. Review the [negative keyword hunter agent](../google-ads/agents/negative-keyword-hunter/) for advanced usage patterns
4. See the [GAQL query guide skill](../google-ads/skills/gaql-query-guide/) for query templates

## Support

- [Google Ads API Documentation](https://developers.google.com/google-ads/api/docs/start)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Report Issues](https://github.com/ctrlswing/channel47-marketplace/issues)
