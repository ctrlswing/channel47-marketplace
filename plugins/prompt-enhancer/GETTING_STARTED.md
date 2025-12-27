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
