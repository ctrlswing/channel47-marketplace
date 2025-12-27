# Prompt Enhancer Plugin: Usage Examples

## Overview

This guide demonstrates how to use the prompt-enhancer plugin effectively with real-world examples.

## Basic Usage

### Using the Skill

The primary way to use this plugin is through the `prompt-enhancer` skill:

```
Use /prompt-enhancer to help me improve my prompt for analyzing customer feedback
```

Claude will:
1. Ask about your task and requirements
2. Guide you through best practices
3. Help you structure your prompt effectively
4. Provide specific techniques and examples
5. Show before/after comparisons

### Using the Command

For quick prompt reviews:

```bash
/build-prompt "Analyze this sales data and find insights"
```

Claude will:
- Review your prompt structure
- Identify missing elements
- Suggest specific improvements
- Provide an enhanced version

## Usage Scenarios

### Scenario 1: Improving a Vague Prompt

**You have:**
```
"Write a report about our Q4 performance"
```

**You ask:**
```
Can you help me improve this prompt using /prompt-enhancer?
```

**Claude helps you transform it to:**
```xml
<context>
You are analyzing Q4 2024 performance for presentation to the board.
Company: B2B SaaS, 500 enterprise customers
Key metrics: MRR growth, churn rate, customer acquisition cost
</context>

<task>
Write an executive summary report analyzing Q4 performance.
</task>

<requirements>
- Length: 2-3 pages
- Audience: Board members (mix of technical and business backgrounds)
- Tone: Professional, data-driven, balanced (celebrate wins, acknowledge challenges)
- Focus areas:
  1. Revenue and growth metrics
  2. Customer acquisition and retention
  3. Operational efficiency
  4. Key challenges and risks
</requirements>

<data>
[Your Q4 metrics here]
</data>

<output_format>
## Executive Summary
[2-3 paragraphs]

## Key Metrics
- MRR: [value] ([% change] vs Q3)
- Churn: [value] ([trend])
- CAC: [value] ([trend])
- [Other key metrics]

## Highlights
[3-5 major wins]

## Challenges
[2-3 key challenges faced]

## Outlook
[Forward-looking assessment for Q1]
</output_format>
```

---

### Scenario 2: Building a Complex Analysis Prompt

**You need to:** Analyze multiple customer feedback sources and generate actionable insights

**You ask:**
```
I need help creating a prompt to analyze customer feedback from surveys, support tickets, and reviews. What's the best approach?
```

**Claude guides you through:**
1. Structuring your data sources
2. Defining analysis objectives
3. Setting output format
4. Adding constraints

**Final prompt:**
```xml
<context>
Analyzing customer feedback for our mobile banking app to inform Q1 product roadmap.
Sources: 500 NPS surveys, 1200 support tickets, 300 app store reviews (Nov-Dec 2024)
Goal: Identify top pain points and feature requests to prioritize
</context>

<data_sources>
<source type="nps_survey">
[Survey responses]
</source>

<source type="support_tickets">
[Ticket summaries]
</source>

<source type="app_reviews">
[Reviews]
</source>
</data_sources>

<analysis_objectives>
1. Identify top 5 pain points by frequency and severity
2. Extract top 5 feature requests
3. Analyze sentiment trends over the time period
4. Segment feedback by user type (new vs. existing, iOS vs. Android)
5. Flag any urgent issues requiring immediate attention
</analysis_objectives>

<output_format>
## Executive Summary
[2-3 sentences highlighting most critical findings]

## Top Pain Points
1. [Pain point]: [frequency %, severity, representative quotes]
2. [Pain point]: [frequency %, severity, representative quotes]
[...]

## Top Feature Requests
1. [Feature]: [request count, user segments requesting, business impact]
2. [Feature]: [request count, user segments requesting, business impact]
[...]

## Sentiment Analysis
- Overall sentiment: [positive/negative/neutral]
- Trend: [improving/declining/stable]
- Key drivers: [what's driving sentiment]

## Segment Insights
### New Users
[Specific patterns]

### Existing Users
[Specific patterns]

### iOS vs Android
[Any platform-specific issues]

## Urgent Issues
[Any critical problems requiring immediate attention]

## Recommendations
[Prioritized list of actions for product team]
</output_format>

<constraints>
- Base findings only on provided feedback
- Include data to support each finding (frequencies, percentages)
- Flag contradictions in feedback if present
- Distinguish between "nice to have" and "critical" issues
- Consider business impact alongside frequency
</constraints>
```

