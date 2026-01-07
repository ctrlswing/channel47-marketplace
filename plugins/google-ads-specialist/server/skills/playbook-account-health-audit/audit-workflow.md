# Account Health Audit Workflow

This document provides detailed step-by-step instructions for conducting a comprehensive Google Ads account health audit.

## Prerequisites

Before starting:
- Access to Google Ads account(s) via MCP server
- Last 30-90 days of performance data
- Baseline understanding of account goals (CPA target, ROAS target, etc.)
- Spreadsheet or document for capturing findings

## Step 1: Account Structure Analysis

**Objective:** Understand account organization and identify structural issues.

### Actions

1. **List all accounts:**
   ```
   Use list_accounts tool
   ```

2. **For each account, document:**
   - Account ID and name
   - Number of campaigns (estimate from campaign query)
   - Primary campaign types (Search, Shopping, Performance Max)
   - Account hierarchy (MCC structure if applicable)

3. **Run campaign count query:**
   ```sql
   SELECT
     campaign.advertising_channel_type,
     COUNT(campaign.id) as campaign_count
   FROM campaign
   WHERE campaign.status IN ('ENABLED', 'PAUSED')
   GROUP BY campaign.advertising_channel_type
   ```

4. **Identify structural red flags:**
   - Too many campaigns (> 20 for small accounts)
   - Too few campaigns (< 2 for accounts spending $5k+/month)
   - Duplicate campaign names
   - Unusual campaign types for the business

### Expected Output

Document with:
- Account hierarchy diagram
- Campaign count by type
- Initial structural observations

## Step 2: Campaign Performance Baseline

**Objective:** Identify top and bottom performing campaigns, establish performance benchmarks.

### Actions

1. **Use the atomic-campaign-performance skill** with 30-day window

2. **Run the baseline query and capture:**
   - Total spend across all campaigns
   - Total conversions
   - Calculated average CPA: `total_spend / total_conversions`
   - Top 5 campaigns by spend
   - Bottom 5 campaigns by conversion rate

3. **For each campaign in top 5, calculate:**
   - Spend percentage of total
   - CPA vs account average
   - ROAS (if conversion value tracked)
   - Impression share

4. **For bottom 5 campaigns, identify:**
   - Why are they underperforming? (low QS, poor targeting, budget issues)
   - Are they worth fixing or should they be paused?
   - How much could be saved by pausing?

5. **Benchmark calculations:**
   ```
   Account Average CPA = Total Spend / Total Conversions
   Good Campaign = CPA < 0.8 × Account Average
   Poor Campaign = CPA > 1.5 × Account Average
   ```

### Expected Output

Spreadsheet with:
- Campaign name, spend, conversions, CPA, performance rating
- Top 5 performers highlighted
- Bottom 5 flagged for review
- Account benchmarks (avg CPA, total spend, total conversions)

## Step 3: Search Terms Waste Analysis

**Objective:** Identify search terms burning budget without converting.

### Actions

1. **Use the atomic-search-terms-report skill** with 30-day window

2. **Run wasted spend query** (from atomic-wasted-spend-analysis skill):
   - Minimum spend threshold: 2x your average CPA
   - Zero conversions filter
   - Sort by cost descending

3. **For each high-waste term, document:**
   - Search term text
   - Total spend
   - Clicks and impressions
   - Matched keyword and match type
   - Campaign/ad group context

4. **Group wasted terms by pattern:**
   - Brand names (competitors)
   - Question keywords ("how to", "what is")
   - Job seekers ("jobs", "careers")
   - Free seekers ("free", "cheap", "discount")
   - Irrelevant variations

5. **Calculate total wasted spend:**
   ```
   Sum of cost for all terms with 0 conversions and spend > threshold
   ```

6. **Prioritize negatives:**
   - Tier 1: > $100 wasted per term
   - Tier 2: $50-100 wasted per term
   - Tier 3: $25-50 wasted per term

### Expected Output

List of negative keyword candidates with:
- Search term
- Spend wasted
- Recommended match type
- Campaign/ad group to apply
- Priority tier
- Total estimated monthly savings

## Step 4: Quality Score Deep Dive

**Objective:** Identify keywords with QS issues and determine root causes.

### Actions

1. **Use the atomic-quality-score-audit skill** with 30-day window

2. **Run QS query filtered for QS ≤ 6** with 100+ impressions

