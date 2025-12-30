# Google Ads MCP Server (Node.js MCPB)

A Node.js MCP Bundle for querying Google Ads data using the Google Ads Query Language (GAQL). This server provides read-only access to campaign, keyword, search term, and account data through OAuth 2.0 authentication.

## Features

- **GAQL Query Execution**: Execute any valid Google Ads Query Language query
- **Account Discovery**: List all accessible accounts under your MCC
- **Read-Only Safety**: Mutation operations are blocked for safe exploration
- **OAuth 2.0 Authentication**: Secure authentication using refresh tokens
- **Response Optimization**: Automatic truncation for large datasets
- **Comprehensive Logging**: Debug-friendly logging to stderr

## Requirements

- Node.js 18.0.0 or higher
- Google Ads API access (Developer Token)
- Google Cloud OAuth 2.0 credentials
- An MCC (Manager) account with sub-accounts

## Installation

### As an MCPB Bundle

1. Install the MCPB CLI:
   ```bash
   npm install -g @anthropic-ai/mcpb
   ```

2. Pack the bundle:
   ```bash
   mcpb pack /path/to/google-ads-nodejs-mcpb
   ```

3. Install in your MCP host (e.g., Claude Desktop)

### For Development

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

3. Set environment variables (see Configuration below)
4. Run the server:
   ```bash
   npm start
   ```

## Configuration

The following environment variables are required:

| Variable | Description |
|----------|-------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Your Google Ads API Developer Token |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | MCC Account ID (10 digits, no dashes) |
| `GOOGLE_ADS_CLIENT_ID` | OAuth 2.0 Client ID from Google Cloud |
| `GOOGLE_ADS_CLIENT_SECRET` | OAuth 2.0 Client Secret |
| `GOOGLE_ADS_REFRESH_TOKEN` | OAuth 2.0 Refresh Token |

## Tools

### `run_google_ads_gaql`

Execute a GAQL query against a Google Ads account.

**Parameters:**
- `customer_id` (required): Google Ads customer ID (e.g., `1234567890` or `123-456-7890`)
- `query` (required): GAQL query string
- `use_streaming` (optional): Use streaming mode for large results (default: `false`)

**Example:**
```json
{
  "customer_id": "1234567890",
  "query": "SELECT campaign.name, metrics.impressions, metrics.clicks FROM campaign WHERE segments.date DURING LAST_7_DAYS"
}
```

### `google_ads_list_accounts`

List all accessible Google Ads accounts under the MCC.

**Parameters:**
- `response_format` (optional): Output format - `"markdown"` or `"json"` (default: `"markdown"`)

**Example:**
```json
{
  "response_format": "json"
}
```

## Common GAQL Queries

### Campaign Performance
```sql
SELECT
  campaign.name,
  campaign.status,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
```

### Keyword Performance
```sql
SELECT
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.impressions,
  metrics.clicks,
  metrics.average_cpc
FROM keyword_view
WHERE segments.date DURING LAST_7_DAYS
ORDER BY metrics.clicks DESC
LIMIT 100
```

### Search Term Report
```sql
SELECT
  search_term_view.search_term,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM search_term_view
WHERE segments.date DURING LAST_14_DAYS
  AND metrics.impressions > 10
ORDER BY metrics.cost_micros DESC
LIMIT 200
```

## GAQL Resources

| Resource | Description |
|----------|-------------|
| `campaign` | Campaign-level settings and metrics |
| `ad_group` | Ad group configuration |
| `keyword_view` | Keyword performance data |
| `search_term_view` | Search query reports |
| `ad_group_ad` | Ad-level data |
| `customer` | Account information |
| `customer_client` | MCC sub-accounts |

## Security

- **Read-Only**: Mutation keywords (CREATE, UPDATE, REMOVE, MUTATE) are blocked
- **OAuth 2.0**: Uses secure refresh token authentication
- **No Secrets in Code**: All credentials via environment variables
- **Response Limits**: Automatic truncation at 25,000 characters

## Error Handling

The server provides detailed error messages including:
- Missing configuration errors with specific variable names
- GAQL query errors with the failing query
- API errors with Google Ads error details
- Timeout errors for long-running queries

## Development

### Project Structure
```
google-ads-nodejs-mcpb/
├── manifest.json       # MCPB manifest (v0.3)
├── package.json        # Node.js dependencies
├── server/
│   └── index.js        # MCP server implementation
├── README.md           # This file
└── GETTING_STARTED.md  # Setup guide
```

### Testing

Run the server in development mode:
```bash
GOOGLE_ADS_DEVELOPER_TOKEN=xxx \
GOOGLE_ADS_LOGIN_CUSTOMER_ID=1234567890 \
GOOGLE_ADS_CLIENT_ID=xxx \
GOOGLE_ADS_CLIENT_SECRET=xxx \
GOOGLE_ADS_REFRESH_TOKEN=xxx \
node server/index.js
```

### Packing

Create an MCPB bundle:
```bash
npm run pack
# or
mcpb pack .
```

## License

MIT License - See LICENSE file for details.

## Related

- [Google Ads API Documentation](https://developers.google.com/google-ads/api/docs/start)
- [GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
- [MCP Specification](https://modelcontextprotocol.io/)
- [MCPB Documentation](https://github.com/anthropics/mcpb)
