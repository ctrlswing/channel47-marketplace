# Prompt Enhancer Plugin Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a prompt-enhancer plugin for the Channel 47 marketplace that optimizes prompts using Anthropic's 2025 best practices for Claude 4.x models.

**Architecture:** Single-skill plugin with progressive disclosure pattern. Main `/prompt-enhancer` skill systematically applies mandatory techniques (XML tags, role, data separation, output format) and contextual techniques (CoT, examples, prefilling, extended thinking) based on task type. Interactive `/build-prompt` command provides step-by-step wizard. Reference materials loaded on-demand to keep token usage efficient.

**Tech Stack:** Markdown for documentation and skills, YAML frontmatter for metadata, progressive disclosure pattern for token efficiency.

---

## Task 1: Plugin Manifest and Core Documentation

**Files:**
- Create: `plugins/prompt-enhancer/.claude-plugin/plugin.json`
- Create: `plugins/prompt-enhancer/README.md`
- Create: `plugins/prompt-enhancer/GETTING_STARTED.md`
- Create: `plugins/prompt-enhancer/CHANGELOG.md`

**Step 1: Create plugin manifest**

Create: `plugins/prompt-enhancer/.claude-plugin/plugin.json`

```json
{
  "name": "prompt-enhancer",
  "version": "1.0.0",
  "description": "Optimize prompts using Anthropic's 2025 best practices for Claude 4.x models",
  "author": {
    "name": "Jackson",
    "url": "https://channel47.dev"
  },
  "homepage": "https://channel47.dev/plugins/prompt-enhancer",
  "repository": "https://github.com/ctrlswing/channel47-marketplace"
}
```

**Step 2: Create README.md**

Create: `plugins/prompt-enhancer/README.md`

```markdown
# Prompt Enhancer

Optimize prompts using Anthropic's 2025 best practices for Claude 4.x models.

## What It Does

Systematically applies proven techniques to improve prompt quality:
- XML tags for clear structure
- Role assignment for better context
- Chain of thought for reasoning tasks
- Data separation for security
- Prefilling, extended thinking, and more

Updated for Claude 4.x literal interpretation and improved instruction following.

## Installation

```bash
/plugin marketplace add ctrlswing/channel47-marketplace
```

## Quick Start

**Optimize an existing prompt:**
```bash
/prompt-enhancer "Your prompt here"
```

**Interactive wizard:**
```bash
/build-prompt
```

## What You Get

- ✅ Mandatory techniques applied automatically
- 💡 Contextual techniques based on task type
- 🎯 Claude 4.x optimizations (Sonnet 4.5, Haiku 4.5)
- 📚 Comprehensive reference library
- 🔍 Before/after examples

## Learn More

See [GETTING_STARTED.md](GETTING_STARTED.md) for detailed guide.

## Features

### Main Skill: `/prompt-enhancer`

Systematically optimizes prompts using:
- Mandatory techniques (XML tags, role, output format, data separation)
- Contextual techniques based on task type
- Claude 4.x-specific optimizations
- Before/after comparison with explanations

### Interactive Command: `/build-prompt`

8-phase wizard for building prompts step-by-step:
1. Task Discovery
2. Role Assignment
3. Context Gathering
4. Data Separation
5. Output Format
6. Advanced Techniques
7. Model Selection
8. Review & Export

### Reference Library

- Before/after gallery (8-10 examples)
- Task-type templates (7 templates)
- Common patterns
- XML tag library
- New techniques guide (prefilling, extended thinking)
- Claude 4.x tips (Sonnet 4.5, Haiku 4.5)
- Quick reference cheat sheet

## Version

Current version: 1.0.0

See [CHANGELOG.md](CHANGELOG.md) for release history.
```

**Step 3: Create GETTING_STARTED.md**

Create: `plugins/prompt-enhancer/GETTING_STARTED.md`

```markdown
# Getting Started with Prompt Enhancer

## Overview

This plugin helps you write better prompts for Claude using Anthropic's documented best practices.

## The 80/20 Techniques

These techniques deliver maximum impact:

### 1. XML Tags (MANDATORY)
Separate prompt components for clarity and accuracy.

**Example:**
```xml
<instructions>
Analyze this data
</instructions>

