# ASCII Art Plugin

Generate ASCII art logos, banners, diagrams, and decorative text for CLI tools and documentation.

Inspired by CLI agents like Claude Code and Gemini CLI that use ASCII art to create memorable brand experiences.

## Features

| Skill | Description |
|-------|-------------|
| `/text` | Create ASCII text art - logos, banners, boxes, and effects (replaces generate-logo, generate-banner, generate-box, text-effects) |
| `/diagrams` | Create diagrams - flowcharts, trees, tables, architecture, sequence (replaces generate-diagram, generate-art) |

## Quick Examples

### Generate a Logo
```
/text "ACME" --type logo --style block
```
```
 █████╗  ██████╗███╗   ███╗███████╗
██╔══██╗██╔════╝████╗ ████║██╔════╝
███████║██║     ██╔████╔██║█████╗
██╔══██║██║     ██║╚██╔╝██║██╔══╝
██║  ██║╚██████╗██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝ ╚═════╝╚═╝     ╚═╝╚══════╝
```

### Create a Banner
```
/text "Welcome to My CLI" --type banner --style rounded
```
```
╭─────────────────────────────────╮
│      Welcome to My CLI          │
╰─────────────────────────────────╯
```

### Generate a Diagram
```
/diagrams "User clicks button → API validates → Database saves → Success message" --type flowchart
```
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    User     │────▶│     API     │────▶│  Database   │────▶│   Success   │
│   clicks    │     │  validates  │     │    saves    │     │   message   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

## Installation

```bash
/plugin marketplace add ctrlswing/channel47-marketplace
```

Then use any skill with `/skill-name`.

## Available Font Styles

| Style | Description |
|-------|-------------|
| `standard` | Classic ASCII art with clean lines |
| `block` | Bold letters using Unicode block characters |
| `slant` | Italicized/slanted for a dynamic feel |
| `banner` | Large, simple letters using hash symbols |
| `small` | Compact 3-line font for inline use |

## Border Styles

| Style | Characters | Best For |
|-------|------------|----------|
| `simple` | ┌─┐ │ └─┘ | General use |
| `double` | ╔═╗ ║ ╚═╝ | Emphasis, headers |
| `rounded` | ╭─╮ │ ╰─╯ | Friendly, approachable |
| `heavy` | ┏━┓ ┃ ┗━┛ | Warnings, important info |
| `ascii` | +-+ \| +-+ | Maximum compatibility |
| `dashed` | ┌╌┐ ╎ └╌┘ | Subtle framing |
| `dotted` | ┌┄┐ ┆ └┄┘ | Light borders |
| `stars` | *** * *** | Celebrations |
| `mixed` | Heavy + light | Visual hierarchy |

## Text Effects

| Effect | Description |
|--------|-------------|
| `shadow` | Drop shadow beneath text |
| `3d` | Extruded 3D appearance |
| `outline` | Hollow outlined letters |
| `gradient` | Color gradient across text |
| `rainbow` | Full spectrum colors |
| `neon` | Glowing neon effect |
| `glitch` | Distorted cyberpunk style |
| `retro` | Vintage terminal aesthetic |

## Color Support

Add ANSI colors to banners, boxes, and text effects:

```
--color red       # Error messages
--color green     # Success states
--color yellow    # Warnings
--color blue      # Information
--color sunset    # Gradient: red → orange → yellow
--color ocean     # Gradient: dark blue → cyan
--color matrix    # Gradient: dark → bright green
```

## Use Cases

- **CLI Splash Screens**: Create memorable startup logos
- **Documentation**: Add visual structure with boxes and banners
- **README Headers**: Stand out with ASCII logos
- **Diagrams**: Visualize architecture and flows in plain text
- **Terminal Art**: Add personality to your tools

## How It Works

The plugin uses progressive disclosure to load only relevant documentation:

- `/text` auto-detects type (logo, banner, box) and loads font or border references on-demand
- `/diagrams` auto-detects type (flowchart, tree, table, architecture, sequence) and loads diagram patterns
- Reference files (`font-loader.md`, `diagram-patterns.md`, examples) are loaded only when needed

This keeps token usage efficient while maintaining quality.

## Documentation

- [Getting Started](./GETTING_STARTED.md) - Detailed setup and usage guide
- [Changelog](./CHANGELOG.md) - Version history

## Reference Assets

- [ANSI Colors](./assets/reference/ansi-colors.md) - Terminal color codes and gradients
- [Character Ramps](./assets/reference/character-ramps.md) - Shading density characters
- [Spinners & Animations](./assets/reference/spinners-animations.md) - Animation frame patterns
- [Font Patterns](./assets/fonts/) - Character patterns for each font style
- [Examples](./assets/examples/) - Logo, border, and diagram galleries

## License

MIT - See [LICENSE](./LICENSE)
