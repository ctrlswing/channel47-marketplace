---
name: gaql-query-guide
description: Technical reference for constructing Google Ads Query Language (GAQL) queries - use when users need Google Ads data analysis
---

# GAQL Query Guide

Technical reference for constructing effective GAQL queries. Use this when helping users analyze Google Ads data.

## Query Syntax

```
SELECT [fields] FROM [resource] WHERE [conditions] ORDER BY [field] [ASC|DESC] LIMIT [n]
```

**Critical Rules:**
- Field compatibility: Not all fields can be selected together (segmentation restrictions)
- WHERE clause limitations: Not all fields are filterable
- Cost values are in micros (divide by 1,000,000 for display)
- Enums must use exact string values (e.g., 'ENABLED' not 'enabled')

## Common Resources

| Resource | Purpose | Key Fields |
|----------|---------|------------|
| `campaign` | Campaign-level data | campaign.id, campaign.name, campaign.status, campaign.advertising_channel_type |
| `ad_group` | Ad group performance | ad_group.id, ad_group.name, ad_group.status |
| `keyword_view` | Keyword performance with Quality Score | ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type, ad_group_criterion.quality_info.quality_score |
| `search_term_view` | Search query performance (negative keywords) | search_term_view.search_term, search_term_view.status, segments.keyword.info.text |
| `ad_group_ad` | Ad-level performance and policy status | ad_group_ad.ad.id, ad_group_ad.status, ad_group_ad.policy_summary.approval_status |
| `customer` | Account-level information | customer.id, customer.descriptive_name, customer.currency_code |

## Essential Metrics

**Performance:**
- `metrics.cost_micros` - Total cost in micros (÷ 1,000,000 for currency)
- `metrics.clicks` - Number of clicks
- `metrics.impressions` - Number of impressions
- `metrics.conversions` - Total conversions
- `metrics.conversions_value` - Conversion value in account currency
- `metrics.ctr` - Click-through rate (decimal, multiply by 100 for %)
- `metrics.average_cpc` - Average cost per click in micros

**Quality:**
- `ad_group_criterion.quality_info.quality_score` - Quality Score (1-10)
- `ad_group_criterion.quality_info.search_predicted_ctr` - Expected CTR component
- `ad_group_criterion.quality_info.creative_quality_score` - Ad relevance component
- `ad_group_criterion.quality_info.post_click_quality_score` - Landing page experience

## Date Filtering

**Always include date filtering** to scope queries:

**Predefined Ranges:**
```sql
WHERE segments.date DURING TODAY
WHERE segments.date DURING YESTERDAY
WHERE segments.date DURING LAST_7_DAYS
WHERE segments.date DURING LAST_14_DAYS
WHERE segments.date DURING LAST_30_DAYS
WHERE segments.date DURING THIS_MONTH
WHERE segments.date DURING LAST_MONTH
WHERE segments.date DURING LAST_BUSINESS_WEEK
WHERE segments.date DURING THIS_WEEK_SUN_TODAY
WHERE segments.date DURING THIS_WEEK_MON_TODAY
```

**Custom Date Range:**
```sql
WHERE segments.date BETWEEN '2024-01-01' AND '2024-01-31'
```

## Query Templates

### Campaign Performance
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
  metrics.conversions_value
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

### Keyword Analysis
```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  ad_group_criterion.quality_info.quality_score,
  metrics.cost_micros,
  metrics.clicks,
  metrics.conversions,
  metrics.ctr
FROM keyword_view
WHERE segments.date DURING LAST_7_DAYS
  AND ad_group_criterion.status = 'ENABLED'
ORDER BY metrics.cost_micros DESC
LIMIT 100
```

### Search Terms (Negative Keyword Discovery)
```sql
SELECT
  search_term_view.search_term,
  campaign.name,
  ad_group.name,
  segments.keyword.info.text,
  segments.keyword.info.match_type,
  metrics.cost_micros,
  metrics.clicks,
  metrics.conversions,
  metrics.conversions_value,
  metrics.impressions
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.cost_micros > 0
ORDER BY metrics.cost_micros DESC
LIMIT 500
```

