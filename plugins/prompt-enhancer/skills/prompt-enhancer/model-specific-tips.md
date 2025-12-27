# Claude 4.x Model-Specific Tips

Detailed guidance for optimizing prompts for specific Claude 4.x models.

---

## Universal Claude 4.x Changes

All Claude 4.x models currently available (Sonnet 4.5, Haiku 4.5) and upcoming (Opus 4.5) share these behavioral changes from Claude 3.x:

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
