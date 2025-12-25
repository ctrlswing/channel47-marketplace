---
name: text
description: Create ASCII text art including logos, banners, boxes, and text effects. Use when generating headers, decorative text, terminal splash screens, or framed content.
args:
  - name: content
    description: Text to render or content to frame
    required: true
  - name: type
    description: "Output type: logo, banner, box (default: logo)"
    required: false
    flag: true
  - name: style
    description: "Font/border style: standard, block, slant, banner, small, rounded, double, etc."
    required: false
    flag: true
  - name: effect
    description: "Text effect: shadow, 3d, outline, gradient, rainbow, neon, glitch, retro"
    required: false
    flag: true
  - name: color
    description: "ANSI color or gradient: red, blue, yellow, green, cyan, magenta, sunset, ocean, matrix"
    required: false
    flag: true
  - name: width
    description: Maximum character width (default: 80)
    required: false
    flag: true
---

# ASCII Text Art

Create decorative ASCII text including logos, banners, boxes, and effects.

## Workflow

**Step 1: Determine Type**

From `--type` flag or auto-detect from content:
- Contains newlines or >50 chars → box
- Multiple words (>2) → banner
- Single word, uppercase → logo
- Default → logo

**Step 2: Load Font or Border Reference**

Read [font-loader.md](font-loader.md) to map `--style` to font file.

For logos:
- standard → [../../assets/fonts/standard.md](../../assets/fonts/standard.md)
- block → [../../assets/fonts/block.md](../../assets/fonts/block.md)
- slant → [../../assets/fonts/slant.md](../../assets/fonts/slant.md)
- banner → [../../assets/fonts/banner.md](../../assets/fonts/banner.md)
- small → [../../assets/fonts/small.md](../../assets/fonts/small.md)

For banners/boxes, reference:
- [examples/banner-examples.md](examples/banner-examples.md)
- [examples/box-examples.md](examples/box-examples.md)

**Step 3: Load Color Reference (if specified)**

If `--color` flag provided, read:
[../../assets/reference/ansi-colors.md](../../assets/reference/ansi-colors.md)

Extract ANSI codes for the requested color or gradient.

**Step 4: Render Base Output**

### Logo Type
- Use character patterns from loaded font file
- Render each character with proper spacing
- Maintain consistent height across all characters
- Apply width constraints if specified

### Banner Type
- Choose border style (simple, double, rounded, heavy, ascii, dashed, dotted, stars)
- Create top border, content line, bottom border
- Center or left-align text based on width
- Reference border patterns from banner-examples.md

### Box Type
- Create complete frame around content
- Support multi-line content with proper wrapping
- Optional title in top border
- Reference box patterns from box-examples.md

**Step 5: Apply Effects (if specified)**

Read effect specifications and apply:
- shadow: Add drop shadow beneath characters
- 3d: Extrude characters for depth
- outline: Hollow outlined letters
- gradient/rainbow: Apply color gradations
- neon: Add glow effect with bright colors
- glitch: Distort with cyberpunk style
- retro: Vintage terminal aesthetic

**Step 6: Apply Colors (if specified)**

Wrap output with ANSI color codes:
- Solid colors: Single code wraps entire output
- Gradients: Apply color progression across lines or characters

**Step 7: Output Result**

Display in code block for proper monospace formatting:

\`\`\`
[ASCII art output]
\`\`\`

## Error Handling

**Empty text**:
```
Please provide text to render.
```

**Unsupported characters**:
```
Some characters couldn't be rendered. ASCII art works best with A-Z, 0-9, and common punctuation.
```

**Text too long for width**:
```
Text exceeds width limit. Try --style small or --width 120, or break into multiple lines.
```

**Unknown style**:
```
Style '[style]' not recognized. Available: standard, block, slant, banner, small (for logos) or simple, double, rounded, heavy (for banners/boxes).
```

## Examples

**Generate logo:**
```
/text "Claude Code" --type logo --style block
```

**Create banner:**
```
/text "Welcome!" --type banner --style rounded --color cyan
```

**Frame content in box:**
```
/text "Important Notice\nThis is a multi-line message" --type box --style double --color red
```

**Add effects:**
```
/text "NEON" --style block --effect neon --color matrix
```

**Constrain width:**
```
/text "Long Application Name" --style small --width 60
```

## Tips

- **Logos**: Use block style for maximum impact, small for space constraints
- **Banners**: Rounded style for friendly tone, heavy for warnings
- **Boxes**: Double borders for emphasis, simple for general use
- **Effects**: Combine with colors for enhanced visual impact
- **Width**: 80 chars fits most terminals, 120 for wide displays
