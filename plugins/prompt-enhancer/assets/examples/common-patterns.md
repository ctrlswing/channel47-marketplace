# Common Patterns: Frequently Used Techniques

## Introduction

Eight essential prompt patterns that solve recurring challenges. These are the building blocks of effective prompts.

---

## Pattern 1: Chain of Thought

**Purpose:** Guide Claude through step-by-step reasoning for better accuracy

**When to use:**
- Complex problem solving
- Multi-step calculations
- Logical reasoning tasks
- When you need to verify thinking

**Basic structure:**
```
Think through this step-by-step:
1. [First reasoning step]
2. [Second reasoning step]
3. [Third reasoning step]
4. [Conclusion]
```

**Advanced version:**
```xml
<instructions>
Before providing your answer, work through these steps:

1. **Understand**: Restate the problem in your own words
2. **Analyze**: Break down into sub-problems
3. **Solve**: Address each sub-problem
4. **Verify**: Check your reasoning
5. **Conclude**: Provide final answer

Show your work for each step.
</instructions>

<problem>
[Your problem here]
</problem>
```

**Example:**
```xml
<instructions>
Calculate the total cost step-by-step:
1. Calculate base cost
2. Apply discounts
3. Add taxes
4. Include shipping
5. Show final total with breakdown
</instructions>

<problem>
5 items at $29.99 each, 15% bulk discount, 8.5% tax, $12 flat-rate shipping
</problem>
```

**Why it works:**
- Reduces logical errors
- Makes reasoning transparent
- Catches mistakes early
- Enables debugging

**Variations:**
- Show reasoning in `<thinking>` tags
- Request confidence level at each step
- Ask Claude to double-check own work

---

## Pattern 2: Few-Shot Learning

**Purpose:** Show examples of exactly what you want instead of describing it

**When to use:**
- Novel output formats
- Specific styles
- Complex transformations
- Pattern matching tasks

**Basic structure:**
```xml
<examples>
<example>
Input: [sample input 1]
Output: [desired output 1]
</example>

<example>
Input: [sample input 2]
Output: [desired output 2]
</example>

<example>
Input: [sample input 3]
Output: [desired output 3]
</example>
</examples>

Now process: [actual input]
```

**Advanced version:**
```xml
<task>
[Task description]
</task>

<examples>
<example label="simple_case">
Input: [Simple example]
Output: [Expected output]
Explanation: [Why this output is correct]
</example>

<example label="edge_case">
Input: [Edge case example]
Output: [Expected output]
Explanation: [How to handle edge case]
</example>

<example label="complex_case">
Input: [Complex example]
Output: [Expected output]
Explanation: [Reasoning for complex case]
</example>
</examples>

<input>
[Your actual input]
</input>
```

**Example:**
```xml
<examples>
<example>
Input: "The API returned a 404 error when requesting user data"
Output: {
  "category": "bug",
  "severity": "high",
  "component": "API",
  "action": "investigate_immediately"
}
</example>

<example>
Input: "Would be nice to have dark mode"
Output: {
  "category": "feature_request",
  "severity": "low",
  "component": "UI",
  "action": "add_to_backlog"
}
</example>
</examples>

Now classify: "Users can't checkout, payment button doesn't work"
```

**Why it works:**
- One example worth 1000 words
- Shows format, style, and edge cases
- Reduces ambiguity
- Demonstrates quality standards

**Best practices:**
- Use 2-5 examples (sweet spot is 3)
- Include diverse cases
- Show edge case handling
- Vary examples to cover pattern space

---

## Pattern 3: Role Prompting

**Purpose:** Give Claude expertise and perspective for better-informed responses

**When to use:**
- Domain-specific tasks
- When expertise matters
- Professional communication
- Specialized analysis

**Basic structure:**
```
You are a [role] with [expertise]. [Task instruction].
```

**Advanced version:**
```xml
<role>
You are a [position] with [years] of experience in [domain].

Your expertise includes:
- [Skill/knowledge area 1]
- [Skill/knowledge area 2]
- [Skill/knowledge area 3]

You are known for:
- [Quality/approach 1]
- [Quality/approach 2]

You communicate with [stakeholders] using [communication style].
</role>

<task>
[Your task]
</task>
```

**Example:**
```xml
<role>
You are a senior security engineer with 12 years of experience in application security.

Your expertise includes:
- OWASP Top 10 vulnerabilities
- Secure coding practices across multiple languages
- Threat modeling and risk assessment
- Security incident response

You are known for:
- Thorough, methodical code reviews
- Clear explanations that help developers learn
- Balancing security with practical development needs

You communicate findings clearly with both developers and management.
</role>

<task>
Review this authentication code for security vulnerabilities.
</task>
```

