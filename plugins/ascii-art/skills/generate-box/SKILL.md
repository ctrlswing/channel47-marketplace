---
name: generate-box
description: Wrap content in decorative ASCII boxes with optional titles
args:
  - name: content
    description: Content to wrap in a box (paste directly or use @file reference)
    required: true
  - name: style
    description: "Box style: simple, double, rounded, heavy, shadow (default: simple)"
    required: false
    flag: true
  - name: title
    description: Optional title for the box header
    required: false
    flag: true
  - name: padding
    description: Internal padding in spaces (default: 1)
    required: false
    flag: true
---

# Generate Box

Wrap existing content in decorative ASCII boxes. Perfect for highlighting code snippets, configuration examples, important notes, and documentation sections.

## Available Box Styles

### simple (default)
Clean single-line borders:
```
┌──────────────────────────────────────┐
│ Your content goes here               │
│ Supports multiple lines              │
└──────────────────────────────────────┘
```

### double
Double-line borders for emphasis:
```
╔══════════════════════════════════════╗
║ Your content goes here               ║
║ Supports multiple lines              ║
╚══════════════════════════════════════╝
```

### rounded
Soft, rounded corners:
```
╭──────────────────────────────────────╮
│ Your content goes here               │
│ Supports multiple lines              │
╰──────────────────────────────────────╯
```

### heavy
Bold borders for maximum visibility:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Your content goes here               ┃
┃ Supports multiple lines              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

### shadow
Box with shadow effect for depth:
```
┌──────────────────────────────────────┐
│ Your content goes here               │
│ Supports multiple lines              │
└──────────────────────────────────────┘░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

## Title Support

Boxes can include a title in the header:
```
┌─ Configuration ──────────────────────┐
│                                      │
│  API_KEY=your_key_here               │
│  DEBUG=false                         │
│  PORT=3000                           │
│                                      │
└──────────────────────────────────────┘
```

```
╔═ WARNING ════════════════════════════╗
║                                      ║
║  This action cannot be undone!       ║
║                                      ║
╚══════════════════════════════════════╝
```

## Workflow

**Step 1: Parse the input**
- Extract the content (from direct input or @file reference)
- Determine the box style (default to "simple")
- Note any title to include
- Set padding value (default to 1)

**Step 2: Process the content**
- Split content into lines
- Find the longest line
- Calculate box width based on content + padding

**Step 3: Render the box**
- Draw top border (with title if specified)
- For each line of content:
  - Add left border with padding
  - Add content
  - Add right padding and border
- Draw bottom border
- Add shadow if using shadow style

**Step 4: Output the result**
- Display in a code block
- Preserve original content formatting

## Error Handling

**Empty content**: "Please provide content to wrap in a box."

**File not found**: "Couldn't find the file at [path]. Please check the path and try again."

**Very wide content**: "Content is quite wide. The box may not display well in narrow terminals."

## Examples

**Basic box:**
```
/generate-box "Important note: Remember to save your work!"
```

**Box with title:**
```
/generate-box @.env.example --title "Environment Variables" --style double
```

**Multi-line content with padding:**
```
/generate-box "Line 1\nLine 2\nLine 3" --padding 2
```

**Shadow effect for depth:**
```
/generate-box "Featured Content" --style shadow --title "Spotlight"
```

**Code snippet in a box:**
```
/generate-box @src/utils/helper.ts --title "Helper Functions" --style rounded
```

## Tips

- Use **titles** to provide context for boxed content
- Use **shadow** style sparingly for special callouts
- Use **double** style for important configuration or warnings
- Use **rounded** style for friendly tips and notes
- Increase **padding** for more breathing room around content
- The box automatically expands to fit the widest line
