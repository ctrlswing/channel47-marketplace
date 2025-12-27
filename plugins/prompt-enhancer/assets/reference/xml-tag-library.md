# XML Tag Library: Comprehensive Guide

## Overview

XML tags are Claude's primary method for structured prompting. They provide clear boundaries, improve parsing accuracy, and enable complex prompt architectures.

**When to use XML tags:**
- Multi-part prompts with distinct sections
- Long documents or data sets
- Complex instructions with multiple steps
- When you need clear separation of concerns
- Templates and reusable prompt patterns

## Core Structural Tags

### `<instructions>`
**Purpose:** Define clear, actionable steps for Claude to follow

**When to use:** Multi-step tasks, complex workflows, procedures

**Best practices:**
- Number your steps clearly
- Make each step actionable and specific
- Order steps logically
- Include decision points if needed

**Example:**
```xml
<instructions>
1. Read the entire document carefully
2. Identify the main argument in each section
3. Extract key supporting evidence
4. Summarize findings in bullet points
5. Rate the overall argument strength (1-10)
</instructions>
```

### `<context>`
**Purpose:** Provide background information Claude needs to understand the task

**When to use:** When domain knowledge, history, or situational awareness is required

**Best practices:**
- Include only relevant context
- Structure chronologically or by importance
- Distinguish facts from opinions
- Reference specific details Claude should consider

**Example:**
```xml
<context>
You are analyzing customer feedback for a SaaS product launched 3 months ago.
The product targets small businesses (10-50 employees).
We recently released v2.0 with a redesigned UI.
Previous feedback indicated the old UI was confusing for new users.
</context>
```

### `<examples>`
**Purpose:** Show Claude exactly what you want through concrete demonstrations

**When to use:** Novel formats, specific styles, pattern matching, edge cases

**Best practices:**
- Provide 2-5 diverse examples
- Include edge cases if relevant
- Show both input and expected output
- Use `<example>` tags for each instance
- Vary examples to cover the pattern space

**Example:**
```xml
<examples>
<example>
Input: "The quick brown fox jumps over the lazy dog"
Output: {"words": 9, "chars": 43, "longest": "quick/brown/jumps"}
</example>

<example>
Input: "AI"
Output: {"words": 1, "chars": 2, "longest": "AI"}
</example>

<example>
Input: ""
Output: {"words": 0, "chars": 0, "longest": null}
</example>
</examples>
```

## Content Organization Tags

### `<document>` / `<documents>`
**Purpose:** Clearly delineate text to be analyzed or processed

**When to use:** Document analysis, content extraction, text processing

**Best practices:**
- Use for any text that's data (not instructions)
- Can nest multiple `<document>` tags in `<documents>`
- Include metadata as attributes when helpful
- Keep instructions separate from document content

**Example:**
```xml
<documents>
<document id="email1" date="2025-01-15">
Subject: Project Update
Hi team, the Q1 launch is on track...
</document>

<document id="email2" date="2025-01-16">
Subject: Re: Project Update
Thanks for the update. One concern...
</document>
</documents>

Summarize the main concerns raised in these emails.
```

### `<data>` / `<dataset>`
**Purpose:** Provide structured data for processing or analysis

**When to use:** JSON, CSV, tables, logs, metrics, or any structured data

**Best practices:**
- Clearly label data format (JSON, CSV, etc.)
- Use for data Claude should process, not instructions
- Can include metadata about data source/type
- Separate multiple datasets with nested tags

**Example:**
```xml
<dataset format="json" source="analytics">
{
  "users": 15234,
  "active_users": 8901,
  "churn_rate": 0.12,
  "avg_session": "8m 34s"
}
</dataset>

Calculate the engagement rate and identify trends.
```

### `<code>`
**Purpose:** Wrap source code for review, analysis, or modification

**When to use:** Code review, debugging, refactoring, documentation

**Best practices:**
- Specify language in attributes
- Include file context when relevant
- Separate code from explanatory text
- Use for both snippets and full files

**Example:**
```xml
<code language="python" file="auth.py">
def authenticate_user(username, password):
    user = db.get_user(username)
    if user and check_password(password, user.hash):
        return create_session(user)
    return None
</code>

Review this authentication function for security vulnerabilities.
```

