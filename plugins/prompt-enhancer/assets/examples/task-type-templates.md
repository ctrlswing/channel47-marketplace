# Task-Type Templates: Ready-to-Use Patterns

## Overview

Seven battle-tested templates for common prompt engineering tasks. Copy, customize, and use immediately.

---

## Template 1: Document Analysis

**Use for:** Analyzing contracts, reports, research papers, technical docs

```xml
<document type="[document_type]">
[Your document content here]
</document>

<analysis_task>
[What you want to learn from the document]
</analysis_task>

<focus_areas>
1. [First area of interest]
2. [Second area of interest]
3. [Third area of interest]
</focus_areas>

<output_format>
## Summary
[High-level overview in 2-3 sentences]

## Key Findings
- [Finding 1 with supporting evidence]
- [Finding 2 with supporting evidence]
- [Finding 3 with supporting evidence]

## [Custom Section 1]
[Specific analysis area]

## [Custom Section 2]
[Specific analysis area]

## Recommendations
[If applicable]
</output_format>

<constraints>
- Focus on [specific aspect]
- Highlight any [concerns/risks/opportunities]
- Use [technical/business/general] language
</constraints>
```

**Customization points:**
- `document_type`: contract, report, research paper, etc.
- `focus_areas`: Adapt to your analysis needs
- `output_format`: Match your deliverable requirements
- `constraints`: Add domain-specific rules

**Example use:**
```xml
<document type="vendor_contract">
[45-page SaaS vendor contract]
</document>

<analysis_task>
Identify potential risks and non-standard terms that legal should review.
</analysis_task>

<focus_areas>
1. Financial obligations and payment terms
2. Liability caps and indemnification
3. Data security and privacy requirements
4. Termination and exit clauses
</focus_areas>
```

---

## Template 2: Code Review

**Use for:** Security review, code quality, architecture feedback

```xml
<role>
You are a [seniority] [specialization] engineer conducting a code review
focused on [focus_area].
</role>

<code language="[language]" file="[filename]">
[Your code here]
</code>

<context>
- Purpose: [What this code does]
- Environment: [Production/dev, scale, constraints]
- Recent changes: [What changed and why]
</context>

<review_criteria>
Evaluate for:
1. [Criterion 1 - e.g., Security vulnerabilities]
2. [Criterion 2 - e.g., Performance issues]
3. [Criterion 3 - e.g., Maintainability]
4. [Criterion 4 - e.g., Best practices]
5. [Criterion 5 - e.g., Error handling]
</review_criteria>

<output_format>
## Overall Assessment
[High-level summary and risk rating]

## Critical Issues
- [Issue]: [Description, location, fix]

## Moderate Issues
- [Issue]: [Description, location, fix]

## Minor Issues / Suggestions
- [Issue]: [Description, location, fix]

## Positive Aspects
[What's done well]

## Recommendations
[Prioritized action items]
</output_format>
```

**Example use:**
```xml
<role>
You are a senior backend engineer conducting a security-focused code review.
</role>

<code language="python" file="api/auth.py">
def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}'"
    user = db.execute(query)
    # ... rest of code
</code>

<review_criteria>
Evaluate for:
1. SQL injection and other security vulnerabilities
2. Authentication best practices
3. Error handling and logging
4. Input validation
</review_criteria>
```

---

## Template 3: Content Creation

**Use for:** Blog posts, documentation, marketing copy, technical writing

```xml
<task>
Write a [content_type] about [topic] for [audience].
</task>

<context>
- Target audience: [Demographics, knowledge level, needs]
- Publication/platform: [Where this will appear]
- Goal: [What reader should do/learn/feel]
- Tone: [Professional, casual, technical, friendly, etc.]
</context>

<requirements>
- Length: [Word count or range]
- Structure: [Outline or required sections]
- Must include: [Key points, examples, CTAs]
- Avoid: [What not to include]
- SEO keywords (if applicable): [Keywords to include naturally]
</requirements>

<examples>
Good example:
"[Sample of style/voice you want]"

Avoid:
"[Sample of what you don't want]"
</examples>

<structure>
1. [Opening section - purpose/content]
2. [Main section 1 - purpose/content]
3. [Main section 2 - purpose/content]
4. [Main section 3 - purpose/content]
5. [Conclusion - purpose/content]
</structure>
```

**Example use:**
```xml
<task>
Write a blog post about API rate limiting for backend developers.
</task>

<context>
- Target audience: Mid-level backend developers
- Publication: Company engineering blog
- Goal: Educate about implementing rate limiting effectively
- Tone: Technical but accessible, practical focus
</context>

<requirements>
- Length: 1200-1500 words
- Include 2-3 code examples (Python or Node.js)
- Must cover: Why rate limit, common strategies, implementation tips
- Avoid: Overly academic discussion, obscure algorithms
</requirements>
```

---

## Template 4: Data Analysis

**Use for:** Analyzing datasets, finding patterns, generating insights

