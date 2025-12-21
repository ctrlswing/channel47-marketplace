---
name: improve-opening
description: Rewrite first 1-3 paragraphs to be more honest and engaging
args:
  - name: content
    description: Content with opening to improve (paste or @file reference)
    required: false
  - name: style-guide
    description: Path to custom style guide (overrides default/settings)
    required: false
    flag: true
---

# Improve Opening Skill

Specialized skill for fixing the first 1-3 paragraphs.

## Workflow

**Step 1: Load style guide**

Check for style guide in this order:
1. `--style-guide` parameter (if provided)
2. `.claude/creative-writing.local.md` custom_style_guide setting
3. Default style guide at `.claude-plugin/default-style-guide.md`

**Step 2: Extract relevant chunks**

Load these sections:
- Voice Principles
- Patterns to Avoid

**Step 3: Get content**

If content not provided, prompt:

```
Paste the content (I'll focus on the opening paragraphs):
```

**Step 4: Extract opening**

Identify first 1-3 paragraphs (or up to first 200 words, whichever is shorter).

**Step 5: Analyze opening**

Check against voice principles:
- Does it lead with honesty or authority?
- Is there a performative declaration?
- Does it use hype words?
- Does it start with a rhetorical question?
- Is there vulnerability or admission?

**Step 6: Rewrite opening**

Create improved version that:
- Starts with something real (admission, observation, vulnerability)
- Removes performative authority
- Cuts hype words
- Shows reasoning if conclusions are stated
- Maintains conversational tone

**Step 7: Present changes**

```markdown
## Original Opening

[original first 1-3 paragraphs]

## Improved Opening

[rewritten opening]

## Why This Works Better

[Brief explanation of changes: honesty over authority, removed performative elements, added vulnerability, etc.]
```

## Error Handling

Same as edit-draft skill.
