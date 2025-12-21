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

## Troubleshooting

### Custom style guide not loading

Check that the path in `.claude/creative-writing.local.md` is correct and the file exists:

```bash
cat .claude/creative-writing.local.md
```

Verify the `custom_style_guide` path matches your file location.

### Skills using wrong style guide

Skills check for style guides in this order:

1. `--style-guide` parameter (highest priority)
2. `.claude/creative-writing.local.md` setting
3. Default style guide (fallback)

Use `--style-guide` to override for one-off tasks.

### Generated content still has AI patterns

Try:

1. Run `/remove-ai-tells` to clean common patterns
2. Use `/review-writing` to identify specific issues
3. Update your custom style guide to emphasize patterns you want to avoid
4. Run `/edit-draft` for a full rewrite

### Want to reset to defaults

Remove or comment out custom_style_guide in `.claude/creative-writing.local.md`:

```yaml
---
custom_style_guide: null  # back to default
---
```
