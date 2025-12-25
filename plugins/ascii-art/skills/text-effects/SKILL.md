---
name: text-effects
description: Apply visual effects to text including shadows, 3D, outlines, gradients, and more
args:
  - name: text
    description: Text to apply effects to
    required: true
  - name: effect
    description: "Effect type: shadow, 3d, outline, double, wave, glitch, gradient, rainbow, neon, retro (default: shadow)"
    required: false
    flag: true
  - name: direction
    description: "Effect direction for shadow/3d: right, left, down (default: right)"
    required: false
    flag: true
  - name: color
    description: "ANSI color or gradient: red, green, blue, cyan, magenta, yellow, sunset, ocean, matrix, fire"
    required: false
    flag: true
  - name: intensity
    description: "Effect intensity: light, medium, heavy (default: medium)"
    required: false
    flag: true
---

# Text Effects

Apply visual effects to text for emphasis, style, and visual interest. Perfect for headers, callouts, and decorative text in CLI tools and documentation.

## Available Effects

### shadow (default)
Text with a shadow beneath/beside it:
```
 HELLO WORLD
░HELLO WORLD
```

With direction variations:
```
Right shadow:        Left shadow:         Down shadow:
 HELLO               HELLO                HELLO
░HELLO              ░HELLO                HELLO
                                         ░░░░░
```

### 3d
Three-dimensional extruded text:
```
 ██╗  ██╗███████╗██╗     ██╗      ██████╗
 ██║  ██║██╔════╝██║     ██║     ██╔═══██╗
 ███████║█████╗  ██║     ██║     ██║   ██║
 ██╔══██║██╔══╝  ██║     ██║     ██║   ██║
 ██║  ██║███████╗███████╗███████╗╚██████╔╝
 ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝
```

### outline
Hollow outlined letters:
```
╔═╗ ╔═╗ ╔═╗ ╔═╗ ╔═╗
║ ║ ║   ║   ║ ║ ║ ║
╠═╣ ╠═╗ ║   ║ ║ ╠═╣
║ ║ ║ ║ ║   ║ ║ ║ ║
╩ ╩ ╚═╝ ╚═╝ ╚═╝ ╩ ╩
```

### double
Double-struck text:
```
ℍ𝔼𝕃𝕃𝕆 𝕎𝕆ℝ𝕃𝔻
```
Or with ASCII approximation:
```
|H| |E| |L| |L| |O|
```

### wave
Wavy/curved text:
```
    H       L   W
  E   L   O   O
        L       R
                  L
                    D
```

### glitch
Distorted glitch-style text:
```
H̷̢E̵̛L̸̨L̵̛O̷̢ ̸̨W̵̛O̷̢R̸̨L̵̛D̷̢
```
Or with ASCII approximation:
```
H#EL|LO W_OR|LD
|-|3LL0 \/\/0RLD
```

### gradient
Color gradient across text (requires ANSI support):
```
Sunset gradient (--color sunset):
\x1b[38;5;196mH\x1b[38;5;202mE\x1b[38;5;208mL\x1b[38;5;214mL\x1b[38;5;220mO\x1b[0m

Rendered as: H E L L O (red → orange → yellow)
```

Available gradient presets:
- `sunset` - Red → Orange → Yellow
- `ocean` - Dark Blue → Cyan
- `matrix` - Dark Green → Bright Green
- `fire` - Dark Red → Orange → Yellow
- `purple` - Dark Purple → Light Purple
- `grayscale` - Dark Gray → White

### rainbow
Full spectrum rainbow colors:
```
\x1b[31mH\x1b[33mE\x1b[32mL\x1b[36mL\x1b[34mO\x1b[35m!\x1b[0m

Rendered as: H E L L O ! (red, yellow, green, cyan, blue, magenta)
```

### neon
Glowing neon effect with bright colors:
```
 ██  ██ ███████ ██       ██       ██████
 ██  ██ ██      ██       ██      ██    ██
 ██████ █████   ██       ██      ██    ██
 ██  ██ ██      ██       ██      ██    ██
 ██  ██ ███████ ███████  ███████  ██████
░░  ░░ ░░░░░░░ ░░░░░░░  ░░░░░░░  ░░░░░░
```
With color: Bright text + dim glow underneath

