---
name: budget-pacing
description: Check budget utilization and pacing across campaigns using the query tool. Returns daily spend rate, projected monthly spend, and limited by budget status. Use when monitoring budget allocation or identifying budget-constrained campaigns.
---

# Budget Pacing Analysis

## Basic Query

Use this GAQL query with the `query` tool to analyze budget pacing:

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign_budget.amount_micros,
  campaign_budget.period,
  metrics.cost_micros,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions,
  metrics.search_impression_share,
  metrics.search_budget_lost_impression_share
FROM campaign
WHERE segments.date DURING LAST_7_DAYS
  AND campaign.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
```

## Understanding Budget Fields

- **campaign_budget.amount_micros**: Daily budget in micros (divide by 1,000,000)
- **campaign_budget.period**: DAILY or MONTHLY budget type
- **metrics.search_budget_lost_impression_share**: % of impressions lost due to budget constraints
- **metrics.cost_micros**: Actual spend in the date range

## Calculating Pacing

To calculate if campaigns are on pace:

1. Get 7-day spend from query results
2. Calculate daily average: `cost_micros / 7 / 1,000,000`
3. Compare to `campaign_budget.amount_micros / 1,000,000`
4. If daily spend is consistently at budget limit, campaign is budget-constrained

## Common Variations

### Budget-Constrained Campaigns Only

```sql
WHERE segments.date DURING LAST_7_DAYS
  AND campaign.status = 'ENABLED'
  AND metrics.search_budget_lost_impression_share > 0.10  -- Losing 10%+ impressions
ORDER BY metrics.search_budget_lost_impression_share DESC
```

### Underspending Campaigns

```sql
WHERE segments.date DURING LAST_7_DAYS
  AND campaign.status = 'ENABLED'
  AND metrics.search_budget_lost_impression_share = 0
ORDER BY metrics.cost_micros ASC
```

### Monthly Budget View

For monthly budget planning:

```sql
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
```

Calculate projected monthly spend:
- Take 30-day total spend
- If partial month, prorate: `(spend / days_elapsed) * days_in_month`

## Budget Signals

**Campaign is Budget-Constrained if:**
- `search_budget_lost_impression_share > 10%`
- Daily spend consistently hits budget limit
- High search_impression_share but low absolute impressions

**Campaign is Underspending if:**
- Daily spend well below budget
- `search_budget_lost_impression_share = 0`
- Low CTR or Quality Score limiting ad delivery

## Action Steps

**For Budget-Constrained Campaigns:**
1. Increase budget if performance is good (positive ROI)
2. Reallocate budget from underspending campaigns
3. Adjust bids downward to stretch budget
4. Reduce keyword list or tighten targeting

**For Underspending Campaigns:**
1. Check if ads are disapproved or paused
2. Review Quality Score (low QS limits delivery)
3. Increase bids to be more competitive
4. Expand keyword targeting or match types
5. Consider reducing budget to match actual spend

## Tips

- Review pacing weekly to catch issues early
- Budget lost impression share indicates opportunity cost
- Consistently maxing daily budget means you could spend more profitably
- Underspending often indicates targeting or quality issues
- Consider shared budgets for campaign groups with variable demand
- Daily budgets can spend up to 2x on high-demand days
- Monthly budgets provide smoother pacing
