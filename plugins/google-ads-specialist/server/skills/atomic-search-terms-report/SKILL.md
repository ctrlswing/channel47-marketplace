---
name: search-terms-report
description: Analyze actual search queries triggering your ads using the query tool. Essential for finding negative keyword opportunities and new keyword ideas. Returns search terms with performance, matched keyword, and match type. Use when identifying wasted spend or discovering keyword opportunities.
---

# Search Terms Report

## Basic Query

Use this GAQL query with the `query` tool to analyze search terms:

```sql
SELECT
  search_term_view.search_term,
  search_term_view.status,
  campaign.name,
  ad_group.name,
  ad_group_criterion.keyword.text,
  ad_group_criterion.keyword.match_type,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.ctr
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.impressions >= 10
ORDER BY metrics.cost_micros DESC
LIMIT 100
```

## Common Variations

### Filter by Minimum Thresholds

**High Spend Terms Only:**
```sql
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.cost_micros >= 50000000  -- $50 minimum
ORDER BY metrics.cost_micros DESC
```

**High Impression Terms:**
```sql
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.impressions >= 100
ORDER BY metrics.impressions DESC
```

### By Match Type

**Broad Match Terms Only:**
```sql
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.keyword.match_type = 'BROAD'
  AND metrics.impressions >= 10
```

**Non-Exact Match (Broad and Phrase):**
```sql
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.keyword.match_type IN ('BROAD', 'PHRASE')
```

### By Campaign or Ad Group

**Specific Campaign:**
```sql
WHERE campaign.id = '12345678'
  AND segments.date DURING LAST_30_DAYS
```

**Specific Ad Group:**
```sql
WHERE ad_group.id = '87654321'
  AND segments.date DURING LAST_30_DAYS
```

### Finding Negative Keyword Candidates

**Zero Conversions with Spend:**
```sql
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.cost_micros >= 10000000  -- $10 minimum
  AND metrics.conversions = 0
ORDER BY metrics.cost_micros DESC
```

**Low CTR Terms:**
```sql
WHERE segments.date DURING LAST_30_DAYS
  AND metrics.impressions >= 50
  AND metrics.ctr < 0.01  -- Less than 1% CTR
ORDER BY metrics.cost_micros DESC
```

## Match Type Analysis

Understanding match types helps identify negative keyword opportunities:

- **EXACT**: Search term matches keyword exactly - usually good performers
- **PHRASE**: Search term contains keyword phrase - monitor for irrelevant variations
- **BROAD**: Search term loosely related - highest risk for wasted spend

## Tips

- Set minimum impression threshold (10+) to filter noise
- Sort by cost to find expensive terms first
- Look for patterns in non-converting terms (brand names, questions, etc.)
- Compare search term to matched keyword to spot irrelevant matches
- Review broad match terms more carefully for negatives
- Use PHRASE match negatives for most cases (blocks variations)
- Cost is in micros (divide by 1,000,000 for actual value)
