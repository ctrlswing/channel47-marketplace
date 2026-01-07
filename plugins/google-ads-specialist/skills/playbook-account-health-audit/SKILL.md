---
name: playbook-account-health-audit
description: Comprehensive account health audit workflow analyzing account structure, campaign performance, budget allocation, and optimization opportunities. Includes GAQL queries, efficiency calculations, and risk assessment. Use when auditing customer health or conducting account reviews.
---

# Account Health Audit Playbook

This playbook guides you through a comprehensive Google Ads account health audit. Follow the checklist workflow to systematically analyze account performance and identify optimization opportunities.

## Workflow Checklist

Execute these steps in order, checking off each as completed:

- [ ] **Step 1**: List all accounts (understand account structure)
- [ ] **Step 2**: Campaign performance baseline (identify top/bottom performers)
- [ ] **Step 3**: Search terms analysis (find wasted spend)
- [ ] **Step 4**: Quality Score audit (identify QS issues)
- [ ] **Step 5**: Budget pacing check (find budget constraints)
- [ ] **Step 6**: Generate recommendations (prioritized action plan)

## Quick Start

### Step 1: List All Accounts

Use the `list_accounts` tool to understand the account structure:

```
Tool: list_accounts
Parameters: { "include_manager_accounts": false }
```

**What to look for:**
- Total number of accounts
- Account names and IDs for subsequent queries
- Manager account hierarchy (if applicable)

### Step 2: Campaign Performance Baseline

Use the `atomic-campaign-performance` skill to get an overview.

Run this query to establish performance baseline:
- Focus on last 30 days
- Sort by cost to see top spenders
- Note campaigns with high spend and low conversions

**Key Metrics to Capture:**
- Total spend
- Total conversions
- Average CPA
- Top 5 campaigns by spend
- Bottom 5 campaigns by performance

### Step 3: Search Terms Analysis

Use the `atomic-search-terms-report` skill to identify wasted spend.

**Focus Areas:**
- Terms with $50+ spend and zero conversions
- Low CTR terms (< 1%)
- Broad match keyword performance
- Brand name leakage

**Output:** List of 10-20 negative keyword candidates

### Step 4: Quality Score Audit

Use the `atomic-quality-score-audit` skill to find QS issues.

**Focus Areas:**
- Keywords with QS ≤ 5
- High-spend keywords with low QS
- Component weaknesses (CTR, ad relevance, landing page)

**Output:** Keywords grouped by weak component

### Step 5: Budget Pacing Check

Use the `atomic-budget-pacing` skill to analyze budget utilization.

**Focus Areas:**
- Campaigns losing impression share due to budget
- Campaigns consistently underspending
- Budget reallocation opportunities

**Output:** Budget recommendations (increase/decrease/reallocate)

### Step 6: Generate Recommendations

Synthesize findings into a prioritized action plan.

## Detailed Instructions

For step-by-step execution details, see [audit-workflow.md](audit-workflow.md)

For ready-to-use GAQL queries, see [query-patterns.md](query-patterns.md)

## Recommendation Framework

Prioritize recommendations based on:

### High Priority (Immediate Action)
- **Wasted Spend > $500/month**: Add negative keywords immediately
- **Budget-Constrained High Performers**: Increase budget for campaigns with good ROAS
- **Critical QS Issues**: Keywords with QS 1-3 and high spend (pause or fix urgently)

### Medium Priority (This Week)
- **Wasted Spend $100-500/month**: Add negatives, review weekly
- **Budget Reallocation**: Move budget from poor to strong performers
- **QS 4-6 Keywords**: Implement ad copy and landing page improvements

### Low Priority (This Month)
- **Minor Optimization**: Bid adjustments, ad copy testing
- **Wasted Spend < $100/month**: Monitor and review next month
- **Structural Changes**: Ad group reorganization, campaign restructuring

## Output Format

Structure your audit findings as:

### Executive Summary
- Total spend and conversions
- Account health score (1-10)
- Top 3 opportunities
- Estimated monthly savings

### Detailed Findings
- Campaign performance (top 5 and bottom 5)
- Wasted spend analysis (top 10 terms)
- Quality Score issues (grouped by component)
- Budget utilization (constrained vs underspending)

### Recommendations
- High priority actions (with expected impact)
- Medium priority actions
- Low priority actions

### Next Steps
- Immediate actions (this week)
- Short-term actions (this month)
- Long-term strategy (this quarter)

## Tips

- **Run the full audit monthly** for proactive optimization
- **Focus on high-impact items first** (large spend, clear problems)
- **Document baseline metrics** to measure improvement
- **Present findings with data** (screenshots, charts)
- **Estimate impact** of each recommendation in dollars
- **Get stakeholder buy-in** before making major changes
- **Track changes made** to measure results over time

## Common Findings

**Healthy Accounts:**
- QS 7+ on most keywords
- < 5% wasted spend
- Budget utilization 70-90%
- Clear conversion tracking
- Consistent optimization history

**Accounts Needing Attention:**
- QS < 5 on 20%+ of keywords
- > 15% wasted spend
- Budget constraints or severe underspending
- Stale ad copy (> 6 months old)
- No recent optimization activity
