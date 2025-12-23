# Changelog

## [1.2.0] - 2025-12-23

### Fixed
- **Dependency conflicts** blocking installation for new users
  - Updated httpx, pydantic, python-dotenv, google-auth, grpcio, protobuf to compatible version ranges
  - Resolves conflicts with mcp 1.25.0 and fastmcp 2.13.0.2
- **OAuth consent screen publishing instructions** causing user confusion
  - Added direct URL to Google Cloud Console OAuth consent screen
  - Made publishing optional with clear trade-offs (Testing vs Production modes)
  - Provided 3 fallback options when UI doesn't match documentation
  - Added comprehensive token expiration troubleshooting guide
- **Incorrect restart command** documentation
  - Corrected `claude code` to `claude` throughout all documentation
  - Added `/resume` instructions for returning to conversations after restart

### Changed
- Updated all documentation (setup.md, README.md, GETTING_STARTED.md) with improved clarity
- Enhanced troubleshooting sections with time estimates and step-by-step fixes

## [1.0.0] - 2024-12-21

### Added
- Initial release
- MCP server with 2 core tools (list accounts, run GAQL)
- Negative keyword hunter agent for wasted spend analysis
- GAQL query guide skill for LLM reference
- Interactive `/setup` command for OAuth credential configuration
- Python scripts for token generation and auth testing
- Comprehensive documentation (README, GETTING_STARTED)

### Technical Details
- Trimmed MCP server from 8 tools to 2 essential tools
- OAuth 2.0 authentication with refresh token
- Support for Python 3.10+
- Compatible with Google Ads API v28+
