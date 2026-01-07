# Google Ads Specialist Plugin

A Claude Code plugin for Google Ads campaign management using GAQL (Google Ads Query Language). This plugin provides a minimal 3-tool MCP server with progressive disclosure through skill files, enabling comprehensive read and write access to Google Ads campaigns, keywords, search terms, and account data.

## Architecture

**Version 3.1.0** introduces npm-based MCP server distribution:

- **NPM Package**: MCP server published as `@channel47/google-ads-mcp`
- **Auto-Installation**: Server installed via npx on first use
- **3 Core MCP Tools**: Minimal data access layer (list_accounts, query, mutate)
- **9 Skill Files**: Progressive disclosure of Google Ads domain knowledge
- **PreToolUse Hook**: Validates skill reference before query/mutate operations
- **~200 Lines of Server Code**: Down from 718 lines

### Design Philosophy

The MCP server is distributed as a standalone npm package and automatically installed when the plugin is activated. The plugin provides:
- **Atomic Skills** (7): Single-operation patterns (performance, search terms, QS, budget, negatives, bids, wasted spend)
- **Playbooks** (1): Multi-step workflows (account health audit)
- **Troubleshooting** (1): Error handling and debugging (GAQL errors)

Claude references skill files to learn proper GAQL patterns, then executes via the core tools.

## Features

- **Minimal Tool Surface**: Just 3 tools vs 13 in previous versions
- **Progressive Disclosure**: Domain knowledge in readable skill files
- **Hook Validation**: Prevents hallucinated queries by requiring skill references
- **Full GAQL Access**: Any SELECT query via `query` tool
- **Safe Mutations**: Write operations via `mutate` tool with dry_run default
- **OAuth 2.0 Authentication**: Secure refresh token auth

## Requirements

- Node.js 18.0.0 or higher
- Google Ads API access (Developer Token)
- Google Cloud OAuth 2.0 credentials
- Claude Code (for plugin installation)

## Installation

### As a Claude Code Plugin

Install via the Claude Code plugin marketplace:

1. Open Claude Code
2. Navigate to Plugin Marketplace
3. Search for "Google Ads Specialist"
4. Click Install

The plugin will automatically install the required MCP server (`@channel47/google-ads-mcp`) via npx when first activated.

**Manual Installation:**

1. Clone this repository
2. Copy to your Claude Code plugins directory: `~/.claude/plugins/google-ads-specialist`
3. Configure OAuth credentials (see GETTING_STARTED.md)

The MCP server is distributed as an npm package and installed automatically. No manual server setup required.

## Configuration

The MCP server requires these environment variables. Configure them before activating the plugin:

**Required:**

| Variable | Description |
|----------|-------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Your Google Ads API Developer Token |
| `GOOGLE_ADS_CLIENT_ID` | OAuth 2.0 Client ID from Google Cloud |
| `GOOGLE_ADS_CLIENT_SECRET` | OAuth 2.0 Client Secret |
| `GOOGLE_ADS_REFRESH_TOKEN` | OAuth 2.0 Refresh Token |

Optional:

| Variable | Description |
|----------|-------------|
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | MCC Account ID (10 digits, no dashes) |
| `GOOGLE_ADS_DEFAULT_CUSTOMER_ID` | Default account ID for queries |

See `GETTING_STARTED.md` for OAuth setup instructions.

**Note:** The MCP server (`@channel47/google-ads-mcp`) is automatically installed via npx. You do not need to manually install it.

## Core MCP Tools

### 1. list_accounts

List all accessible Google Ads accounts.

**Parameters:**
- `include_manager_accounts` (boolean, optional): Include MCC accounts (default: false)

**Example:**
```json
{
  "include_manager_accounts": false
}
```

### 2. query

Execute any GAQL SELECT query. **Requires skill reference** (enforced by hook).

**Parameters:**
- `customer_id` (string, optional): Account ID (uses default if not specified)
- `query` (string, required): Full GAQL SELECT query
- `limit` (integer, optional): Max rows to return (default: 100, max: 10000)

**Example:**
```json
{
  "query": "SELECT campaign.name, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_30_DAYS",
  "limit": 50
}
```

### 3. mutate

Execute write operations via GoogleAdsService.Mutate. **Requires skill reference** (enforced by hook).

**Parameters:**
- `customer_id` (string, optional): Account ID
- `operations` (array, required): Array of mutation operation objects
- `partial_failure` (boolean, optional): Enable partial failure mode (default: true)
- `dry_run` (boolean, optional): Validate only, don't execute (default: **true** for safety)

**Example:**
```json
{
  "operations": [
    {
      "campaign_criterion_operation": {
        "create": {
          "campaign": "customers/1234567890/campaigns/987654321",
          "negative": true,
          "keyword": {
            "text": "free",
            "match_type": "PHRASE"
          }
        }
      }
    }
  ],
  "dry_run": true
}
```

## Skills

Skills contain GAQL patterns, best practices, and troubleshooting guides. Reference skills before using `query` or `mutate` tools.

### Atomic Skills