---

### Scenario 3: Code Review Prompt

**You ask:**
```
I need to review code for security issues. Help me create an effective prompt.
```

**Claude helps you build:**
```xml
<role>
You are a senior security engineer specializing in web application security.
You conduct thorough code reviews focused on identifying vulnerabilities before they reach production.
</role>

<code language="javascript" file="api/auth/login.js">
[Your code here]
</code>

<context>
This is the authentication endpoint for a fintech application handling sensitive financial data.
Recent changes: Migrated from JWT to session-based auth, added 2FA support
Security requirements: SOC 2 compliant, must prevent: SQL injection, XSS, CSRF, session hijacking
</context>

<review_criteria>
Evaluate for:
1. Authentication vulnerabilities (session fixation, weak session management)
2. Input validation and sanitization
3. Error handling and information leakage
4. Cryptography usage (hashing, encryption)
5. Rate limiting and brute force protection
6. OWASP Top 10 vulnerabilities
7. Secure coding best practices
</review_criteria>

<output_format>
## Security Risk Assessment
Overall risk: [Critical/High/Medium/Low]
Summary: [1-2 sentence assessment]

## Critical Issues
[Issues that could lead to immediate compromise]
- [Issue]:
  - Location: [file:line]
  - Risk: [description]
  - Exploit scenario: [how this could be exploited]
  - Fix: [specific remediation]

## High Priority Issues
[Issues that should be addressed before production]
[Same format as Critical]

## Medium Priority Issues
[Security improvements, best practice violations]
[Same format]

## Recommendations
1. [Immediate action items]
2. [Longer-term improvements]

## Positive Security Practices
[What's done well - for learning/morale]
</output_format>

<constraints>
- Focus on exploitable vulnerabilities, not just theoretical risks
- Provide specific remediation code examples
- Consider defense-in-depth: multiple layers of protection
- Flag any compliance issues (SOC 2, PCI DSS if applicable)
</constraints>
```

---

### Scenario 4: Content Creation

**You ask:**
```
Help me create a prompt for writing a technical blog post
```

**Result:**
```xml
<task>
Write a technical blog post about implementing rate limiting in REST APIs.
</task>

<context>
- Target audience: Backend developers (2-5 years experience)
- Publication: Company engineering blog
- Goal: Educate + showcase our engineering expertise
- Tone: Technical but accessible, practical focus, friendly/conversational
- SEO keywords: "rate limiting", "API rate limiting", "REST API best practices"
</context>

<requirements>
- Length: 1500-2000 words
- Include:
  - Why rate limiting matters (business + technical reasons)
  - Common rate limiting algorithms (token bucket, leaky bucket, fixed/sliding window)
  - Implementation example in Node.js or Python
  - Best practices and gotchas
  - Testing strategies
- Code examples: Clear, well-commented, production-ready quality
- Avoid: Overly academic theory, obscure algorithms, framework-specific details
</requirements>

<structure>
1. Hook (1-2 paragraphs)
   - Real-world scenario where lack of rate limiting caused problems
   - Why this matters to readers

2. Fundamentals (3-4 paragraphs)
   - What is rate limiting
   - When and why to implement it
   - Key concepts (rate, window, throttling)

3. Algorithms Explained (main section)
   - Fixed window: [explanation + pros/cons]
   - Sliding window: [explanation + pros/cons]
   - Token bucket: [explanation + pros/cons]
   - When to use each

4. Implementation Guide
   - Step-by-step implementation (choose token bucket)
   - Code walkthrough
   - Configuration considerations

5. Best Practices
   - Choosing appropriate limits
   - Error handling and user communication
   - Distributed systems considerations
   - Monitoring and alerting

6. Conclusion
   - Summary of key points
   - Call to action (engage with content)
</structure>

<examples>
Good code example:
```javascript
// Token bucket implementation
class RateLimiter {
  constructor(tokensPerInterval, interval) {
    this.tokens = tokensPerInterval;
    this.maxTokens = tokensPerInterval;
    this.interval = interval;

    setInterval(() => this.refill(), interval);
  }

