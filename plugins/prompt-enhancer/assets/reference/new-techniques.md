# 2025 Prompt Engineering Techniques

## Overview

Advanced techniques introduced with Claude 3.5 and Opus 4 models (2024-2025).

**Key innovations:**
- Extended Thinking (Opus 4.5)
- Enhanced prefilling
- Long-context optimization (200K tokens)
- Improved multimodal prompting
- Better structured outputs

## 1. Extended Thinking (Opus 4.5)

### Overview
Claude Opus 4.5 can engage in deep reasoning before responding, sometimes taking minutes to thoroughly analyze complex problems.

### When to Use
✅ Complex math/logic, advanced coding, strategic analysis, novel problem-solving
❌ Simple queries, quick generation, classification, high-volume tasks

### Enable via API
```python
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[...]
)
```

### Enable via Prompt
```xml
<claude_info>
Use extended thinking to deeply analyze this problem.
Consider multiple approaches and evaluate trade-offs.
</claude_info>
```

### Example
```xml
<problem>
Design distributed caching for 50M daily users globally.
</problem>

<constraints>
- 10M item catalog
- Handle 10x traffic spikes
- $200K/year budget
- 99.99% uptime
</constraints>

<claude_info>
Use extended thinking to:
1. Analyze requirements
2. Consider caching strategies (CDN, Redis, application-level)
3. Evaluate trade-offs (cost, latency, consistency)
4. Design solution with failure handling
</claude_info>
```

## 2. Enhanced Prefilling

### Overview
Start Claude's response to strictly control output format from the first character.

### JSON Prefilling
```
User: Analyze sentiment: "Great product but expensive"Assistant: {"sentiment": "mixed", "product_quality": "positive", "price_concern": true}
```

Enforces JSON from first character - highly reliable.

### Style Prefilling
```
User: Write a product description for noise-canceling headphones.
Assistant: Escape the noise.
```

Continues in the established tone.

## 3. Long-Context Optimization

### 200K Token Context
All modern Claude models support 200K token context (~500 pages).

### Best Practices
1. **Structure documents**: Use XML tags to organize content
2. **Request specific sections**: Tell Claude which parts matter most
3. **Use caching**: Cache large documents for efficiency
4. **Prioritize content**: Put most important info first

### Example
```xml
<documents>
<document id="contract" priority="high">
[Full 200-page contract]
</document>

<document id="exhibits" priority="medium">
[Supporting exhibits]
</document>
</documents>

<task>
Focus primarily on the main contract (id="contract").
Identify all financial obligations and termination clauses.
Reference exhibits only if directly relevant.
</task>
```

## 4. Multimodal Prompting

### Image + Text Analysis
Claude Sonnet models excel at combining visual and textual information.

### Pattern
```python
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": image_data}},
            {"type": "text", "text": "Analyze this UI mockup for accessibility issues"}
        ]
    }]
)
```

### Best for
- UI/UX review
- Document analysis (screenshots, PDFs)
- Diagram interpretation
- Visual QA

## 5. Structured Outputs

### JSON Schema Enforcement
Request strict JSON format with validation.

### Pattern
```xml
<output_format type="json">
{
  "field1": "string",
  "field2": number,
  "field3": ["array"],
  "required_field": "must be present"
}

Validation:
- field2 must be 0-100
- field3 must have 1-5 items
</output_format>
```

### Benefits
- Reliable parsing
- Type safety
- API integration
- Automated processing

## 6. Prompt Caching

### Cache Large Content
Save cost and latency by caching repeated content.

### Example
```python
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    system=[{
        "type": "text",
        "text": "Large system prompt or context...",
        "cache_control": {"type": "ephemeral"}
    }],
    messages=[...]
)
```

### Cache These
- System prompts
- Large documents
- Reference materials
- Code bases
- Tool definitions

## Combining Techniques

### Advanced Pattern
```xml
<!-- Opus 4.5 with extended thinking, long context, structured output -->

<claude_info>
Use extended thinking to analyze these documents comprehensively.
</claude_info>

<documents>
[Multiple large documents - 100K tokens total]
</documents>

<task>
Synthesize insights and identify contradictions across all documents.
</task>

<output_format type="json">
{
  "insights": [
    {"theme": "string", "supporting_docs": ["doc1", "doc2"], "confidence": number}
  ],
  "contradictions": [
    {"issue": "string", "doc1_position": "string", "doc2_position": "string"}
  ]
}
</output_format>
```

## Summary

**2025 capabilities:**
1. **Extended thinking** - Deep analysis for complex tasks (Opus 4.5)
2. **Prefilling** - Strict format control
3. **Long context** - 200K tokens effectively
4. **Multimodal** - Images + text analysis  
5. **Structured output** - Reliable JSON generation
6. **Caching** - Cost/latency optimization

**When to use what:**
- Complex reasoning → Extended thinking (Opus 4.5)
- Format control → Prefilling
- Large documents → Long-context + caching
- Visual analysis → Multimodal (Sonnet)
- API integration → Structured output

See other guides for detailed examples and patterns.
