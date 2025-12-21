# Creative Writing Plugin Design

## Overview

The creative-writing plugin is a pure Claude Code plugin that helps users improve their writing through editing, generation, and review. It provides focused skills for common writing tasks and supports customization through user-defined style guides.

## Core Philosophy

Built on principles of clear, honest prose: leading with honesty over authority, showing reasoning rather than conclusions, and acknowledging trade-offs. The plugin helps users write naturally and conversationally across different content types while avoiding common AI writing patterns.

## Plugin Structure

```
plugins/creative-writing/
├── .claude-plugin/
│   ├── plugin.json
│   ├── default-style-guide.md
│   ├── creative-writing.local.md.template
│   └── skills/
│       ├── edit-draft.md
│       ├── generate-content.md
│       ├── review-writing.md
│       ├── improve-opening.md
│       ├── strengthen-ending.md
│       ├── remove-ai-tells.md
│       └── generate-style-guide.md
├── README.md
├── GETTING_STARTED.md
└── CHANGELOG.md
```

### Plugin Manifest

Standard Claude Code plugin manifest with no external dependencies:

```json
{
  "name": "creative-writing",
  "version": "1.0.0",
  "description": "Writing assistant for editing, generating, and improving prose",
  "author": {
    "name": "Jackson",
    "url": "https://channel47.dev"
  },
  "homepage": "https://channel47.dev/plugins/creative-writing",
  "repository": "https://github.com/yourusername/channel47-marketplace"
}
```

### Default Style Guide

The `default-style-guide.md` contains generalized best practices applicable to multiple content types:

**Voice Principles**
- Lead with honesty instead of authority
- Show reasoning rather than just stating conclusions
- Acknowledge trade-offs openly

**Structure Guidelines**
- Vary sentence length (mix short punches with longer explanations)
- Use natural paragraph breaks (one idea per paragraph)
- Favor prose over bullet points in body text

**Word Choice Standards**
- Prioritize concrete details over abstractions
- Use simple metaphors that clarify rather than impress
- Include conversational asides that add warmth

**Patterns to Avoid**
- Em-dashes and colons (overused in AI writing)
- Hype words ("game-changer," "revolutionary")
- Rhetorical questions as transitions
- Generic CTAs
- Opening with bold declarations
- Headers every 2-3 paragraphs

**Quick Reference Checklist**
1. Does the opening feel honest or performative?
2. Am I telling the reader what to think, or showing them how I got there?
3. Are there any lists that could be prose?
4. Did I acknowledge a real trade-off or limitation?
5. Is my ending a genuine question or a formality?
6. Could I cut any sentence without losing meaning?

## Skills Design

### `/edit-draft`

Rewrites content to match style guide principles.

**Chunks loaded**: Voice Principles, Structure, Word Choice, Patterns to Avoid, Quick Reference

**Input**: Content (pasted or file reference)

**Parameters**:
- `--style-guide <path>`: Optional custom style guide for this edit

**Output**: Before/after comparison with brief explanation of major changes

**Workflow**:
1. Load appropriate style guide (custom if specified, otherwise default/settings)
2. Extract relevant chunks
3. Analyze content against principles
4. Rewrite while preserving core meaning
5. Present changes with reasoning

### `/generate-content`

Creates first drafts matching the style guide.

**Chunks loaded**: Full style guide (all sections)

**Input**: Topic, audience, content type prompt

**Parameters**:
- `--outline <text>`: Optional outline for structured generation
- `--style-guide <path>`: Optional custom style guide

**Output**: Complete draft matching style principles

**Workflow**:
1. Parse initial prompt
2. Ask clarifying questions if prompt is vague
3. Load full style guide
4. Generate content following all principles
5. Present draft

### `/review-writing`

Provides feedback without rewriting.

**Chunks loaded**: Quick Reference (editing checklist), Patterns to Avoid

**Input**: Content to review

**Parameters**:
- `--style-guide <path>`: Optional custom style guide

