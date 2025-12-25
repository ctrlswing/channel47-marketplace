# Character Density Ramps

Reference for ASCII shading using character density (light → dark).

## Standard Ramps

### Simple (10 chars)
```
 .:-=+*#%@
```

### Extended (70 chars)
```
 .'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
```

### Compact (16 chars)
```
 .,:;+*?%S#@
```

### Blocks (4 chars)
```
 ░▒▓█
```

### Dots (4 chars)
```
 ·•●█
```

## Specialized Ramps

### Letters Only
```
 ilxt1jfLCOQ0M@
```

### Numbers Only
```
 1234567890
```

### Symbols Only
```
 .-:=+*#%@
```

### Unicode Blocks (8 levels)
```
 ▁▂▃▄▅▆▇█
```

### Horizontal Bars (8 levels)
```
 ▏▎▍▌▋▊▉█
```

## Density Values

### Character Weights (approximate %)

| Char | Density | Char | Density | Char | Density |
|------|---------|------|---------|------|---------|
| ` ` | 0% | `.` | 5% | `-` | 10% |
| `:` | 15% | `=` | 20% | `+` | 25% |
| `*` | 35% | `#` | 50% | `%` | 60% |
| `@` | 75% | `█` | 100% | | |

### Block Characters

| Char | Name | Density |
|------|------|---------|
| ` ` | Space | 0% |
| `░` | Light shade | 25% |
| `▒` | Medium shade | 50% |
| `▓` | Dark shade | 75% |
| `█` | Full block | 100% |

## Usage Examples

### Gradient Bar
```
Light ░░▒▒▓▓██ Dark
```

### Shaded Sphere
```
      .:::::..
    .:-======-:.
   .:=+*####*+=:.
  .:-+*########*+-.
  :-=*##########*=-:
  :-+*##########*+-:
  .:-+*########*+-.
   .:-=+*####*+=:.
    .:-======-:.
      .:::::..
```

### Depth Shading
```
Background:  . : - = +
Midground:   * # % &
Foreground:  @ M W █
```

### Mountain with Shading
```
              .
             /#\
            /##%\
           /###%%\
          /#####%%\
         /######%%%\
        /########%%%\
       /##########%%%%\
      /#############%%%%\
     .-=================-.
    .'                   '.
```

## Tips

1. **Fewer characters = simpler look**: Use 4-8 char ramps for clean output
2. **More characters = finer gradients**: Use 16+ chars for detailed shading
3. **Match your font**: Different fonts render chars differently
4. **Test your ramp**: Print all chars side-by-side to verify density order
5. **Consider aspect ratio**: Characters are taller than wide; adjust accordingly

## Creating Custom Ramps

Sort characters by visual density:
1. View each character at 200%+ zoom
2. Estimate the "ink coverage" percentage
3. Arrange from least to most dense
4. Test with a gradient to verify smooth transition
