# Changelog

All notable changes to the Nano Banana Pro plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-12-28

### Added
- **Future-Ready Architecture**: New `number_of_images` parameter implemented for future API support (currently limited to 1 by Gemini API)
- **Content Safety Controls**: New `safety_level` parameter with four filtering levels:
  - `STRICT` (default): Maximum content filtering (BLOCK_LOW_AND_ABOVE)
  - `MODERATE`: Balanced filtering (BLOCK_MEDIUM_AND_ABOVE)
  - `PERMISSIVE`: Minimal filtering (BLOCK_ONLY_HIGH)
  - `OFF`: No filtering (BLOCK_NONE, may be overridden by API)
- **Reproducible Generation**: New `seed` parameter for deterministic image generation
- Safety settings mapping function to convert user-friendly levels to Gemini API format

### Changed
- Updated `GenerateImageInput` model with new optional parameters
- Enhanced generation config to include `candidateCount` and `seed` values
- All API requests now include explicit safety settings
- Fixed `aspectRatio` parameter structure (now correctly nested in `imageConfig`)

### Known Limitations
- **Multiple Images**: Gemini image models (gemini-2.5-flash-image, gemini-3-pro-image-preview) currently only support `candidateCount=1`. Google's separate Imagen API does support multiple images if needed.
- The code is architected to support multiple images when/if the Gemini API adds this capability

### Documentation
- Added examples for multiple image generation, seed usage, and safety levels
- Updated README.md with Advanced Parameters section
- Updated SKILL.md with detailed parameter documentation
- Enhanced usage examples in documentation

## [1.1.1] - 2025-12-28

### Fixed
- Fixed bug where `aspect_ratio` parameter was being ignored by the API because it was missing from the generation configuration.

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

### Note
- The `quick_generate` tool mentioned in early documentation was never implemented in the initial release
