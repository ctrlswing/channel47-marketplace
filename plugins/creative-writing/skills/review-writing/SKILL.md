---
name: review-writing
description: Provide feedback on content without rewriting it
args:
  - name: content
    description: Content to review (paste directly or use @file reference)
    required: false
  - name: style-guide
    description: Path to custom style guide (overrides default/settings)
    required: false
    flag: true
---

# Review Writing Skill

This skill provides specific, actionable feedback without rewriting.

## Workflow

**Step 1: Load style guide**

Check for style guide in this order:
1. `--style-guide` parameter (if provided)
2. `.claude/creative-writing.local.md` custom_style_guide setting
3. Default style guide at `default-style-guide.md`

**Step 2: Extract relevant chunks**

Load these sections:
- Quick Reference Checklist
- Patterns to Avoid

**Step 2.5: Load Pattern Reference**

Read [../write/writing-patterns.md](../write/writing-patterns.md) for AI pattern detection rules.

Use this to identify:
- Hype words and superlatives
- Em-dash and colon overuse
- Rhetorical transition questions
- Generic CTAs
- Performative openings

**Step 3: Get content**

If content not provided as argument, prompt:

```
Paste the content you want reviewed, or use @file reference:
```

**Step 4: Analyze against checklist**

Review each item from Quick Reference:
1. Opening: honest or performative?
2. Reasoning: shown or stated?
3. Lists vs prose?
4. Trade-offs acknowledged?
5. Ending: genuine or generic?
6. Unnecessary sentences?

Also scan for patterns to avoid:
- Em-dashes and colons
- Hype words
- Rhetorical questions as transitions
- Generic CTAs
- Bold opening declarations
- Excessive headers

**Step 5: Organize feedback**

Present notes in categories:

```markdown
## Opening

[Specific feedback about first 1-3 paragraphs with examples]

## Reasoning & Trade-offs

[Feedback on whether conclusions are earned and limitations acknowledged]

## Structure

[Notes on sentence variety, paragraph breaks, lists vs prose]

## Word Choice

[Comments on concrete vs abstract, metaphors, conversational tone]

## Ending

[Feedback on conclusion and CTA]

## Patterns to Clean

[Specific instances of AI tells with line references if possible]

## Strengths

[What's already working well - be specific]
```

**Step 6: End with actionable summary**

```
## Next Steps

Consider:
1. [Most impactful change]
2. [Second priority]
3. [Third priority]

Use /improve-opening or /strengthen-ending for focused rewrites, or /edit-draft for a full revision.
```

## Error Handling

Same as edit-draft skill.
