---
name: write
description: Generate or refine written content using style guide principles. Use when writing drafts, editing content, improving openings or endings, or removing AI writing patterns.
args:
  - name: content
    description: Content to edit (paste or @file), or topic for new content
    required: false
  - name: mode
    description: "Operation: draft, edit, opening, ending, clean (default: auto-detect)"
    required: false
    flag: true
  - name: style-guide
    description: Path to custom style guide (overrides default/settings)
    required: false
    flag: true
---

# Write Skill

Generate new content or refine existing writing using style guide principles.

## Workflow

**Step 1: Load Style Guide**

Check for style guide in this order:
1. `--style-guide` parameter (if provided)
2. `.claude/creative-writing.local.md` custom_style_guide setting
3. Default style guide at `../../default-style-guide.md`

**Step 2: Detect Mode**

If `--mode` not specified, auto-detect:

```
No content provided → draft (generate new)
Content < 100 words → opening
Content mentions "ending"/"conclusion" → ending
Content has AI patterns (check writing-patterns.md) → clean
Otherwise → edit
```

**Step 3: Load Relevant Style Guide Sections**

Read [style-guide-loader.md](style-guide-loader.md) to determine sections needed.

Load specified sections from the style guide using header matching (`## Section Name` through next `##`).

**Step 4: Get or Generate Content**

If no content provided:
```
Paste content to edit, or provide a topic for new draft:
```

Wait for user input.

**Step 5: Execute Mode-Specific Operation**

### Draft Mode
Generate new content from topic:
- Use full style guide
- Focus on honest opening, clear reasoning, genuine ending
- Avoid lists, use prose
- Show trade-offs where relevant

### Edit Mode
Rewrite full content:
- Apply Voice Principles, Structure, Word Choice
- Check against [writing-patterns.md](writing-patterns.md) for AI tells
- Preserve core meaning, upgrade execution
- Vary sentence length, natural paragraphs

### Opening Mode
Refine first 1-3 paragraphs:
- Lead with honesty, not authority
- Remove performative declarations
- Check against Patterns to Avoid
- Set genuine tone for rest of piece

### Ending Mode
Strengthen conclusion:
- Replace generic CTAs with specific questions
- Ensure genuine curiosity, not formality
- Check Endings section of style guide
- Avoid "What do you think?" or "Let me know below!"

### Clean Mode
Remove AI patterns only:
- Load full Patterns to Avoid from [writing-patterns.md](writing-patterns.md)
- Remove em-dashes, excessive colons
- Replace hype words with concrete language
- Fix rhetorical questions as transitions
- Minimal structural changes, focus on pattern removal

**Step 6: Present Results**

Show:

```markdown
## Original
[original content if editing, or "New Draft" if generating]

## Revised
[improved content]

## Key Changes
- [Change 1 with brief reasoning]
- [Change 2 with brief reasoning]
- [Change 3 with brief reasoning]
```

## Error Handling

**Missing style guide**:
```
Couldn't load custom style guide at [path], using default instead.
```

**Short content** (< 50 words):
```
Content seems short. For better results, provide at least a paragraph or two.
```

**No content after prompt**:
```
No content received. Please paste your draft or provide a topic.
```

## Examples

**Generate new content:**
```
/write "The benefits of plugin marketplaces for AI tools"
```

**Edit existing:**
```
/write @draft.md
```

**Improve opening:**
```
/write --mode opening
[paste opening paragraphs]
```

**Remove AI patterns:**
```
/write --mode clean @article.md
```
