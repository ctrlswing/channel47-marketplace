# Claude 4.x Model-Specific Optimization Guide

## Model Overview

### Claude Opus 4.5 (claude-opus-4-5-20251101)
- **Best for**: Most demanding tasks, extended thinking, complex reasoning
- **Context**: 200K tokens
- **Special features**: Extended thinking mode
- **Use when**: Accuracy and depth matter more than speed/cost

### Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)
- **Best for**: Balance of intelligence, speed, and cost
- **Context**: 200K tokens
- **Special features**: Excellent coding, strong multimodal
- **Use when**: General-purpose tasks, coding, analysis

### Claude 3.5 Sonnet (claude-3-5-sonnet-20241022)
- **Best for**: Fast, intelligent responses
- **Context**: 200K tokens
- **Use when**: Real-time applications, high-volume processing

### Claude 3.5 Haiku (claude-3-5-haiku-20241022)
- **Best for**: Speed and efficiency
- **Context**: 200K tokens
- **Use when**: Simple tasks, high-volume, tight latency requirements

## Optimization Tips by Model

### Opus 4.5 Specific

**Enable Extended Thinking**
```python
# For complex reasoning tasks
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[{"role": "user", "content": "Complex task..."}]
)
```

**Best practices:**
- Use for novel problem-solving
- Enable thinking for multi-step reasoning
- Provide clear success criteria
- Allow sufficient thinking budget

**Ideal use cases:**
- Advanced mathematics and logic
- Strategic planning
- Complex code generation
- Research synthesis
- Creative writing requiring depth

### Sonnet 4.5 Specific

**Leverage coding strength**
```xml
<task>
Review this codebase and suggest architectural improvements.
</task>

<code>
[Your code here]
</code>

<context>
- Tech stack: React, Node.js, PostgreSQL
- Team size: 5 developers
- Main pain points: Slow queries, complex state management
</context>
```

**Best practices:**
- Excellent for code review and generation
- Strong multimodal capabilities (images + text)
- Use for balanced tasks requiring both speed and quality
- Great for interactive applications

**Ideal use cases:**
- Full-stack development
- Code review and refactoring
- Technical documentation
- Data analysis with visualization
- General-purpose API integration

### Sonnet 3.5 & Haiku 3.5 Specific

**Optimize for speed**
```python
# Batch processing pattern
messages = [
    {"role": "user", "content": f"Classify: {item}"}
    for item in items
]

# Process concurrently
results = await asyncio.gather(*[
    client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=100,
        messages=[msg]
    )
    for msg in messages
])
```

**Best practices:**
- Keep prompts concise
- Use clear, direct instructions
- Leverage caching for repeated content
- Batch similar requests

**Ideal use cases (Haiku):**
- Classification tasks
- Data extraction
- Simple Q&A
- Content moderation
- High-volume processing

## Prompt Optimization by Task Complexity

### Simple Tasks (Haiku)
```
Extract the email address from this text: [text]
```

**No need for:**
- XML tags
- Multiple examples
- Chain-of-thought reasoning

### Moderate Tasks (Sonnet 3.5/4.5)
```xml
<document>
[Document content]
</document>

Analyze this document and provide:
1. Main themes (3-5 bullet points)
2. Key stakeholders mentioned
3. Action items with priorities
4. Overall sentiment (positive/negative/neutral)

<format>
Use markdown with clear headers for each section.
</format>
```

### Complex Tasks (Opus 4.5)
```xml
<context>
[Rich background information]
</context>

<documents>
<document id="1">[Doc 1]</document>
<document id="2">[Doc 2]</document>
<document id="3">[Doc 3]</document>
</documents>

<task>
Synthesize insights across these documents and develop a strategic recommendation.
</task>

<claude_info>
Use extended thinking to:
1. Identify patterns and contradictions
2. Evaluate multiple strategic options
3. Consider second-order consequences
4. Develop well-reasoned recommendation
</claude_info>

<output_format>
1. Executive Summary (2-3 paragraphs)
2. Key Findings (bulleted)
3. Strategic Options (with pros/cons for each)
4. Recommendation (with justification)
5. Implementation Roadmap
</output_format>
```

## Performance Optimization

### Caching (All Models)
```python
# Use prompt caching for repeated content
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    system=[
        {
            "type": "text",
            "text": "Long system prompt...",
            "cache_control": {"type": "ephemeral"}
        }
    ],
    messages=[...]
)
```