```xml
<context>
You are analyzing [data_type] for [business_purpose].
Key questions: [Main questions to answer]
</context>

<data format="[csv/json/table]">
[Your data here]
</data>

<analysis_objectives>
1. [Objective 1 - e.g., Identify trends]
2. [Objective 2 - e.g., Find anomalies]
3. [Objective 3 - e.g., Compare segments]
4. [Objective 4 - e.g., Generate recommendations]
</analysis_objectives>

<output_format>
## Executive Summary
[2-3 sentences with most important findings]

## Key Metrics
- [Metric 1]: [Value and significance]
- [Metric 2]: [Value and significance]

## Trend Analysis
[Patterns observed with supporting data]

## Insights
1. [Insight with data support]
2. [Insight with data support]
3. [Insight with data support]

## Recommendations
- [Action 1]: [Expected impact]
- [Action 2]: [Expected impact]
- [Action 3]: [Expected impact]
</output_format>

<constraints>
- Focus on actionable insights
- Support claims with specific data points
- Highlight anything urgent or surprising
</constraints>
```

**Example use:**
```xml
<context>
You are analyzing e-commerce sales data for Q4 2024.
Key questions: Why did conversion rate drop in November? Which products drove revenue?
</context>

<data format="csv">
date,visits,conversions,revenue,cart_abandonment_rate
2024-10-01,15000,750,125000,0.35
...
</data>

<analysis_objectives>
1. Identify causes of conversion rate decline
2. Determine top revenue drivers
3. Analyze cart abandonment patterns
4. Recommend optimization opportunities
</analysis_objectives>
```

---

## Template 5: Problem Solving

**Use for:** Debugging, system design, optimization, decision-making

```xml
<problem>
[Clear description of the problem]
</problem>

<context>
- Current situation: [What's happening now]
- Impact: [Why this matters, who's affected]
- Timeline: [When it started, urgency]
- Previous attempts: [What's been tried]
</context>

<technical_details>
- System architecture: [Relevant tech stack]
- Scale: [Users, requests, data volume]
- Constraints: [Budget, time, resources]
- Recent changes: [What changed before problem appeared]
</technical_details>

<data_points>
[Metrics, logs, error messages, performance data]
</data_points>

<instructions>
1. Analyze the problem and likely root causes
2. Consider multiple solution approaches
3. Evaluate trade-offs (cost, time, complexity)
4. Provide specific, actionable recommendations
5. Include implementation steps
</instructions>

<output_format>
## Problem Analysis
[Root cause analysis]

## Solution Options
### Option 1: [Name]
- Approach: [Description]
- Pros: [Benefits]
- Cons: [Drawbacks]
- Cost: [Estimate]
- Timeline: [Estimate]

### Option 2: [Name]
[Same structure]

## Recommendation
[Which option and why]

## Implementation Plan
1. [Step 1]
2. [Step 2]
3. [Step 3]
</output_format>
```

**Example use:**
```xml
<problem>
API response times degraded from 200ms to 2000ms over the past week,
causing user complaints and increased error rates.
</problem>

<context>
- Impact: 50,000 daily active users experiencing slow app
- Timeline: Started Monday after weekend deployment
- Previous attempts: Restarted servers (temporary fix), rolled back code (no change)
</context>

<technical_details>
- Architecture: Node.js API, PostgreSQL, Redis cache
- Scale: 100,000 requests/day
- Recent changes: Added new analytics tracking, updated ORM library
</technical_details>

<data_points>
- Average query time: 1.5s (was 50ms)
- Cache hit rate: 45% (was 85%)
- Database connections: 95/100 (was 30/100)
</data_points>
```

---

## Template 6: Classification / Categorization

**Use for:** Tagging, sentiment analysis, triage, labeling

```xml
<task>
Classify [items] by [classification_dimensions].
</task>

<classification_schema>
[Dimension 1]: [option1 | option2 | option3]
[Dimension 2]: [option1 | option2 | option3]
[Dimension 3]: [value range or categories]
[Additional metadata]: [type/format]
</classification_schema>

<examples>
<example>
Input: "[Sample input]"
Output: {
  "[dimension1]": "[value]",
  "[dimension2]": "[value]",
  "[dimension3]": "[value]",
  "[metadata]": "[value]"
}
</example>

<example>
Input: "[Another sample]"
Output: {
  "[dimension1]": "[value]",
  "[dimension2]": "[value]",
  "[dimension3]": "[value]",
  "[metadata]": "[value]"
}
</example>
</examples>

<items>
[Your items to classify]
</items>

<output_format>
Return a JSON array with one object per item.
Include confidence score for uncertain classifications.
</output_format>

<edge_cases>
- If [scenario], classify as [value]
- If [scenario], set [dimension] to [value]
</edge_cases>
```

**Example use:**
```xml
<task>
Classify customer support tickets by priority, category, and required expertise.
</task>

<classification_schema>
priority: low | medium | high | critical
category: billing | technical | feature_request | bug | account
expertise: tier1 | tier2 | engineering | billing_specialist
estimated_time: number (minutes)
</classification_schema>

<examples>
<example>
Input: "Can't log in, getting 'invalid password' error even after reset"
Output: {
  "priority": "high",
  "category": "technical",
  "expertise": "tier2",
  "estimated_time": 15
}
</example>
</examples>
```

