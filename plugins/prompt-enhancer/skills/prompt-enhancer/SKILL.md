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
