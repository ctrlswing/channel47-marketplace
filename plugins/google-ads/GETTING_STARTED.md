# Getting Started with Google Ads MCP

## Prerequisites

- Python 3.10 or higher
- Google Ads account with API access
- Google Cloud project with Ads API enabled

## Step 1: Google Cloud Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google Ads API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download client secrets JSON

## Step 2: Generate Refresh Token

1. Run the OAuth setup script:
   ```bash
   python ${CLAUDE_PLUGIN_ROOT}/scripts/generate_refresh_token.py
   ```

2. Follow browser prompts to authorize

3. Copy the refresh token from terminal output

## Step 3: Configure Claude Code

Add to Claude Code settings or .env:

```
GOOGLE_ADS_DEVELOPER_TOKEN=your-developer-token
GOOGLE_ADS_LOGIN_CUSTOMER_ID=your-customer-id
GOOGLE_ADS_CLIENT_ID=your-client-id
GOOGLE_ADS_CLIENT_SECRET=your-client-secret
GOOGLE_ADS_REFRESH_TOKEN=your-refresh-token
```

## Step 4: Verify Installation

Test the connection:
```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/test_auth.py
```

## Troubleshooting

Common issues and solutions will be documented here as they arise.