---

## Template 7: Comparison / Evaluation

**Use for:** Vendor selection, A/B test analysis, competitive research

```xml
<task>
Compare [items] and recommend the best option for [use_case].
</task>

<items_to_compare>
<item name="[Item 1]">
[Details, specs, features]
</item>

<item name="[Item 2]">
[Details, specs, features]
</item>

<item name="[Item 3]">
[Details, specs, features]
</item>
</items_to_compare>

<evaluation_criteria>
Weight each criterion by importance (1-10):
1. [Criterion 1]: [weight/10] - [description]
2. [Criterion 2]: [weight/10] - [description]
3. [Criterion 3]: [weight/10] - [description]
4. [Criterion 4]: [weight/10] - [description]
</evaluation_criteria>

<context>
- Use case: [How this will be used]
- Constraints: [Budget, timeline, technical requirements]
- Current situation: [What's being replaced/added]
- Success criteria: [What defines the right choice]
</context>

<output_format>
## Summary
[Quick recommendation with reasoning]

## Detailed Comparison
| Criterion | [Item 1] | [Item 2] | [Item 3] |
|-----------|----------|----------|----------|
| [Crit 1]  | [Rating + note] | [Rating + note] | [Rating + note] |
| [Crit 2]  | [Rating + note] | [Rating + note] | [Rating + note] |

## Scores
[Item 1]: [Score]/100
[Item 2]: [Score]/100
[Item 3]: [Score]/100

## Recommendation
[Which option and detailed why]

## Trade-offs
[What you gain/lose with this choice]

## Next Steps
[How to proceed with chosen option]
</output_format>
```

**Example use:**
```xml
<task>
Compare three CRM platforms and recommend the best for our sales team.
</task>

<items_to_compare>
<item name="Salesforce">
Price: $150/user/month
Users: 25 seat minimum
Integration: Excellent (500+ apps)
Learning curve: Steep
Customization: Highly customizable
</item>

<item name="HubSpot">
[Similar details]
</item>

<item name="Pipedrive">
[Similar details]
</item>
</items_to_compare>

<evaluation_criteria>
Weight each criterion:
1. Ease of use: 9/10 - Team is not technical
2. Integration with email: 8/10 - Critical workflow
3. Price: 6/10 - Budget conscious but not primary factor
4. Customization: 5/10 - Nice to have
</evaluation_criteria>

<context>
- Use case: Managing sales pipeline for 15-person sales team
- Constraints: $3000/month budget, need to launch in 30 days
- Current situation: Using spreadsheets and email
- Success criteria: Team adoption > 80% within 3 months
</context>
```

---

## How to Use These Templates

### 1. Choose Your Template
Match your task to the template type:
- Analyzing documents → Template 1
- Reviewing code → Template 2
- Creating content → Template 3
- Analyzing data → Template 4
- Solving problems → Template 5
- Classifying items → Template 6
- Comparing options → Template 7

### 2. Customize
Replace bracketed placeholders:
- `[content_type]` → "blog post", "documentation", "email"
- `[audience]` → "backend developers", "executives", "customers"
- `[focus_area]` → "security", "performance", "usability"

### 3. Add Your Content
Fill in the sections:
- Your documents, code, data
- Specific requirements
- Context and constraints
- Examples (if applicable)

### 4. Test and Refine
- First run: See if output matches expectations
- Adjust: Add more examples, clarify requirements
- Iterate: Refine template for your specific use case

### 5. Save Your Customized Versions
Build a library of templates for:
- Repeated tasks
- Team standards
- Domain-specific needs

## Mixing Templates

Combine templates for complex tasks:

**Example: Code + Analysis**
```xml
<!-- Start with Code Review template -->
<code language="python">
[Algorithm implementation]
</code>

<!-- Add Analysis template section -->
<performance_data>
[Benchmark results]
</performance_data>

<task>
Review code for correctness AND analyze performance data
to identify optimization opportunities.
</task>
```

## Template Customization Tips

1. **Add domain vocabulary**: Include industry terms Claude should know
2. **Provide style guides**: Show examples of your preferred output style
3. **Set quality bars**: Define what "good enough" looks like
4. **Include edge cases**: Specify how to handle unusual inputs
5. **Define success metrics**: How will you measure if output is useful?

## Common Mistakes

❌ **Using templates without customization**
- Templates are starting points, not final forms
- Add your context, examples, requirements

❌ **Overcomplicating simple tasks**
- Not every prompt needs every section
- Simple task? Use simpler version

❌ **Missing key context**
- Templates remind you what to include
- Don't skip context, examples, or constraints

❌ **One-size-fits-all**
- Customize for your domain
- Different teams/tasks need different versions

## Next Steps

1. Try one template on a real task
2. Measure: Is output better than your usual prompt?
3. Customize: Adjust template based on results
4. Save: Keep customized version for reuse
5. Share: Help teammates use effective prompts

## Template Library Maintenance

As you use these:
- Track which templates work best for which tasks
- Note common customizations
- Build team-specific versions
- Update with new techniques as they emerge
- Share successful variations
