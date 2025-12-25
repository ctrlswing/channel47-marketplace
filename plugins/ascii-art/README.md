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

## Use Cases

- **CLI Splash Screens**: Create memorable startup logos
- **Documentation**: Add visual structure with boxes and banners
- **README Headers**: Stand out with ASCII logos
- **Diagrams**: Visualize architecture and flows in plain text
- **Terminal Art**: Add personality to your tools

## Documentation

- [Getting Started](./GETTING_STARTED.md) - Detailed setup and usage guide
- [Changelog](./CHANGELOG.md) - Version history

## License

MIT - See [LICENSE](./LICENSE)