### retro
Vintage computer/terminal style:
```
████████████████████████████████████████
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░ ██  ██ ███████ ██       ██       ░░░█
█░ ██  ██ ██      ██       ██       ░░░█
█░ ██████ █████   ██       ██       ░░░█
█░ ██  ██ ██      ██       ██       ░░░█
█░ ██  ██ ███████ ███████  ███████  ░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
████████████████████████████████████████
```

## Effect Intensity

Some effects support intensity levels:

```
Light shadow:        Medium shadow:       Heavy shadow:
 TEXT                 TEXT                 TEXT
░TEXT                ▒TEXT                ▓TEXT
```

## Workflow

**Step 1: Parse the input**
- Extract the text to transform
- Determine the effect type (default: shadow)
- Note any directional preference

**Step 2: Apply the effect**
- Transform the text according to the selected effect
- Apply any directional modifications
- Ensure consistent rendering

**Step 3: Output the result**
- Display in a code block
- Preserve alignment and spacing

## Effect Character Reference

| Effect | Primary Characters |
|--------|-------------------|
| Shadow | `░` `▒` `▓` `█` |
| 3D     | `╔` `═` `╗` `║` `╚` `╝` `█` `▀` `▄` |
| Outline| `╔` `╗` `╚` `╝` `═` `║` |
| Double | `║` `│` or Unicode double-struck |
| Wave   | Standard letters with positioning |
| Glitch | `̷` `̵` `̸` `#` `\|` `_` `/` `\` |
| Gradient | ANSI escape codes (256 color) |
| Rainbow | ANSI escape codes (8 color) |
| Neon   | `█` `░` + bright ANSI colors |
| Retro  | `█` `░` border frame |

## Color Options

### Basic Colors
```
--color red       # Bright red text
--color green     # Bright green text
--color blue      # Bright blue text
--color cyan      # Cyan text
--color magenta   # Magenta text
--color yellow    # Yellow text
```

### Gradient Presets (for --effect gradient)
```
--color sunset    # Red → Orange → Yellow
--color ocean     # Dark Blue → Light Blue → Cyan
--color matrix    # Dark Green → Bright Green
--color fire      # Black → Red → Orange → Yellow
--color purple    # Dark Purple → Light Purple
--color grayscale # Dark Gray → White
```

> **Note**: Colors require ANSI-compatible terminal. See `assets/reference/ansi-colors.md` for details.

## Error Handling

**Empty text**: "Please provide text to apply effects to."

**Very long text**: "Long text may not render well with some effects. Consider using shorter text or the 'shadow' effect which handles length best."

**Unsupported characters**: "Some special characters may not render correctly with this effect. Alphanumeric characters work best."

## Examples

**Basic shadow:**
```
/text-effects "IMPORTANT"
```

**3D effect:**
```
/text-effects "HELLO" --effect 3d
```

**Outline style:**
```
/text-effects "ALERT" --effect outline
```

**Shadow with direction:**
```
/text-effects "NOTICE" --effect shadow --direction down
```

**Glitch for style:**
```
/text-effects "ERROR" --effect glitch
```

**Wave effect:**
```
/text-effects "GROOVY" --effect wave
```

## Combining with Other Skills

Text effects work great with other ASCII art skills:

```
# Generate a logo, then add shadow
/generate-logo "ACME" --style block
# Then add shadow effect to result

# Create a banner with 3D title
/generate-banner "Welcome" --style double
# Use text-effects for the title before wrapping
```

## Tips

- **UPPERCASE** text generally works better with effects
- **shadow** is the most versatile and works with any length
- **3d** is best for short words (1-6 characters)
- **outline** is great for section headers
- **glitch** adds a cyberpunk/tech aesthetic
- **wave** is playful and works well for casual content
- **gradient** creates smooth color transitions (requires ANSI support)
- **rainbow** is eye-catching but use sparingly
- **neon** works great for retro/synthwave aesthetics
- **retro** evokes vintage computer terminals
- Use **--intensity light** for subtle effects, **heavy** for bold
- Combine with **--color** to add semantic meaning
- Keep text **short** for best visual impact
- Test different **directions** to see what looks best in context
- See `assets/reference/ansi-colors.md` for color code reference
- See `assets/reference/character-ramps.md` for shading characters