## Reasoning and Analysis Tags

### `<thinking>`
**Purpose:** Request or demonstrate step-by-step reasoning

**When to use:** Complex problems, multi-step analysis, debugging, decision-making

**Best practices:**
- Place early in prompt to encourage upfront reasoning
- Can be used to show Claude's reasoning process
- Combine with chain-of-thought instructions
- Helps with accuracy on complex tasks

**Example:**
```xml
Before providing your final answer, use this format:

<thinking>
1. What is the core problem?
2. What information do I have?
3. What approach should I use?
4. Step-by-step solution...
</thinking>

<answer>
[Your final answer here]
</answer>
```

### `<analysis>`
**Purpose:** Structure analytical thinking and findings

**When to use:** Reports, evaluations, critiques, assessments

**Best practices:**
- Break analysis into logical sections
- Support claims with evidence
- Distinguish observation from interpretation
- Can nest sub-sections

**Example:**
```xml
<analysis>
<strengths>
- Clear value proposition
- Strong technical implementation
- Responsive customer support
</strengths>

<weaknesses>
- Limited market differentiation
- High customer acquisition cost
- Dependency on single channel
</weaknesses>

<recommendations>
1. Develop unique features
2. Diversify marketing channels
3. Implement referral program
</recommendations>
</analysis>
```

## Output Control Tags

### `<output_format>`
**Purpose:** Define exact structure, style, and format of response

**When to use:** Structured data, consistent formatting, API responses, templates

**Best practices:**
- Show exact format with placeholder examples
- Specify data types and constraints
- Include all required fields
- Note optional vs required elements

**Example:**
```xml
<output_format>
Provide your response as a JSON object with this exact structure:

{
  "summary": "string (max 200 chars)",
  "sentiment": "positive|negative|neutral",
  "confidence": number (0-100),
  "key_points": ["string", "string"],
  "action_required": boolean
}
</output_format>
```

### `<constraints>`
**Purpose:** Define boundaries, limitations, and rules

**When to use:** When you need to prevent certain behaviors or enforce specific requirements

**Best practices:**
- Be explicit about what NOT to do
- Include limits (length, time, scope)
- Specify required vs optional elements
- Define edge case handling

**Example:**
```xml
<constraints>
- Response must be under 300 words
- Use only information from provided documents
- Do not make assumptions about user intent
- If uncertain, explicitly state your confidence level
- Avoid technical jargon; write for a general audience
- Do not include recommendations unless specifically asked
</constraints>
```

### `<format>`
**Purpose:** Specify presentation style and structure (simpler than output_format)

**When to use:** Basic formatting needs without complex structure

**Example:**
```xml
<format>
- Use bullet points for lists
- Bold key terms
- Include a summary at the end
- Write in active voice
</format>
```

## Specialized Tags

### `<role>`
**Purpose:** Define Claude's persona, expertise, and perspective

**When to use:** When domain expertise or specific perspective matters

**Best practices:**
- Be specific about expertise level
- Include relevant background
- Define communication style if needed
- Align role with task requirements

**Example:**
```xml
<role>
You are a senior DevOps engineer with 10 years of experience in cloud infrastructure.
You specialize in AWS, Kubernetes, and CI/CD pipelines.
You communicate clearly with both technical and non-technical stakeholders.
You prioritize security, reliability, and cost-effectiveness.
</role>
```

### `<background>`
**Purpose:** Provide historical or contextual information

**When to use:** Similar to context but more focused on history/backstory

**Example:**
```xml
<background>
This API was originally built in 2018 using REST principles.
In 2022, we migrated core services to GraphQL.
The hybrid approach has created maintenance challenges.
We're now evaluating a full GraphQL migration.
</background>
```

### `<criteria>`
**Purpose:** Define evaluation standards or success metrics

**When to use:** Reviews, assessments, scoring, decision-making

**Example:**
```xml
<criteria>
Evaluate each proposal against these criteria:
1. Technical feasibility (0-10)
2. Cost effectiveness (0-10)
3. Time to implementation (0-10)
4. Team expertise match (0-10)
5. Long-term maintainability (0-10)

Provide scores and justification for each.
</criteria>
```

### `<metadata>`
**Purpose:** Include supplementary information about content

**When to use:** When additional context about data/documents is relevant

