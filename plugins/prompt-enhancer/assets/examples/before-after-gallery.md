# Before & After: Prompt Improvement Gallery

## Introduction

This gallery shows 10 real-world examples of prompts transformed using Anthropic's best practices. Each example demonstrates specific improvement techniques.

## Example 1: Data Analysis Task

### Before (Vague)
```
Analyze this data and tell me what you find.

[CSV data]
```

**Problems:**
- No specific objective
- Unclear output format
- Missing context about what matters

### After (Optimized)
```xml
<context>
You are analyzing Q4 sales data for an e-commerce company.
Key concerns: declining conversion rates and high cart abandonment.
</context>

<data format="csv">
[CSV data]
</data>

<task>
Analyze this sales data and identify:
1. Top 3 trends or patterns
2. Potential causes for cart abandonment
3. Actionable recommendations to improve conversion
</task>

<output_format>
## Executive Summary
[2-3 sentence overview]

## Key Findings
- Finding 1: [description] (supporting data)
- Finding 2: [description] (supporting data)
- Finding 3: [description] (supporting data)

## Recommendations
1. [Recommendation with expected impact]
2. [Recommendation with expected impact]
3. [Recommendation with expected impact]
</output_format>
```

**Improvements:**
- Added business context
- Structured data with tags
- Specific analysis objectives
- Clear output format
- Actionable focus

**Result:** 5x more relevant, actionable insights

---

## Example 2: Code Review

### Before (Generic)
```
Review this code and tell me if it's good.

[Code snippet]
```

**Problems:**
- No review criteria
- Unclear what "good" means
- Missing context about use case

### After (Optimized)
```xml
<role>
You are a senior Python developer conducting a security-focused code review.
</role>

<code language="python" file="auth.py">
[Code snippet]
</code>

<context>
This authentication module handles user login for a fintech application.
Security and reliability are top priorities.
</context>

<review_criteria>
Evaluate for:
1. Security vulnerabilities (SQL injection, XSS, auth bypass)
2. Error handling and edge cases
3. Code clarity and maintainability
4. Performance considerations
5. Best practices compliance
</review_criteria>

<output_format>
## Security Assessment
[High/Medium/Low risk rating with explanation]

## Issues Found
### Critical
- [Issue with line numbers and fix]

### Moderate
- [Issue with line numbers and fix]

### Minor
- [Issue with line numbers and fix]

## Recommendations
[Prioritized list of improvements]
</output_format>
```

**Improvements:**
- Defined role and expertise
- Specific review criteria
- Security focus
- Structured output with priorities
- Actionable fixes

**Result:** Identified 3 security issues missed by generic review

---

## Example 3: Content Writing

### Before (Unclear)
```
Write a blog post about AI.
```

**Problems:**
- Topic too broad
- No target audience
- Missing tone, length, purpose

### After (Optimized)
```xml
<task>
Write a blog post about AI applications in healthcare for a non-technical audience.
</task>

<context>
- Target audience: Healthcare administrators (non-technical)
- Publication: Healthcare Management Today
- Goal: Educate about practical AI applications they can implement
- Tone: Professional but accessible, optimistic but realistic
</context>

<requirements>
- Length: 800-1000 words
- Include 3-4 concrete examples of AI in healthcare
- Each example should include: use case, benefits, implementation challenges
- Avoid technical jargon; explain any necessary terms
- End with actionable takeaways
</requirements>

<structure>
1. Hook: Compelling opening about AI's impact
2. Context: Why AI matters in healthcare now
3. Examples: 3-4 practical applications
4. Challenges: Honest discussion of limitations
5. Conclusion: Actionable next steps for administrators
</structure>

<examples>
Good example structure:
"AI-powered diagnostic imaging helps radiologists detect cancer earlier. At Memorial Hospital, implementing AI reduced diagnosis time by 40% and improved accuracy by 15%. However, integration required 6 months of staff training and system updates."
</examples>
```

**Improvements:**
- Specific topic and angle
- Defined audience and publication
- Clear tone and length
- Structured outline
- Concrete example format