**Output**: Specific, actionable notes organized by category

**Workflow**:
1. Analyze content against editing checklist
2. Identify patterns to avoid
3. Organize feedback by category (opening, reasoning, trade-offs, structure, word choice, ending)
4. Provide specific examples and suggestions

### `/improve-opening`

Specialized skill for first 1-3 paragraphs.

**Chunks loaded**: Voice Principles, Patterns to Avoid

**Input**: Opening paragraphs or full content (focuses on beginning)

**Parameters**:
- `--style-guide <path>`: Optional custom style guide

**Output**: Rewritten opening

**Workflow**:
1. Extract opening section
2. Check against voice principles (honesty over authority)
3. Remove performative declarations
4. Rewrite with reasoning

### `/strengthen-ending`

Focuses on conclusions and CTAs.

**Chunks loaded**: Endings section, Patterns to Avoid

**Input**: Ending paragraphs or full content (focuses on conclusion)

**Parameters**:
- `--style-guide <path>`: Optional custom style guide

**Output**: Rewritten ending

**Workflow**:
1. Extract ending section
2. Identify generic CTAs or weak conclusions
3. Replace with specific, genuine questions or natural closings
4. Present improved version

### `/remove-ai-tells`

Scans for and removes common AI writing patterns.

**Chunks loaded**: Patterns to Avoid (full table)

**Input**: Content to clean

**Parameters**:
- `--style-guide <path>`: Optional custom style guide

**Output**: Clean version with annotations of changes

**Workflow**:
1. Scan for AI patterns (em-dashes, colons, bullet point abuse, hype words, rhetorical questions)
2. Remove or replace each pattern
3. Annotate what was changed and why
4. Present cleaned version

### `/generate-style-guide`

Interactive questionnaire to help users create personalized style guides.

**Chunks loaded**: Full default guide (as template structure)

**Input**: None (interactive)

**Output**: Generated `my-style-guide.md` file

**Workflow**:
1. Ask content formats question (multiple choice: blog posts, technical docs, marketing, emails, essays, etc.)
2. Ask favored writers question (multiple choice with 4-5 distinct authors showing short writing examples + open-ended option)
3. Ask tone preference (formal vs. conversational, authoritative vs. humble, technical vs. accessible)
4. Ask structure preferences (paragraph length, use of examples, etc.)
5. Ask about target audience (technical peers, general, executives, customers)
6. Ask about deal-breakers (patterns to absolutely avoid)
7. Generate personalized style guide using default structure as template
8. Write to `my-style-guide.md`

**Example authors for Question 2**:
- Hemingway: Short, direct sentences. "He was an old man who fished alone in a skiff in the Gulf Stream and he had gone eighty-four days now without taking a fish."
- Didion: Introspective, rhythmic. "We tell ourselves stories in order to live. The princess is caged in the consulate. The man with the candy will lead the children into the sea."
- Orwell: Clear, political. "Political language is designed to make lies sound truthful and murder respectable, and to give an appearance of solidity to pure wind."
- McPhee: Detailed, observational. "The river was not high. It lacked at least a foot of being bankfull, and there was no perceptible current where we stood."
- Custom input option

## Smart Chunking Implementation

Each skill loads only the style guide sections it needs to keep token usage efficient.

