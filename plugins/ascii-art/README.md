# ASCII Art Plugin

Generate ASCII art logos, banners, diagrams, and decorative text for CLI tools and documentation.

Inspired by CLI agents like Claude Code and Gemini CLI that use ASCII art to create memorable brand experiences.

## Features

| Skill | Description |
|-------|-------------|
| `/generate-logo` | Create large ASCII text logos in various font styles |
| `/generate-banner` | Create decorative banners with customizable borders |
| `/generate-box` | Wrap content in ASCII boxes with optional titles |
| `/generate-diagram` | Create flowcharts, trees, tables, and architecture diagrams |
| `/generate-art` | Generate freeform ASCII art from descriptions |
| `/text-effects` | Apply shadow, 3D, outline, and other effects to text |

## Quick Examples

### Generate a Logo
```
/generate-logo "ACME" --style block
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
/generate-banner "Welcome to My CLI" --style rounded
```
```
╭─────────────────────────────────╮
│      Welcome to My CLI          │
╰─────────────────────────────────╯
```

### Generate a Diagram
```
/generate-diagram "User clicks button -> API validates -> Database saves -> Success message" --type flowchart
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
