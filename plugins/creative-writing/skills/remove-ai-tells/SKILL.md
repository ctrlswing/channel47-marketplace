---
name: remove-ai-tells
description: Scan for and remove common AI writing patterns
args:
  - name: content
    description: Content to clean (paste or @file reference)
    required: false
  - name: style-guide
    description: Path to custom style guide (overrides default/settings)
    required: false
    flag: true
---

# Remove AI Tells Skill

Scans for and removes common AI writing patterns.

## Workflow

**Step 1: Load style guide**

Check for style guide in this order:
1. `--style-guide` parameter (if provided)
2. `.claude/creative-writing.local.md` custom_style_guide setting
3. Default style guide at `default-style-guide.md`

**Step 2: Extract patterns table**

Load "Patterns to Avoid" section (full table).

**Step 3: Get content**

If content not provided, prompt:

```
Paste the content to clean:
```

**Step 4: Scan for AI patterns**

Find instances of:
- **Em-dashes**: Replace with commas, periods, or rewrite
- **Colons**: Rewrite as separate sentences or use other punctuation
- **Hype words**: Remove or replace with specific, honest descriptions
  - "game-changer" → describe actual impact
  - "revolutionary" → explain what changed
  - "just changed everything" → be specific about changes
- **Rhetorical questions as transitions**: Remove or make genuine questions
  - "But what does this mean for you?" → remove or rephrase
- **Generic CTAs**: Make specific or remove
  - "What do you think?" → ask specific question
  - "Let me know in the comments" → genuine curiosity about specific aspect
- **Bold opening declarations**: Rewrite with honesty/vulnerability
- **Excessive headers**: Consolidate if headers every 2-3 paragraphs

**Step 5: Clean content**

Create cleaned version with all patterns removed/replaced.

**Step 6: Annotate changes**

Track what was changed:

```markdown
## Cleaned Content

[content with AI patterns removed]

## Changes Made

**Em-dashes (12 instances)**
- Line 3: "The approach is simple—just follow these steps" → "The approach is simple. Just follow these steps."
- Line 15: "Consider this—what if we tried" → "Consider this. What if we tried"
- [etc.]

**Colons (8 instances)**
- Line 5: "Here's the key insight: users want simplicity" → "Here's the key insight. Users want simplicity."
- [etc.]

**Hype words (4 instances)**
- Line 10: "This game-changer will transform" → "This approach changes"
- [etc.]

**Rhetorical questions (3 instances)**
- Line 20: "But what does this mean for you?" → [removed]
- [etc.]

**Generic CTAs (1 instance)**
- Last paragraph: "What do you think? Let me know!" → "I'm curious if this matches your experience with [specific topic]?"
```

## Error Handling

**No patterns found**:
```
No common AI patterns detected. Content looks clean!
```

**Very few patterns**:
```
Found only [N] minor patterns. See changes above. Content is mostly clean.
```

Same error handling as edit-draft for missing files, short content, etc.
