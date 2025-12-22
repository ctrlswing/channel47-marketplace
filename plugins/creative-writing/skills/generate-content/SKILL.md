---
name: generate-content
description: Create first drafts matching style guide principles
args:
  - name: prompt
    description: What to write (topic, audience, content type)
    required: false
  - name: outline
    description: Optional outline for structured generation
    required: false
    flag: true
  - name: style-guide
    description: Path to custom style guide (overrides default/settings)
    required: false
    flag: true
---

# Generate Content Skill

This skill creates first drafts that match style guide principles.

## Workflow

**Step 1: Load full style guide**

Check for style guide in this order:
1. `--style-guide` parameter (if provided)
2. `.claude/creative-writing.local.md` custom_style_guide setting
3. Default style guide at `default-style-guide.md`

Load ALL sections (full guide) for generation.

**Step 2: Parse prompt**

If prompt not provided, ask:

```
What would you like to write? Include:
- Topic or subject
- Target audience
- Content type (blog post, email, documentation, essay, etc.)
- Any specific points to cover
```

If prompt is vague (missing content type or audience), ask clarifying questions:

```
What type of content? (blog post, email, technical doc, essay, etc.)
```

```
Who's the audience? (technical peers, general readers, executives, customers, etc.)
```

**Step 3: Check for outline**

If `--outline` provided, parse it as structure guide.

If no outline but content seems complex, ask:

```
Want to provide an outline? It'll help structure the piece. (Optional, press enter to skip)
```

**Step 4: Generate content**

Create draft following ALL style guide principles:

**Voice:**
- Lead with honesty (personal admission or real observation)
- Show reasoning (walk through thought process)
- Acknowledge trade-offs (nothing is perfect)

**Structure:**
- Vary sentence length (mix short and long)
- Natural paragraph breaks (one idea per paragraph)
- Prose over lists (incorporate items into narrative)

**Word Choice:**
- Concrete details (specific examples)
- Simple metaphors (clarify, don't impress)
- Conversational asides (add warmth)

**Avoid:**
- Em-dashes and colons
- Hype words
- Rhetorical questions as transitions
- Generic CTAs
- Bold declarations as opening
- Headers every 2-3 paragraphs

**Ending:**
- Genuine question (specific, not generic)

**Step 5: Present draft**

```markdown
## Draft

[Generated content]

## Notes

This draft follows [default/custom] style guide principles:
- [Brief note on voice]
- [Brief note on structure]
- [Brief note on word choice]

Use /review-writing to get feedback or /edit-draft to refine further.
```

## Error Handling

**Ambiguous prompt**: If can't determine content type after clarification:
```
I need more context to generate useful content. Please describe what you want to write in more detail.
```

**Missing style guide**: Same as edit-draft.
