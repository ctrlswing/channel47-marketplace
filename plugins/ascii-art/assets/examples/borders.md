# Border and Box Examples

Reference examples of ASCII borders and box styles.

## Basic Border Styles

### Simple (Single Line)
```
┌────────────────────────────────────┐
│ Content goes here                  │
│ More content on another line       │
└────────────────────────────────────┘
```

### Double Line
```
╔════════════════════════════════════╗
║ Content goes here                  ║
║ More content on another line       ║
╚════════════════════════════════════╝
```

### Rounded Corners
```
╭────────────────────────────────────╮
│ Content goes here                  │
│ More content on another line       │
╰────────────────────────────────────╯
```

### Heavy/Bold
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Content goes here                  ┃
┃ More content on another line       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

### ASCII Only
```
+------------------------------------+
| Content goes here                  |
| More content on another line       |
+------------------------------------+
```

## Titled Boxes

### Title Left
```
┌─ Title ────────────────────────────┐
│                                    │
│ Content goes here                  │
│                                    │
└────────────────────────────────────┘
```

### Title Center
```
┌────────────── Title ───────────────┐
│                                    │
│ Content goes here                  │
│                                    │
└────────────────────────────────────┘
```

### Title with Double Border
```
╔═ Configuration ════════════════════╗
║                                    ║
║ API_KEY=your_key_here              ║
║ DEBUG=false                        ║
║                                    ║
╚════════════════════════════════════╝
```

## Shadow Effects

### Right Shadow
```
┌────────────────────────────────┐
│ Content with shadow            │
│ Creates depth effect           │
└────────────────────────────────┘░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

### Block Shadow
```
┌────────────────────────────────┐
│ Content with shadow            │▒
│ Creates depth effect           │▒
└────────────────────────────────┘▒
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
```

## Decorative Borders

### Stars
```
*************************************
*                                   *
*   Important Announcement          *
*                                   *
*************************************
```

### Equals
```
=====================================
|                                   |
|   Section Header                  |
|                                   |
=====================================
```

### Fancy
```
╔══════════════════════════════════════╗
║ ┌──────────────────────────────────┐ ║
║ │                                  │ ║
║ │       Double Framed Box          │ ║
║ │                                  │ ║
║ └──────────────────────────────────┘ ║
╚══════════════════════════════════════╝
```

## Dividers

### Simple
```
────────────────────────────────────
```

### Double
```
════════════════════════════════════
```

### Decorative
```
─────────── ◆ ◆ ◆ ───────────
```

### Wave
```
∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿
```

### Dots
```
• • • • • • • • • • • • • • • • • •
```

## Nested Boxes

### Simple Nesting
```
┌──────────────────────────────────────┐
│ ┌────────────────────────────────┐   │
│ │ Nested content                 │   │
│ └────────────────────────────────┘   │
└──────────────────────────────────────┘
```

### Multiple Sections
```
┌─ Main ────────────────────────────────┐
│                                       │
│  ┌─ Section A ─────┐ ┌─ Section B ─┐  │
│  │                 │ │             │  │
│  │  Content A      │ │  Content B  │  │
│  │                 │ │             │  │
│  └─────────────────┘ └─────────────┘  │
│                                       │
└───────────────────────────────────────┘
```

## Character Reference

| Style | TL | TR | BL | BR | H | V |
|-------|----|----|----|----|---|---|
| Simple | ┌ | ┐ | └ | ┘ | ─ | │ |
| Double | ╔ | ╗ | ╚ | ╝ | ═ | ║ |
| Rounded | ╭ | ╮ | ╰ | ╯ | ─ | │ |
| Heavy | ┏ | ┓ | ┗ | ┛ | ━ | ┃ |
| ASCII | + | + | + | + | - | \| |

TL=Top Left, TR=Top Right, BL=Bottom Left, BR=Bottom Right, H=Horizontal, V=Vertical
