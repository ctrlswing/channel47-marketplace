# ASCII Art Plugin Implementation Plan

## Overview

Create a skills-based plugin for generating ASCII art, inspired by CLI agents like Claude Code and Gemini CLI that use ASCII art logos to create memorable brand experiences. This plugin will enable users to create text-based logos, banners, decorative elements, and diagrams for CLI tools, documentation, and creative projects.

## Plugin Type Decision

**Chosen: Skills-based plugin** (like creative-writing)

Rationale:
- ASCII art generation is primarily a content generation/transformation task
- No external APIs or persistent state required
- Skills can leverage Claude's pattern recognition and creative abilities
- Simpler architecture, faster to implement
- Could be extended with MCP server later if image-to-ASCII conversion is desired

---

## Plugin Structure

```
plugins/ascii-art/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── generate-logo/
│   │   └── SKILL.md           # Text-to-ASCII logo banners (figlet-style)
│   ├── generate-banner/
│   │   └── SKILL.md           # Decorative banners with borders
│   ├── generate-box/
│   │   └── SKILL.md           # Box/frame around text content
│   ├── generate-diagram/
│   │   └── SKILL.md           # ASCII diagrams (flowcharts, trees, tables)
│   ├── generate-art/
│   │   └── SKILL.md           # Freeform ASCII art from descriptions
│   └── text-effects/
│       └── SKILL.md           # Stylized text (shadow, 3D, outline)
├── assets/
│   ├── fonts/                 # Reference font patterns
│   │   ├── block.md
│   │   ├── banner.md
│   │   ├── slant.md
│   │   ├── small.md
│   │   └── standard.md
│   └── examples/
│       ├── logos.md           # Example logos for reference
│       ├── borders.md         # Border/box patterns
│       └── diagrams.md        # Diagram examples
├── README.md
├── GETTING_STARTED.md
├── CHANGELOG.md
└── LICENSE
```

---

## Skill Specifications

### 1. generate-logo

**Purpose**: Create large ASCII text logos in various font styles (similar to figlet/toilet CLI tools)

**Arguments**:
| Name | Description | Required | Flag |
|------|-------------|----------|------|
| text | The text to convert to ASCII logo | true | false |
| style | Font style: block, banner, slant, small, standard | false | true |
| width | Maximum character width (default: 80) | false | true |

**Example Output**:
```
  ____ _                 _
 / ___| | __ _ _   _  __| | ___
| |   | |/ _` | | | |/ _` |/ _ \
| |___| | (_| | |_| | (_| |  __/
 \____|_|\__,_|\__,_|\__,_|\___|
```

**Workflow**:
1. Parse input text and style preference
2. Load character patterns for selected font style
3. Render each character using the pattern
4. Combine and align characters
5. Output formatted ASCII art

---

### 2. generate-banner

**Purpose**: Create decorative banners with borders and optional styling

**Arguments**:
| Name | Description | Required | Flag |
|------|-------------|----------|------|
| text | Banner text content | true | false |
| style | Border style: simple, double, rounded, heavy, ascii | false | true |
| width | Banner width (auto-fits if not specified) | false | true |
| align | Text alignment: left, center, right | false | true |

**Example Output**:
```
╔══════════════════════════════════════╗
║     Welcome to Channel47 CLI         ║
║     Version 2.0.0                    ║
╚══════════════════════════════════════╝
```

**Border Style Examples**:
```
simple:   +--+    double:  ╔══╗    rounded: ╭──╮    heavy: ┏━━┓
          |  |             ║  ║             │  │           ┃  ┃
          +--+             ╚══╝             ╰──╯           ┗━━┛
```

---

### 3. generate-box

**Purpose**: Wrap existing content in decorative ASCII boxes

**Arguments**:
| Name | Description | Required | Flag |
|------|-------------|----------|------|
| content | Content to wrap in a box (text or @file) | true | false |
| style | Box style: simple, double, rounded, heavy, shadow | false | true |
| title | Optional title for the box header | false | true |
| padding | Internal padding (default: 1) | false | true |

**Example Output**:
```
┌─ Configuration ──────────────────────┐
│                                      │
│  API_KEY=your_key_here               │
│  DEBUG=false                         │
│  PORT=3000                           │
│                                      │
└──────────────────────────────────────┘
```

---

### 4. generate-diagram

**Purpose**: Create ASCII diagrams from descriptions or structured data

**Arguments**:
| Name | Description | Required | Flag |
|------|-------------|----------|------|
| description | Natural language description or structured input | true | false |
| type | Diagram type: flowchart, tree, table, sequence, architecture | false | true |
| style | Line style: unicode, ascii-only | false | true |

**Example Outputs**:

*Flowchart*:
```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Start  │────▶│ Process │────▶│   End   │
└─────────┘     └─────────┘     └─────────┘
                    │
                    ▼
               ┌─────────┐
               │ Branch  │
               └─────────┘
```

*Tree*:
```
src/
├── components/
│   ├── Button.tsx
│   └── Input.tsx
├── utils/
│   └── helpers.ts
└── index.ts
```

*Table*:
```
┌──────────┬─────────┬──────────┐
│ Feature  │ Status  │ Priority │
├──────────┼─────────┼──────────┤
│ Auth     │ Done    │ High     │
│ API      │ WIP     │ High     │
│ Tests    │ Pending │ Medium   │
└──────────┴─────────┴──────────┘
```

---

### 5. generate-art