**Why it works:**
- Activates relevant knowledge
- Sets appropriate tone and depth
- Frames perspective appropriately
- Improves domain-specific responses

**Common roles:**
- Technical: "senior developer", "data scientist", "DevOps engineer"
- Business: "product manager", "business analyst", "consultant"
- Creative: "UX writer", "content strategist", "technical writer"
- Analytical: "financial analyst", "researcher", "statistician"

---

## Pattern 4: Structured Output

**Purpose:** Get consistent, parseable, formatted responses

**When to use:**
- API integrations
- Automated processing
- Consistent formatting needed
- Data extraction tasks

**Basic structure:**
```xml
<output_format>
Provide response in this exact format:

[Show exact structure with placeholders]
</output_format>
```

**Advanced version:**
```xml
<output_format>
Return a JSON object with this exact schema:

{
  "field1": "string",
  "field2": number,
  "field3": ["array", "of", "strings"],
  "field4": {
    "nested_field": "string"
  },
  "field5": boolean
}

Requirements:
- All fields are required
- Validate [specific field] must be [constraint]
- If [condition], set [field] to [value]
- Do not include fields not in schema
</output_format>
```

**Example:**
```xml
<output_format>
Return your analysis as a JSON object:

{
  "summary": "string (max 200 chars)",
  "sentiment": "positive" | "negative" | "neutral" | "mixed",
  "confidence": number between 0 and 1,
  "key_themes": ["theme1", "theme2", "theme3"],
  "urgency": "low" | "medium" | "high" | "critical",
  "requires_action": boolean,
  "recommended_actions": ["action1", "action2"] or null
}

Validation:
- confidence must be 0-1
- key_themes must have 1-5 items
- recommended_actions is null if requires_action is false
</output_format>
```

**Why it works:**
- Enables automated parsing
- Ensures consistency
- Prevents format errors
- Makes integration easy

**Formats:**
- JSON (most common)
- XML
- CSV/TSV
- Markdown tables
- Custom text formats

---

## Pattern 5: Constraint-Driven

**Purpose:** Define boundaries and rules to guide output

**When to use:**
- Need to prevent certain behaviors
- Specific requirements must be met
- Quality control important
- Regulated or sensitive content

**Basic structure:**
```xml
<constraints>
- [Rule 1]
- [Rule 2]
- [Rule 3]
</constraints>
```

**Advanced version:**
```xml
<constraints>
<must>
- [Requirement that must be met]
- [Another required element]
</must>

<must_not>
- [Behavior to avoid]
- [Content to exclude]
</must_not>

<limits>
- Length: [word/character count]
- Time: [time constraint]
- Scope: [boundaries]
</limits>

<quality_standards>
- [Quality requirement 1]
- [Quality requirement 2]
</quality_standards>

<edge_cases>
- If [condition], then [handling]
- If [condition], then [handling]
</edge_cases>
</constraints>
```

**Example:**
```xml
<constraints>
<must>
- Base response on ONLY the provided documents
- Cite sources with [doc_id, page_num] format
- Include confidence level for each claim
- Flag any contradictions in source material
</must>

<must_not>
- Do not use external knowledge
- Do not make assumptions about missing information
- Do not include opinions, only facts from documents
- Do not extrapolate beyond what's explicitly stated
</must_not>

<limits>
- Response length: 500-750 words
- Citations: minimum 3 per major claim
- Processing time: prioritize first 3 documents if time-constrained
</limits>

<edge_cases>
- If documents conflict, present both views and flag the conflict
- If information is missing, explicitly state "not found in documents"
- If confidence is below 70%, include a disclaimer
</edge_cases>
</constraints>
```

**Why it works:**
- Prevents common errors
- Ensures compliance
- Defines quality bars
- Handles edge cases upfront

---

## Pattern 6: Context Loading

**Purpose:** Provide all necessary background for accurate responses

**When to use:**
- Domain-specific tasks
- When general knowledge insufficient
- Building on previous work
- Specialized terminology

**Basic structure:**
```xml
<context>
[Background information]
[Relevant details]
[Important constraints or factors]
</context>

[Task instructions]
```

**Advanced version:**
```xml
<context>
<background>
[Historical context, why this matters]
</background>

<current_situation>
[Current state, what's happening now]
</current_situation>

<stakeholders>
[Who's involved, their interests/concerns]
</stakeholders>

<constraints>
[Limitations, requirements, boundaries]
</constraints>

<terminology>
- [Term 1]: [Definition]
- [Term 2]: [Definition]
</terminology>

<related_work>
[Previous attempts, related projects]
</related_work>
</context>

<task>
[Your specific task]
</task>
```

