# Google Ads MCP Plugin

Query Google Ads data using GAQL with OAuth authentication.

## Quick Start

1. Install the plugin:
   ```bash
   /plugin install google-ads@channel47
   ```

2. Run setup wizard:
   ```bash
   /setup
   ```

3. Try it out:
   ```
   "List my Google Ads accounts"
   "Find negative keyword opportunities for account 1234567890"
   ```

## What's Included

- **MCP Server** - Two essential tools:
  - List all accessible Google Ads accounts
  - Execute any GAQL query for custom analysis

- **Agent** - Negative Keyword Hunter
  - Analyzes search terms to identify wasted spend
  - Recommends negative keywords to add
  - Prioritizes by budget impact

- **Skill** - GAQL Query Guide
  - Reference for constructing effective queries
  - Field compatibility rules
  - Common query patterns

- **Command** - `/setup`
  - Interactive credential configuration wizard

## Requirements

- Python 3.10+
- Google Ads account with MCC access
- Google Cloud project with Ads API enabled
- OAuth 2.0 credentials

## Documentation

- [Getting Started Guide](GETTING_STARTED.md) - Detailed setup walkthrough
- [Changelog](CHANGELOG.md) - Version history

## Support

Visit [channel47.dev/plugins/google-ads](https://channel47.dev/plugins/google-ads) for examples and guides.
