# Spinners & Animation Patterns

Reference for terminal spinners, progress bars, and animation frames.

## Spinner Patterns

### Classic Spinners

**Line (4 frames)**
```
| / - \
```

**Dot (4 frames)**
```
.  ..  ...  ..
```

**Bounce (5 frames)**
```
.    o    O    o    .
```

### Unicode Spinners

**Braille (8 frames)**
```
⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏
```

**Braille Dots (8 frames)**
```
⣾ ⣽ ⣻ ⢿ ⡿ ⣟ ⣯ ⣷
```

**Circle (4 frames)**
```
◐ ◓ ◑ ◒
```

**Arc (6 frames)**
```
◜ ◠ ◝ ◞ ◡ ◟
```

**Clock (12 frames)**
```
🕐 🕑 🕒 🕓 🕔 🕕 🕖 🕗 🕘 🕙 🕚 🕛
```

**Moon (8 frames)**
```
🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘
```

### Block Spinners

**Corner (4 frames)**
```
▖ ▘ ▝ ▗
```

**Block (4 frames)**
```
▌ ▀ ▐ ▄
```

**Square (4 frames)**
```
◰ ◳ ◲ ◱
```

### Arrow Spinners

**Arrow (8 frames)**
```
← ↖ ↑ ↗ → ↘ ↓ ↙
```

**Triangle (4 frames)**
```
◢ ◣ ◤ ◥
```

## Progress Bars

### Basic Styles

**Hash Bar**
```
[####------] 40%
[########--] 80%
[##########] 100%
```

**Equals Bar**
```
[====      ] 40%
[========  ] 80%
[==========] 100%
```

**Arrow Bar**
```
[===>      ] 40%
[=======>  ] 80%
[=========>] 100%
```

### Unicode Bars

**Block Bar (8 increments)**
```
▏▎▍▌▋▊▉█
```

**Example:**
```
Progress: ████████▌         42%
Progress: █████████████████ 100%
```

**Shade Bar**
```
░░░░░░░░░░ 0%
███░░░░░░░ 30%
██████████ 100%
```

**Thin Bar**
```
┃▏         ┃ 10%
┃█████     ┃ 50%
┃██████████┃ 100%
```

### Fancy Bars

**Gradient Bar**
```
▓▓▓▓▓▒▒▒░░ 50%
```

**Bubble Bar**
```
○○○○○○○○○○ 0%
●●●●●○○○○○ 50%
●●●●●●●●●● 100%
```

**Box Bar**
```
□□□□□□□□□□ 0%
■■■■■□□□□□ 50%
■■■■■■■■■■ 100%
```

## Animation Frames

### Loading Text

**Dots (3 frames)**
```
Loading.
Loading..
Loading...
```

**Bracket (4 frames)**
```
[    ]
[=   ]
[==  ]
[=== ]
```

### Status Indicators

**Pulse (3 frames)**
```
●
◉
○
```

**Heartbeat (4 frames)**
```
♡ ♥ ♡ ♥
```

**Radio (4 frames)**
```
◌ ○ ◎ ●
```

### Scrolling Text

**Marquee Pattern**
```
Frame 1: [  TEXT  ]
Frame 2: [ TEXT   ]
Frame 3: [TEXT    ]
Frame 4: [EXT    T]
Frame 5: [XT    TE]
Frame 6: [T    TEX]
Frame 7: [    TEXT]
Frame 8: [   TEXT ]
```

## Combining Elements

### Spinner + Text
```
⠋ Loading...
⠙ Loading...
⠹ Loading...
```

### Progress + Percentage + ETA
```
████████░░ 80% | ETA: 2s
```

### Multi-bar Layout
```
Downloading: ████████░░ 80%
Installing:  ████░░░░░░ 40%
Configuring: ░░░░░░░░░░  0%
```

## Implementation Tips

1. **Frame timing**: 80-120ms per frame looks smooth
2. **Cursor control**: Use `\r` to return to line start
3. **Hide cursor**: `\x1b[?25l` hide, `\x1b[?25h` show
4. **Clear line**: `\x1b[2K` clears entire line
5. **Terminal width**: Check width to avoid wrapping

## Quick Reference

| Type | Simple | Unicode | Use Case |
|------|--------|---------|----------|
| Spinner | `\|/-` | `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` | Indeterminate wait |
| Bar | `[###---]` | `████░░` | Known progress |
| Dots | `...` | `⣾⣽⣻⢿⡿⣟⣯⣷` | Background task |
| Pulse | `o O o` | `◌○◎●` | Heartbeat/alive |