**Example:**
```xml
<context>
<background>
We're a B2B SaaS company that launched 18 months ago. Our initial target market was enterprise (1000+ employees) but we're seeing more traction with mid-market (100-1000 employees).
</background>

<current_situation>
Q4 revenue grew 40% but came entirely from mid-market. Enterprise sales cycle is 9+ months vs. 6 weeks for mid-market. We're considering pivoting our go-to-market strategy.
</current_situation>

<stakeholders>
- Sales team: Frustrated by long enterprise cycles
- Product team: Built features for enterprise use cases
- Investors: Expecting us to move upmarket over time
- Current customers: 75% mid-market, 25% enterprise
</stakeholders>

<constraints>
- 12 months runway at current burn rate
- Can't afford to serve both markets equally well
- Product roadmap committed for next 2 quarters
</constraints>
</context>

<task>
Analyze whether we should pivot fully to mid-market or double down on enterprise. Provide strategic recommendation with reasoning.
</task>
```

**Why it works:**
- Gives Claude full picture
- Prevents assumptions
- Enables informed analysis
- Grounds responses in reality

---

## Pattern 7: Multi-Stage Pipeline

**Purpose:** Break complex tasks into sequential steps with checkpoints

**When to use:**
- Complex multi-step workflows
- When intermediate validation needed
- Building on previous outputs
- Quality control important

**Basic structure:**
```
Step 1: [First task]
[Wait for output]

Step 2: Using the output from Step 1, [second task]
[Wait for output]

Step 3: Using outputs from Steps 1-2, [final task]
```

**Advanced version:**
```xml
<pipeline>
<stage id="1" name="[stage_name]">
<task>[What to do]</task>
<output>[What to produce]</output>
<validation>[How to verify quality]</validation>
</stage>

<stage id="2" name="[stage_name]">
<input>Output from Stage 1</input>
<task>[What to do]</task>
<output>[What to produce]</output>
<validation>[How to verify quality]</validation>
</stage>

<stage id="3" name="[stage_name]">
<input>Outputs from Stages 1-2</input>
<task>[What to do]</task>
<output>[Final deliverable]</output>
<validation>[How to verify quality]</validation>
</stage>
</pipeline>

Execute Stage 1 first. I'll review before proceeding to Stage 2.
```

**Example:**
```xml
<pipeline>
<stage id="1" name="data_analysis">
<task>Analyze the user feedback data and identify the top 5 themes</task>
<output>List of themes with frequency counts and representative quotes</output>
<validation>Each theme should appear in at least 10% of feedback</validation>
</stage>

<stage id="2" name="impact_assessment">
<input>Top 5 themes from Stage 1</input>
<task>For each theme, assess business impact and implementation difficulty</task>
<output>Themes ranked by priority (impact vs. effort matrix)</output>
<validation>Impact scores must be justified with data or business logic</validation>
</stage>

<stage id="3" name="recommendation">
<input>Prioritized themes from Stage 2</input>
<task>Develop action plan for top 3 priorities</task>
<output>
- Detailed implementation plan
- Resource requirements
- Timeline
- Success metrics
</output>
<validation>Plans must be specific enough to start execution</validation>
</stage>
</pipeline>

Start with Stage 1. I'll review before we proceed.
```

**Why it works:**
- Enables quality checkpoints
- Prevents compounding errors
- Allows mid-course corrections
- Breaks complexity into manageable pieces

**When to use single-pass vs. pipeline:**
- Single-pass: Simple, linear tasks
- Pipeline: Complex tasks where early errors cascade

---

## Pattern 8: Comparative Analysis

**Purpose:** Evaluate multiple options against defined criteria

**When to use:**
- Decision-making
- Vendor/tool selection
- A/B test analysis
- Trade-off evaluation

**Basic structure:**
```xml
<options>
<option name="[Option 1]">[Details]</option>
<option name="[Option 2]">[Details]</option>
<option name="[Option 3]">[Details]</option>
</options>

<criteria>
1. [Criterion 1]
2. [Criterion 2]
3. [Criterion 3]
</criteria>

Compare options and recommend the best choice.
```

