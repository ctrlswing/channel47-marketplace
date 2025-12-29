---
name: diagrams
description: Create ASCII diagrams including flowcharts, trees, tables, and architecture visualizations. Use when visualizing flows, hierarchies, data structures, or system architecture.
args:
  - name: description
    description: What to diagram or visualize (natural language description)
    required: true
  - name: type
    description: "Diagram type: flowchart, tree, table, architecture, sequence (default: auto-detect)"
    required: false
    flag: true
  - name: direction
    description: "Layout direction: horizontal, vertical (default: horizontal for flowcharts, vertical for trees)"
    required: false
    flag: true
  - name: style
    description: "Box style: simple, double, rounded, heavy (default: simple)"
    required: false
    flag: true
---

# ASCII Diagrams

Create structural diagrams for visualizing flows, hierarchies, and architectures.

## Workflow

**Step 1: Parse Description**

Extract diagram structure from natural language:
- Identify nodes/entities
- Identify relationships/connections
- Detect hierarchy or sequence
- Extract labels and annotations

**Step 2: Detect Diagram Type**

If `--type` not specified, auto-detect:
- Contains "→" or "then" or "after" → flowchart
- Contains "parent/child" or "under" or hierarchical structure → tree
- Contains rows/columns or tabular data → table
- Contains "system" or "component" or "service" → architecture
- Contains "user/actor" or temporal sequence → sequence

**Step 3: Load Diagram Patterns**

Read [diagram-patterns.md](diagram-patterns.md) for:
- Box drawing characters for the selected style
- Connector symbols
- Layout rules for the diagram type

Reference examples:
[../../assets/examples/diagrams.md](../../assets/examples/diagrams.md)

**Step 4: Generate Diagram by Type**

### Flowchart
```
Parse: Node1 → Node2 → Node3 (conditional) → Node4

Render:
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  Node1   │────▶│  Node2   │────▶│  Node3   │────▶│  Node4   │
└──────────┘     └──────────┘     │  (cond)  │     └──────────┘
                                  └──────────┘
```

Layout rules:
- Horizontal: nodes side-by-side with arrows between
- Vertical: nodes stacked with downward arrows
- Decisions: diamond or labeled box with multiple exits
- Use connector arrows: ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ ▶ ▼

### Tree
```
Parse: Root > Child1, Child2 > Grandchild1, Grandchild2

Render:
         Root
          │
    ┌─────┴─────┐
    │           │
  Child1     Child2
    │           │
    │      ┌────┴────┐
    │      │         │
Grandchild1  Grandchild2
```

Layout rules:
- Root at top (or left for horizontal)
- Branches use ├ ┤ └ ┘ ┬ ┴ │ ─
- Balanced spacing for visual clarity
- Align children under parents

### Table
```
Parse: Header1, Header2, Header3 | Row1Col1, Row1Col2, Row1Col3

Render:
┌───────────┬───────────┬───────────┐
│  Header1  │  Header2  │  Header3  │
├───────────┼───────────┼───────────┤
│ Row1Col1  │ Row1Col2  │ Row1Col3  │
├───────────┼───────────┼───────────┤
│ Row2Col1  │ Row2Col2  │ Row2Col3  │
└───────────┴───────────┴───────────┘
```

Layout rules:
- Calculate column widths from content
- Header row with separator
- Align text (left, right, center) as appropriate
- Use box drawing: ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘ │ ─

### Architecture
```
Parse: Frontend → API Gateway → Backend Services → Database

Render:
┏━━━━━━━━━━━┓     ┏━━━━━━━━━━━┓     ┏━━━━━━━━━━━━━━━┓     ┏━━━━━━━━━━┓
┃ Frontend  ┃────▶┃    API    ┃────▶┃    Backend    ┃────▶┃ Database ┃
┃   (React) ┃     ┃  Gateway  ┃     ┃   Services    ┃     ┃ (Postgres┃
┗━━━━━━━━━━━┛     ┗━━━━━━━━━━━┛     ┗━━━━━━━━━━━━━━━┛     ┗━━━━━━━━━━┛
```

Layout rules:
- System components in boxes (heavy borders for emphasis)
- Arrows show data/control flow
- Optional: add labels on arrows
- Support for layers (vertical grouping)

### Sequence
```
Parse: User → System: login | System → Database: verify | Database → System: success

Render:
  User         System       Database
    │            │              │
    │───login───▶│              │
    │            │───verify────▶│
    │            │◀──success────│
    │◀──token────│              │
```

Layout rules:
- Actors/systems as headers
- Vertical lifelines (│)
- Horizontal arrows for messages (───▶)
- Return arrows (◀───)
- Time flows top to bottom

**Step 5: Apply Box Style**

If `--style` specified, use corresponding box drawing characters from diagram-patterns.md:
- simple: ┌─┐ │ └─┘
- double: ╔═╗ ║ ╚═╝
- rounded: ╭─╮ │ ╰─╯
- heavy: ┏━┓ ┃ ┗━┛

**Step 6: Output Result**

Display in code block:

\`\`\`
[Diagram output]
\`\`\`

## Error Handling

**Unclear structure**:
```
Couldn't parse diagram structure clearly. Try being more explicit:
- "A → B → C" for flowcharts
- "Parent > Child1, Child2" for trees
- "Col1, Col2 | Row1Val1, Row1Val2" for tables
```

**Too complex**:
```
Diagram has [N] nodes which may not render well. Consider:
- Breaking into multiple diagrams
- Simplifying to key components
- Using --direction horizontal for better fit
```

**Missing connections**:
```
Some nodes appear disconnected. Verify relationships are specified.
```

## Examples

**Flowchart:**
```
/diagrams "User clicks button → Validate input → Save to database → Show success message"
```

**Tree:**
```
/diagrams "Company > Engineering, Sales > Frontend Team, Backend Team, Customer Success" --type tree
```

**Architecture:**
```
/diagrams "Web App → Load Balancer → App Servers → Cache Layer → Database" --type architecture --style heavy
```

**Table:**
```
/diagrams "Feature, Status, Owner | Dark Mode, Complete, Alice | Search, In Progress, Bob" --type table
```

**Sequence:**
```
/diagrams "User → API: get data, API → DB: query, DB → API: results, API → User: response" --type sequence --direction vertical
```

## Tips

- **Flowcharts**: Keep to 5-7 nodes per diagram for clarity
- **Trees**: Balance depth vs. breadth (max 4 levels recommended)
- **Tables**: Use for structured data, not complex relationships
- **Architecture**: Show high-level components, not every detail
- **Sequence**: Order matters - specify temporal flow clearly
- **Direction**: Horizontal for wide diagrams, vertical for deep ones
- **Style**: Heavy borders for architecture, simple for flowcharts