**Caching benefits:**
- Reduces latency for repeated content
- Lowers costs
- Improves throughput

**Cache effectively:**
- System prompts
- Large documents
- Reference materials
- Tool definitions
- Examples and templates

### Batch Processing
```python
# Async batch processing for efficiency
async def process_batch(items, model="claude-3-5-haiku-20241022"):
    tasks = [process_item(item, model) for item in items]
    return await asyncio.gather(*tasks)
```

### Token Management

**Monitor token usage:**
```python
response = client.messages.create(...)
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

**Optimize token usage:**
- Use concise prompts for simple tasks
- Set appropriate `max_tokens`
- Leverage caching for large context
- Choose right model for task complexity

## Multimodal Optimization (Sonnet Models)

### Image + Text Prompts
```python
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": base64_image
                }
            },
            {
                "type": "text",
                "text": "Analyze this UI mockup and suggest improvements"
            }
        ]
    }]
)
```

**Best practices:**
- Sonnet models excel at vision tasks
- Provide clear instructions about what to analyze
- Can handle multiple images
- Combine images with structured questions

## Function Calling Optimization

### Structured Tool Use
```python
tools = [{
    "name": "get_weather",
    "description": "Get current weather for a location",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {"type": "string"},
            "unit": {"type": "string", "enum": ["F", "C"]}
        },
        "required": ["location"]
    }
}]

response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}]
)
```

**Best practices:**
- Clear tool descriptions
- Well-defined schemas
- Handle tool errors gracefully
- Sonnet models excellent for function calling

## Cost Optimization

### Model Selection Matrix

| Task Type | Recommended Model | Why |
|-----------|------------------|-----|
| Simple classification | Haiku 3.5 | Lowest cost, fast |
| Content generation | Sonnet 3.5 | Good balance |
| Code generation | Sonnet 4.5 | Best coding ability |
| Complex analysis | Opus 4.5 | Highest capability |
| High-volume API | Haiku 3.5 | Cost-effective |
| Interactive chat | Sonnet 3.5/4.5 | Speed + quality |

### Cost Reduction Strategies

1. **Right-size your model**: Don't use Opus for simple tasks
2. **Use caching**: Cache system prompts and large context
3. **Optimize max_tokens**: Set appropriate limits
4. **Batch when possible**: Reduce overhead
5. **Streaming**: Show results faster, better UX

## Quality Optimization

### For Best Results (Any Model)

1. **Be specific**: "Write a 500-word blog post" vs "Write about this"
2. **Provide examples**: Show what good looks like
3. **Structure complex prompts**: Use XML tags
4. **Request reasoning**: Ask Claude to think through problems
5. **Iterate**: Refine prompts based on results

### Debugging Poor Results

**If output is:**
- Too generic → Add specific examples and constraints
- Wrong format → Use `<output_format>` with exact structure
- Inaccurate → Request step-by-step reasoning, use Opus
- Inconsistent → Add more examples, clearer instructions
- Off-topic → Better context and constraints

## Model Comparison Example

**Same task, different models:**

**Haiku (Fast, simple):**
```
Summarize this article in 3 bullet points: [article]
```

**Sonnet (Balanced):**
```xml
<article>
[Article content]
</article>

Provide a structured summary:
1. Main argument (1-2 sentences)
2. Key supporting points (3-5 bullets)
3. Implications (1 paragraph)
```

**Opus (Deep analysis):**
```xml
<article>
[Article content]
</article>

<claude_info>
Use extended thinking to analyze this article thoroughly:
- Identify explicit and implicit arguments
- Evaluate strength of evidence
- Consider counterarguments
- Assess logical consistency
- Identify biases or assumptions
</claude_info>

Provide comprehensive analysis with:
1. Executive summary
2. Detailed argument analysis
3. Evidence evaluation
4. Critical assessment
5. Broader implications
```

## Summary

**Quick decision tree:**
1. Simple, high-volume? → Haiku 3.5
2. General purpose, coding? → Sonnet 4.5
3. Need absolute best? → Opus 4.5
4. Complex reasoning? → Opus 4.5 with extended thinking

**Remember:**
- Match model to task complexity
- Use caching for efficiency
- Optimize prompts for each model
- Monitor token usage
- Iterate and refine
