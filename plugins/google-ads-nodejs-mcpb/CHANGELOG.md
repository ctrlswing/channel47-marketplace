# Changelog

All notable changes to the Google Ads MCP Server (Node.js) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-25

### Added

- Initial release of Google Ads MCP Server as Node.js MCPB bundle
- **Tools**:
  - `run_google_ads_gaql`: Execute any GAQL query for data retrieval
  - `google_ads_list_accounts`: List accessible accounts under MCC
- **Features**:
  - OAuth 2.0 authentication with refresh token
  - Read-only safety enforcement (blocks mutation operations)
  - Response truncation at 25,000 characters
  - Comprehensive error handling with query context
  - Debug logging to stderr
  - Timeout management (2 minute default)
- **MCPB Compliance**:
  - Manifest version 0.3
  - User configuration schema for credentials
  - Platform compatibility (darwin, win32, linux)
  - Node.js 18+ runtime requirement
- **Documentation**:
  - README with usage examples and GAQL reference
  - GETTING_STARTED guide for setup
  - Inline JSDoc comments

### Migrated From

- Python implementation in `plugins/google-ads/src/google_ads_mcp.py`
- Maintains feature parity with Python version
- Uses same environment variable names for easy migration