**Example:**
```xml
<document>
<metadata>
author: John Smith
date: 2025-01-15
version: 2.3
status: draft
</metadata>

[Document content here...]
</document>
```

## Advanced Patterns

### Nested Tags for Complex Structure
```xml
<project_analysis>
  <context>
    <business_context>
    [Business background]
    </business_context>

    <technical_context>
    [Technical background]
    </technical_context>
  </context>

  <requirements>
    <functional>
    [Functional requirements]
    </functional>

    <non_functional>
    [Performance, security, etc.]
    </non_functional>
  </requirements>

  <constraints>
    <technical>
    [Technical limitations]
    </technical>

    <business>
    [Budget, timeline, etc.]
    </business>
  </constraints>
</project_analysis>
```

### Multi-Document Processing
```xml
<documents>
  <document id="1" type="email" priority="high">
  [Email content]
  </document>

  <document id="2" type="report" priority="medium">
  [Report content]
  </document>

  <document id="3" type="note" priority="low">
  [Note content]
  </document>
</documents>

<instructions>
1. Process documents in priority order
2. Extract action items from each
3. Identify dependencies between documents
4. Create consolidated task list
</instructions>
```

### Template Pattern
```xml
<template>
Use this structure for each item:

<item>
  <title>[Item title]</title>
  <description>[Brief description]</description>
  <impact>
    <positive>[Positive impacts]</positive>
    <negative>[Negative impacts]</negative>
  </impact>
  <recommendation>[Recommended action]</recommendation>
</item>
</template>

<items_to_process>
[List of items]
</items_to_process>
```

## Tag Naming Best Practices

1. **Use descriptive names**: `<user_feedback>` not `<uf>`
2. **Be consistent**: If you use `<example>`, don't mix with `<sample>`
3. **Use snake_case or lowercase**: `<output_format>` or `<outputformat>`
4. **Match content purpose**: Tag name should describe what's inside
5. **Avoid ambiguity**: `<code>` vs `<code_snippet>` vs `<source_code>` - pick one
6. **Nest logically**: `<examples><example>...</example></examples>`

## Common Anti-Patterns

❌ **Don't over-tag simple prompts**
```xml
<instruction>Write a poem about cats</instruction>
```
Better: "Write a poem about cats"

❌ **Don't use tags as emphasis**
```xml
This is <important>very important</important>!
```
Better: Use clear language or proper structure

❌ **Don't create unnecessary nesting**
```xml
<outer><middle><inner>Content</inner></middle></outer>
```
Better: Use nesting only when it adds clarity

❌ **Don't mix instructions and data without separation**
```xml
<document>
Analyze this document:
[Document text...]
</document>
```
Better: Keep instructions outside tags

## When NOT to Use XML Tags

Simple prompts don't need tags:
- ✅ "Summarize this article in 3 sentences"
- ✅ "What's the capital of France?"
- ✅ "Write a haiku about programming"

Use tags when:
- Multiple distinct sections (examples + instructions + data)
- Long documents or datasets
- Complex multi-step workflows
- Structured output required
- Preventing ambiguity in parsing

## Quick Tag Selection Guide

| Task Type | Recommended Tags |
|-----------|------------------|
| Document analysis | `<document>`, `<instructions>`, `<output_format>` |
| Data processing | `<data>`, `<criteria>`, `<format>` |
| Code review | `<code>`, `<analysis>`, `<recommendations>` |
| Creative writing | `<context>`, `<examples>`, `<constraints>` |
| Problem solving | `<thinking>`, `<context>`, `<instructions>` |
| Comparison tasks | `<examples>`, `<criteria>`, `<analysis>` |
| Multi-doc processing | `<documents>`, `<document>`, `<instructions>` |

## Testing Your Tags

Good test: Can you swap content between tags without confusion?
- If `<context>` and `<instructions>` are interchangeable, rethink your structure
- Each tag should have a clear, distinct purpose
- Tag boundaries should align with logical content boundaries

## Summary

XML tags are tools for clarity, not decoration:
1. Use them to prevent ambiguity
2. Structure complex prompts clearly
3. Separate data from instructions
4. Enable consistent parsing
5. Make prompts maintainable and reusable

Start simple, add tags as complexity grows.
