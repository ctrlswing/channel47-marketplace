# Creative Writing Plugin

A Claude Code plugin that helps you write clearer, more honest prose.

## What It Does

- **Write and edit content** with unified workflow for drafts, editing, openings, endings, and pattern removal
- **Review writing** with specific, actionable feedback
- **Configure style guides** through interactive questionnaire

## Installation

```bash
claude plugin install channel47-marketplace/creative-writing
```

## Quick Start

See [GETTING_STARTED.md](./GETTING_STARTED.md) for detailed instructions.

## Skills

- `/write` - Generate or refine content (drafts, editing, openings, endings, pattern removal)
- `/review` - Get feedback without rewriting
- `/configure` - Create personalized style guide

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

## Examples

See `examples/my-style-guide.md` for a sample custom style guide tailored to technical writing.

## How It Works

The plugin uses progressive disclosure to load only relevant documentation:

- `/write` auto-detects mode (draft, edit, opening, ending, clean) and loads appropriate style guide sections
- `/review` loads pattern detection reference for consistent feedback
- Reference files (`writing-patterns.md`, `style-guide-loader.md`) are loaded on-demand

This keeps token usage efficient while maintaining quality.

## License

MIT
