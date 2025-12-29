# Getting Started with ASCII Art

This guide will help you get up and running with the ASCII Art plugin.

## Installation

Install the Channel47 marketplace to get access to the ASCII Art plugin:

```bash
/plugin marketplace add ctrlswing/channel47-marketplace
```

## Basic Usage

### Generate a Logo

Create eye-catching ASCII logos for your CLI tools:

```bash
# Basic logo with default (standard) font
/generate-logo "Hello"

# With a specific font style
/generate-logo "ACME" --style block

# Available styles: standard, block, slant, banner, small
```

**Example output (block style):**
```
 █████╗  ██████╗███╗   ███╗███████╗
██╔══██╗██╔════╝████╗ ████║██╔════╝
███████║██║     ██╔████╔██║█████╗
██╔══██║██║     ██║╚██╔╝██║██╔══╝
██║  ██║╚██████╗██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝ ╚═════╝╚═╝     ╚═╝╚══════╝
```

### Create Banners

Wrap text in decorative borders:

```bash
# Basic banner
/generate-banner "Welcome!"

# With style and alignment
/generate-banner "Version 2.0" --style rounded --align center

# Multi-line banner
/generate-banner "App Name\nVersion 1.0\nBy Author" --style double
```

**Example output:**
```
╔═══════════════════════════════════╗
║            App Name               ║
║           Version 1.0             ║
║            By Author              ║
╚═══════════════════════════════════╝
```

### Box Content

Frame existing content in ASCII boxes:

```bash
# Basic box
/generate-box "Important note here"

# With title
/generate-box "API_KEY=xxx\nDEBUG=false" --title "Configuration"

# From a file
/generate-box @.env.example --title "Environment Variables" --style double
```

**Example output:**
```
┌─ Configuration ────────────────────┐
│                                    │
│  API_KEY=xxx                       │
│  DEBUG=false                       │
│                                    │
└────────────────────────────────────┘
```

### Create Diagrams

Generate diagrams from natural language:

```bash
# Flowchart
/generate-diagram "Start -> Process data -> Validate -> Save to DB -> End" --type flowchart

# Directory tree
/generate-diagram "src with components and utils folders, components has Button and Input" --type tree

# Table
/generate-diagram "Columns: Name, Status, Priority. Rows: Auth/Done/High, API/WIP/Medium" --type table

# Sequence diagram
/generate-diagram "Client sends request to Server, Server queries Database, Database returns data" --type sequence
```

### Generate Freeform Art

Create custom ASCII art from descriptions:

```bash
# Animals
/generate-art "a cute cat"

# Objects
/generate-art "a rocket ship" --size large

# With style
/generate-art "a heart" --style geometric --size small
```

### Apply Text Effects

Add visual effects to text:

```bash
# Shadow effect
/text-effects "IMPORTANT" --effect shadow

# 3D effect
/text-effects "HELLO" --effect 3d

# Other effects: outline, double, wave, glitch
```

## Font Style Guide

| Style | Height | Best For | Example Use |
|-------|--------|----------|-------------|
| `standard` | 5-6 lines | General logos | README headers |
| `block` | 6 lines | Maximum impact | Splash screens |
| `slant` | 5 lines | Modern/dynamic | Tech products |
| `banner` | 5 lines | Retro aesthetic | Classic tools |
| `small` | 3 lines | Space-constrained | Inline headers |

## Border Style Guide

| Style | Appearance | Best For |
|-------|------------|----------|
| `simple` | Single lines │ ─ | General content |
| `double` | Double lines ║ ═ | Important info |
| `rounded` | Curved corners ╭╮╰╯ | Friendly messages |
| `heavy` | Bold lines ┃ ━ | Warnings/errors |
| `ascii` | Basic chars +- | Legacy terminals |
| `shadow` | With shadow effect | Callouts |

## Diagram Types

### Flowchart
Describe your process step by step:
```
/generate-diagram "User submits form, if valid save to DB else show error"
```

### Tree
Describe hierarchy with parent/child relationships:
```
/generate-diagram "project folder with src and tests, src has index.ts and utils.ts"
```

### Table
Provide columns and rows:
```
/generate-diagram "Table: Name, Role, Status | Alice, Admin, Active | Bob, User, Pending"
```

### Sequence
Describe interactions in order:
```
/generate-diagram "Browser calls API, API queries Cache, if miss API queries DB"
```

### Architecture
Describe components and connections:
```
/generate-diagram "Load balancer connects to 3 web servers, all connect to primary DB with replica"
```

## Tips & Best Practices

1. **Use UPPERCASE** for logos - renders more consistently
2. **Keep text short** for effects - 1-6 characters work best for 3D
3. **Specify width** if output is too wide for your terminal
4. **Use ascii style** when targeting systems without Unicode support
5. **Combine skills** - generate a logo, then wrap it in a box!

## Troubleshooting

**Logo looks misaligned?**
- Ensure your terminal uses a monospace font
- Try a different font style (small or standard)

**Characters look wrong?**
- Your terminal may not support Unicode
- Use `--style ascii` for maximum compatibility

**Diagram too complex?**
- Break it into multiple simpler diagrams
- Be more specific in your description

## Examples Gallery

Check the `assets/examples/` folder for more inspiration:
- `logos.md` - Logo design examples
- `borders.md` - Border and box patterns
- `diagrams.md` - Diagram templates

## Next Steps

- Explore all available options with `/help generate-logo`
- Check the font patterns in `assets/fonts/`
- Create your own ASCII art collection!