1. **atomic-campaign-performance**: Query campaign metrics with date ranges and filters
2. **atomic-search-terms-report**: Analyze search queries triggering ads
3. **atomic-wasted-spend-analysis**: Identify high-spend, zero-conversion opportunities
4. **atomic-quality-score-audit**: Analyze Quality Score and improvement opportunities
5. **atomic-budget-pacing**: Check budget utilization and pacing
6. **atomic-add-negative-keywords**: Add negative keywords with mutation checklist
7. **atomic-adjust-bids**: Modify bids for keywords and ad groups

### Playbooks

8. **playbook-account-health-audit**: Comprehensive 6-step account health audit workflow

### Troubleshooting

9. **troubleshooting-gaql-errors**: Common GAQL errors, causes, and fixes

## Workflow Example

1. **User:** "Show me campaign performance for the last 30 days"

2. **Claude** references `atomic-campaign-performance` skill to learn GAQL pattern

3. **Claude** constructs query from skill example:
   ```sql
   SELECT campaign.id, campaign.name, metrics.cost_micros, metrics.conversions
   FROM campaign
   WHERE segments.date DURING LAST_30_DAYS
   ```

4. **Hook** detects skill reference in transcript and allows operation

5. **Tool** executes query and returns results

## Hook Validation

The PreToolUse hook prevents hallucinated queries:

- **Blocks** `query` and `mutate` operations without skill reference
- **Exempts** `list_accounts` (safe enumeration)
- **Fail-open** on errors (prevents workflow breakage)
- **Clear error message** directs Claude to reference appropriate skill

This ensures Claude always consults domain knowledge before executing operations.

## Architecture Details

### Server Structure (199 lines)

```
server/
├── index.js              # MCP server with 3 tools
├── auth.js              # OAuth authentication
├── tools/
│   ├── list-accounts.js  # Account enumeration
│   ├── gaql-query.js     # GAQL SELECT execution
│   └── mutate.js         # Write operations
├── resources/           # GAQL reference docs
├── prompts/             # Prompt templates
└── utils/               # Validation, formatting
```

### Skills Structure

```
skills/
├── atomic-campaign-performance/
│   └── SKILL.md
├── atomic-search-terms-report/
│   └── SKILL.md
├── atomic-wasted-spend-analysis/
│   └── SKILL.md
├── atomic-quality-score-audit/
│   └── SKILL.md
├── atomic-budget-pacing/
│   └── SKILL.md
├── atomic-add-negative-keywords/
│   └── SKILL.md
├── atomic-adjust-bids/
│   └── SKILL.md
├── playbook-account-health-audit/
│   ├── SKILL.md              # Main workflow
│   ├── audit-workflow.md     # Detailed steps
│   └── query-patterns.md     # Copy-paste queries
└── troubleshooting-gaql-errors/
    └── SKILL.md
```

### Hook Configuration

```
.claude/
├── hooks/
│   └── validate-google-ads.py   # Validation script
└── settings.json                # Hook registration
```

## Security

- **Dry Run Default**: Mutations default to `dry_run: true` for safety
- **Mutation Blocking**: Query tool blocks CREATE/UPDATE/REMOVE keywords
- **Hook Validation**: Requires skill reference before operations
- **OAuth 2.0**: Secure refresh token authentication
- **Input Validation**: All parameters validated before execution

## Development

This plugin uses the `@channel47/google-ads-mcp` npm package for the MCP server.

### Plugin Development

To modify skills or documentation:

1. Clone this repository
2. Edit skill files in `skills/`
3. Update documentation as needed
4. Test locally by copying to `~/.claude/plugins/google-ads-specialist`

### MCP Server Development

The MCP server is developed separately at [github.com/channel47/google-ads-mcp-server](https://github.com/channel47/google-ads-mcp-server).

To test with a local server build:
1. Clone the server repository
2. Update `.mcp.json` to point to local server: `"command": "node", "args": ["/path/to/server/index.js"]`
3. Restore npx command before committing

### Publish to Marketplace

```bash
npm run publish-to-marketplace
```

## Migration from v2.x

Version 3.0.0 is a **breaking change**:

**Removed:**
- 11 specialized tools (get_performance, search_terms_report, find_wasted_spend, etc.)
- All tools now accessible via `query` and `mutate` with skill guidance

**Migration Path:**
1. Update to v3.0.0
2. Reference appropriate skills for your use case
3. Use `query` tool with GAQL from skills
4. Use `mutate` tool for write operations (with dry_run checklist)

**Benefits:**
- Simpler mental model (3 tools instead of 13)
- More flexible (any GAQL query possible)
- Better learning (skills teach proper patterns)
- Safer (hook validation prevents mistakes)

## Resources

- [Getting Started Guide](GETTING_STARTED.md)
- [Changelog](CHANGELOG.md)
- [MCP Server (npm)](https://www.npmjs.com/package/@channel47/google-ads-mcp)
- [MCP Server (GitHub)](https://github.com/channel47/google-ads-mcp-server)
- [Google Ads API Docs](https://developers.google.com/google-ads/api/docs/start)
- [GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
- [Claude Code Documentation](https://code.claude.com/docs)

## License

MIT License - See LICENSE file for details.
