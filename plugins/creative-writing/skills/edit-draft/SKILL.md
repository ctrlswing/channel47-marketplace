---
name: edit-draft
description: Rewrite content to match style guide principles
args:
  - name: content
    description: Content to edit (paste directly or use @file reference)
    required: false
  - name: style-guide
    description: Path to custom style guide (overrides default/settings)
    required: false
    flag: true
---

# Edit Draft Skill

This skill rewrites content to match style guide principles.

## Workflow

**Step 1: Load style guide**

Check for style guide in this order:
1. `--style-guide` parameter (if provided)
2. `.claude/creative-writing.local.md` custom_style_guide setting
3. Default style guide at `default-style-guide.md`

**Step 2: Extract relevant chunks**

Load these sections from the style guide:
- Voice Principles
- Structure Guidelines
- Word Choice Standards
- Patterns to Avoid
- Quick Reference Checklist

Use header matching: `## Voice Principles` through next `##` header.

If custom guide doesn't have these headers, load full guide.

**Step 3: Get content**

If content not provided as argument, prompt:

```
Paste the content you want to edit, or use @file reference:
```

Wait for user input.

**Step 4: Analyze content**

Review against loaded style guide sections:
- Opening: honest or performative?
- Reasoning: shown or just stated?
- Trade-offs: acknowledged?
- Structure: varied sentences, natural paragraphs?
- Word choice: concrete or abstract?
- Lists: could they be prose?
- Ending: genuine question or generic CTA?
- AI patterns: em-dashes, colons, hype words?

**Step 5: Rewrite**

Create improved version that:
- Preserves core meaning and key information
- Applies voice principles (honesty, reasoning, trade-offs)
- Improves structure (varied sentences, natural breaks)
- Upgrades word choice (concrete details, simple metaphors)
- Removes patterns to avoid
- Strengthens opening and ending

**Step 6: Present changes**

Show:

```markdown
## Original

[original content]

## Edited

[rewritten content]

## Key Changes

- [Major change 1 with brief reasoning]
- [Major change 2 with brief reasoning]
- [Major change 3 with brief reasoning]
```

## Error Handling

**Missing style guide**: If specified custom guide doesn't exist, show:
```
Couldn't load custom style guide at [path], using default instead.
```

**Short content**: If less than 50 words:
```
Content seems short. For better results, provide at least a paragraph or two.
```

**No content provided**: If user doesn't paste content after prompt:
```
No content received. Please paste your draft or use @file reference.
```