<data>
{{USER_INPUT}}
</data>
```

### 2. Specific Role (MANDATORY)
Prime Claude with relevant expertise.

**Example:**
```
You are a senior e-commerce data analyst with expertise in retail sales patterns.
```

### 3. Clear Output Format (MANDATORY)
Show exactly what you expect.

**Example:**
```xml
<output_format>
| Product | Revenue | % of Total |
|---------|---------|------------|
</output_format>
```

### 4. Data Separation (MANDATORY)
Security: never mix user data with instructions.

### 5. Chain of Thought (CONTEXTUAL)
Add reasoning for complex tasks.

**When to use:** Analysis, multi-step problems, debugging

### 6. Few-Shot Examples (CONTEXTUAL)
Show format/structure (NOT for creative writing).

**When to use:** Formatting tasks, categorization, structured outputs
**When to skip:** Creative writing, simple queries

### 7. Prefilling (NEW)
Guide output format and skip preambles.

**Example:** Prefill `{` to force JSON output

### 8. Extended Thinking (NEW)
Enable deep reasoning for complex problems.

**When to use:** Multi-step math, debugging, algorithm optimization

## Usage Patterns

### Pattern 1: Quick Optimization
```bash
/prompt-enhancer "Analyze this sales data and create a report"
```

Claude will:
1. Detect task type (data-analysis)
2. Apply mandatory techniques
3. Add contextual techniques (CoT for analysis)
4. Show before/after comparison

### Pattern 2: Interactive Building
```bash
/build-prompt
```

Follow the 8-phase wizard:
- Answer questions about your task
- Get guidance on techniques to use
- Receive production-ready prompt

### Pattern 3: Task-Specific Template
```bash
/prompt-enhancer --task-type data-analysis
```

Loads the data-analysis template and optimizes from there.

## Claude 4.x Optimizations

Claude 4.x models take you literally - be explicit!

### Sonnet 4.5
- More forgiving with ambiguous prompts
- Strong multi-step reasoning
- Ideal for open-ended tasks

### Haiku 4.5
- Needs tighter constraints
- Benefits from schema-constrained outputs
- Best for well-structured problems

### Key Difference
Claude 4.x does exactly what you ask, nothing more. Request "helpful extras" explicitly:
- "Suggest improvements or alternatives"
- "Flag any potential issues you notice"
- "Add helpful context or explanations"

## Examples

The plugin includes real-world improvements:
- Data analysis prompts
- Legal review prompts
- Code generation prompts
- Creative writing prompts (showing when to skip examples)
- Customer support prompts
- And more...

## Reference Library

Access comprehensive guides:
- **Quick reference:** One-page cheat sheet
- **Before/after gallery:** See real improvements
- **Task templates:** 7 ready-to-use templates
- **XML tag library:** Complete catalog
- **Claude 4.x tips:** Model-specific optimization

## Next Steps

1. Try `/prompt-enhancer` on an existing prompt
2. Use `/build-prompt` to create a new one from scratch
3. Explore the before/after gallery for inspiration
4. Read Claude 4.x tips for model-specific optimization

## Tips for Success

- ✅ Always use XML tags (even for "simple" prompts)
- ✅ Be explicit with Claude 4.x (no inference)
- ✅ Skip examples for creative writing
- ✅ Use prefilling for format enforcement
- ✅ Enable extended thinking for complex reasoning
- ⚠️ Haiku 4.5 needs tighter constraints than Sonnet 4.5
```

**Step 4: Create CHANGELOG.md**

Create: `plugins/prompt-enhancer/CHANGELOG.md`

```markdown
# Changelog

All notable changes to the Prompt Enhancer plugin will be documented in this file.

## [1.0.0] - 2025-12-27

### Added
- Initial release of Prompt Enhancer plugin
- `/prompt-enhancer` skill with systematic optimization workflow
- `/build-prompt` interactive wizard command
- Comprehensive before/after examples gallery (8-10 examples)
- Task-type specific templates (7 types: data-analysis, legal, creative, code-gen, customer-feedback, qa, summarization)
- Common patterns reference (8 patterns)
- XML tag library with comprehensive catalog
- 2025 techniques guide (prefilling, extended thinking, prompt chaining, long context)
- Claude 4.x optimization tips (Sonnet 4.5, Haiku 4.5)
- Quick reference cheat sheet

### Features
- Mandatory technique enforcement (XML tags, role, format, data separation)
- Contextual technique application (CoT, examples, prefilling, extended thinking)
- Progressive disclosure for efficient token usage
- Model-specific optimization (Sonnet 4.5 vs Haiku 4.5)
- Before/after comparison with explanations
- Production-ready output
- Interactive 8-phase wizard for building prompts

### Documentation
- README with quick start guide
- GETTING_STARTED with detailed usage patterns
- Usage examples
- Comprehensive reference materials
- Migration guide from Claude 3.x to Claude 4.x

### Techniques Covered
- **Mandatory:** XML tags, specific role, clear output format, data separation
- **Contextual:** Chain of thought, few-shot examples (with nuanced guidance)
- **New (2025):** Prefilling, extended thinking, prompt chaining, long context tips
- **Claude 4.x:** Literal interpretation, model-specific optimization, migration guidance
```

**Step 5: Commit core documentation**

```bash
git add plugins/prompt-enhancer/.claude-plugin/plugin.json \
        plugins/prompt-enhancer/README.md \
        plugins/prompt-enhancer/GETTING_STARTED.md \
        plugins/prompt-enhancer/CHANGELOG.md
git commit -m "docs(prompt-enhancer): add plugin manifest and core documentation"
```

---

## Task 2: Main Prompt Enhancer Skill

**Files:**
- Create: `plugins/prompt-enhancer/skills/prompt-enhancer/SKILL.md`

**Step 1: Create main skill file with frontmatter and overview**

Create: `plugins/prompt-enhancer/skills/prompt-enhancer/SKILL.md` (Part 1)

```markdown
---
name: prompt-enhancer
description: Use when asked to optimize, improve, enhance, or refine prompts for Claude. Also use when reviewing prompts for quality, clarity, or effectiveness. Applies Anthropic best practices systematically.
args:
  - name: content
    description: The prompt to optimize (optional - can ask user for it)
    required: false
  - name: task-type
    description: Type of task (data-analysis, legal, creative, code-gen, etc.)
    required: false
    flag: true
---

# Prompt Enhancer

## Overview

Optimize prompts using Anthropic's documented best practices. This skill prevents common failures: skipping XML tags under pressure, forgetting chain-of-thought, mentioning examples without adding them, and weak data/instruction separation.

**Updated for Claude 4.x:** These models take you literally and do exactly what you ask, nothing more. Being explicit is MORE important than ever.

## When to Use

Use when the user asks to:
- "Optimize this prompt"
- "Improve my prompt"
- "Make this prompt better"
- "Enhance this for Claude"
- "Review this prompt"
- Questions about prompt quality or effectiveness

Use even under time pressure - these techniques take seconds but dramatically improve results.

## The 80/20 Techniques

Core Anthropic techniques that deliver maximum impact. Some are mandatory for every prompt, others are contextual based on task type:

### 1. XML Tags for Structure (MANDATORY)

**The #1 missing technique in baseline tests.** Use XML tags to separate prompt components:

```xml
<instructions>
[What Claude should do]
</instructions>

<data>
{{USER_INPUT}}
</data>

<examples>
<example>
<input>[example input]</input>
<output>[example output]</output>
</example>
</examples>

<output_format>
[How to structure the output]
</output_format>
```

**Why XML tags:**
- Clarity: Prevents Claude from mixing instructions with data
- Accuracy: Reduces errors from misinterpreting prompt parts
- Parseability: Makes Claude's output easier to extract programmatically
- Nesting: Supports hierarchical structure `<outer><inner></inner></outer>`
- **Claude 4.x:** Even more critical due to literal interpretation

**Common tags:** `<instructions>`, `<data>`, `<context>`, `<examples>`, `<example>`, `<output_format>`, `<thinking>`, `<answer>`, `<constraints>`, `<output>`, `<role>`, `<document>`, `<document_content>`, `<source>`

### 2. Chain of Thought (CONTEXTUAL)

Add reasoning before conclusions for complex tasks:

```xml
<instructions>
Think through this problem step by step in <thinking> tags, then provide your answer in <answer> tags.
</instructions>
```

Or simply: "Think step by step before answering."

**When to use:** Analysis, complex reasoning, multi-step problems, debugging, evaluation, legal review
**When to skip:** Simple transformations, basic summarization, straightforward Q&A

### 3. Few-Shot Examples (CONTEXTUAL)

When examples would help clarify the expected output, add them:

```xml
<examples>
<example>
<input>Customer said: "The app crashes when I upload photos"</input>
<output>
Theme: Technical Stability
Category: Bug Report
Severity: High
Sentiment: Frustrated
</output>
</example>

<example>
<input>Customer said: "Love the new dark mode!"</input>
<output>
Theme: UI/UX Improvement
Category: Feature Appreciation
Severity: N/A
Sentiment: Positive
</output>
</example>
</examples>
```

**When to use:**
- ✅ Formatting/structure enforcement (classification, extraction, JSON output)
- ✅ Technical domains with specific conventions
- ✅ Tone matching for consistent voice
- ✅ Edge case demonstration

**When to skip:**
- ❌ Creative writing (limits creative capacity)
- ❌ Simple transformations (instructions suffice)
- ❌ When you want novel/varied outputs
- ❌ Tasks where Claude's judgment is preferred

**Guideline:** When used, include 2-5 diverse examples showing edge cases and variations, not just the happy path. Examples are particularly valuable for unfamiliar formats or complex categorization tasks.

**⚠️ Claude 4.x Warning:** These models pay VERY close attention to example details. Bad examples = bad outputs. Examples must align precisely with desired behavior.

### 4. Clear Role Assignment (MANDATORY)

Start with specific role and context:

```
You are a [specific role] with expertise in [domain].
Your task is to [specific objective].

Context: [relevant background information]
```

Better: "You are a senior data analyst specializing in e-commerce metrics"
Not: "You are a helpful assistant"

### 5. Be Clear and Direct (MANDATORY)

**Strip ambiguity. Use plain language. Specify exactly what you want.**

This is MORE critical for Claude 4.x - these models do exactly what you ask, nothing more.

| ❌ Vague | ✅ Clear |
|---------|---------|
| "Tell me about risks" | "Identify business risks, legal risks, and compliance risks. For each risk, provide severity (HIGH/MEDIUM/LOW) and specific clause references." |
| "Analyze the data" | "Calculate total revenue, identify top 5 products by revenue with percentages, and show month-over-month growth rates." |
| "Make it professional" | "Use formal business tone. Structure as: Executive Summary, Key Findings (bullet points), Recommendations (numbered list)." |

**Claude 4.x Addition:** Request "helpful extras" explicitly:
- "Suggest improvements or alternatives"
- "Flag any potential issues you notice"
- "Add helpful context or explanations"

### 6. Separate Data from Instructions (MANDATORY)

**Always use XML tags to delimit user data from instructions:**

```xml
<instructions>
Analyze this customer feedback for sentiment and themes.
</instructions>

<customer_feedback>
{{FEEDBACK}}
</customer_feedback>
```

This prevents Claude from treating user data as additional instructions (prompt injection).

---

## New Techniques (2025)

### 7. Prefilling (CONTEXTUAL)

**What:** Start Claude's response to guide format/tone/behavior

**When to use:**
- Format enforcement (JSON, XML)
- Skip preambles
- Role consistency in role-playing
- Enforce specific opening

**How:** Add assistant message with initial text

**Examples:**
- JSON output: Prefill `{`
- XML output: Prefill `<response>`
- Role-playing: Prefill `[CHARACTER_NAME]:`
- Skip preamble: Prefill `Here are the results:`

**⚠️ Not compatible with extended thinking**

### 8. Extended Thinking (CONTEXTUAL)

**What:** Claude spends more time reasoning through complex problems

**When to use:**
- Multi-step math problems
- Debugging complex code
- Philosophical analysis
- Algorithm optimization
- Tasks requiring deep reasoning

**When to skip:**
- Simple queries
- When speed matters more than depth
- Well-structured straightforward problems

**Token Budgets:**
- Minimum: 1024 tokens
- Recommended start: 2048 tokens
- Incrementally increase based on complexity

**Best Practices:**
- High-level instructions work best (not step-by-step prescriptive)
- Use multishot prompting with `<thinking>` examples
- Works best in English (output can be any language)

**⚠️ Not compatible with prefilling**

---

## Claude 4.x Specific Optimizations

### Universal Changes

**1. Literal Interpretation**

Claude 4.x takes you literally - no inference, no expansion on vague requests.

**Impact:** Be MORE explicit in all instructions.

**Example:**
- ❌ "Tell me about risks" → Claude 4.x might give brief overview
- ✅ "Identify and list ALL business risks, legal risks, and compliance risks. For each risk, provide severity (HIGH/MEDIUM/LOW), specific clause references, and mitigation recommendations" → Comprehensive analysis

**2. Request "Helpful Extras" Explicitly**

Claude 4.x won't add "above and beyond" behaviors unless asked.

Add phrases like:
- "Suggest improvements or alternatives"
- "Flag any potential issues you notice"
- "Add helpful context or explanations"
- "Provide examples to clarify"

**3. Examples Must Align Precisely**

Claude 4.x pays VERY close attention to example details.

⚠️ Bad example showing outdated API → Claude might use outdated API
⚠️ Example with typos → Claude might include typos

✅ Curate 3-5 perfect examples that demonstrate EXACTLY desired behavior

### Model-Specific Tips

**Sonnet 4.5:**
- More forgiving with ambiguous prompts
- Excellent multi-step reasoning
- Handles open-ended tasks well
- Strong at synthesis and nuance
- Can handle longer, more complex instructions
- Works well with high-level goals vs rigid step-by-step

**Haiku 4.5:**
- Needs tighter constraints than Sonnet
- Benefits from schema-constrained outputs
- Defensive prompting recommended
- Use tighter templates (less room for interpretation)
- Shorter, more focused instructions
- Validation rules spelled out clearly
- Best for well-structured problems

---

## Systematic Optimization Process

When optimizing a prompt, follow this workflow:

**Step 1: Receive Prompt**
- Get prompt from user (via args or ask)
- If vague, ask clarifying questions

**Step 2: Detect Task Type**
- Auto-identify: data-analysis, legal, creative, code-gen, customer-feedback, qa, summarization
- This determines which techniques are mandatory vs contextual

**Step 3: Apply Mandatory Techniques (ALWAYS)**
- ✅ XML tags - At minimum: `<instructions>`, `<data>`, `<output_format>`
- ✅ Specific role - Replace "helpful assistant" with domain expert
- ✅ Clear output format - Template or explicit structure
- ✅ Data separation - User data in `<data>` tags, never mixed with instructions

**Step 4: Apply Contextual Techniques (BASED ON TASK)**
- 💡 Chain of thought - For analysis, reasoning, multi-step problems
- 💡 Few-shot examples - For formatting/structure (NOT creative writing)
- 💡 Prefilling - For format enforcement (JSON, XML, role-playing)
- 💡 Extended thinking - For complex reasoning (Claude 4.x only)
- 💡 Constraints/edge cases - For production systems

**Step 5: Add Claude 4.x Optimizations**
- 🎯 Explicit instructions - Claude 4.x takes you literally
- 🎯 Request "helpful extras" - Must ask explicitly for "above and beyond"
- 🎯 Model-specific tips - Sonnet 4.5 vs Haiku 4.5
- 🎯 Examples must align precisely - Claude 4.x pays close attention

**Step 6: Present Before/After**
- Show original prompt
- Show optimized version with XML structure
- Explain each improvement and why it matters
- Provide evaluation checklist

---

## Quick Reference: Technique Selection

| Task Type | Mandatory Techniques | Contextual (Recommended) | Skip |
|-----------|-------------------|---------------------|------|
| Data analysis | XML tags, Role, Output format | CoT, Examples | - |
| Legal/Contract review | XML tags, Role, Output format, CoT | Examples | - |
| Creative writing | XML tags, Role, Tone specification | Constraints | Examples |
| Code generation | XML tags, Output format | Examples, Edge cases | - |
| Customer feedback analysis | XML tags, Role, Categorization structure | Examples | - |
| Question answering | XML tags (context separation), Output format | CoT (if complex) | Examples (usually) |
| Summarization | XML tags, Role, Output format (length, structure) | - | Examples |

---

## Technique Requirements: What's Mandatory vs Contextual

**These techniques are MANDATORY for every single prompt optimization:**

| Technique | Why Mandatory | Minimum Implementation |
|-----------|--------------|----------------------|
| **XML tags** | Data/instruction separation prevents prompt injection. Anthropic's #1 recommendation. Claude 4.x literal interpretation makes this even more critical. | At minimum: `<instructions>` and `<data>` (if user data present) |
| **Specific role** | Primes Claude with relevant context. One line, massive impact. | Replace "helpful assistant" with specific expert role |
| **Clear output format** | Eliminates ambiguity. Shows exact structure expected. Claude 4.x needs this for literal interpretation. | Provide template or specific format (bullets, sections, etc.) |
| **Data separation** | Security and accuracy. Never mix user data with instructions. | Use `<data>` or similar tag for ALL user variables |

**These techniques are CONTEXTUAL (apply based on task):**

| Technique | When to Apply | When You Can Skip |
|-----------|--------------|-------------------|
| **Chain of thought** | Analysis, complex reasoning, multi-step problems, debugging, legal review | Simple transformations, basic summarization, straightforward Q&A |
| **Few-shot examples** | Formatting/structure, categorization, unfamiliar formats | Creative writing, simple tasks, when flexibility needed |
| **Prefilling** | Format enforcement (JSON/XML), skip preambles, role consistency | When using extended thinking, simple queries |
| **Extended thinking** | Complex reasoning, multi-step math, debugging, algorithm optimization | Simple queries, when speed matters, well-structured problems |
| **Constraints/edge cases** | Production systems, reusable templates, handling variable data | One-off personal use with controlled inputs |

**The "Simple Task" Trap:**

Don't rationalize skipping mandatory techniques by claiming the task is "simple." Even the simplest prompt benefits from:
- ✅ XML tags (2 extra lines)
- ✅ Specific role (1 line)
- ✅ Output format (3-5 lines showing structure)

**Total overhead: ~10 lines. Impact: Dramatically better results.**

---

## Common Mistakes to Avoid

| Mistake | Why It Happens | Fix |
|---------|---------------|-----|
| **No XML tags** | Feels like extra syntax | XML tags are Anthropic's #1 recommendation. Always use them. |
| **Mentioning examples without adding them** | Faster to describe than write | If you decide examples would help, write 2-5 actual examples. Takes 2 minutes, massive quality boost. |
| **Using examples for creative writing** | Assumed they always help | Examples limit creative capacity. Skip for creative tasks. |
| **Skipping chain of thought** | Seems unnecessary | Complex tasks need reasoning. Add `<thinking>` tags. |
| **Vague output format** | Assumes Claude will figure it out | Specify exact structure: sections, format, precision, tone. |
| **Generic role** | "helpful assistant" is easy | Specific roles (senior analyst, legal expert) improve outputs. |
| **Time pressure shortcuts** | Demo in 10 minutes | Mandatory techniques take seconds. Never skip. |
| **Settling for "good enough"** | Sunk cost fallacy | Apply ALL mandatory techniques, not just some. |
| **"This task is simple enough"** | Rationalization to skip techniques | MANDATORY techniques apply to ALL prompts, simple or complex. |
| **Assuming Claude 4.x will infer** | Used to Claude 3.x behavior | Claude 4.x takes you literally. Be explicit. |

---

## Red Flags - You're Skipping Best Practices

- Prompt has no XML tags
- Using headers/caps instead of XML tags
- "We could add examples..." without actually adding them (when you've decided they'd help)
- No `<thinking>` tags for complex reasoning
- Data and instructions not clearly separated
- Mentioned "chain of thought" but didn't implement it
- "Under time pressure, so I'll skip mandatory techniques"
- Output format described in prose instead of shown in template
- **"This task is simple enough to skip [mandatory technique]"** ← Rationalization detected!
- **"The user wants it short/simple, so I'll skip XML tags/role/format"** ← User preferences don't override mandatory techniques
- **"Already has some XML tags, so I'll skip other improvements"** ← Partial implementation isn't sufficient
- **"Claude 4.x is smart enough to figure it out"** ← These models take you literally!

**All of these mean: Go back and apply the mandatory techniques. Check the Technique Requirements table above.**

---

## Before/After Example

**❌ Before (typical baseline optimization):**
```
You are a data analyst. Analyze this sales data and create a summary report.

Data: {{SALES_DATA}}

Include:
- Total revenue
- Top performing products
- Monthly trends

Format as a professional report.
```

**✅ After (with Anthropic best practices + Claude 4.x optimizations):**
```xml
<role>
You are a senior e-commerce data analyst with expertise in retail sales patterns and trend analysis.
</role>

<instructions>
Analyze the provided sales data and create a structured summary report. Use step-by-step reasoning to identify meaningful patterns.

As you analyze, flag any unusual patterns or potential issues you notice.
</instructions>

<data>
{{SALES_DATA}}
</data>

<analysis_requirements>
1. Total Revenue: Sum all transactions, report in USD with 2 decimal places
2. Top Performers: Identify top 5 products by revenue, include percentage of total
3. Monthly Trends: Calculate month-over-month growth/decline as percentages
4. Anomalies: Flag any outliers or unusual patterns
</analysis_requirements>

<output_format>
Structure your response as:

<thinking>
[Your step-by-step analysis and reasoning]
</thinking>

<executive_summary>
[2-3 sentence overview of key findings]
</executive_summary>

<key_metrics>
- Total Revenue: $X.XX
- Time Period: [dates]
- Transaction Count: X
</key_metrics>

<top_products>
| Product | Revenue | % of Total |
|---------|---------|------------|
| ...     | ...     | ...        |
</top_products>

<trend_analysis>
[Month-by-month breakdown with growth rates]
</trend_analysis>

<recommendations>
1. [Actionable insight based on data]
2. [Actionable insight based on data]
</recommendations>
</output_format>

<examples>
<example>
<sample_finding>
If Product A generated $50K out of $200K total revenue:
Product A: $50,000 (25.0% of total revenue)
</sample_finding>
</example>
</examples>

<constraints>
- If data is incomplete, note this explicitly in your report
- Round percentages to 1 decimal place
- Flag any anomalies or outliers in the trend analysis
</constraints>
```

**Key improvements:**
- ✅ XML tags throughout (`<role>`, `<instructions>`, `<data>`, `<output_format>`, `<thinking>`, `<examples>`, `<constraints>`)
- ✅ Specific role (senior e-commerce analyst vs generic data analyst)
- ✅ Clear separation of data from instructions
- ✅ Concrete output template showing exact structure
- ✅ Chain of thought (`<thinking>` tags) for analysis
- 💡 Few-shot example demonstrating format
- ✅ Edge case handling (incomplete data)
- ✅ Precision specifications (decimal places)
- ✅ Claude 4.x: Explicit request to "flag any unusual patterns" (helpful extras)
- ✅ Claude 4.x: Very specific analysis requirements (literal interpretation)

---

## Evaluation Criteria

After optimizing a prompt, verify:

1. ✅ **XML tags present** - At minimum: `<instructions>`, `<data>` (if applicable), `<output_format>`
2. ✅ **Specific role assigned** - Not "helpful assistant"
3. ✅ **Data separated from instructions** - Clear boundaries
4. ✅ **Output format specified** - Template or explicit structure
5. 💡 **Examples included IF appropriate** - 2-5 actual examples for formatting tasks (skip for creative writing)
6. ✅ **Chain of thought added IF needed** - For reasoning/analysis tasks
7. ✅ **Clear and direct language** - No ambiguity, especially for Claude 4.x
8. ✅ **Edge cases addressed** - What if data is missing/malformed?
9. ✅ **Claude 4.x optimizations** - Explicit instructions, "helpful extras" requested if desired
10. ✅ **Model-specific tips** - Sonnet 4.5 vs Haiku 4.5 considerations

**If any ✅ checkbox is unchecked, the optimization is incomplete. The 💡 item is contextual based on task type.**

---

## Progressive Disclosure

To keep this skill efficient, detailed reference materials are loaded on-demand:

**Load when needed:**
- `technique-loader.md` - Deep dive on specific technique
- `model-specific-tips.md` - Detailed Claude 4.x model comparison
- `assets/reference/quick-reference.md` - One-page cheat sheet
- `assets/examples/before-after-gallery.md` - 8-10 real-world examples
- `assets/examples/task-type-templates.md` - Ready-to-use templates
- `assets/reference/xml-tag-library.md` - Comprehensive tag catalog
- `assets/reference/new-techniques.md` - Prefilling, extended thinking details
- `assets/reference/claude-4x-tips.md` - Complete model-specific guide

---

## Real-World Impact

Baseline tests showed that without systematic prompt engineering, agents:
- **0/4** used XML tags despite it being Anthropic's #1 recommendation
- **0/4** added chain of thought for reasoning tasks
- **0/4** actually implemented few-shot examples when they would have helped (only mentioned conceptually)
- **1/4** explicitly skipped "advanced techniques" under time pressure

With this skill, prompts systematically apply proven Anthropic techniques, resulting in:
- Higher quality Claude outputs
- More consistent results
- Better handling of edge cases
- Easier programmatic parsing of responses
- Reduced hallucinations and errors
- Better performance with Claude 4.x literal interpretation

---

## Sources

This skill synthesizes best practices from:
- Anthropic's Prompt Engineering Interactive Tutorial (9 chapters)
- Anthropic's Real World Prompting Course (5 lessons)
- Anthropic's Prompt Evaluations Course
- Anthropic's official documentation on XML tags and prompt engineering
- Claude 4.x model documentation and best practices
- Testing with baseline pressure scenarios revealing common failure patterns
- 2025 updates: Prefilling, Extended Thinking, Prompt Chaining guides
```

**Step 2: Commit main skill file**

```bash
git add plugins/prompt-enhancer/skills/prompt-enhancer/SKILL.md
git commit -m "feat(prompt-enhancer): add main optimization skill with Claude 4.x support"
```

---

## Task 3: Progressive Disclosure Support Files

**Files:**
- Create: `plugins/prompt-enhancer/skills/prompt-enhancer/technique-loader.md`
- Create: `plugins/prompt-enhancer/skills/prompt-enhancer/model-specific-tips.md`

**Step 1: Create technique-loader.md**

Create: `plugins/prompt-enhancer/skills/prompt-enhancer/technique-loader.md`

```markdown
# Technique Deep Dives

This file provides detailed guidance on specific prompt engineering techniques. Load sections on-demand.

---

## Chain of Thought (Extended Guide)

### What It Is
Chain of thought prompting encourages Claude to show its reasoning process before reaching conclusions.

### When to Use
- Multi-step problems requiring logical progression
- Analysis tasks where reasoning path matters
- Debugging complex issues
- Legal or contract review
- Comparative analysis
- Tasks where you need to verify the reasoning

### When to Skip
- Simple transformations (string formatting, basic math)
- Well-defined classification tasks
- Straightforward Q&A with factual answers
- When you only care about final output, not reasoning

### Implementation Patterns

**Pattern 1: Explicit Thinking Tags**
```xml
<instructions>
Analyze the contract and provide your reasoning in <thinking> tags, then your conclusion in <answer> tags.
</instructions>
```

**Pattern 2: Step-by-Step Instruction**
```xml
<instructions>
Before providing your final recommendation:
1. List all relevant factors
2. Evaluate pros and cons of each option
3. Explain your reasoning
4. Then provide final recommendation
</instructions>
```

**Pattern 3: Implicit Request**
```
Think through this step-by-step before answering.
```

### Best Practices
- Give Claude space to think (don't rush to answer)
- Use `<thinking>` and `<answer>` tags to separate reasoning from conclusion
- For complex tasks, break into explicit steps
- Review the reasoning, not just the answer

### Claude 4.x Considerations
- Claude 4.x is more literal - explicitly ask for step-by-step reasoning
- Consider using extended thinking for very complex reasoning tasks

---

## Few-Shot Examples (Extended Guide)

### What They Are
Providing 2-5 examples of the exact input/output pattern you want.

### When to Use

**✅ Use for:**
1. **Formatting/Structure Enforcement**
   - JSON extraction with specific schema
   - Classification into predefined categories
   - Table generation with specific columns
   - Structured data transformation

2. **Technical Domains**
   - Code generation with specific patterns
   - API responses with exact format
   - Regex patterns
   - SQL queries

3. **Tone/Style Matching**
   - Consistent voice across outputs
   - Brand-specific language
   - Technical vs. non-technical writing

4. **Edge Case Demonstration**
   - How to handle missing data
   - Error conditions
   - Boundary cases

**❌ Skip for:**
1. **Creative Writing**
   - Blog posts
   - Stories
   - Poetry
   - Brainstorming
   - Reason: Examples constrain creativity

2. **Simple Tasks**
   - Basic summarization
   - Straightforward transformations
   - When instructions are sufficient

3. **Novel Outputs**
   - When you want varied responses
   - Exploration tasks
   - Open-ended questions

### Implementation Pattern

```xml
<examples>
<example>
<input>
[Exact example input]
</input>
<output>
[Exact example output]
</output>
</example>

<example>
<input>
[Second example showing variation]
</input>
<output>
[Second example output]
</output>
</example>

<example>
<input>
[Edge case example]
</input>
<output>
[How to handle edge case]
</output>
</example>
</examples>
```

### How Many Examples?
- **Simple tasks:** 1-2 examples
- **Complex tasks:** 3-5 examples
- **Show diversity:** Include edge cases, not just happy path

### Claude 4.x Warning

**CRITICAL:** Claude 4.x pays VERY close attention to example details.

**Bad examples lead to bad outputs:**
- Example with typo → Claude might include typos
- Example with outdated API → Claude might use outdated API
- Example with suboptimal approach → Claude might use suboptimal approach

**Make examples pristine:**
- Perfect formatting
- Current best practices
- No errors or inconsistencies
- Exactly aligned with desired behavior

---

## Prefilling (Extended Guide)

### What It Is
Starting Claude's response with initial text to guide format, tone, or behavior.

### How It Works
Add an assistant message with the beginning of the response. Claude continues from there.

### Common Use Cases

**1. Force JSON Output**
```
User: Extract user data as JSON
Assistant: {
```
Result: Claude continues with JSON, skipping preamble.

**2. Force XML Output**
```
User: Provide structured analysis
Assistant: <analysis>
```
Result: Claude continues with XML structure.

**3. Skip Preambles**
```
User: List the top 5 products
Assistant: Here are the top 5 products:

1.
```
Result: Claude goes straight to the list.

**4. Role-Playing Consistency**
```
User: Respond as Sherlock Holmes
Assistant: [SHERLOCK HOLMES]:
```
Result: Claude maintains character throughout response.

**5. Enforce Specific Opening**
```
User: Write executive summary
Assistant: ## Executive Summary

Key findings:
```
Result: Claude uses exact format and structure.

### When to Use
- Format enforcement (JSON, XML, specific structure)
- Skip unnecessary preambles ("Certainly! I'd be happy to...")
- Maintain role consistency in multi-turn conversations
- Guide specific opening patterns

### When to Skip
- When using extended thinking (not compatible)
- When you want Claude's natural preamble
- Simple queries where format doesn't matter

### Claude 4.x Considerations
- Very effective with Claude 4.x literal interpretation
- Sonnet 4.5 and Haiku 4.5 both respect prefilling precisely
- Use for Haiku 4.5 when you need tight format control

### API Implementation
```json
{
  "model": "claude-sonnet-4-5-20250929",
  "messages": [
    {
      "role": "user",
      "content": "Extract name, email, and age as JSON"
    },
    {
      "role": "assistant",
      "content": "{"
    }
  ]
}
```

---

## Extended Thinking (Extended Guide)

### What It Is
A Claude 4.x feature that allows the model to spend more tokens on internal reasoning before responding.

### How It Works
You set a token budget for thinking. Claude uses those tokens to work through the problem step-by-step internally, then provides the final response.

### When to Use

**✅ Ideal for:**
- Multi-step mathematical problems
- Complex debugging scenarios
- Algorithm optimization
- Philosophical analysis
- Multi-layered reasoning tasks
- Tasks where you want Claude to explore multiple approaches

**❌ Skip when:**
- Simple queries (wastes tokens and time)
- Speed is critical
- Well-structured straightforward problems
- Basic transformations

### Token Budgets

**Recommendations:**
- **Minimum:** 1024 tokens (required minimum)
- **Starting point:** 2048 tokens
- **Complex tasks:** 4096-8192 tokens
- **Very complex:** 10000+ tokens

**Strategy:** Start with minimum, incrementally increase if results aren't deep enough.

### Implementation Pattern

**Via API:**
```json
{
  "model": "claude-sonnet-4-5-20250929",
  "thinking": {
    "type": "enabled",
    "budget_tokens": 2048
  },
  "messages": [...]
}
```

**Via Chat Interface:**
1. Select Claude 4 model
2. Click "Search and tools"
3. Toggle "Extended thinking" on
4. Set token budget

### Best Practices

**1. High-Level Instructions**
✅ "Optimize this algorithm for better performance"
❌ "Step 1: Analyze time complexity. Step 2: Identify bottlenecks. Step 3:..."

Extended thinking works best with goals, not prescriptive steps.

**2. Use Multishot Prompting**
Show Claude examples of thinking patterns:

```xml
<examples>
<example>
<problem>What is 15% of 80?</problem>
<thinking>
To find 15% of 80:
1. Convert 15% to decimal: 15% = 0.15
2. Multiply: 0.15 × 80 = 12
</thinking>
<answer>12</answer>
</example>
</examples>

<problem>What is 35% of 240?</problem>
```

**3. Language Considerations**
- Extended thinking works best in English
- Final output can be any language Claude supports
- If prompting in another language, consider switching to English for complex reasoning

### Limitations

**Not compatible with:**
- Prefilling (can't prefill when using extended thinking)
- Manual thinking block modification

**Performance:**
- Adds latency (more thinking = longer response time)
- Costs more tokens (thinking budget counts toward usage)
- Best for tasks where depth matters more than speed

### Claude 4.x Models

**Sonnet 4.5:**
- Excellent extended thinking performance
- Handles complex multi-step reasoning well
- Can explore nuanced approaches

**Haiku 4.5:**
- Supports extended thinking
- More pragmatic reasoning style
- Best for well-defined problems even with extended thinking

---

## Prompt Chaining (Extended Guide)

### What It Is
Breaking complex tasks into sequential prompts, where the output of one prompt becomes the input to the next.

### When to Use
- Multi-stage processing with validation between steps
- Different techniques needed for different stages
- Tasks too complex for single prompt
- When you need to inspect/validate intermediate results

### Pattern

```
Prompt 1: Extract structured data from documents
   ↓ Output: JSON with extracted fields

Prompt 2: Analyze structured data for patterns
   ↓ Output: Analysis with insights

Prompt 3: Generate report from analysis
   ↓ Output: Final formatted report
```

### Implementation Best Practices

**1. Use XML Tags to Pass Data**
```xml
<!-- Prompt 2 -->
<instructions>
Analyze the extracted data for patterns
</instructions>

<extracted_data>
{{OUTPUT_FROM_PROMPT_1}}
</extracted_data>
```

**2. Each Prompt Has Single Clear Goal**
- Don't try to do too much in one prompt
- Each stage should have one primary objective
- Easier to debug and optimize

**3. Validate Between Stages**
- Check output quality before proceeding
- Handle errors at each stage
- Log intermediate results

**4. Maintain Context Across Chain**
- Pass relevant context forward
- Reference earlier stages when needed
- Use consistent terminology

### Example Chain

**Stage 1: Extraction**
```xml
<instructions>
Extract the following fields from each document
</instructions>

<documents>
{{DOCUMENTS}}
</documents>

<output_format>
Return as JSON array with fields: title, author, date, summary
</output_format>
```

**Stage 2: Analysis**
```xml
<instructions>
Analyze the extracted documents for common themes and patterns
</instructions>

<extracted_data>
{{STAGE_1_OUTPUT}}
</extracted_data>

<output_format>
Provide:
1. Top 5 themes with document counts
2. Timeline analysis
3. Author analysis
</output_format>
```

**Stage 3: Report Generation**
```xml
<instructions>
Generate executive summary report from analysis
</instructions>

<analysis>
{{STAGE_2_OUTPUT}}
</analysis>

<output_format>
Markdown report with:
- Executive Summary
- Key Themes
- Timeline Insights
- Recommendations
</output_format>
```

### Benefits
- Better quality (focused prompts)
- Easier debugging (isolate problems)
- Validation points (catch errors early)
- Flexible (can modify stages independently)

### Trade-offs
- More API calls (higher cost)
- More latency (sequential processing)
- Requires orchestration logic

---

## Long Context Tips (Extended Guide)

### What It Is
Best practices for working with 100K+ token prompts containing multiple documents or large codebases.

### Key Challenges
- Claude might miss important details in middle of context
- Hard to reference specific parts
- Difficult to verify sources

### Best Practices

**1. Put Key Instructions at Beginning AND End**
```xml
<instructions>
Your primary task: Identify all security vulnerabilities
</instructions>

<!-- 100K tokens of documents here -->

<reminder>
Remember: Your primary task is to identify ALL security vulnerabilities.
Be thorough and cite specific locations.
</reminder>
```

**2. Use Document Tags with Metadata**
```xml
<documents>
<document index="1">
<source>security-audit-2024.pdf</source>
<document_content>
[content here]
</document_content>
</document>

<document index="2">
<source>codebase-review.md</source>
<document_content>
[content here]
</document_content>
</document>
</documents>
```

**3. Ask Claude to Quote Sources**
```xml
<instructions>
For each finding, cite the specific document and quote the relevant section.

Format:
Finding: [description]
Source: [document index or source name]
Quote: "[exact quote from document]"
</instructions>
```

**4. Use Retrieval Augmented Generation (RAG) Pattern**
For very large datasets:
1. Prompt 1: Find relevant sections
2. Prompt 2: Analyze only relevant sections

### Document Structure

**For multiple documents:**
```xml
<document index="1">
<metadata>
  <title>Annual Report 2024</title>
  <source>reports/annual-2024.pdf</source>
  <date>2024-12-01</date>
  <type>financial</type>
</metadata>
<document_content>
[content]
</document_content>
</document>
```

**Benefits:**
- Easy to reference: "See document 3"
- Claude can cite sources accurately
- Metadata helps Claude prioritize

### Verification Strategies

**Ask Claude to:**
- Quote specific passages
- Cite document indices
- Provide page numbers if available
- Reference section headings

**Verify by:**
- Checking quoted text against source
- Confirming document references are correct
- Validating claims against original docs

### Performance Optimization

**Structure matters:**
- Put most relevant docs first
- Use clear section headers
- Break very long documents into logical chunks
- Consider summarization for peripheral content

**Claude 4.x Considerations:**
- Sonnet 4.5 handles long context very well
- Haiku 4.5 works with long context but benefits from clearer structure
- Both models: explicit instructions about thoroughness help
```

**Step 2: Create model-specific-tips.md**

Create: `plugins/prompt-enhancer/skills/prompt-enhancer/model-specific-tips.md`

```markdown
# Claude 4.x Model-Specific Tips

Detailed guidance for optimizing prompts for specific Claude 4.x models.

---

## Universal Claude 4.x Changes

All Claude 4.x models (Sonnet 4.5, Haiku 4.5, Opus 4.5) share these behavioral changes from Claude 3.x:

### 1. Literal Interpretation

**Before (Claude 3.x):**
- Inferred user intent
- Expanded on vague requests
- Added helpful context proactively
- "Above and beyond" behavior by default

**Now (Claude 4.x):**
- Takes you literally
- Does exactly what you ask, nothing more
- Doesn't expand on vague requests
- Requires explicit request for "helpful extras"

**Impact on Prompting:**

❌ **Vague (works with 3.x, fails with 4.x):**
```
Analyze this contract for risks.
```
Claude 3.x: Lists 10+ risks, suggests mitigations, flags unusual clauses
Claude 4.x: Might give brief overview of general risks

✅ **Explicit (works with both):**
```
Analyze this contract and identify:
1. ALL business risks with severity ratings (HIGH/MEDIUM/LOW)
2. ALL legal risks with specific clause references
3. ALL compliance risks with regulatory citations
4. Unusual or non-standard clauses with explanations
5. Recommended mitigations for each risk

Be thorough and comprehensive.
```

### 2. Request "Helpful Extras" Explicitly

**What to add to prompts:**

```xml
<instructions>
[Your main task instructions]

Additionally:
- Flag any potential issues or concerns you notice
- Suggest improvements or alternatives
- Add helpful context or explanations where relevant
- Provide examples to clarify complex points
</instructions>
```

**Common additions:**
- "Suggest improvements or alternatives"
- "Flag any potential issues you notice"
- "Add helpful context or explanations"
- "Provide examples to clarify"
- "Point out edge cases I should consider"

### 3. Examples Must Align Precisely

**Claude 3.x:** Forgave minor inconsistencies in examples
**Claude 4.x:** Pays VERY close attention to every detail

**Implications:**

❌ **Bad example:**
```xml
<example>
<input>User: john@email</input>
<output>Invalid email - missing domain</output>
</example>
```
Problem: If this example has a typo or suboptimal error message, Claude 4.x will replicate it.

✅ **Perfect example:**
```xml
<example>
<input>User: john@email</input>
<output>
{
  "valid": false,
  "error": "Invalid email format: missing top-level domain",
  "suggestion": "Did you mean john@email.com?"
}
</output>
</example>
```

**Best practices:**
- Curate 3-5 pristine examples
- No typos or errors
- Current best practices only
- Exactly aligned with desired behavior
- Show precise format/structure you want

### 4. Specify Output Completeness

**Claude 3.x:** Might proactively include "all relevant" items
**Claude 4.x:** Includes exactly what you ask for

**Example:**

❌ "List the main points"
→ Claude 4.x might list 3-5 main points, skipping minor but important ones

✅ "List ALL points from the document, including minor details. Be comprehensive and thorough."

---

## Sonnet 4.5 Specific Optimization

### Strengths

1. **Forgiving with Ambiguity**
   - Can handle less precise instructions
   - Infers intent better than Haiku
   - More tolerant of unclear requirements

2. **Multi-Step Reasoning**
   - Excellent at complex logical chains
   - Strong synthesis across information
   - Handles nuanced analysis well

3. **Open-Ended Tasks**
   - Great for exploration
   - Creative problem-solving
   - Adaptive to unexpected situations

4. **Context and Nuance**
   - Understands subtle distinctions
   - Good at balancing multiple factors
   - Handles gray areas well

### Best Use Cases

- Research and analysis
- Complex customer support
- Agentic planning and decision-making
- Coding with explanations
- Tasks requiring judgment calls
- Multi-step workflows
- Synthesis across documents
- Strategic thinking

### Optimization Tips

**1. Can Handle Longer Instructions**
```xml
<instructions>
Analyze this codebase and provide:
1. Architecture overview with component relationships
2. Code quality assessment across multiple dimensions
3. Security audit with severity ratings
4. Performance optimization opportunities
5. Maintainability recommendations
6. Testing coverage gaps
7. Documentation quality review

For each section, provide:
- Current state assessment
- Specific examples from code
- Priority ranking
- Recommended improvements
- Estimated effort

Use <thinking> tags to work through your analysis systematically.
</instructions>
```

**2. Works Well with High-Level Goals**

✅ **Good for Sonnet:**
```
Optimize this algorithm for better performance. Consider time complexity, space complexity, and real-world usage patterns. Suggest the best approach.
```

vs.

❌ **Too prescriptive (unnecessary for Sonnet):**
```
Step 1: Calculate current time complexity
Step 2: Identify bottlenecks
Step 3: Research alternative algorithms
Step 4: Compare approaches
Step 5: Select best option
Step 6: Implement optimization
```

**3. Benefits from Context/Motivation**

✅ **With context (better results):**
```xml
<context>
This analysis will inform a board decision about whether to proceed with the acquisition. Thoroughness and accuracy are critical. The board needs to understand both opportunities and risks.
</context>

<instructions>
Analyze this financial data...
</instructions>
```

**4. Good at Inferring Edge Cases**

Still specify edge cases, but Sonnet is better at handling unexpected scenarios:

```xml
<instructions>
Process these user inputs and extract structured data.

Handle edge cases appropriately (malformed data, missing fields, etc.).
</instructions>
```

### When to Choose Sonnet 4.5

- Task requires deep reasoning
- Instructions are somewhat ambiguous
- Need adaptive behavior
- Multiple valid approaches exist
- Synthesis across information needed
- Quality matters more than speed
- Complex multi-turn interactions

---

## Haiku 4.5 Specific Optimization

### Strengths

1. **Low Latency**
   - Near-instant responses
   - Feels real-time in UI
   - Great for interactive experiences

2. **Cost Efficiency**
   - Lower cost per token
   - Good for high-volume use cases

3. **High Concurrency**
   - Handles many parallel requests
   - Scales well

4. **Competent Instruction Following**
   - Follows clear instructions well
   - Pragmatic approach
   - Gets the job done

### Characteristics

1. **Needs Tighter Constraints**
   - Less forgiving than Sonnet
   - Requires more precision
   - Benefits from explicit guidance

2. **Pragmatic > Perfectionist**
   - Focuses on completing task
   - Less likely to add extras
   - Efficient, direct approach

3. **Best for Well-Structured Problems**
   - Excels when requirements are clear
   - Struggles more with ambiguity
   - Prefers defined structure

### Best Use Cases

- Classification tasks
- Lightweight RAG (retrieval augmented generation)
- Structured data extraction
- Content transformation
- UI-side assistants (need instant feel)
- High-volume processing
- Simple Q&A
- Format conversions
- Validation checks

### Optimization Tips

**1. Use Schema-Constrained Outputs**

✅ **With JSON schema:**
```xml
<instructions>
Extract user data as JSON matching this exact schema:

{
  "name": "string (required, 1-100 chars)",
  "email": "string (required, must match ^[^@]+@[^@]+\\.[^@]+$)",
  "age": "integer (optional, 0-150)",
  "phone": "string (optional, format: +1-XXX-XXX-XXXX)"
}

Rules:
- If required field missing: set to null
- If email invalid: set to null
- If age out of range: set to null
- Return ONLY the JSON, no other text
</instructions>
```

**2. Defensive Prompting**

✅ **Explicit edge case handling:**
```xml
<instructions>
Classify customer feedback into: positive, negative, neutral, unclear

Rules:
- If message is empty: return "unclear"
- If message contains both positive and negative: return "neutral"
- If language is ambiguous: return "unclear"
- If message is off-topic: return "unclear"
- If you're uncertain: return "unclear"
</instructions>
```

**3. Tighter Templates**

✅ **Less room for interpretation:**
```xml
<output_format>
Return EXACTLY this format, no additional text:

Category: [positive|negative|neutral|unclear]
Confidence: [high|medium|low]
Keywords: [comma-separated list]
</output_format>
```

❌ **Too loose for Haiku:**
```xml
<output_format>
Provide the category and your confidence level
</output_format>
```

**4. Shorter, More Focused Instructions**

✅ **Good for Haiku:**
```xml
<instructions>
Extract: name, email, phone
Format: JSON
Rules: null if missing
</instructions>
```

vs.

❌ **Too verbose for Haiku (use Sonnet instead):**
```xml
<instructions>
Please carefully review the provided text and extract any personal information you find, including but not limited to the person's full name, their email address, and their phone number. When extracting this information, please ensure accuracy and format the results as a well-structured JSON object. In cases where certain fields are not present in the input text, use null values to indicate their absence. Additionally, consider edge cases such as multiple email addresses or international phone number formats...
</instructions>
```

**5. Validation Rules Spelled Out**

✅ **Explicit validation:**
```xml
<instructions>
Extract email addresses.

Validation:
- Must contain exactly one @ symbol
- Must have text before and after @
- Must have . after @
- Must have at least 2 chars after final .
- Invalid emails: set to null
</instructions>
```

**6. Use Prefilling for Format Control**

Very effective with Haiku to enforce output format:

```
User: Extract data as JSON
Assistant: {
```

Haiku will continue with JSON, no preamble, tight format.

### When to Choose Haiku 4.5

- Speed is critical
- Cost efficiency needed
- High request volume
- Clear, well-defined task
- Structured input/output
- Classification or extraction
- Simple transformations
- UI interactions (need instant feel)
- Task has single correct approach

### When NOT to Choose Haiku 4.5

- Complex reasoning required
- Ambiguous requirements
- Need synthesis across information
- Open-ended exploration
- Multiple valid approaches
- Nuanced judgment needed
- Task requires "above and beyond" thinking

---

## Sonnet vs Haiku: Decision Matrix

| Factor | Choose Sonnet 4.5 | Choose Haiku 4.5 |
|--------|------------------|------------------|
| **Task Complexity** | Complex, multi-step | Simple, well-defined |
| **Instructions** | Can be somewhat ambiguous | Must be very clear |
| **Reasoning Depth** | Deep analysis needed | Surface-level sufficient |
| **Speed Priority** | Quality > Speed | Speed > Quality |
| **Cost Sensitivity** | Budget flexible | Cost optimization critical |
| **Volume** | Lower volume | High volume |
| **Output Format** | Flexible | Structured/constrained |
| **Edge Cases** | Many unknowns | Well-defined |
| **Interaction Type** | Multi-turn, adaptive | Single-turn, focused |

---

## Migration Guide: Claude 3.x → Claude 4.x

### Common Changes Needed

**1. Add Explicit Success Criteria**

Before (3.x):
```
Analyze this contract
```

After (4.x):
```
Analyze this contract and identify:
1. ALL risks with severity ratings
2. ALL obligations with deadlines
3. ALL unusual clauses with explanations
4. Recommended actions
```

**2. Request Helpful Behaviors**

Before (3.x):
```
Review this code
```
(Claude 3.x would proactively suggest improvements)

After (4.x):
```
Review this code. Flag any issues, suggest improvements, and point out potential edge cases.
```

**3. Tighten Examples**

Before (3.x):
- Examples could be approximate
- Minor inconsistencies forgiven

After (4.x):
- Examples must be pristine
- Zero tolerance for errors
- Exactly aligned with desired output

**4. Specify Output Completeness**

Before (3.x):
```
List the main points
```

After (4.x):
```
List ALL points from the document, including minor details. Be comprehensive.
```

**5. Add Context/Motivation (Optional but Helpful)**

New in 4.x:
```xml
<context>
This analysis will inform a critical business decision. Thoroughness is essential.
</context>
```

### Model Selection Migration

**If using Claude 3 Opus:**
→ Migrate to Claude Sonnet 4.5 (similar capability, better performance)

**If using Claude 3 Sonnet:**
→ Try Claude Sonnet 4.5 first
→ Consider Haiku 4.5 for simple, high-volume tasks

**If using Claude 3 Haiku:**
→ Haiku 4.5 is excellent upgrade
→ May need to tighten prompts slightly

---

## Opus 4.5 Specific (When Released)

**Placeholder section for when Opus 4.5 is released.**

Expected characteristics:
- Highest reasoning capability
- Best for most complex tasks
- Premium pricing
- When you need absolute best quality

Will update this section when Opus 4.5 launches.
```

**Step 3: Commit progressive disclosure files**

```bash
git add plugins/prompt-enhancer/skills/prompt-enhancer/technique-loader.md \
        plugins/prompt-enhancer/skills/prompt-enhancer/model-specific-tips.md
git commit -m "feat(prompt-enhancer): add progressive disclosure support files"
```

---

## Task 4: Interactive Build Prompt Command

**Files:**
- Create: `plugins/prompt-enhancer/commands/build-prompt.md`

**Step 1: Create build-prompt command file**

Create: `plugins/prompt-enhancer/commands/build-prompt.md`

```markdown
---
description: Interactive wizard to build optimized prompts step-by-step using Anthropic best practices
---

# Build Prompt Wizard

Welcome! This wizard will guide you through building an optimized prompt using Anthropic's best practices.

## Phase 1: Task Discovery

**Ask the user:**

"What do you want Claude to do? Please describe your task."

**After receiving answer:**

1. Auto-detect task type based on description:
   - Data analysis keywords: analyze, calculate, metrics, report, statistics, trends
   - Legal keywords: contract, review, terms, compliance, risk, legal
   - Creative keywords: write, create, story, blog, content, compose
   - Code keywords: code, function, implement, debug, refactor, optimize
   - Customer feedback keywords: feedback, sentiment, classify, categorize
   - QA keywords: question, answer, explain, summarize
   - Summarization keywords: summarize, brief, overview, key points

2. Load relevant template from `task-type-templates.md` if match found

3. Confirm with user:
   "I've detected this as a **[task-type]** task. Is that correct?"

## Phase 2: Role Assignment

**Show user:**

"For [task-type] tasks, I recommend this role:

**[Suggested role based on task type]**

Would you like to:
A. Use this role (recommended)
B. Customize the role
C. Skip role assignment (not recommended)"

**Suggested roles by task type:**
- Data analysis: "Senior data analyst specializing in [domain]"
- Legal: "Legal expert specializing in contract review"
- Creative: "Professional content writer with expertise in [domain]"
- Code: "Senior software engineer specializing in [language/domain]"
- Customer feedback: "Customer experience analyst"
- QA: "Subject matter expert in [domain]"
- Summarization: "Research analyst specializing in synthesis"

**If B (customize):**
Ask: "What role and expertise should Claude have?"

## Phase 3: Context Gathering

**Ask the user:**

"What context does Claude need to know? This could include:
- Background information
- Constraints or requirements
- Success criteria
- Relevant details

(Optional - press enter to skip)"

**If provided:**
Store context for `<context>` section.

## Phase 4: Data Separation

**Ask the user:**

"Will this prompt process user data or variables (like {{USER_INPUT}}, {{CUSTOMER_FEEDBACK}}, etc.)?

A. Yes - will process user data
B. No - instructions only"

**If A:**

Show pattern:
```xml
<data>
{{YOUR_VARIABLE_NAME}}
</data>
```

Ask: "What should we call your data variable? (e.g., USER_INPUT, FEEDBACK, SALES_DATA)"

Store for `<data>` section.

## Phase 5: Output Format

**Ask the user:**

"What should the output look like?

A. Structured data (JSON, XML)
B. Markdown report
C. Plain text
D. Custom format (I'll describe it)"

**If A:**
Ask: "JSON or XML?"
Then: "What fields should be included?"

Generate schema.

**If B:**
Ask: "What sections should the report include?"

Generate markdown template.

**If C:**
Ask: "Describe the plain text format you want."

**If D:**
Ask: "Describe the custom format."

Generate `<output_format>` template based on choice.

## Phase 6: Advanced Techniques

**Show user:**

"Based on your [task-type] task, I recommend these optional techniques:

**Recommended for your task:**
[List recommended techniques with checkboxes]

**Other available techniques:**
[List other techniques with checkboxes]

Please select any you'd like to include (multi-select):

□ Chain of Thought - Add step-by-step reasoning (recommended for: analysis, complex tasks)
□ Prefilling - Force specific output format (recommended for: JSON/XML output)
□ Extended Thinking - Deep reasoning for complex problems (recommended for: multi-step reasoning)
□ Few-Shot Examples - Show 3-5 examples (recommended for: formatting, NOT creative writing)
□ Constraints/Edge Cases - Handle edge cases explicitly (recommended for: production use)
"

**Recommendations by task type:**
- Data analysis: CoT ✓, Examples ✓
- Legal: CoT ✓, Examples ✓
- Creative: Constraints ✓, (skip Examples)
- Code: Examples ✓, Edge cases ✓
- Customer feedback: Examples ✓
- QA: CoT (if complex)
- Summarization: Constraints ✓

**If Chain of Thought selected:**
Add `<thinking>` and `<answer>` tags to output format.

**If Prefilling selected:**
Ask: "What should the prefill text be? (e.g., '{' for JSON, '<response>' for XML)"

**If Extended Thinking selected:**
Ask: "Token budget for thinking? (Start with 2048, increase if needed)"
Load details from `new-techniques.md`

**If Examples selected:**
Load `before-after-gallery.md` for inspiration
Ask: "How many examples would you like to include? (Recommended: 3-5)"
For each example, ask for input and expected output.

## Phase 7: Model Selection

**Ask the user:**

"Which Claude model will use this prompt?

A. Sonnet 4.5 (recommended - balanced performance)
B. Haiku 4.5 (fast, cost-efficient, needs tighter constraints)
C. Opus 4.5 (when available - highest capability)
D. Not sure / other"

**If A (Sonnet 4.5):**
- Note: Can handle more complex instructions
- Add context/motivation if helpful
- More forgiving with ambiguity

**If B (Haiku 4.5):**
- Tighten constraints
- Add explicit validation rules
- Use schema-constrained outputs
- Shorter, more focused instructions
- Consider adding prefilling for format control

Load model-specific tips from `claude-4x-tips.md`

Apply model-specific optimizations.

## Phase 8: Review & Export

**Generate complete prompt:**

```xml
<role>
[Generated role]
</role>

<instructions>
[Task description with explicit details]

[If helpful extras requested:]
Additionally:
- Flag any potential issues or concerns you notice
- Suggest improvements or alternatives where relevant
</instructions>

[If context provided:]
<context>
[Context content]
</context>

[If data variable specified:]
<data>
{{VARIABLE_NAME}}
</data>

[If CoT selected:]
<output_format>
Provide your response in this format:

<thinking>
[Your step-by-step reasoning]
</thinking>

<answer>
[Structured output as specified]
</answer>
</output_format>

[Else:]
<output_format>
[Generated format template]
</output_format>

[If examples selected:]
<examples>
[Generated examples]
</examples>

[If constraints/edge cases selected:]
<constraints>
[Generated constraints]
</constraints>
```

**Show user the complete prompt with explanations:**

"Here's your optimized prompt:

---
[Complete prompt]
---

**What I included and why:**

✅ XML tags - Separates components for clarity (Anthropic's #1 recommendation)
✅ Specific role - Primes Claude with expertise: [role description]
✅ Clear output format - Template shows exact structure expected
✅ Data separation - Security boundary between instructions and user data
[If CoT:] ✅ Chain of thought - Adds reasoning for better analysis
[If Examples:] 💡 Few-shot examples - Shows exact format expected
[If Prefilling:] 🎯 Prefilling - Forces format: [prefill text]
[If Extended thinking:] 🎯 Extended thinking - Deep reasoning with [N] token budget
[If Constraints:] ✅ Edge cases - Handles [specific scenarios]

**Claude 4.x optimizations applied:**
- Explicit instructions (literal interpretation)
[If Sonnet:] - Optimized for Sonnet 4.5: Balanced complexity
[If Haiku:] - Optimized for Haiku 4.5: Tight constraints, clear validation
[If helpful extras:] - Requests 'helpful extras' explicitly

**Next steps:**

1. Copy this prompt
2. Test with sample data
3. Iterate based on results

Would you like me to:
A. Save this to a file
B. Copy to clipboard
C. Modify something
D. Done"

**If A (save):**
Ask: "Filename? (e.g., my-prompt.md)"
Save to file.

**If C (modify):**
Ask: "What would you like to change?"
Return to relevant phase.

---

## Helper Functions

**Load template function:**
When loading task-type template, load from `assets/examples/task-type-templates.md` and adapt based on user's specific task.

**Load examples function:**
When user requests examples, load relevant examples from `assets/examples/before-after-gallery.md` for inspiration.

**Generate format function:**
Based on user's output format choice, generate appropriate template with proper XML structure.

**Apply model optimizations function:**
Load from `assets/reference/claude-4x-tips.md` and apply model-specific tweaks:
- Sonnet 4.5: Add context/motivation, can be more verbose
- Haiku 4.5: Tighten constraints, add validation, shorter instructions

---

## Progressive Disclosure

Load these files only when needed:
- `assets/examples/task-type-templates.md` - Phase 1 (task detection)
- `assets/examples/before-after-gallery.md` - Phase 6 (if examples selected)
- `assets/reference/new-techniques.md` - Phase 6 (if prefilling/extended thinking selected)
- `assets/reference/claude-4x-tips.md` - Phase 7 (model selection)
- `assets/reference/quick-reference.md` - Any phase (if user asks for help)
```

**Step 2: Commit build-prompt command**

```bash
git add plugins/prompt-enhancer/commands/build-prompt.md
git commit -m "feat(prompt-enhancer): add interactive build-prompt wizard command"
```

---

## Task 5: Reference Assets - Quick Reference

**Files:**
- Create: `plugins/prompt-enhancer/assets/reference/quick-reference.md`

**Step 1: Create quick reference cheat sheet**

Create: `plugins/prompt-enhancer/assets/reference/quick-reference.md`

```markdown
# Prompt Engineering Quick Reference

One-page cheat sheet for Anthropic's best practices.

---

## ✅ Mandatory Techniques (EVERY prompt)

Apply to ALL prompts, no exceptions:

- [ ] **XML tags** - At minimum: `<instructions>`, `<data>`, `<output_format>`
- [ ] **Specific role** - Domain expert, not "helpful assistant"
- [ ] **Clear output format** - Template or explicit structure
- [ ] **Data separation** - User data in `<data>` tags, not mixed with instructions

**Total overhead:** ~10 lines | **Impact:** Dramatically better results

---

## 💡 Contextual Techniques (based on task)

| Technique | When to Use | When to Skip |
|-----------|------------|--------------|
| **Chain of thought** | Analysis, reasoning, multi-step problems, debugging, legal review | Simple transformations, basic Q&A, straightforward tasks |
| **Few-shot examples** | Formatting, structure, categorization, technical domains | Creative writing, simple queries, when flexibility needed |
| **Prefilling** | Format enforcement (JSON/XML), skip preambles, role consistency | When using extended thinking, simple queries |
| **Extended thinking** | Complex reasoning, debugging, multi-step math, algorithm optimization | Simple queries, when speed matters, well-structured problems |
| **Constraints/edge cases** | Production systems, reusable templates, variable data | One-off personal use with controlled inputs |

---

## 🏷️ Top 10 XML Tags

| Tag | Purpose | Example |
|-----|---------|---------|
| `<instructions>` | What Claude should do | Main task description |
| `<data>` | User input (security boundary) | `{{USER_INPUT}}` |
| `<output_format>` | Expected structure | Template or format spec |
| `<role>` | Expert assignment | Senior analyst in [domain] |
| `<thinking>` | Chain of thought reasoning | Step-by-step analysis |
| `<answer>` | Final conclusion | After `<thinking>` |
| `<examples>` | Few-shot examples container | Multiple `<example>` tags |
| `<context>` | Background information | Relevant details |
| `<constraints>` | Rules and limitations | Edge case handling |
| `<document>` | Individual document wrapper | Multi-document analysis |

---

## 🎯 Task Type → Techniques Mapping

| Task Type | Mandatory | Recommended | Skip |
|-----------|-----------|-------------|------|
| **Data Analysis** | XML, Role, Output format | CoT, Examples | - |
| **Legal Review** | XML, Role, Output format, CoT | Examples | - |
| **Creative Writing** | XML, Role, Tone spec | Constraints | Examples |
| **Code Generation** | XML, Output format | Examples, Edge cases | - |
| **Classification** | XML, Role, Output format | Examples | CoT (unless complex) |
| **Summarization** | XML, Role, Length spec | - | Examples |
| **Customer Feedback** | XML, Role, Categories | Examples | - |

---

## 🎨 Claude 4.x Optimizations

### Universal Changes

**1. Literal Interpretation**
- Claude 4.x does exactly what you ask, nothing more
- Be MORE explicit in all instructions
- No inference or expansion on vague requests

**2. Request "Helpful Extras"**
Add to instructions:
- "Flag any potential issues you notice"
- "Suggest improvements or alternatives"
- "Add helpful context or explanations"

**3. Examples Must Be Perfect**
- Claude 4.x pays VERY close attention
- Zero tolerance for errors in examples
- Examples must align precisely with desired output

### Model Selection

| Feature | Sonnet 4.5 | Haiku 4.5 |
|---------|-----------|-----------|
| **Complexity** | Complex, multi-step | Simple, well-defined |
| **Ambiguity** | More forgiving | Needs precision |
| **Instructions** | Can be longer | Shorter, focused |
| **Speed** | Balanced | Fast |
| **Cost** | Standard | Efficient |
| **Best for** | Analysis, synthesis | Classification, extraction |

**Haiku 4.5 needs:**
- Tighter constraints
- Schema-constrained outputs
- Explicit validation rules
- Defensive prompting

**Sonnet 4.5 benefits from:**
- Context/motivation
- High-level goals
- Adaptive behavior

---

## ⚠️ Common Mistakes

| Mistake | Fix |
|---------|-----|
| No XML tags | Always use XML tags (Anthropic's #1 recommendation) |
| Generic role | "Senior analyst in [domain]" not "helpful assistant" |
| Vague output | Show exact template/structure |
| Data mixed with instructions | Use `<data>` tags for security |
| Mentioned examples, didn't add | Write 2-5 actual examples |
| Examples for creative writing | Skip examples, they limit creativity |
| Skipped CoT for complex task | Add `<thinking>` tags |
| Assumed Claude 4.x infers | Be explicit, literal interpretation |
| "Task is simple enough" | Mandatory techniques apply to ALL prompts |

---

## 📏 Quick Template

```xml
<role>
You are a [specific expert] with expertise in [domain].
</role>

<instructions>
[Explicit task description]

[For Claude 4.x, optionally add:]
Additionally: Flag issues, suggest improvements, add helpful context.
</instructions>

<context>
[Background info]
</context>

<data>
{{USER_INPUT}}
</data>

<output_format>
[Exact template or structure]

[If CoT needed:]
<thinking>
[Step-by-step reasoning]
</thinking>

<answer>
[Final response]
</answer>
</output_format>

<examples>
<example>
<input>[Example input]</input>
<output>[Example output]</output>
</example>
</examples>

<constraints>
- [Edge case handling]
- [Validation rules]
</constraints>
```

---

## 🔄 Before → After Quick Example

**❌ Before:**
```
Analyze this data and make a report.

Data: {{SALES_DATA}}
```

**✅ After:**
```xml
<role>
You are a senior e-commerce analyst specializing in sales trends.
</role>

<instructions>
Analyze the sales data and create a structured report with revenue, top products, and trends.
Flag any unusual patterns.
</instructions>

<data>
{{SALES_DATA}}
</data>

<output_format>
<executive_summary>
[2-3 sentences]
</executive_summary>

<key_metrics>
- Total Revenue: $X.XX
- Top 5 Products: [list with %]
- Growth: X% MoM
</key_metrics>
</output_format>
```

---

## 🚀 Quick Checklist

After writing a prompt, verify:

1. [ ] Has XML tags (`<instructions>`, `<data>`, `<output_format>`)
2. [ ] Specific role assigned (not "helpful assistant")
3. [ ] Data separated from instructions
4. [ ] Output format is explicit (template shown)
5. [ ] Examples included if needed (not for creative writing)
6. [ ] Chain of thought for complex reasoning
7. [ ] Clear, explicit language (Claude 4.x literal interpretation)
8. [ ] Edge cases addressed
9. [ ] Model-specific optimizations (Sonnet vs Haiku)

If any checkbox unchecked → Fix it!

---

## 📚 Full Reference

For detailed guides, load:
- `technique-loader.md` - Deep dives on each technique
- `model-specific-tips.md` - Claude 4.x model comparison
- `before-after-gallery.md` - 8-10 real examples
- `task-type-templates.md` - Ready-to-use templates
- `new-techniques.md` - Prefilling, extended thinking
- `claude-4x-tips.md` - Complete model guide
```

**Step 2: Commit quick reference**

```bash
git add plugins/prompt-enhancer/assets/reference/quick-reference.md
git commit -m "feat(prompt-enhancer): add quick reference cheat sheet"
```

---

## Task 6: Reference Assets - XML Tag Library

**Files:**
- Create: `plugins/prompt-enhancer/assets/reference/xml-tag-library.md`

**Step 1: Create comprehensive XML tag catalog**

Create file with frontmatter and structure, then add comprehensive tag listings.

**Step 2: Commit XML tag library**

```bash
git add plugins/prompt-enhancer/assets/reference/xml-tag-library.md
git commit -m "feat(prompt-enhancer): add comprehensive XML tag library"
```

---

## Task 7: Reference Assets - New Techniques Guide

**Files:**
- Create: `plugins/prompt-enhancer/assets/reference/new-techniques.md`

**Step 1: Create new techniques reference**

Create detailed guide covering prefilling, extended thinking, prompt chaining, and long context tips with examples and API usage.

**Step 2: Commit new techniques guide**

```bash
git add plugins/prompt-enhancer/assets/reference/new-techniques.md
git commit -m "feat(prompt-enhancer): add 2025 techniques reference (prefilling, extended thinking)"
```

---

## Task 8: Reference Assets - Claude 4.x Tips

**Files:**
- Create: `plugins/prompt-enhancer/assets/reference/claude-4x-tips.md`

**Step 1: Create Claude 4.x optimization guide**

Create comprehensive model-specific guide with Sonnet 4.5 vs Haiku 4.5 comparison and migration guidance.

**Step 2: Commit Claude 4.x tips**

```bash
git add plugins/prompt-enhancer/assets/reference/claude-4x-tips.md
git commit -m "feat(prompt-enhancer): add Claude 4.x model-specific optimization guide"
```

---

## Task 9: Example Assets - Before/After Gallery

**Files:**
- Create: `plugins/prompt-enhancer/assets/examples/before-after-gallery.md`

**Step 1: Create before/after examples**

Create 8-10 real-world prompt improvement examples across different task types.

**Step 2: Commit before/after gallery**

```bash
git add plugins/prompt-enhancer/assets/examples/before-after-gallery.md
git commit -m "feat(prompt-enhancer): add before/after gallery with 10 examples"
```

---

## Task 10: Example Assets - Task Type Templates

**Files:**
- Create: `plugins/prompt-enhancer/assets/examples/task-type-templates.md`

**Step 1: Create task-specific templates**

Create 7 ready-to-use templates for common task types.

**Step 2: Commit task templates**

```bash
git add plugins/prompt-enhancer/assets/examples/task-type-templates.md
git commit -m "feat(prompt-enhancer): add 7 task-type templates"
```

---

## Task 11: Example Assets - Common Patterns

**Files:**
- Create: `plugins/prompt-enhancer/assets/examples/common-patterns.md`

**Step 1: Create common patterns reference**

Create 8 frequently-used prompt patterns.

**Step 2: Commit common patterns**

```bash
git add plugins/prompt-enhancer/assets/examples/common-patterns.md
git commit -m "feat(prompt-enhancer): add 8 common prompt patterns"
```

---

## Task 12: Usage Examples

**Files:**
- Create: `plugins/prompt-enhancer/examples/usage-examples.md`

**Step 1: Create usage examples**

Create practical examples showing how to use the plugin.

**Step 2: Commit usage examples**

```bash
git add plugins/prompt-enhancer/examples/usage-examples.md
git commit -m "docs(prompt-enhancer): add usage examples"
```

---

## Task 13: Final Integration Testing

**Step 1: Test skill loading**

```bash
# From plugins/prompt-enhancer directory
cat skills/prompt-enhancer/SKILL.md | head -20
```

Expected: Should show YAML frontmatter and skill content

**Step 2: Test plugin manifest**

```bash
cat .claude-plugin/plugin.json
```

Expected: Valid JSON with correct metadata

**Step 3: Verify directory structure**

```bash
find . -type f -name "*.md" | sort
```

Expected: Should list all created markdown files

**Step 4: Test file references**

Verify all references between files are correct (no broken links to assets)

**Step 5: Final commit**

```bash
git add -A
git commit -m "feat(prompt-enhancer): complete v1.0.0 plugin implementation"
```

---

## Task 14: Update Marketplace README

**Files:**
- Modify: `README.md` (repository root)

**Step 1: Read current README**

```bash
cat README.md
```

**Step 2: Add prompt-enhancer to plugins list**

Update the plugins section to include prompt-enhancer.

**Step 3: Commit README update**

```bash
git add README.md
git commit -m "docs: add prompt-enhancer plugin to marketplace README"
```

---

## Implementation Complete!

After completing all tasks, the prompt-enhancer plugin will be:
- ✅ Fully structured with proper manifest
- ✅ Main `/prompt-enhancer` skill with Claude 4.x support
- ✅ Interactive `/build-prompt` wizard
- ✅ Comprehensive reference library
- ✅ Before/after examples (10 examples)
- ✅ Task-type templates (7 templates)
- ✅ Common patterns (8 patterns)
- ✅ Progressive disclosure for efficiency
- ✅ Complete documentation

Total files created: ~20 files across skills, commands, assets, examples, and docs.