  // Refill tokens at the specified interval
  refill() {
    this.tokens = this.maxTokens;
  }

  // Attempt to consume a token
  tryConsume() {
    if (this.tokens > 0) {
      this.tokens--;
      return true;
    }
    return false;
  }
}
```

Writing style example:
"Rate limiting is your API's bouncer – it decides who gets in and how fast. Without it, you're leaving the door open for abuse, accidents, and angry customers. Let's build a proper bouncer."
</examples>

<constraints>
- Keep code examples under 30 lines each
- Explain any technical terms on first use
- Use active voice
- Include practical warnings from real-world experience
- No marketing speak, stay technical but engaging
</constraints>
```

---

## Advanced Techniques

### Using On-Demand Resources

**During prompt enhancement, ask:**
```
"Can you show me the quick reference guide?"
```

Claude will load: `assets/reference/quick-reference.md`

**Or ask:**
```
"What are some common patterns I should consider?"
```

Claude will load: `assets/examples/common-patterns.md`

**Or ask:**
```
"Show me before/after examples similar to my task"
```

Claude will load: `assets/examples/before-after-gallery.md`

### Iterative Improvement

**Round 1:**
```
Help me improve this prompt: [your initial prompt]
```

**Round 2:**
```
The output was good but too generic. How can I make it more specific to my industry?
```

**Round 3:**
```
Can you add examples to make the format clearer?
```

### Template Customization

**Ask:**
```
I frequently need to analyze customer feedback. Can we create a reusable template?
```

Claude will:
1. Review your typical tasks
2. Build a custom template
3. Include your specific requirements
4. Save it for reuse

---

## Common Workflows

### Workflow 1: Quick Improvement

```
User: "/build-prompt 'Summarize this document'"

Claude: [Analyzes and suggests improvements]

User: [Implements suggestions]
```

**Time**: 2-3 minutes

---

### Workflow 2: Comprehensive Enhancement

```
User: "I need help building a prompt for [complex task]"

Claude: "Let me ask a few questions to understand your needs..."
- What's the task?
- Who's the audience?
- What format do you need?
- Any constraints?

User: [Answers questions]

Claude: [Builds comprehensive prompt using best practices]

User: "Can you explain why you structured it this way?"

Claude: [Explains rationale + provides relevant resources]
```

**Time**: 10-15 minutes

---

### Workflow 3: Template Building

```
User: "I need to create a reusable template for code reviews"

Claude: "Let's build a template together. What type of code reviews?"

User: "Security-focused reviews for our backend services"

Claude: [Creates specialized template]
[Explains customization points]
[Shows usage examples]

User: [Saves template for team]
```

**Time**: 15-20 minutes

---

## Tips for Best Results

### 1. Be Specific About Your Task
❌ "Help me write better prompts"
✅ "Help me create a prompt for analyzing customer survey data to identify product improvements"

### 2. Share Context
Tell Claude:
- What you're trying to accomplish
- Who the audience is
- Any constraints or requirements
- What good output looks like

### 3. Iterate
Don't expect perfection on first try:
- Start with a basic prompt
- Get Claude's suggestions
- Refine based on results
- Build your library over time

### 4. Ask Questions
- "Why did you suggest using XML tags here?"
- "What's the difference between few-shot and chain-of-thought?"
- "When should I use this pattern vs. that pattern?"