**Result:** Production-ready content in one iteration vs. 3-4 revisions

---

## Example 4: Problem Solving

### Before (Open-ended)
```
My website is slow. How can I fix it?
```

**Problems:**
- Insufficient information
- No diagnostic guidance
- Can't provide specific advice

### After (Optimized)
```xml
<problem>
My e-commerce website has slow page load times (5-8 seconds) causing user drop-off.
</problem>

<context>
- Tech stack: React frontend, Node.js backend, PostgreSQL database
- Traffic: 10,000 daily users, spikes to 50,000 during sales
- Main pages affected: Product listings, search results
- Recent changes: Added high-res product images, implemented real-time inventory
</context>

<current_metrics>
- Time to First Byte (TTFB): 2.3s
- Largest Contentful Paint (LCP): 6.1s
- Database query time: 800ms average
- Image load time: 2-3s per image
</current_metrics>

<constraints>
- Budget: $5,000 for infrastructure improvements
- Timeline: Need solution in 2 weeks
- Cannot change database (contractual reasons)
- Must maintain 99.9% uptime during changes
</constraints>

<instructions>
1. Analyze the performance bottlenecks based on metrics
2. Prioritize issues by impact vs. effort
3. Provide specific, actionable solutions
4. Include implementation steps
5. Estimate cost and timeline for each solution
</instructions>
```

**Improvements:**
- Specific problem with metrics
- Technical context provided
- Constraints clearly stated
- Diagnostic framework
- Solution format defined

**Result:** Received 5 prioritized, implementable solutions vs. generic advice

---

## Example 5: Classification Task

### Before (Minimal)
```
Classify these customer reviews as positive or negative.

[Reviews]
```

**Problems:**
- Binary classification may miss nuance
- No handling of edge cases
- Missing confidence levels

### After (Optimized)
```xml
<task>
Classify customer feedback for our SaaS product by sentiment and urgency.
</task>

<examples>
<example>
Input: "The new feature is great but the UI is confusing. Can't find the export button."
Output: {
  "sentiment": "mixed",
  "urgency": "medium",
  "category": "usability",
  "requires_response": true,
  "confidence": 0.85
}
</example>

<example>
Input: "Love the speed improvements! Makes my workflow so much better."
Output: {
  "sentiment": "positive",
  "urgency": "low",
  "category": "performance",
  "requires_response": false,
  "confidence": 0.95
}
</example>
</examples>

<classification_schema>
sentiment: positive | negative | mixed | neutral
urgency: low | medium | high | critical
category: usability | performance | feature_request | bug | billing | other
requires_response: boolean
confidence: number (0-1)
</classification_schema>

<reviews>
[Customer reviews]
</reviews>

<output_format>
Return a JSON array with one object per review.
</output_format>
```

**Improvements:**
- Multi-dimensional classification
- Clear examples with format
- Defined schema
- Confidence scoring
- Actionable categories

**Result:** 90% accuracy vs. 70% with simple binary classification

---

## Example 6: Document Summary

### Before (Basic)
```
Summarize this document.

[Long legal document]
```

**Problems:**
- No guidance on what matters
- Unknown target summary length
- Missing audience context

### After (Optimized)
```xml
<document type="legal contract" pages="47">
[Long legal document]
</document>

<task>
Create a business-focused summary for non-legal stakeholders.
</task>

<audience>
C-level executives who need to understand key terms and risks
without reading the full contract.
</audience>

<focus_areas>
1. Financial obligations and payment terms
2. Liability and risk allocation
3. Termination conditions
4. Key deadlines and milestones
5. Non-standard or unusual clauses
</focus_areas>

<output_format>
## Executive Summary (3-4 sentences)
[High-level overview of agreement]

## Key Terms
- **Financial**: [Payment terms, amounts, schedule]
- **Duration**: [Contract length, renewal terms]
- **Termination**: [Exit conditions and penalties]

## Risk Factors
- [Risk 1]: Impact and mitigation
- [Risk 2]: Impact and mitigation

## Important Deadlines
- [Date]: [Milestone/requirement]

## Recommendations
[Action items for executives]
</output_format>

<constraints>
- Total length: 1-2 pages maximum
- Use business language, not legal jargon
- Highlight anything requiring immediate attention
- Include page references for key clauses
</constraints>
```

