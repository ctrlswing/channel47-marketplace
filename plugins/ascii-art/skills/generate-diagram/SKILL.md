---
name: generate-diagram
description: Create ASCII diagrams including flowcharts, trees, tables, and architecture diagrams
args:
  - name: description
    description: Natural language description of the diagram or structured data
    required: true
  - name: type
    description: "Diagram type: flowchart, tree, table, sequence, architecture (default: auto-detect)"
    required: false
    flag: true
  - name: style
    description: "Line style: unicode, ascii-only (default: unicode)"
    required: false
    flag: true
---

# Generate Diagram

Create ASCII diagrams from natural language descriptions or structured data. Supports flowcharts, directory trees, tables, sequence diagrams, and architecture diagrams.

## Diagram Types

### flowchart
Process flows with decision points:
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    Start    │────▶│   Process   │────▶│     End     │
└─────────────┘     └─────────────┘     └─────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │  Decision?  │
                    └─────────────┘
                      │       │
                 Yes  │       │  No
                      ▼       ▼
               ┌───────┐   ┌───────┐
               │ Path A│   │ Path B│
               └───────┘   └───────┘
```

### tree
Directory structures and hierarchies:
```
project/
├── src/
│   ├── components/
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   └── Modal.tsx
│   ├── utils/
│   │   ├── helpers.ts
│   │   └── constants.ts
│   └── index.ts
├── tests/
│   └── components/
│       └── Button.test.tsx
├── package.json
└── README.md
```

### table
Data tables with borders:
```
┌──────────────┬─────────────┬──────────┬─────────┐
│ Feature      │ Status      │ Priority │ Owner   │
├──────────────┼─────────────┼──────────┼─────────┤
│ Auth         │ ✓ Complete  │ High     │ Alice   │
│ API Routes   │ ◐ In Progress│ High     │ Bob     │
│ Tests        │ ○ Pending   │ Medium   │ Carol   │
│ Docs         │ ○ Pending   │ Low      │ Dave    │
└──────────────┴─────────────┴──────────┴─────────┘
```

### sequence
Interaction sequences between components:
```
┌─────────┐          ┌─────────┐          ┌─────────┐
│  Client │          │  Server │          │   DB    │
└────┬────┘          └────┬────┘          └────┬────┘
     │                    │                    │
     │  POST /login       │                    │
     │───────────────────▶│                    │
     │                    │  SELECT user       │
     │                    │───────────────────▶│
     │                    │                    │
     │                    │  user data         │
     │                    │◀───────────────────│
     │                    │                    │
     │  200 OK + token    │                    │
     │◀───────────────────│                    │
     │                    │                    │
```

### architecture
System architecture diagrams:
```
                    ┌─────────────────┐
                    │   Load Balancer │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
     ┌────────────┐   ┌────────────┐   ┌────────────┐
     │  Server 1  │   │  Server 2  │   │  Server 3  │
     └─────┬──────┘   └─────┬──────┘   └─────┬──────┘
           │                │                │
           └────────────────┼────────────────┘
                            │
                    ┌───────┴───────┐
                    │               │
                    ▼               ▼
             ┌───────────┐   ┌───────────┐
             │  Primary  │   │  Replica  │
             │    DB     │──▶│    DB     │
             └───────────┘   └───────────┘
```

## Arrow Characters Reference

| Direction | Unicode | ASCII-only |
|-----------|---------|------------|
| Right     | ──▶     | -->        |
| Left      | ◀──     | <--        |
| Down      | │ ▼     | \| v       |
| Up        | ▲ │     | ^ \|       |
| Bidirectional | ◀──▶ | <-->     |

## Workflow

**Step 1: Parse the input**
- Analyze the description to determine diagram type (or use specified type)
- Identify key elements, relationships, and flow
- Note style preference (unicode or ascii-only)

**Step 2: Plan the layout**
- Identify all nodes/entities
- Map connections and flow direction
- Calculate approximate sizing and spacing

**Step 3: Render the diagram**
- Draw boxes/nodes with appropriate borders
- Connect with arrows showing direction
- Add labels and annotations
- Ensure proper alignment

**Step 4: Output the result**
- Display in a code block
- Verify alignment is preserved

## Error Handling

**Vague description**: "Could you provide more details? For example, list the steps in your process or the components in your system."

**Too complex**: "This diagram is getting complex. Consider breaking it into multiple simpler diagrams."

**Unknown type**: "I'll try to auto-detect the best diagram type. You can also specify --type flowchart|tree|table|sequence|architecture."

## Examples

**Flowchart from description:**
```
/generate-diagram "User submits form, validate input, if valid save to database and show success, if invalid show error"
```

**Directory tree:**
```
/generate-diagram "src folder with components and utils subfolders, components has Button and Input files" --type tree
```

**Table from data:**
```
/generate-diagram "Table with columns Name, Role, Status. Rows: Alice/Admin/Active, Bob/User/Active, Carol/User/Inactive" --type table
```

**Sequence diagram:**
```
/generate-diagram "Client sends request to API, API queries Database, Database returns data, API sends response to Client" --type sequence
```

**ASCII-only for compatibility:**
```
/generate-diagram "Simple flow: Start -> Process -> End" --style ascii-only
```

## Tips

- For **flowcharts**, describe the process step by step including any decision points
- For **trees**, describe the hierarchy with parent/child relationships
- For **tables**, provide column headers and row data
- For **sequences**, describe interactions in order: "A sends X to B, B responds with Y"
- For **architecture**, describe components and their connections
- Use **ascii-only** style for maximum terminal compatibility
- Keep diagrams focused - split complex systems into multiple diagrams