**Advanced version:**
```xml
<options>
<option id="A" name="[Option name]">
<details>[Full description, specs, costs, etc.]</details>
<pros>[Known advantages]</pros>
<cons>[Known disadvantages]</cons>
</option>

<option id="B" name="[Option name]">
[Same structure]
</option>

<option id="C" name="[Option name]">
[Same structure]
</option>
</options>

<evaluation_criteria>
<criterion name="[Name]" weight="[1-10]">
[Description of what makes this criterion important]
[How to measure/evaluate it]
</criterion>

<criterion name="[Name]" weight="[1-10]">
[Description and evaluation method]
</criterion>
</evaluation_criteria>

<context>
Use case: [How this will be used]
Constraints: [Budget, timeline, technical limits]
Success criteria: [What defines the right choice]
</context>

<output_format>
## Summary
[One-sentence recommendation with key reasoning]

## Detailed Scoring
| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|----------|----------|----------|
| [Name] | [W] | [Score + rationale] | [Score + rationale] | [Score + rationale] |

## Total Scores
- Option A: [Score]/100
- Option B: [Score]/100
- Option C: [Score]/100

## Recommendation
[Detailed explanation of recommended option]

## Trade-offs
[What you gain and lose with this choice]

## Risk Factors
[Potential issues to watch for]
</output_format>
```

**Example:**
```xml
<options>
<option id="A" name="Build In-House">
<details>
Develop custom solution with internal team
Estimated cost: $150K (6 months of dev time)
Ongoing maintenance: 1 FTE
</details>
<pros>Full control, custom to our needs, IP ownership</pros>
<cons>Long timeline, ongoing maintenance burden, opportunity cost</cons>
</option>

<option id="B" name="SaaS Platform">
<details>
Use existing platform (e.g., Segment)
Cost: $2K/month ($24K/year)
Setup time: 2 weeks
</details>
<pros>Quick deployment, maintained by vendor, proven</pros>
<cons>Recurring cost, vendor lock-in, less customization</cons>
</option>
</options>

<evaluation_criteria>
<criterion name="time_to_market" weight="9">
How quickly can we deploy and start getting value?
Critical: Need solution for upcoming product launch in 8 weeks.
</criterion>

<criterion name="total_cost_3yr" weight="7">
Total cost of ownership over 3 years (dev + maintenance + opportunity cost)
</criterion>

<criterion name="flexibility" weight="6">
Ability to customize and adapt to changing requirements
</criterion>
</evaluation_criteria>
```

**Why it works:**
- Systematic evaluation
- Transparent reasoning
- Weighted decision-making
- Defensible recommendations

---

## Combining Patterns

Most effective prompts combine multiple patterns:

### Example: Chain of Thought + Structured Output
```xml
<instructions>
Analyze step-by-step:
1. Identify the main issue
2. Consider root causes
3. Evaluate potential solutions
4. Recommend best approach
</instructions>

<output_format>
{
  "issue": "string",
  "root_causes": ["cause1", "cause2"],
  "solutions": [
    {"name": "string", "pros": [], "cons": []}
  ],
  "recommendation": "string"
}
</output_format>
```

### Example: Role + Constraints + Few-Shot
```xml
<role>
You are a technical writer creating API documentation.
</role>

<constraints>
- Write for developers with basic REST API knowledge
- Include code examples in Python and JavaScript
- Keep descriptions under 100 words
- Use active voice
</constraints>

<examples>
<example>
Endpoint: GET /users/{id}
Doc: "Retrieves a specific user by ID. Returns user object with profile data, preferences, and account status. Requires authentication token in header."

```python
response = requests.get(
  'https://api.example.com/users/123',
  headers={'Authorization': f'Bearer {token}'}
)
```
</example>
</examples>
```

## Pattern Selection Guide

| Task Type | Recommended Patterns |
|-----------|---------------------|
| Complex reasoning | Chain of Thought + Structured Output |
| Novel format | Few-Shot Learning + Structured Output |
| Domain expertise | Role Prompting + Context Loading |
| Quality control | Constraint-Driven + Multi-Stage Pipeline |
| Decision making | Comparative Analysis + Chain of Thought |
| Data extraction | Structured Output + Few-Shot Learning |
| Analysis task | Context Loading + Structured Output |

## Anti-Patterns to Avoid

❌ **Pattern overload**: Don't use every pattern on simple tasks
❌ **Inconsistent structure**: Mix patterns thoughtfully, not randomly
❌ **Missing examples**: Few-shot learning needs actual examples
❌ **Vague constraints**: "Be concise" vs. "Max 200 words"
❌ **Role without task**: Role sets context but doesn't replace clear instructions

## Next Steps

1. **Master one pattern**: Start with the most relevant to your work
2. **Practice combination**: Try Chain of Thought + your chosen pattern
3. **Build templates**: Save successful pattern combinations
4. **Iterate**: Refine patterns based on results
5. **Share**: Help teammates learn effective patterns