**Critical for negative keywords:**
- Filter: `metrics.cost_micros > 0` to find spend
- Look for: `metrics.conversions = 0` with significant cost
- Match type helps determine negative keyword level (exact/phrase/broad)

### Ad Status Check
```sql
SELECT
  campaign.name,
  ad_group.name,
  ad_group_ad.ad.id,
  ad_group_ad.ad.name,
  ad_group_ad.status,
  ad_group_ad.policy_summary.approval_status,
  ad_group_ad.policy_summary.review_status
FROM ad_group_ad
WHERE segments.date DURING LAST_7_DAYS
  AND ad_group_ad.policy_summary.approval_status != 'APPROVED'
ORDER BY campaign.name, ad_group.name
```

### Account List
```sql
SELECT
  customer.id,
  customer.descriptive_name,
  customer.currency_code,
  customer.time_zone
FROM customer
WHERE customer.status = 'ENABLED'
ORDER BY customer.id
```

## Filters & Operators

**Comparison:**
- `=` Equal to
- `!=` Not equal to
- `>`, `<`, `>=`, `<=` Numeric comparison

**Multiple Values:**
```sql
WHERE campaign.status IN ('ENABLED', 'PAUSED')
WHERE campaign.advertising_channel_type IN ('SEARCH', 'SHOPPING')
```

**Combining Conditions:**
```sql
WHERE campaign.status = 'ENABLED'
  AND metrics.cost_micros > 10000000
  AND segments.date DURING LAST_30_DAYS
```

**Cost Thresholds:**
```sql
WHERE metrics.cost_micros > 50000000  -- $50
WHERE metrics.cost_micros >= 100000000  -- $100
```

## Field Compatibility Gotchas

**Segmentation Requirements:**
- Some resources require `segments.date` in both SELECT and WHERE
- `search_term_view` always requires date segmentation
- Mixing segment types can cause "incompatible fields" errors

**Resource-Specific Fields:**
- Quality Score fields only available from `keyword_view`
- Search term data only in `search_term_view`
- Policy information only in `ad_group_ad`
- Campaign type filtering uses `campaign.advertising_channel_type`

**Not All Fields Are Filterable:**
- Check error messages - some fields can only be selected, not filtered
- Use ORDER BY and LIMIT instead when filtering unavailable

## Performance Best Practices

1. **Always include date filtering** - Prevents scanning entire history
2. **Use ORDER BY with high-impact metrics** - Focus on cost or conversions
3. **Apply LIMIT** - Prevent overwhelming responses (50-500 typical)
4. **Filter by campaign/ad group when possible** - Reduces result set
5. **Streaming mode:**
   - `use_streaming: false` for small result sets (<1000 rows)
   - `use_streaming: true` for large exports (>1000 rows)

## Common Patterns for Analysis

**Find high-cost, low-conversion campaigns:**
```sql
WHERE metrics.cost_micros > 100000000
  AND metrics.conversions < 5
  AND campaign.status = 'ENABLED'
```

**Find poor Quality Score keywords:**
```sql
WHERE ad_group_criterion.quality_info.quality_score < 5
  AND metrics.impressions > 100
```

**Identify negative keyword candidates:**
```sql
WHERE metrics.cost_micros > 10000000
  AND metrics.conversions = 0
  AND search_term_view.status = 'ADDED'
```

## Micros Conversion

All cost values returned in micros (1/1,000,000):
- `metrics.cost_micros = 1234567` → $1.23
- `metrics.average_cpc = 500000` → $0.50
- Always divide by 1,000,000 when displaying to users

## Error Messages

**"Field cannot be selected with other fields"**
- Segmentation conflict - remove conflicting segment fields

**"Immutable field in WHERE clause"**
- Field can be selected but not filtered - use ORDER BY instead

**"Invalid date range"**
- Check date format: 'YYYY-MM-DD'
- Verify predefined range name is correct

**"Customer not found"**
- Verify customer_id format (10 digits, no dashes)
- Check user has access to the account
