# Changelog

All notable changes to the Nano Banana Pro plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-12-28

### Changed
- Updated Gemini models to latest state-of-the-art versions:
  - Pro Tier: `gemini-2.0-flash-preview-image-generation` -> `gemini-3-pro-image-preview`
  - Flash Tier: `gemini-2.0-flash-preview-image-generation` -> `gemini-2.5-flash-image`
- Updated documentation to reflect 4K generation capabilities of the new Pro model.

## [1.0.0] - 2025-01-01

### Added
- Initial release of Nano Banana Pro plugin
- MCP server integration with Gemini API for image generation
- `generate_image` tool with full control over generation parameters
  - Model selection (Flash/Pro/Auto)
  - Aspect ratio control (1:1, 16:9, 9:16, 21:9, 4:3, 3:4, 2:1)
  - Thinking level configuration (LOW/HIGH)
  - Google Search grounding support
  - File output option
- `quick_generate` tool for simplified generation with smart defaults
- `list_files` tool for viewing uploaded files
- `upload_file` tool for adding files to Gemini Files API
- `delete_file` tool for removing uploaded files
- Smart model selection based on prompt analysis
- Image generation skill with comprehensive workflow
- Image creator agent for guided image creation
- Setup command wizard for easy configuration
- Detailed documentation (README, GETTING_STARTED)
- Prompt engineering tips and aspect ratio guide
- Authentication test script

### Technical
- FastMCP-based MCP server implementation
- Async HTTP client (httpx) for API communication
- Pydantic models for input validation
- Comprehensive error handling and reporting
