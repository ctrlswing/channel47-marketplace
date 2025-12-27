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
  "model": "claude-sonnet-4-5-YYYYMMDD",  // Use latest available version
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
  "model": "claude-sonnet-4-5-YYYYMMDD",  // Use latest available version
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
