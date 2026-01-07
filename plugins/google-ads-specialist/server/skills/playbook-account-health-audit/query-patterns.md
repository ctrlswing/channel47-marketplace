# Account Health Audit Query Patterns

Ready-to-use GAQL queries for each step of the account health audit. Copy and paste these queries into the `query` tool.

## Step 1: Account Structure Queries

### Campaign Count by Type

```sql
SELECT
  campaign.advertising_channel_type,
  campaign.status,
  COUNT(campaign.id) as campaign_count
FROM campaign
GROUP BY campaign.advertising_channel_type, campaign.status
```

### Campaign List with Basic Info

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  campaign_budget.amount_micros
FROM campaign
WHERE campaign.status IN ('ENABLED', 'PAUSED')
ORDER BY campaign.name
```

## Step 2: Campaign Performance Queries

### Performance Baseline (30 Days)

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  metrics.cost_micros,
  metrics.clicks,
  metrics.impressions,
  metrics.conversions,
  metrics.conversions_value,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_per_conversion,
  metrics.value_per_conversion,
  metrics.search_impression_share
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

### Top Performers (Best CPA)

```sql
SELECT
  campaign.name,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion,
  metrics.conversions_value,
  metrics.value_per_conversion
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
  AND metrics.conversions > 5
ORDER BY metrics.cost_per_conversion ASC
LIMIT 10
```

### Bottom Performers (Worst CPA)

```sql
SELECT
  campaign.name,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion,
  metrics.clicks,
  metrics.ctr
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
  AND metrics.conversions > 0
ORDER BY metrics.cost_per_conversion DESC
LIMIT 10
```

### Zero Conversion Campaigns

```sql
SELECT
  campaign.name,
  metrics.cost_micros,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
  AND metrics.cost_micros >= 10000000
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
```

## Step 3: Search Terms Waste Queries

### High-Waste Search Terms ($50+ spend, 0 conversions)

```sql
SELECT
  search_term_view.search_term,
  campaign.name,
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.cost_micros,
  metrics.clicks,
  metrics.impressions,
  metrics.ctr
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.cost_micros >= 50000000
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

### Wasted Spend by Match Type

```sql
SELECT
  ad_group_criterion.keyword.match_type,
  SUM(metrics.cost_micros) as total_waste_micros,
  COUNT(DISTINCT search_term_view.search_term) as wasted_term_count
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.cost_micros >= 10000000
  AND metrics.conversions = 0
GROUP BY ad_group_criterion.keyword.match_type
ORDER BY total_waste_micros DESC
```

### Low CTR Search Terms

```sql
SELECT
  search_term_view.search_term,
  campaign.name,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.impressions >= 50
  AND metrics.ctr < 0.01
  AND metrics.cost_micros >= 10000000
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

## Step 4: Quality Score Queries

### Low Quality Score Keywords (QS ≤ 5)

```sql
SELECT
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.creative_quality_score,
  ad_group_criterion.quality_info.post_click_quality_score,
  ad_group_criterion.quality_info.search_predicted_ctr,
  campaign.name,
  ad_group.name,
  metrics.cost_micros,
  metrics.impressions,
  metrics.conversions
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND metrics.impressions >= 100
  AND ad_group_criterion.quality_info.quality_score <= 5
ORDER BY metrics.cost_micros DESC
LIMIT 100
```

### High-Spend Low QS Keywords (Critical)

```sql
SELECT
  ad_group_criterion.keyword.text,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.creative_quality_score,
  ad_group_criterion.quality_info.post_click_quality_score,
  ad_group_criterion.quality_info.search_predicted_ctr,
  campaign.name,
  metrics.cost_micros,
  metrics.clicks,
  metrics.conversions
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND metrics.impressions >= 100
  AND ad_group_criterion.quality_info.quality_score <= 4
  AND metrics.cost_micros >= 50000000
ORDER BY metrics.cost_micros DESC
```

### QS Distribution

```sql
SELECT
  ad_group_criterion.quality_info.quality_score,
  COUNT(ad_group_criterion.criterion_id) as keyword_count,
  SUM(metrics.cost_micros) as total_spend_micros
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND metrics.impressions >= 50
GROUP BY ad_group_criterion.quality_info.quality_score
ORDER BY ad_group_criterion.quality_info.quality_score DESC
```

### Keywords by Weak Component

**Poor Expected CTR:**
```sql
SELECT
  ad_group_criterion.keyword.text,
  campaign.name,
  ad_group.name,
  ad_group_criterion.quality_info.quality_score,
  metrics.cost_micros,
  metrics.ctr
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND ad_group_criterion.quality_info.search_predicted_ctr = 'BELOW_AVERAGE'
  AND metrics.impressions >= 50
ORDER BY metrics.cost_micros DESC
```

**Poor Ad Relevance:**
```sql
SELECT
  ad_group_criterion.keyword.text,
  campaign.name,
  ad_group.name,
  ad_group_criterion.quality_info.quality_score,
  metrics.cost_micros
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND ad_group_criterion.quality_info.creative_quality_score = 'BELOW_AVERAGE'
  AND metrics.impressions >= 50
ORDER BY metrics.cost_micros DESC
```

**Poor Landing Page:**
```sql
SELECT
  ad_group_criterion.keyword.text,
  campaign.name,
  ad_group.name,
  ad_group_criterion.quality_info.quality_score,
  metrics.cost_micros
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND ad_group_criterion.quality_info.post_click_quality_score = 'BELOW_AVERAGE'
  AND metrics.impressions >= 50
ORDER BY metrics.cost_micros DESC
```

## Step 5: Budget Pacing Queries

### Budget Utilization (7-Day Window)

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign_budget.amount_micros,
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

### Budget-Constrained Campaigns

```sql
SELECT
  campaign.name,
  campaign_budget.amount_micros,
  metrics.cost_micros,
  metrics.search_budget_lost_impression_share,
  metrics.search_impression_share,
  metrics.conversions,
  metrics.cost_per_conversion
FROM campaign
WHERE segments.date DURING LAST_7_DAYS
  AND campaign.status = 'ENABLED'
  AND metrics.search_budget_lost_impression_share > 0.10
ORDER BY metrics.search_budget_lost_impression_share DESC
```

### Underspending Campaigns

```sql
SELECT
  campaign.name,
  campaign_budget.amount_micros,
  metrics.cost_micros,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions
FROM campaign
WHERE segments.date DURING LAST_7_DAYS
  AND campaign.status = 'ENABLED'
  AND metrics.search_budget_lost_impression_share = 0
ORDER BY metrics.cost_micros ASC
LIMIT 20
```

## Bonus Queries

### Account-Level Summary

```sql
SELECT
  SUM(metrics.cost_micros) as total_cost_micros,
  SUM(metrics.conversions) as total_conversions,
  SUM(metrics.conversions_value) as total_conversion_value,
  SUM(metrics.clicks) as total_clicks,
  SUM(metrics.impressions) as total_impressions,
  AVG(metrics.ctr) as avg_ctr
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
```

### Daily Spend Trend

```sql
SELECT
  segments.date,
  SUM(metrics.cost_micros) as daily_cost_micros,
  SUM(metrics.conversions) as daily_conversions,
  SUM(metrics.clicks) as daily_clicks
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
GROUP BY segments.date
ORDER BY segments.date DESC
```

### Ad Group Performance

```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group.status,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion,
  metrics.ctr
FROM ad_group
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group.status = 'ENABLED'
  AND metrics.cost_micros >= 10000000
ORDER BY metrics.cost_micros DESC
LIMIT 50
```
