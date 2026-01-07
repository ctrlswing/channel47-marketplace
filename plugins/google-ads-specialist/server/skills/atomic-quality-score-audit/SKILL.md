---
name: quality-score-audit
description: Analyze Quality Score distribution and identify improvement opportunities using the query tool. Returns keywords with QS breakdown (expected CTR, ad relevance, landing page experience) and identifies weakest components. Use when improving ad relevance, CTR, or landing page experience.
---

# Quality Score Audit

## Basic Query

Use this GAQL query with the `query` tool to analyze Quality Score:

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
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions
FROM keyword_view
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND metrics.impressions >= 100
  AND ad_group_criterion.quality_info.quality_score <= 6
ORDER BY metrics.cost_micros DESC
LIMIT 200
```

## Quality Score Components

Quality Score ranges from 1-10 and is based on three components:

- **creative_quality_score**: Ad relevance (how well ad matches keyword)
- **post_click_quality_score**: Landing page experience (page quality and relevance)
- **search_predicted_ctr**: Expected CTR (how likely ad will be clicked)

Each component is rated: `BELOW_AVERAGE`, `AVERAGE`, or `ABOVE_AVERAGE`

## Common Variations

### Low Quality Score Only (4 or below)

```sql
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND metrics.impressions >= 100
  AND ad_group_criterion.quality_info.quality_score <= 4
```

### By Weak Component

**Poor Ad Relevance:**
```sql
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND ad_group_criterion.quality_info.creative_quality_score = 'BELOW_AVERAGE'
  AND metrics.impressions >= 50
```

**Poor Expected CTR:**
```sql
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND ad_group_criterion.quality_info.search_predicted_ctr = 'BELOW_AVERAGE'
  AND metrics.impressions >= 50
```

**Poor Landing Page:**
```sql
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND ad_group_criterion.quality_info.post_click_quality_score = 'BELOW_AVERAGE'
  AND metrics.impressions >= 50
```

### High Spend, Low QS

```sql
WHERE segments.date DURING LAST_30_DAYS
  AND ad_group_criterion.status = 'ENABLED'
  AND metrics.impressions >= 100
  AND ad_group_criterion.quality_info.quality_score <= 5
  AND metrics.cost_micros >= 10000000  -- $10 minimum
ORDER BY metrics.cost_micros DESC
```

## Improvement Actions by Component

**If Expected CTR is Below Average:**
- Improve ad copy relevance to keyword
- Add more specific keywords to ad headlines
- Test different ad variations
- Consider pausing if consistently low

**If Ad Relevance is Below Average:**
- Move keyword to more specific ad group
- Create dedicated ad group with targeted ad copy
- Ensure keyword appears in headline or description
- Review keyword-to-ad-group match

**If Landing Page is Below Average:**
- Ensure landing page content matches keyword intent
- Improve page load speed
- Add relevant content and clear CTAs
- Consider creating dedicated landing pages

## Tips

- Focus on keywords with 100+ impressions for reliable data
- QS 7+ is generally good, 5-6 needs improvement, 1-4 is critical
- Prioritize high-spend keywords for biggest impact
- All three components must be strong for high QS
- QS affects ad rank and CPC (higher QS = lower CPC)
- Re-check QS after making improvements (can take weeks to update)
- Consider pausing QS 1-3 keywords that don't improve
- Group findings by component to batch improvements
