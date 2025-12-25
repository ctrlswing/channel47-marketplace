# ANSI Color Codes Reference

Complete reference for adding colors and styles to ASCII art in terminal output.

## Escape Sequence Format

```
\x1b[{code}m    or    \033[{code}m    or    \e[{code}m
```

Reset all styles: `\x1b[0m`

## Text Styles

| Code | Style | Code | Reset |
|------|-------|------|-------|
| `1` | Bold | `22` | Normal |
| `2` | Dim | `22` | Normal |
| `3` | Italic | `23` | No Italic |
| `4` | Underline | `24` | No Underline |
| `5` | Blink | `25` | No Blink |
| `7` | Reverse | `27` | No Reverse |
| `9` | Strikethrough | `29` | No Strike |

## Standard Colors (8 colors)

| Color | FG | BG | Bright FG | Bright BG |
|-------|----|----|-----------|-----------|
| Black | 30 | 40 | 90 | 100 |
| Red | 31 | 41 | 91 | 101 |
| Green | 32 | 42 | 92 | 102 |
| Yellow | 33 | 43 | 93 | 103 |
| Blue | 34 | 44 | 94 | 104 |
| Magenta | 35 | 45 | 95 | 105 |
| Cyan | 36 | 46 | 96 | 106 |
| White | 37 | 47 | 97 | 107 |

## 256 Color Mode

```
Foreground: \x1b[38;5;{n}m
Background: \x1b[48;5;{n}m
```

| Range | Description |
|-------|-------------|
| 0-7 | Standard colors |
| 8-15 | Bright colors |
| 16-231 | 216-color cube (6×6×6) |
| 232-255 | Grayscale (24 shades) |

## 24-bit True Color (RGB)

```
Foreground: \x1b[38;2;{r};{g};{b}m
Background: \x1b[48;2;{r};{g};{b}m
```

## Combining Codes

```bash
\x1b[1;31mBold Red\x1b[0m
\x1b[4;96mUnderlined Cyan\x1b[0m
\x1b[1;44;97mBold White on Blue\x1b[0m
```

## Gradient Palettes (256-color codes)

### Sunset
```
196 → 202 → 208 → 214 → 220 → 226
```

### Ocean
```
17 → 18 → 19 → 20 → 27 → 33 → 39 → 45 → 51
```

### Forest
```
22 → 28 → 34 → 40 → 46 → 82 → 118
```

### Matrix
```
232 → 22 → 28 → 34 → 40 → 46
```

### Fire
```
232 → 52 → 88 → 124 → 160 → 196 → 202 → 208 → 214 → 220
```

### Purple Haze
```
53 → 54 → 55 → 56 → 57 → 93 → 129 → 165
```

### Grayscale
```
232 → 236 → 240 → 244 → 248 → 252 → 255
```

## Practical Examples

### Colored Banner
```bash
echo -e "\x1b[1;34m╔════════════════════╗\x1b[0m"
echo -e "\x1b[1;34m║\x1b[0m   \x1b[1;36mMY CLI TOOL\x1b[0m    \x1b[1;34m║\x1b[0m"
echo -e "\x1b[1;34m╚════════════════════╝\x1b[0m"
```

### Rainbow Text
```bash
\x1b[31mR\x1b[33mA\x1b[32mI\x1b[36mN\x1b[34mB\x1b[35mO\x1b[31mW\x1b[0m
```

### Status Messages
```bash
# Success
echo -e "\x1b[1;32m✓\x1b[0m Operation complete"

# Warning
echo -e "\x1b[1;33m⚠\x1b[0m Proceed with caution"

# Error
echo -e "\x1b[1;31m✗\x1b[0m Something went wrong"

# Info
echo -e "\x1b[1;34mℹ\x1b[0m Additional information"
```

### Block Gradient
```bash
\x1b[38;5;196m█\x1b[38;5;202m█\x1b[38;5;208m█\x1b[38;5;214m█\x1b[38;5;220m█\x1b[38;5;226m█\x1b[0m
```

## Terminal Compatibility

| Terminal | 8 | 256 | True Color |
|----------|---|-----|------------|
| macOS Terminal | ✓ | ✓ | ✓ |
| iTerm2 | ✓ | ✓ | ✓ |
| Windows Terminal | ✓ | ✓ | ✓ |
| VS Code | ✓ | ✓ | ✓ |
| GNOME Terminal | ✓ | ✓ | ✓ |
| xterm | ✓ | ✓ | Partial |

## Tips

1. Always reset with `\x1b[0m` after colored output
2. Use bold (`1;`) to make colors more vibrant
3. Test on target terminals for compatibility
4. Pipe to `lolcat` for easy rainbow effects
