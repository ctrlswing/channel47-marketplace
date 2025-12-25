# Changelog

## [2.0.0] - 2025-12-25

### Added
- New `/write` skill consolidating 5 content operations (edit-draft, generate-content, improve-opening, strengthen-ending, remove-ai-tells)
- Progressive disclosure pattern for style guide loading
- `writing-patterns.md` reference file for AI pattern detection
- `style-guide-loader.md` for explicit chunk routing
- Mode auto-detection based on content characteristics

### Changed
- `/configure` renamed from `/generate-style-guide`
- `/review` enhanced with writing-patterns.md reference for consistent feedback

### Removed (BREAKING CHANGES)
- `/edit-draft` - Use `/write` instead
- `/generate-content` - Use `/write` instead
- `/improve-opening` - Use `/write --mode opening`
- `/strengthen-ending` - Use `/write --mode ending`
- `/remove-ai-tells` - Use `/write --mode clean`

Migration: All removed skills are now modes of the unified `/write` skill with auto-detection.

## [1.0.0] - 2025-12-21

### Added
- Initial release
- Seven core skills: edit-draft, generate-content, review-writing, improve-opening, strengthen-ending, remove-ai-tells, generate-style-guide
- Default style guide with smart chunking
- Settings file support via `.claude/creative-writing.local.md`
- Custom style guide support with `--style-guide` parameter
