---
name: configure
description: Interactive questionnaire to create personalized style guide
---

# Generate Style Guide Skill

Interactive questionnaire that creates personalized style guides.

## Workflow

**Step 1: Load default guide as template**

Read `default-style-guide.md` to use as structure template.

**Step 2: Ask content formats**

```
What types of content do you primarily write? (Select all that apply)

- Blog posts
- Technical documentation
- Marketing copy
- Emails
- Essays
- Social media
- Other: [text input]
```

**Step 3: Ask about favored writers**

```
Which writing style resonates most with you?

- Hemingway: Short, direct sentences
  Example: "He was an old man who fished alone in a skiff in the Gulf Stream and he had gone eighty-four days now without taking a fish."

- Didion: Introspective, rhythmic
  Example: "We tell ourselves stories in order to live. The princess is caged in the consulate. The man with the candy will lead the children into the sea."

- Orwell: Clear, political
  Example: "Political language is designed to make lies sound truthful and murder respectable, and to give an appearance of solidity to pure wind."

- McPhee: Detailed, observational
  Example: "The river was not high. It lacked at least a foot of being bankfull, and there was no perceptible current where we stood."

- Other: [text input for custom preference]
```

**Step 4: Ask tone preferences**

```
How do you prefer to sound?

- Formal or conversational?
- Authoritative or humble?
- Technical or accessible?
```

**Step 5: Ask structure preferences**

```
Structure preferences:

- Paragraph length: Short (2-3 sentences) / Medium (4-6) / Long (7+)
- Use of examples: Minimal / Moderate / Extensive
- Lists vs prose: Prefer lists / Mix of both / Mostly prose
```

**Step 6: Ask about audience**

```
Who typically reads your work?

- Technical peers
- General audience
- Executives/decision-makers
- Customers/users
- Other: [text input]
```

**Step 7: Ask about deal-breakers**

```
Are there any patterns or phrases you absolutely want to avoid? (Optional)

Examples: "just", "simply", "obviously", excessive exclamation points, etc.

[text input]
```

**Step 8: Generate personalized guide**

Using default guide structure, create customized version:

**Voice Principles section:**
- Adapt based on tone preferences (formal/conversational, etc.)
- Include deal-breakers from step 7

**Structure Guidelines section:**
- Customize based on paragraph length preference
- Adjust list/prose guidance based on preference
- Consider content formats from step 1

**Word Choice Standards section:**
- Tailor to audience (technical vs general)
- Reference favored writer's style if applicable
- Include example preferences

**Patterns to Avoid section:**
- Keep core patterns (em-dashes, hype words, etc.)
- Add user-specified deal-breakers
- Customize based on content type

**Endings section:**
- Adapt based on content formats and audience

**Quick Reference Checklist section:**
- Customize checklist items based on user priorities

**Step 9: Write to file**

Save generated guide to `my-style-guide.md` in current directory.

Present:

```markdown
## Your Personalized Style Guide

Created: `my-style-guide.md`

Based on your preferences:
- Content types: [list from step 2]
- Style inspiration: [choice from step 3]
- Tone: [preferences from step 4]
- Audience: [from step 6]

## Next Steps

1. Review and edit `my-style-guide.md` as needed
2. Set it as default in `.claude/creative-writing.local.md`:

```yaml
---
custom_style_guide: my-style-guide.md
---
```

3. Use with any skill: `/edit-draft --style-guide my-style-guide.md`

All creative-writing skills will now use your personalized guide.
```

## Error Handling

**File already exists**:
```
File `my-style-guide.md` already exists. Overwrite? (yes/no)
```

If no, ask for alternate filename.

**Incomplete responses**:
If user skips questions, use sensible defaults from default guide.
