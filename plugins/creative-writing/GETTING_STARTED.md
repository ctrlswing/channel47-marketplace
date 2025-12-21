# Getting Started with Creative Writing Plugin

## First Use

1. **Try editing existing content**

```bash
/edit-draft
```

Paste your content when prompted. The plugin will rewrite it following style guide principles.

2. **Generate new content**

```bash
/generate-content
```

Describe what you want to write. The plugin will ask clarifying questions and generate a draft.

3. **Create a personal style guide** (optional)

```bash
/generate-style-guide
```

Answer a few questions about your writing preferences. The plugin generates a custom style guide.

## Typical Workflow

1. Write a draft
2. Run `/review-writing` to get feedback
3. Use `/improve-opening` or `/strengthen-ending` for specific sections
4. Polish with `/edit-draft`

## Customization

### Use a Custom Style Guide

All skills accept `--style-guide`:

```bash
/edit-draft --style-guide docs/my-guide.md
```

### Set Persistent Preferences

Create `.claude/creative-writing.local.md`:

```yaml
---
preferred_tone: conversational
target_audience: technical
custom_style_guide: docs/technical-writing-guide.md
---

# Additional Notes

I prefer short paragraphs and minimal jargon.
```

Now all skills use your custom guide by default.

## Tips

- Start with `/review-writing` before making changes
- Use `/remove-ai-tells` to quickly clean AI-generated drafts
- Create multiple style guides for different content types
- Override settings with `--style-guide` for one-off variations