### 5. Request Examples
- "Can you show me a before/after for this type of task?"
- "What's an example of a well-structured data analysis prompt?"
- "Show me how to apply this pattern to my use case"

### 6. Save Successful Prompts
Build a library:
- Document what works for your common tasks
- Create team templates
- Note why certain patterns work well
- Share learnings with colleagues

---

## Troubleshooting

### Problem: Prompt is too long/complex

**Ask:**
```
"This prompt seems overly complicated. Can we simplify while keeping it effective?"
```

Claude will help you:
- Identify unnecessary sections
- Simplify structure
- Focus on essentials

---

### Problem: Output isn't matching expectations

**Ask:**
```
"The output is good but not quite what I need. The tone is too formal and it's missing specific examples. How should I adjust my prompt?"
```

Claude will:
- Diagnose the gap
- Suggest specific prompt modifications
- Show examples of better specifications

---

### Problem: Not sure which technique to use

**Ask:**
```
"I have [describe task]. Which prompt engineering techniques are most relevant?"
```

Claude will:
- Recommend specific patterns
- Explain why they fit your task
- Show how to combine them

---

## Learning Path

### Beginner (Week 1)
1. Use `/build-prompt` on your everyday prompts
2. Learn one pattern: Structured Output
3. Read: `quick-reference.md`

### Intermediate (Week 2-3)
1. Master few-shot learning and chain-of-thought
2. Study: `before-after-gallery.md`
3. Create your first template

### Advanced (Week 4+)
1. Combine multiple patterns
2. Build team template library
3. Explore: `xml-tag-library.md` and `new-techniques.md`
4. Teach others

---

## Integration with Workflows

### In Code Reviews
```bash
# Before reviewing code
/build-prompt "Review this authentication code for security issues: [paste code]"

# Use enhanced prompt
# Get detailed security analysis
```

### In Content Creation
```bash
# Before writing
/build-prompt "Write a blog post about [topic]"

# Refine with Claude's suggestions
# Get publication-ready content faster
```

### In Data Analysis
```bash
# Before analyzing data
/build-prompt "Analyze this sales data: [data]"

# Get structured, actionable insights
# Make better decisions
```

---

## Getting Help

### Ask for Specific Resources
```
"Show me the XML tag library"
"What are the 2025 techniques?"
"Give me templates for data analysis"
"Show me before/after examples"
```

### Ask for Explanations
```
"Why is structured output important?"
"When should I use chain-of-thought?"
"Explain the difference between context and background"
```

### Request Customization
```
"Adapt this template for my use case"
"How can I make this work for my industry?"
"Create a version for my team's needs"
```

---

## Success Metrics

Track your improvement:
- **Time to good output**: How many iterations needed?
- **Output quality**: Meeting requirements on first try?
- **Reusability**: Building a template library?
- **Team adoption**: Others using your templates?

---

## Next Steps

1. **Try it now**: Pick a prompt you use regularly and enhance it
2. **Measure results**: Compare output quality before/after
3. **Build library**: Save successful prompts as templates
4. **Share knowledge**: Help teammates write better prompts
5. **Keep learning**: Explore advanced techniques as you grow

---

## Additional Resources

Within the plugin:
- `/assets/reference/quick-reference.md` - One-page cheat sheet
- `/assets/reference/xml-tag-library.md` - Complete tag guide
- `/assets/reference/new-techniques.md` - 2025 advanced techniques
- `/assets/reference/claude-4x-tips.md` - Model-specific optimization
- `/assets/examples/before-after-gallery.md` - 10 transformation examples
- `/assets/examples/task-type-templates.md` - 7 ready-to-use templates
- `/assets/examples/common-patterns.md` - 8 essential patterns

---

## Community & Support

Have questions or want to share your success stories?
- Open issues on GitHub
- Share templates with the community
- Contribute improvements to the plugin

Happy prompting!
