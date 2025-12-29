# Diagram Pattern Reference

Box drawing characters and layout patterns for ASCII diagrams.

## Box Drawing Character Sets

### Simple (default)
```
Corners: ┌ ┐ └ ┘
Lines:   ─ │
T-joins: ├ ┤ ┬ ┴
Cross:   ┼
```

### Double
```
Corners: ╔ ╗ ╚ ╝
Lines:   ═ ║
T-joins: ╠ ╣ ╦ ╩
Cross:   ╬
```

### Rounded
```
Corners: ╭ ╮ ╰ ╯
Lines:   ─ │
T-joins: ├ ┤ ┬ ┴
Cross:   ┼
```

### Heavy
```
Corners: ┏ ┓ ┗ ┛
Lines:   ━ ┃
T-joins: ┣ ┫ ┳ ┻
Cross:   ╋
```

### ASCII-only (maximum compatibility)
```
Corners: + + + +
Lines:   - |
T-joins: + + + +
Cross:   +
```

## Arrow and Connector Symbols

### Horizontal Arrows
```
Right:  ─▶ ──▶ ───▶ ────▶
Left:   ◀─ ◀── ◀─── ◀────
Both:   ◀──▶ ◀───▶
```

### Vertical Arrows
```
Down:   │
        ▼

Up:     ▲
        │

Both:   ▲
        │
        ▼
```

### Diagonal Connectors
```
Tree branches:
  └── child
  ├── child

Flow splits:
     ┌─▶ path1
  ───┤
     └─▶ path2
```

## Layout Patterns

### Flowchart Node Spacing

**Horizontal layout:**
```
[Node width: 10-20 chars]
[Spacing between nodes: 4-6 chars]

┌──────────┐     ┌──────────┐     ┌──────────┐
│  Node A  │────▶│  Node B  │────▶│  Node C  │
└──────────┘     └──────────┘     └──────────┘
```

**Vertical layout:**
```
[Vertical spacing: 1 blank line]

┌──────────┐
│  Node A  │
└──────────┘
      │
      ▼
┌──────────┐
│  Node B  │
└──────────┘
```

### Tree Node Spacing

**Binary tree:**
```
        Root
         │
    ┌────┴────┐
    │         │
  Left      Right
    │         │
 ┌──┴──┐   ┌─┴──┐
 │     │   │    │
 L1   L2   R1   R2
```

**Wide tree:**
```
           Root
            │
  ┌─────┬───┴───┬─────┐
  │     │       │     │
Child1 Child2 Child3 Child4
```

### Table Column Sizing

**Auto-sizing algorithm:**
1. Measure longest content in each column
2. Add 2 chars padding (1 each side)
3. Minimum width: 8 chars
4. Maximum width: 30 chars (truncate with ...)

**Example:**
```
Content: "Name", "Alice" → Column width: 7
Content: "Description", "A very long..." → Column width: 20 (truncated)

┌─────────┬────────────────────┐
│  Name   │    Description     │
├─────────┼────────────────────┤
│  Alice  │ A very long desc...│
└─────────┴────────────────────┘
```

### Architecture Layer Grouping

**Horizontal layers:**
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Presentation Layer       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
              │
              ▼
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         Business Layer          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
              │
              ▼
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          Data Layer             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

**Vertical layers:**
```
┌─────────┐  ┌─────────┐  ┌─────────┐
│  Web UI │  │   API   │  │ Database│
│         │─▶│ Gateway │─▶│         │
└─────────┘  └─────────┘  └─────────┘
```

### Sequence Diagram Lifelines

```
Actor spacing: 12-15 chars between actors

  ActorA        ActorB        ActorC
    │             │             │
    │──message───▶│             │
    │             │──request───▶│
    │             │◀──response──│
    │◀──result────│             │
    │             │             │
```

## Decision Nodes

### Diamond (compact):
```
     ┌─yes─▶
  ◇──┤
     └─no──▶
```

### Box (clear):
```
┌──────────┐
│ condition│
│   met?   │
└──┬───┬───┘
   │   │
  yes  no
   │   │
   ▼   ▼
```

## Rendering Guidelines

1. **Consistent spacing**: Maintain uniform gaps between elements
2. **Alignment**: Ensure boxes and connectors align properly
3. **Balance**: Center nodes when possible, avoid cramming
4. **Clarity**: Prefer readability over density
5. **Width**: Aim for 80 chars total width, max 120 for complex diagrams
6. **Labels**: Keep node labels concise (10-15 chars), truncate if needed
7. **Whitespace**: Use blank lines to separate diagram sections