3. **For each low-QS keyword, capture:**
   - Keyword text and match type
   - Quality Score (1-10)
   - Component scores (Expected CTR, Ad Relevance, Landing Page)
   - Spend and conversions
   - Campaign and ad group

4. **Group keywords by weak component:**
   - **Poor Expected CTR:** Low click-through rate
   - **Poor Ad Relevance:** Keyword doesn't match ad copy
   - **Poor Landing Page:** Page not relevant or slow

5. **Calculate QS distribution:**
   ```
   % of keywords with QS 1-3: Critical
   % of keywords with QS 4-6: Needs improvement
   % of keywords with QS 7-10: Good
   ```

6. **Identify high-impact QS improvements:**
   - High spend + low QS = highest priority
   - Keywords spending > $100/month with QS ≤ 4

### Expected Output

QS improvement plan with:
- Keywords grouped by weak component
- High-priority keywords (high spend + low QS)
- Recommended actions per component
- Estimated CPC reduction from QS improvements

## Step 5: Budget Utilization Check

**Objective:** Identify budget-constrained and underspending campaigns.

### Actions

1. **Use the atomic-budget-pacing skill** with 7-day window

2. **Run budget pacing query** and capture for each campaign:
   - Daily budget (amount_micros / 1,000,000)
   - Actual 7-day spend
   - Average daily spend (7-day spend / 7)
   - Budget lost impression share
   - Search impression share

3. **Identify budget-constrained campaigns:**
   ```
   Constrained if:
   - search_budget_lost_impression_share > 10%
   OR
   - average_daily_spend ≥ 0.95 × daily_budget (consistently maxing out)
   ```

4. **Identify underspending campaigns:**
   ```
   Underspending if:
   - average_daily_spend < 0.5 × daily_budget
   AND
   - search_budget_lost_impression_share = 0
   ```

5. **Calculate reallocation opportunities:**
   - Sum unused budget from underspending campaigns
   - Compare to budget needs of constrained campaigns
   - Prioritize reallocation to campaigns with good ROAS/CPA

6. **Check overall account pacing:**
   ```
   Total 7-day spend × 30 / 7 = Projected monthly spend
   Compare to monthly budget or target
   ```

### Expected Output

Budget recommendation report with:
- Constrained campaigns (recommend increase)
- Underspending campaigns (recommend decrease or investigation)
- Reallocation opportunities
- Total budget optimization potential

## Step 6: Synthesis and Recommendations

**Objective:** Compile findings into actionable recommendations with prioritization.

### Actions

1. **Calculate total opportunity value:**
   ```
   Wasted spend savings: $X/month
   Budget reallocation impact: $Y/month additional revenue
   QS improvements: $Z/month CPC reduction
   Total potential monthly impact: $X + $Y + $Z
   ```

2. **Generate high-priority recommendations:**
   - Add negatives for terms with > $100 wasted
   - Increase budget for constrained high performers
   - Pause or fix critical QS keywords (QS 1-3 with high spend)

3. **Generate medium-priority recommendations:**
   - Add negatives for $50-100 waste
   - Reallocate budget from poor to strong performers
   - Implement QS improvements (ad copy, landing pages)

4. **Generate low-priority recommendations:**
   - Minor bid adjustments
   - Ad copy testing
   - Structural reorganization

5. **Create implementation timeline:**
   - Week 1: High-priority actions
   - Week 2-4: Medium-priority actions
   - Month 2-3: Low-priority actions

6. **Estimate impact of each recommendation:**
   - Expected monthly savings/revenue
   - Implementation effort (hours)
   - Risk level (low/medium/high)

### Expected Output

Executive summary with:
- Account health score (1-10)
- Total opportunity value
- Top 3-5 recommendations
- 30-day action plan
- 90-day strategic plan

## Quality Checks

Before finalizing the audit:

- [ ] All queries returned valid data (no errors)
- [ ] Calculations are accurate (spot-check CPA, percentages)
- [ ] Recommendations align with account goals
- [ ] High-priority items have clear next steps
- [ ] Impact estimates are realistic and conservative
- [ ] Stakeholders reviewed and approved recommendations

## Next Steps After Audit

1. **Present findings** to stakeholders with data
2. **Get approval** for high-priority changes
3. **Implement changes** starting with high priority
4. **Track results** weekly for 30 days
5. **Re-audit** after 30 days to measure improvement
6. **Schedule monthly audits** for ongoing optimization
