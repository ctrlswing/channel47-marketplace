---
name: strengthen-ending
description: "[DEPRECATED] Use /write --mode ending instead. This skill will be removed in v2.0. Strengthen conclusion."
args:
  - name: content
    description: Content with ending to strengthen (paste or @file reference)
    required: false
  - name: style-guide
    description: Path to custom style guide (overrides default/settings)
    required: false
    flag: true
---

# ⚠️ DEPRECATED - Use `/write --mode ending` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/write` with ending mode:
- `/write` then paste ending with "conclusion" (auto-detects ending mode)
- `/write --mode ending` (explicit ending mode)

---

# Original Skill Documentation

# Strengthen Ending Skill

Focuses on improving conclusions and calls to action.

## Workflow

**Step 1: Load style guide**

Check for style guide in this order:
1. `--style-guide` parameter (if provided)
2. `.claude/creative-writing.local.md` custom_style_guide setting
3. Default style guide at `default-style-guide.md`

**Step 2: Extract relevant chunks**

Load these sections:
- Endings
- Patterns to Avoid

**Step 3: Get content**

If content not provided, prompt:

```
Paste the content (I'll focus on the ending):
```

**Step 4: Extract ending**

Identify last 1-3 paragraphs (or last 200 words, whichever is shorter).

**Step 5: Analyze ending**

Check for weak patterns:
- Generic CTA ("What do you think?", "Let me know in the comments")
- Rhetorical question that adds nothing
- Summary that just repeats points
- Sales-pitch tone
- Formal closing that feels tacked on

**Step 6: Rewrite ending**

Create improved version that:
- Asks a specific, genuine question (not generic)
- Shows real curiosity about reader perspective
- Connects to content in meaningful way
- Feels natural, not forced

Or if conclusion doesn't need question:
- Ends with natural closure
- Leaves reader with clear takeaway
- Doesn't oversell or hype

**Step 7: Present changes**

```markdown
## Original Ending

[original last 1-3 paragraphs]

## Strengthened Ending

[rewritten ending]

## Why This Works Better

[Brief explanation: replaced generic CTA with specific question, showed genuine curiosity, removed sales pitch, etc.]
```

## Error Handling

Same as edit-draft skill.
