---
name: generate-banner
description: Create decorative banners with customizable borders and styling
args:
  - name: text
    description: Banner text content (can be multi-line)
    required: true
  - name: style
    description: "Border style: simple, double, rounded, heavy, ascii, dashed, dotted, stars, mixed (default: double)"
    required: false
    flag: true
  - name: width
    description: Banner width (auto-fits to content if not specified)
    required: false
    flag: true
  - name: align
    description: "Text alignment: left, center, right (default: center)"
    required: false
    flag: true
  - name: color
    description: "ANSI color: red, green, blue, cyan, magenta, yellow, or gradient name (sunset, ocean, matrix)"
    required: false
    flag: true
---

# Generate Banner

Create decorative banners with borders for CLI tool headers, section dividers, and announcement displays.

## Available Border Styles

### simple
Basic single-line borders:
```
┌──────────────────────────────────────┐
│     Welcome to Channel47 CLI         │
│     Version 2.0.0                    │
└──────────────────────────────────────┘
```

### double (default)
Double-line borders for emphasis:
```
╔══════════════════════════════════════╗
║     Welcome to Channel47 CLI         ║
║     Version 2.0.0                    ║
╚══════════════════════════════════════╝
```

### rounded
Rounded corners for a softer look:
```
╭──────────────────────────────────────╮
│     Welcome to Channel47 CLI         │
│     Version 2.0.0                    │
╰──────────────────────────────────────╯
```

### heavy
Bold/heavy borders for maximum impact:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Welcome to Channel47 CLI         ┃
┃     Version 2.0.0                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

### ascii
ASCII-only characters for maximum compatibility:
```
+--------------------------------------+
|     Welcome to Channel47 CLI         |
|     Version 2.0.0                    |
+--------------------------------------+
```

### dashed
Dashed border for a lighter feel:
```
┌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┐
╎     Welcome to Channel47 CLI         ╎
╎     Version 2.0.0                    ╎
└╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘
```

### dotted
Dotted border for subtle framing:
```
┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┆     Welcome to Channel47 CLI         ┆
┆     Version 2.0.0                    ┆
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
```

### stars
Decorative star border for celebrations:
```
***************************************
*     Welcome to Channel47 CLI        *
*     Version 2.0.0                   *
***************************************
```

### mixed
Heavy outer border with light inner separators:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     Welcome to Channel47 CLI         ┃
┠──────────────────────────────────────┨
┃     Version 2.0.0                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Border Character Reference

| Style   | Top-Left | Top-Right | Bottom-Left | Bottom-Right | Horizontal | Vertical |
|---------|----------|-----------|-------------|--------------|------------|----------|
| simple  | ┌        | ┐         | └           | ┘            | ─          | │        |
| double  | ╔        | ╗         | ╚           | ╝            | ═          | ║        |
| rounded | ╭        | ╮         | ╰           | ╯            | ─          | │        |
| heavy   | ┏        | ┓         | ┗           | ┛            | ━          | ┃        |
| ascii   | +        | +         | +           | +            | -          | \|       |
| dashed  | ┌        | ┐         | └           | ┘            | ╌          | ╎        |
| dotted  | ┌        | ┐         | └           | ┘            | ┄          | ┆        |
| stars   | *        | *         | *           | *            | *          | *        |
| mixed   | ┏        | ┓         | ┗           | ┛            | ━          | ┃        |

## Color Options

Add terminal colors to your banners using the `--color` flag.

### Basic Colors
```
--color red       # Red border
--color green     # Green border (success)
--color blue      # Blue border
--color cyan      # Cyan border
--color magenta   # Magenta border
--color yellow    # Yellow border (warning)
```

### Gradient Presets
```
--color sunset    # Red → Orange → Yellow
--color ocean     # Dark Blue → Cyan
--color matrix    # Dark → Bright Green
--color fire      # Dark Red → Orange → Yellow
```

### Color Example Output
When using `--color red`:
```
\x1b[31m╔══════════════════════════╗\x1b[0m
\x1b[31m║\x1b[0m     Important Notice     \x1b[31m║\x1b[0m
\x1b[31m╚══════════════════════════╝\x1b[0m
```

> **Note**: Colors require ANSI-compatible terminal. See `assets/reference/ansi-colors.md` for details.

## Workflow

**Step 1: Parse the input**
- Extract the banner text (handle multi-line content)
- Determine the border style (default to "double")
- Note alignment preference (default to "center")
- Calculate or use specified width

**Step 2: Calculate dimensions**
- Find the longest line in the content
- Add padding (1 space on each side minimum)
- Determine final banner width

**Step 3: Render the banner**
- Draw the top border with appropriate corner characters
- For each line of text:
  - Add left border
  - Add padded and aligned text
  - Add right border
- Draw the bottom border with appropriate corner characters

**Step 4: Output the result**
- Display in a code block for proper monospace rendering
- Ensure all lines are the same length

## Error Handling

**Empty text**: "Please provide text content for the banner."

**Width too narrow**: "The specified width is too narrow for the content. Expanding to fit."

**Very long lines**: "Some lines exceed typical terminal width. Consider breaking them up or specifying a smaller width."

## Examples

**Basic banner:**
```
/generate-banner "Welcome to My App"
```

**Multi-line with style:**
```
/generate-banner "Project Status\nBuild: Passing\nTests: 42/42" --style rounded
```

**Custom width and alignment:**
```
/generate-banner "ERROR: Connection failed" --style heavy --width 50 --align left
```

**ASCII-only for compatibility:**
```
/generate-banner "Compatible Banner" --style ascii
```

## Tips

- Use **double** borders for important announcements and headers
- Use **rounded** borders for friendly, approachable messages
- Use **heavy** borders for warnings or critical information
- Use **ascii** style when targeting systems that may not support Unicode
- Use **dashed** or **dotted** for subtle, less prominent framing
- Use **stars** for celebratory messages or achievements
- Use **mixed** for multi-section banners with visual hierarchy
- Add **--color red** for errors, **--color green** for success
- Multi-line banners work great for version info, status displays, and menus
- See `assets/reference/ansi-colors.md` for full color code reference
