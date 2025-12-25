# Style Guide Section Loader

Maps operation modes to required style guide sections.

## Section Loading by Mode

### Draft Mode
Load complete style guide:
- Voice Principles
- Structure Guidelines
- Word Choice Standards
- Patterns to Avoid
- Endings
- Quick Reference Checklist

### Edit Mode
Load these sections:
- Voice Principles
- Structure Guidelines
- Word Choice Standards
- Patterns to Avoid
- Quick Reference Checklist

### Opening Mode
Load these sections:
- Voice Principles (especially "Lead with honesty")
- Patterns to Avoid (performative openings)

### Ending Mode
Load these sections:
- Endings
- Patterns to Avoid (generic CTAs)

### Clean Mode
Load pattern detection only:
- Full "Patterns to Avoid" table
- Reference [writing-patterns.md](writing-patterns.md) for comprehensive rules

## Section Extraction Method

Use header matching to extract sections from style guide:

```
Find: ## Voice Principles
Extract: From this header through the line before next ## header
```

If custom style guide doesn't have these exact headers, load full guide.