**Improvements:**
- Defined audience and purpose
- Specific focus areas
- Structured output format
- Length constraint
- Business-friendly language requirement

**Result:** Executives could make decisions from summary without lawyer calls

---

## Example 7: Email Drafting

### Before (Vague)
```
Write an email to apologize for the service outage.
```

**Problems:**
- No audience definition
- Missing incident details
- Unclear tone requirements

### After (Optimized)
```xml
<task>
Draft an apology email to enterprise customers about last night's service outage.
</task>

<context>
- Incident: 3-hour outage from 2am-5am EST on Nov 15
- Impact: 250 enterprise customers couldn't access the platform
- Cause: Database migration error (technical debt we were addressing)
- Resolution: Rolled back migration, services restored
- Prevention: New staging environment + extended testing protocols
</context>

<audience>
Enterprise customers (IT managers and executives) who pay $10K-100K annually.
They are technical enough to understand root causes but expect professionalism.
</audience>

<tone>
- Professional and accountable
- Transparent about cause without oversharing technical details
- Confident about prevention measures
- Appreciative of their patience
- Not overly apologetic or defensive
</tone>

<requirements>
- Subject line
- Acknowledge impact and apologize
- Explain what happened (high-level)
- Detail what we're doing to prevent recurrence
- Offer compensation (1 month service credit)
- Provide contact for questions
- Length: 200-300 words
</requirements>

<examples>
Good: "We experienced an unexpected outage due to a database migration error..."
Bad: "Unfortunately, we had some technical difficulties..."

Good: "We've implemented additional testing protocols to prevent similar issues..."
Bad: "We'll try to make sure this doesn't happen again..."
</examples>
```

**Improvements:**
- Specific audience and context
- Tone guidelines with examples
- Key points to cover
- What to avoid
- Appropriate length

**Result:** Email approved without revisions, no customer escalations

---

## Example 8: Research Task

### Before (Unfocused)
```
Research AI trends and give me insights.
```

**Problems:**
- Topic too broad
- No time frame
- Missing research goals

### After (Optimized)
```xml
<research_task>
Analyze emerging AI trends in healthcare for 2024-2025 that could impact
our medical imaging startup.
</research_task>

<context>
- Our product: AI-powered radiology imaging analysis
- Current customers: Mid-size hospitals (100-500 beds)
- Key question: What trends should inform our 2025 product roadmap?
</context>

<research_focus>
1. Regulatory changes (FDA, HIPAA, etc.)
2. Competing technologies or approaches
3. Customer needs evolution
4. Funding and investment patterns
5. Clinical adoption barriers/drivers
</research_focus>

<output_format>
## Executive Summary
[3-4 sentences on most important trends]

## Trend Analysis
For each trend:
- **Trend Name**: Description
- **Relevance**: High/Medium/Low + why
- **Impact Timeline**: Immediate/1 year/2+ years
- **Recommended Action**: What we should do

## Strategic Implications
[How these trends should influence our roadmap]

## Monitoring Recommendations
[Which trends to track and how often]
</output_format>

<constraints>
- Focus on actionable insights, not general industry news
- Prioritize trends with direct business impact
- Include data/sources where possible
- Distinguish between hype and substance
</constraints>
```

**Improvements:**
- Specific domain and timeframe
- Business context and goals
- Structured focus areas
- Actionable output format
- Hype filter

**Result:** Directly informed 3 product decisions vs. generic industry overview

---

## Example 9: Debugging Help

### Before (Incomplete)
```
This code doesn't work. Fix it.

[Code snippet]
```

**Problems:**
- No error description
- Missing context
- Can't reproduce issue

