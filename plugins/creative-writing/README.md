# Creative Writing Plugin

A Claude Code plugin that helps you write clearer, more honest prose.

## What It Does

- **Edit drafts** to remove AI writing patterns and improve clarity
- **Generate content** that matches your style guide
- **Review writing** with specific, actionable feedback
- **Improve openings** and strengthen endings
- **Remove AI tells** like em-dashes and hype words
- **Create style guides** through interactive questionnaire

## Installation

```bash
claude plugin install channel47-marketplace/creative-writing
```

## Quick Start

See [GETTING_STARTED.md](./GETTING_STARTED.md) for detailed instructions.

## Skills

- `/edit-draft` - Rewrite content to match style guide
- `/generate-content` - Create first drafts
- `/review-writing` - Get feedback without rewriting
- `/improve-opening` - Fix first 1-3 paragraphs
- `/strengthen-ending` - Improve conclusions
- `/remove-ai-tells` - Clean common AI patterns
- `/generate-style-guide` - Create personalized guide

## Customization

Create `.claude/creative-writing.local.md` to set preferences:

```yaml
---
preferred_tone: conversational
target_audience: general
custom_style_guide: docs/my-style-guide.md
---
```

All skills accept `--style-guide <path>` to override defaults.

## License

MIT
