---
name: adjust-bids
description: Modify bids for keywords, ad groups, or product groups using the mutate tool. Supports setting absolute values or percentage adjustments. Use when optimizing bids based on performance data or Quality Score changes.
---

# Adjust Bids

## Mutation Checklist

**IMPORTANT: Always follow this workflow when adjusting bids:**

- [ ] Identify keywords/ad groups to adjust (from performance analysis)
- [ ] Calculate new bid values
- [ ] Build operations array with resource IDs and new bids
- [ ] Run mutate tool with dry_run: true
- [ ] Review preview results with user
- [ ] Get explicit user confirmation
- [ ] Run mutate tool with dry_run: false
- [ ] Verify results

## Keyword Bid Adjustment

Use this mutation structure with the `mutate` tool:

```json
{
  "customer_id": "1234567890",
  "operations": [
    {
      "ad_group_criterion_operation": {
        "update": {
          "resource_name": "customers/1234567890/adGroupCriteria/111222333~444555666",
          "cpc_bid_micros": 2500000
        },
        "update_mask": "cpc_bid_micros"
      }
    }
  ],
  "dry_run": true
}
```

**Note:** Bid is in micros (2500000 = $2.50)

## Ad Group Bid Adjustment

```json
{
  "customer_id": "1234567890",
  "operations": [
    {
      "ad_group_operation": {
        "update": {
          "resource_name": "customers/1234567890/adGroups/111222333",
          "cpc_bid_micros": 3000000
        },
        "update_mask": "cpc_bid_micros"
      }
    }
  ],
  "dry_run": true
}
```

## Bulk Bid Adjustments

Adjust multiple bids in a single mutation:

```json
{
  "customer_id": "1234567890",
  "operations": [
    {
      "ad_group_criterion_operation": {
        "update": {
          "resource_name": "customers/1234567890/adGroupCriteria/111222333~444555666",
          "cpc_bid_micros": 2500000
        },
        "update_mask": "cpc_bid_micros"
      }
    },
    {
      "ad_group_criterion_operation": {
        "update": {
          "resource_name": "customers/1234567890/adGroupCriteria/111222333~777888999",
          "cpc_bid_micros": 1800000
        },
        "update_mask": "cpc_bid_micros"
      }
    }
  ],
  "dry_run": true
}
```

## Bid Calculation Strategies

### Based on Target CPA

If target CPA is $50 and current CPA is:
- $30 (below target): Increase bid by 20-30%
- $70 (above target): Decrease bid by 10-20%

### Based on Quality Score

- QS 8-10: Can bid more aggressively (higher CPCs, better positions)
- QS 5-7: Moderate bids
- QS 1-4: Lower bids or pause

### Based on Position

- Position 1-2: May be overpaying, test reducing 10-15%
- Position 3-4: Good balance
- Position 5+: Increase bids 20-30% if performance is good

### Percentage Adjustments

**Increase by 25%:**
```
New bid = current_bid * 1.25
Example: $2.00 * 1.25 = $2.50
```

**Decrease by 20%:**
```
New bid = current_bid * 0.80
Example: $2.00 * 0.80 = $1.60
```

## Common Bid Adjustment Scenarios

**High Performers (Good CPA, QS 7+):**
```
Action: Increase bids 20-30%
Goal: Capture more volume while maintaining efficiency
```

**Poor Performers (High CPA, QS < 5):**
```
Action: Decrease bids 30-50% or pause
Goal: Reduce waste while testing improvement
```

**Budget-Constrained Campaigns:**
```
Action: Decrease all bids 10-20%
Goal: Stretch budget across more clicks
```

**Underspending Campaigns:**
```
Action: Increase bids 20-40%
Goal: Increase visibility and volume
```

## Bid Limits

Set reasonable min/max bid limits:

**Minimum Bids:**
- Search campaigns: $0.50 - $1.00
- Shopping campaigns: $0.25 - $0.50

**Maximum Bids:**
- Based on target CPA: Usually 0.5-1.0x target CPA
- Based on conversion value: Usually 10-20% of AOV

## Tips

- **Always run dry_run: true first** - Preview bid changes before executing
- Make incremental changes (10-30% at a time)
- Wait 7-14 days between adjustments to see impact
- Adjust based on sufficient data (100+ impressions minimum)
- Monitor CPA and conversion volume after changes
- Use portfolio bid strategies for automated optimization when possible
- Document why bids were changed for future reference
- Review performance weekly and adjust as needed
- Consider seasonality and day-of-week patterns
- Convert currency to micros: amount * 1,000,000