**Purpose**: Create freeform ASCII art from text descriptions

**Arguments**:
| Name | Description | Required | Flag |
|------|-------------|----------|------|
| description | Description of the ASCII art to create | true | false |
| size | Approximate size: small, medium, large | false | true |
| style | Art style: detailed, minimal, emoji-hybrid | false | true |

**Example Output** (description: "a rocket launching"):
```
        /\
       /  \
      /    \
     |  CC  |
     |      |
    /|      |\
   / |      | \
  |  |      |  |
  |  |      |  |
  |__|      |__|
     |  /\  |
     | /  \ |
     |/ ** \|
      \ ** /
       \  /
        \/
       /||\
      / || \
     /  ||  \
    ~~~~  ~~~~
```

---

### 6. text-effects

**Purpose**: Apply visual effects to text (shadows, 3D, outlines)

**Arguments**:
| Name | Description | Required | Flag |
|------|-------------|----------|------|
| text | Text to apply effects to | true | false |
| effect | Effect type: shadow, 3d, outline, double, wave | false | true |
| direction | Effect direction for shadow/3d: right, left, down | false | true |

**Example Outputs**:

*Shadow effect*:
```
 HELLO
░HELLO
```

*3D effect*:
```
 __  __  ____  __    __     ___
|  \/  || ___||  |  |  |   / _ \
| |\/| ||  _| |  |__|  |__| | | |
|_|  |_||____||_____|_____| |_| |
       /_____/_____/\___/
```

*Outline effect*:
```
╔╗╔╗╔═╗╦  ╦  ╔═╗
╠╣║╣║  ║  ║  ║ ║
╩ ╩╚╝╚═╝╩═╝╩═╝╚═╝
```

---

## Font Assets

The plugin will include reference character patterns for consistent rendering:

### fonts/standard.md
- Complete A-Z, 0-9, common symbols
- 5-6 lines height
- Standard FIGlet-style patterns

### fonts/block.md
- Bold, blocky characters using ▓░▒█
- High visual impact for logos

### fonts/slant.md
- Italicized/slanted ASCII text
- Dynamic, modern feel

### fonts/small.md
- Compact 3-line height
- Good for inline headers

### fonts/banner.md
- Large, banner-style letters
- Maximum visibility

---

## Implementation Steps

### Phase 1: Foundation Setup
1. Create plugin directory structure
2. Create `.claude-plugin/plugin.json` manifest
3. Add plugin to marketplace.json registry
4. Create README.md and GETTING_STARTED.md

### Phase 2: Core Skills Implementation
5. Implement `generate-logo` skill with standard font
6. Implement `generate-banner` skill with border styles
7. Implement `generate-box` skill for content framing

### Phase 3: Advanced Skills
8. Implement `generate-diagram` skill with multiple diagram types
9. Implement `generate-art` skill for freeform creation
10. Implement `text-effects` skill

### Phase 4: Asset Library
11. Create font pattern references in assets/fonts/
12. Create example collections in assets/examples/
13. Document all available patterns

### Phase 5: Documentation & Polish
14. Complete GETTING_STARTED.md with usage examples
15. Create CHANGELOG.md
16. Add LICENSE file
17. Test all skills and refine prompts

---

## Plugin Manifest

```json
{
  "name": "ascii-art",
  "version": "1.0.0",
  "description": "Generate ASCII art logos, banners, diagrams, and decorative text for CLI tools and documentation",
  "author": {
    "name": "Jackson",
    "url": "https://channel47.dev"
  },
  "homepage": "https://channel47.dev/plugins/ascii-art",
  "repository": "https://github.com/ctrlswing/channel47-marketplace"
}
```

## Marketplace Entry

```json
{
  "name": "ascii-art",
  "source": "./plugins/ascii-art",
  "description": "Generate ASCII art logos, banners, diagrams, and decorative text for CLI tools and documentation",
  "version": "1.0.0",
  "author": { "name": "Jackson" },
  "category": "creative",
  "tags": ["ascii-art", "cli", "logos", "banners", "diagrams", "text-art", "creative"]
}
```

---

## Usage Examples

After installation, users can:

```bash
# Generate a logo
/generate-logo Claude --style slant

# Create a welcome banner
/generate-banner "Welcome to My CLI" --style rounded --align center

# Wrap config in a box
/generate-box @.env.example --title "Environment Variables" --style double

# Create a flowchart
/generate-diagram "User clicks login -> Validate credentials -> Success/Failure branches" --type flowchart

# Generate freeform art
/generate-art "a cat sitting at a computer" --size medium

# Apply text effects
/text-effects "IMPORTANT" --effect shadow
```

---

## Future Enhancements (Post v1.0)

1. **MCP Server Extension**: Add image-to-ASCII conversion using Python PIL
2. **Animation Frames**: Generate multi-frame ASCII animations for CLI spinners
3. **Color Support**: ANSI color codes for terminal output
4. **Export Formats**: Save as .txt, embed in markdown, copy to clipboard
5. **Font Gallery**: Interactive font preview and selection
6. **Custom Fonts**: Allow users to define their own character patterns

---

## Success Criteria

- [ ] All 6 skills implemented and functional
- [ ] Consistent output quality across skills
- [ ] Comprehensive documentation with examples
- [ ] Font assets provide reliable character rendering
- [ ] Plugin successfully registered in marketplace
- [ ] Users can generate professional-looking ASCII art with minimal input
