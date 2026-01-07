---
name: campaign-performance
description: Query campaign metrics including cost, conversions, CTR, and impression share using the query tool. Returns performance data with date range and status filtering. Use when analyzing campaign performance or reviewing account spend.
---

# Campaign Performance Analysis

## Basic Query

Use this GAQL query with the `query` tool to get campaign performance metrics:

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  metrics.cost_micros,
  metrics.clicks,
  metrics.impressions,
  metrics.conversions,
  metrics.conversions_value,
  metrics.ctr,
  metrics.average_cpc,
  metrics.search_impression_share
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
LIMIT 50
```

## Common Variations

### By Date Range

**Last 7 Days:**
```sql
WHERE segments.date DURING LAST_7_DAYS
```

**Last 90 Days:**
```sql
WHERE segments.date DURING LAST_90_DAYS
```

**Custom Date Range:**
```sql
WHERE segments.date BETWEEN '2024-01-01' AND '2024-01-31'
```

### By Campaign Type

**Search Campaigns Only:**
```sql
WHERE campaign.advertising_channel_type = 'SEARCH'
  AND campaign.status = 'ENABLED'
```

**Shopping Campaigns Only:**
```sql
WHERE campaign.advertising_channel_type = 'SHOPPING'
  AND campaign.status = 'ENABLED'
```

**Performance Max:**
```sql
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND campaign.status = 'ENABLED'
```

### By Status

**All Campaigns (Enabled and Paused):**
```sql
WHERE campaign.status IN ('ENABLED', 'PAUSED')
```

**Include Removed:**
```sql
WHERE campaign.status IN ('ENABLED', 'PAUSED', 'REMOVED')
```

### Additional Metrics

**Add ROAS and CPA:**
```sql
SELECT
  campaign.id,
  campaign.name,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.cost_per_conversion,
  metrics.value_per_conversion
FROM campaign
WHERE campaign.status = 'ENABLED'
  AND segments.date DURING LAST_30_DAYS
ORDER BY metrics.conversions_value DESC
```

## Tips

- **Always filter out REMOVED campaigns** unless specifically analyzing historical data
- Use `metrics.*` fields for performance data (cost_micros, clicks, impressions, etc.)
- Order by relevant metric for easier analysis (cost, conversions, conversion_value)
- Combine with `segments.date` for trend analysis
- Cost is returned in micros (divide by 1,000,000 for actual currency value)
- Limit results to improve query performance and readability
- Filter by campaign.status = 'ENABLED' to see only active campaigns
