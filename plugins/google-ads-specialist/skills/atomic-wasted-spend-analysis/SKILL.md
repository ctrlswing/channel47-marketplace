---
name: wasted-spend-analysis
description: Identify search terms, keywords, or product groups burning budget without converting using the query tool. Returns high-spend, zero-conversion entities ranked by waste severity. Use when optimizing budget efficiency or finding quick wins to reduce wasted ad spend.
---

# Wasted Spend Analysis

## Basic Query - Search Terms

Use this GAQL query with the `query` tool to find wasted spend:

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
  metrics.conversions,
  metrics.ctr
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.cost_micros >= 50000000  -- $50 minimum spend
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

## Alternative Queries

### Keywords with Zero Conversions

```sql
SELECT
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  campaign.name,
  ad_group.name,
  metrics.cost_micros,
  metrics.clicks,
  metrics.impressions,
  metrics.conversions,
  metrics.ctr
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND metrics.cost_micros >= 50000000  -- $50 minimum
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

### Shopping Products with No Sales

```sql
SELECT
  segments.product_item_id,
  segments.product_title,
  campaign.name,
  metrics.cost_micros,
  metrics.clicks,
  metrics.impressions,
  metrics.conversions,
  metrics.conversions_value
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.cost_micros >= 20000000  -- $20 minimum
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

## Threshold Customization

Adjust cost thresholds based on your average CPA:

**If Average CPA is $25:**
```sql
AND metrics.cost_micros >= 50000000  -- 2x CPA = $50
```

**If Average CPA is $100:**
```sql
AND metrics.cost_micros >= 200000000  -- 2x CPA = $200
```

**Conservative (1x CPA):**
```sql
AND metrics.cost_micros >= 25000000  -- 1x CPA = $25
```

## Low Conversion Rate Analysis

Instead of zero conversions, find poor performers:

```sql
SELECT
  search_term_view.search_term,
  campaign.name,
  metrics.cost_micros,
  metrics.conversions,
  metrics.cost_per_conversion,
  metrics.ctr
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.conversions > 0
  AND metrics.conversions < 0.5  -- Less than 1 conversion
  AND metrics.cost_micros >= 50000000
ORDER BY metrics.cost_per_conversion DESC
```

## Prioritization Framework

When reviewing wasted spend results:

1. **Highest Priority**: $100+ spend, 0 conversions, multiple clicks
2. **High Priority**: $50-100 spend, 0 conversions
3. **Medium Priority**: $25-50 spend, 0 conversions
4. **Review Later**: <$25 spend (may not have enough data yet)

## Action Steps

After identifying wasted spend:

1. **Add as Negatives**: Use the `add-negative-keywords` skill for search terms
2. **Pause Keywords**: Consider pausing expensive non-performers
3. **Adjust Bids**: Use the `adjust-bids` skill to reduce bids on marginal performers
4. **Check Match Types**: Broad match keywords often generate most waste

## Tips

- Set minimum spend threshold based on your CPA (1-2x average)
- Review last 30-90 days for sufficient data
- Consider seasonality before marking as waste
- Low CTR often indicates relevance issues
- Broad match generates more wasted spend than exact/phrase
- Cost is in micros (divide by 1,000,000)
- Add negatives at phrase match to block variations
- Re-run weekly to catch new waste patterns
