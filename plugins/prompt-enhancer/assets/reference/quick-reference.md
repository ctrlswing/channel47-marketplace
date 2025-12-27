# Quick Reference: Anthropic Prompt Engineering

## Core Principles

1. **Be Clear and Direct** - State exactly what you want
2. **Use XML Tags** - Structure complex prompts with `<tags>`
3. **Show Examples** - Demonstrate the pattern you want
4. **Think Step-by-Step** - Break complex tasks into steps
5. **Assign Roles** - Give Claude context about its role
6. **Control Output** - Specify format, length, and style

## Essential XML Tags

```xml
<examples>          <!-- Show Claude what good output looks like -->
<thinking>          <!-- Let Claude reason through problems -->
<context>           <!-- Provide background information -->
<instructions>      <!-- Clear step-by-step guidance -->
<constraints>       <!-- Define boundaries and rules -->
<output_format>     <!-- Specify exact output structure -->
```

## The 5-Minute Prompt Formula

```
[Role]: You are a [specific role] with [expertise]

[Task]: [Clear, specific objective]

[Context]:
<context>
[Relevant background information]
</context>

[Examples]:
<examples>
<example>
Input: [sample]
Output: [desired result]
</example>
</examples>

[Instructions]:
1. [First step]
2. [Second step]
3. [Third step]

[Output Format]:
[Specify structure, length, style]
```

## Common Patterns

### Pattern 1: Chain of Thought
```
Think through this step-by-step:
1. First, [analyze X]
2. Then, [consider Y]
3. Finally, [conclude Z]
```

### Pattern 2: Few-Shot Learning
```
<examples>
Input: [example 1 input]
Output: [example 1 output]

Input: [example 2 input]
Output: [example 2 output]
</examples>

Now process: [actual input]
```

### Pattern 3: Structured Output
```
Provide your response in this format:

<analysis>
[Your analysis here]
</analysis>

<recommendation>
[Your recommendation here]
</recommendation>

<reasoning>
[Your reasoning here]
</reasoning>
```

## Quick Wins for Better Prompts

1. **Add specificity**: "Write a 3-paragraph summary" vs "Summarize this"
2. **Use examples**: Show 2-3 examples of what you want
3. **Request reasoning**: Ask Claude to think through the problem
4. **Define constraints**: "Under 500 words", "JSON format only"
5. **Provide context**: Include relevant background information
6. **Structure with XML**: Use tags for complex, multi-part prompts

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Output too generic | Add specific examples and constraints |
| Wrong format | Use `<output_format>` tags with exact structure |
| Missing details | Add `<thinking>` tags to encourage reasoning |
| Inconsistent results | Provide more examples and clearer instructions |
| Too verbose | Specify exact length/word count constraints |
| Off-topic responses | Add `<context>` and `<constraints>` sections |

## Model Selection Guide

- **Claude 3.5 Sonnet**: Best balance - fast, intelligent, cost-effective
- **Claude Opus 4.5**: Most capable - complex reasoning, creative tasks
- **Claude 3.5 Haiku**: Fastest - simple tasks, high-volume processing

## Power Features

### Extended Thinking (Opus 4.5)
```
<claude_info>
Before answering, use extended thinking to deeply analyze this problem.
</claude_info>
```

### Prefilling
Start Claude's response to control format:
```
User: What's the capital of France?
Assistant: The capital is
```
Claude continues: "Paris."

### Document Analysis
```
Analyze this document:

<document>
[Paste full document here]
</document>

Questions:
1. [Question 1]
2. [Question 2]
```

## 3 Rules for Expert Prompts

1. **CLARITY**: If a human wouldn't understand it, Claude won't either
2. **EXAMPLES**: One example is worth a thousand words of instruction
3. **STRUCTURE**: XML tags transform chaos into clarity

## Quick Reference Card

```
┌─────────────────────────────────────┐
│ PROMPT ENGINEERING CHECKLIST        │
├─────────────────────────────────────┤
│ □ Clear task description            │
│ □ Specific role/context provided    │
│ □ 2-3 concrete examples             │
│ □ Step-by-step instructions         │
│ □ Output format specified           │
│ □ Constraints and boundaries set    │
│ □ XML tags for structure (if complex)│
└─────────────────────────────────────┘
```

## Further Reading

- Full guide: `assets/reference/xml-tag-library.md`
- 2025 techniques: `assets/reference/new-techniques.md`
- Model tips: `assets/reference/claude-4x-tips.md`
- Examples: `assets/examples/before-after-gallery.md`