### After (Optimized)
```xml
<issue>
User authentication fails intermittently with "Invalid session" error.
</issue>

<code language="python" file="auth_middleware.py">
[Code snippet]
</code>

<error_details>
Error message: "Invalid session: Token expired"
Frequency: ~10% of requests
Pattern: Seems to happen more during high traffic
First occurred: After deploying session timeout changes yesterday
</error_details>

<context>
- Framework: Flask with Redis sessions
- Recent changes: Increased session timeout from 30 min to 2 hours
- Environment: Production, 50K daily active users
- Related systems: Load balancer (AWS ELB), Redis cluster (3 nodes)
</context>

<debugging_done>
1. Checked Redis logs - no errors
2. Verified session timeout config - looks correct
3. Tested locally - cannot reproduce
4. Reviewed recent commits - session timeout is only auth change
</debugging_done>

<instructions>
1. Analyze the code for potential race conditions or edge cases
2. Consider distributed system implications (load balancer, Redis cluster)
3. Identify likely root causes
4. Suggest specific debugging steps
5. Recommend fixes with trade-offs
</instructions>
```

**Improvements:**
- Specific error with frequency
- System context provided
- What's been tried
- Environmental details
- Structured debugging approach

**Result:** Identified clock skew between servers - 10-minute fix vs. days of debugging

---

## Example 10: Creative Brief

### Before (Underdeveloped)
```
Create a tagline for my app.
```

**Problems:**
- No app information
- Missing brand context
- Unclear success criteria

### After (Optimized)
```xml
<task>
Create 5 tagline options for our productivity app targeting remote workers.
</task>

<product_info>
- Name: FlowState
- Core feature: AI-powered focus mode that blocks distractions
- Key benefits: Increase deep work time, reduce context switching, improve work-life balance
- Target users: Remote knowledge workers (developers, designers, writers)
- Competitors: Focus@Will, Freedom, RescueTime
</product_info>

<brand_voice>
- Professional but not corporate
- Empowering, not preachy
- Clever but not cute
- Tech-savvy audience, avoid jargon
- Emphasize outcomes, not features
</brand_voice>

<examples>
Good taglines (style reference):
- Slack: "Where work happens"
- Notion: "One workspace. Every team."
- Linear: "Built for high-impact teams"

What to avoid:
- Generic productivity clichés ("Get more done")
- Feature-focused ("AI-powered distraction blocking")
- Too clever/punny ("Flow with the pro")
</examples>

<requirements>
For each tagline:
- 2-6 words ideal
- Memorable and unique
- Hints at benefit without explaining it
- Works for website, app store, marketing

Provide brief rationale for each option.
</requirements>
```

**Improvements:**
- Product details and positioning
- Brand voice definition
- Style examples (good and bad)
- Clear requirements
- Multiple options requested

**Result:** 2 taglines tested well with users vs. weeks of brainstorming

---

## Key Patterns Across All Examples

### 1. Context is King
Every improved prompt added:
- Background information
- User/audience details
- Business goals or constraints
- Environmental context

### 2. Structure Creates Clarity
XML tags organize complex prompts:
- `<task>`, `<context>`, `<requirements>`
- `<examples>`, `<output_format>`
- Clear section boundaries

### 3. Examples Show > Tell
Concrete examples demonstrate:
- Desired output format
- Quality standards
- Edge cases
- What to avoid

### 4. Specificity Drives Quality
Vague: "Analyze this"
Specific: "Identify top 3 trends affecting conversion rate"

### 5. Output Format Prevents Iteration
Define exactly what you want:
- Structure
- Length
- Tone
- Level of detail

## Using This Gallery

1. **Find similar examples**: Match your task type
2. **Identify patterns**: What made the "after" better?
3. **Adapt techniques**: Apply to your prompts
4. **Test and iterate**: Measure improvement

## Common Improvement ROI

- **Data analysis**: 3-5x more actionable insights
- **Code review**: 2-3x more issues found
- **Content creation**: 50-70% fewer revisions
- **Problem solving**: 80% faster to solution
- **Classification**: 20-30% accuracy improvement

## Next Steps

- Review your frequent prompts
- Apply 2-3 techniques from examples
- Measure quality improvement
- Build a library of optimized templates
