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

Note: Replace [domain], [language], etc. with specific details from user input.

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

**If A (Structured data):**
Ask the user: "JSON or XML?"
Then ask: "What fields should be included?"
Generate schema and store for `<output_format>` section.

**If B (Markdown report):**
Ask the user: "What sections should the report include?"
Generate markdown template and store for `<output_format>` section.

**If C (Plain text):**
Ask the user: "Describe the plain text format you want."
Store description for `<output_format>` section.

**If D (Custom format):**
Ask the user: "Describe the custom format."
Generate `<output_format>` template based on description.

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
Ask the user: "What should the prefill text be? (e.g., '{' for JSON, '<response>' for XML)"

**If Extended Thinking selected:**
Ask the user: "Token budget for thinking? (Start with 2048, increase if needed)"
Load details from `new-techniques.md`

**If Examples selected:**
Load `before-after-gallery.md` for inspiration
Ask the user: "How many examples would you like to include? (Recommended: 3-5)"
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
[If Examples:] ✅ Few-shot examples - Shows exact format expected
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

**Load template function (Phase 1):**
When loading task-type template, load from `assets/examples/task-type-templates.md` and adapt based on user's specific task.

**Load examples function (Phase 6):**
When user requests examples, load relevant examples from `assets/examples/before-after-gallery.md` for inspiration.

**Generate format function (Phase 5):**
Based on user's output format choice, generate appropriate template with proper XML structure.

**Apply model optimizations function (Phase 7):**
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
