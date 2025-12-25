# Changelog

All notable changes to the ASCII Art plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-12-25

### Added

- New `/text` skill consolidating 4 text operations (generate-logo, generate-banner, generate-box, text-effects)
- New `/diagrams` skill consolidating 2 diagram operations (generate-diagram, generate-art)
- Progressive disclosure pattern for asset file loading
- `font-loader.md` reference mapping styles to font files
- `diagram-patterns.md` reference for box drawing characters and layouts
- Example reference files for logos, banners, and boxes
- Type auto-detection based on content characteristics

### Changed

- Font files now explicitly referenced by skills (progressive disclosure)
- Color references now loaded on-demand when --color specified

### Removed (BREAKING CHANGES)

- `/generate-logo` - Use `/text` instead
- `/generate-banner` - Use `/text --type banner`
- `/generate-box` - Use `/text --type box`
- `/text-effects` - Use `/text --effect [name]`
- `/generate-diagram` - Use `/diagrams`
- `/generate-art` - Use `/diagrams` or `/text`

Migration: All removed skills are now unified under `/text` (for text art) and `/diagrams` (for structural diagrams) with auto-detection.

---

## [1.1.0] - 2024-12-25

### Added

- **New border styles**: dashed, dotted, stars, mixed for banners and boxes
- **Color support**: ANSI color options for banners, boxes, and text effects
- **Gradient presets**: sunset, ocean, matrix, fire, purple, grayscale
- **New text effects**: gradient, rainbow, neon, retro
- **Status icons**: info, success, warning, error, tip, note for boxes
- **Intensity control**: light, medium, heavy options for effects
- **Reference assets**:
  - ANSI color codes reference with gradient palettes
  - Character density ramps for shading
  - Spinner and animation frame patterns

### Enhanced

- **generate-banner**: Added 4 new border styles (dashed, dotted, stars, mixed), color support, gradient presets
- **generate-box**: Added 4 new styles (dashed, ascii, nested, callout), status icons, color support
- **text-effects**: Added 4 new effects (gradient, rainbow, neon, retro), color/gradient options, intensity control

---

## [1.0.0] - 2024-12-25

### Added

- Initial release of ASCII Art plugin
- **generate-logo**: Create ASCII text logos in multiple font styles
  - Supports: standard, block, slant, banner, small fonts
  - Configurable width constraint
- **generate-banner**: Create decorative banners with borders
  - Supports: simple, double, rounded, heavy, ascii border styles
  - Text alignment options: left, center, right
  - Multi-line support
- **generate-box**: Wrap content in ASCII boxes
  - Optional title headers
  - Configurable padding
  - Shadow effect option
  - File input support via @file references
- **generate-diagram**: Create ASCII diagrams from descriptions
  - Flowcharts with decision points
  - Directory trees
  - Data tables
  - Sequence diagrams
  - Architecture diagrams
  - Unicode and ASCII-only modes
- **generate-art**: Generate freeform ASCII art
  - Size options: small, medium, large
  - Style options: detailed, minimal, geometric, retro
- **text-effects**: Apply visual effects to text
  - Shadow effect with direction control
  - 3D extruded text
  - Outline style
  - Double-struck text
  - Wave effect
  - Glitch effect

### Assets

- Font pattern references for 5 font styles
- Example galleries for logos, borders, and diagrams
- Complete character reference documentation