**Chunking strategy**: Default style guide uses clear markdown headers (## Voice Principles, ## Structure, ## Word Choice, etc.). Skills extract specific sections via header matching.

**Skill-to-chunk mapping**:
- `/edit-draft`: Voice Principles, Structure, Word Choice, Patterns to Avoid, Quick Reference
- `/generate-content`: Full style guide (all sections)
- `/review-writing`: Quick Reference, Patterns to Avoid
- `/improve-opening`: Voice Principles, Patterns to Avoid
- `/strengthen-ending`: Endings section, Patterns to Avoid
- `/remove-ai-tells`: Patterns to Avoid (full table)
- `/generate-style-guide`: Full guide (as template)

**Custom style guide handling**: When users provide custom guides, skills attempt to match similar section headers. If structure differs, falls back to passing the full custom guide for that execution.

**Implementation**: Each skill's markdown file includes preprocessing logic that reads the appropriate style guide file, extracts relevant sections using header matching, and injects them into the prompt context.

## Settings and Customization

Users can customize behavior through `.claude/creative-writing.local.md` for persistent preferences.

**Settings file structure**:

```markdown
---
preferred_tone: conversational
target_audience: general
content_types:
  - blog posts
  - technical writing
  - essays
custom_style_guide: null  # or path like "docs/my-style-guide.md"
---

# My Writing Preferences

[Optional: Additional style notes that supplement the default guide]
```

**How skills use settings**:
1. Check for `.claude/creative-writing.local.md`
2. Parse YAML frontmatter for configuration
3. Check if `custom_style_guide` points to external file
4. If external file exists, use it instead of default; if null, use default
5. Read markdown content after frontmatter as supplemental guidance

**Parameter overrides**: All skills accept `--style-guide <path>` parameter for one-off customization. This overrides both default guide and settings file for that execution.

**Initialization**: Plugin ships with `.claude-plugin/creative-writing.local.md.template` showing the structure. Users copy to `.claude/creative-writing.local.md` and customize. Not required - plugin works with defaults.

## Error Handling and Edge Cases

**Missing or malformed style guides**: If custom style guide doesn't exist or can't be parsed, skill falls back to default and shows warning: "Couldn't load custom style guide at [path], using default instead."

**Empty or very short content**: Skills requiring minimum content (like `/edit-draft` or `/review-writing`) check input length. If less than ~50 words, prompt: "Content seems short. For better results, provide at least a paragraph or two."

**Ambiguous content type**: When `/generate-content` can't determine content type from prompt, asks clarifying question: "What type of content? (blog post, email, documentation, essay, etc.)"

**Conflicting settings**: If both settings file has custom style guide AND user passes `--style-guide` parameter, parameter wins. Skill notifies: "Using [parameter file] for this task (overriding settings)."

**Style guide structure mismatch**: When smart chunking can't find expected sections in custom guide, loads full custom guide instead with note: "Custom guide structure differs from default, using full content."

## User Experience Flow

### First-time user

1. Installs plugin from Channel 47 marketplace
2. Uses `/generate-style-guide` to create personalized style guide (optional)
3. Tries `/edit-draft` with existing content to see improvements
4. Uses `/generate-content` for new drafts
5. Optionally creates `.claude/creative-writing.local.md` for persistent preferences

### Regular workflow

1. User writes draft
2. Runs `/review-writing` to get feedback
3. Uses focused skills (`/improve-opening`, `/strengthen-ending`, `/remove-ai-tells`) for specific issues
4. Final polish with `/edit-draft`

### Advanced customization

1. User creates detailed style guide in `docs/my-style-guide.md`
2. Sets `custom_style_guide: docs/my-style-guide.md` in settings
3. All skills now use custom guide by default
4. Can still override with `--style-guide` for one-off variations

## Implementation Notes

**Pure Claude Code**: No external dependencies, MCP servers, or Python requirements. Skills are markdown files with prompts.

**Token efficiency**: Smart chunking ensures only relevant style guide sections are loaded per skill, keeping context manageable.

**Extensibility**: Users can add their own style guides without modifying plugin code. Settings file provides clean customization point.

**Portability**: Works on any Claude Code installation with no setup beyond plugin installation.

## Success Criteria

1. Users can edit drafts to remove AI writing patterns and improve clarity
2. Generated content matches style guide principles without manual cleanup
3. Custom style guides work seamlessly with all skills
4. Skills provide actionable, specific feedback (not generic encouragement)
5. Token usage stays efficient through smart chunking
6. First-time users can get value within 5 minutes of installation
