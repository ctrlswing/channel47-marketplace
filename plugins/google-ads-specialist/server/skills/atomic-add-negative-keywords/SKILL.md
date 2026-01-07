---
name: add-negative-keywords
description: Add negative keywords to campaigns or ad groups using the mutate tool. Supports campaign-level, ad group-level, and shared list negatives. Use when adding negatives from search terms analysis or preventing wasted spend.
---

# Add Negative Keywords

## Mutation Checklist

**IMPORTANT: Always follow this workflow when adding negative keywords:**

- [ ] Identify keywords to add (from search terms analysis)
- [ ] Build operations array with keyword text and match type
- [ ] Run mutate tool with dry_run: true
- [ ] Review preview results with user
- [ ] Get explicit user confirmation
- [ ] Run mutate tool with dry_run: false
- [ ] Verify results

## Campaign-Level Negative

Use this mutation structure with the `mutate` tool:

```json
{
  "customer_id": "1234567890",
  "operations": [
    {
      "campaign_criterion_operation": {
        "create": {
          "campaign": "customers/1234567890/campaigns/987654321",
          "negative": true,
          "keyword": {
            "text": "free",
            "match_type": "PHRASE"
          }
        }
      }
    }
  ],
  "dry_run": true
}
```

## Ad Group-Level Negative

```json
{
  "customer_id": "1234567890",
  "operations": [
    {
      "ad_group_criterion_operation": {
        "create": {
          "ad_group": "customers/1234567890/adGroups/111222333",
          "negative": true,
          "keyword": {
            "text": "free shipping",
            "match_type": "PHRASE"
          }
        }
      }
    }
  ],
  "dry_run": true
}
```

## Bulk Negative Keywords

Add multiple negatives in a single mutation:

```json
{
  "customer_id": "1234567890",
  "operations": [
    {
      "campaign_criterion_operation": {
        "create": {
          "campaign": "customers/1234567890/campaigns/987654321",
          "negative": true,
          "keyword": {
            "text": "free",
            "match_type": "PHRASE"
          }
        }
      }
    },
    {
      "campaign_criterion_operation": {
        "create": {
          "campaign": "customers/1234567890/campaigns/987654321",
          "negative": true,
          "keyword": {
            "text": "cheap",
            "match_type": "PHRASE"
          }
        }
      }
    },
    {
      "campaign_criterion_operation": {
        "create": {
          "campaign": "customers/1234567890/campaigns/987654321",
          "negative": true,
          "keyword": {
            "text": "coupon code",
            "match_type": "PHRASE"
          }
        }
      }
    }
  ],
  "dry_run": true
}
```

## Match Type Selection

Choose the right match type for your negative:

**EXACT Match:**
- Blocks only the exact keyword phrase
- Use for specific terms you want to exclude
- Example: "free trial" (exact) blocks only "free trial"

**PHRASE Match (Recommended):**
- Blocks the phrase and close variations
- Use for most negative keywords
- Example: "free trial" (phrase) blocks "free trial offer", "get free trial"

**BROAD Match:**
- Blocks broad matches and variations
- Use cautiously - may block too much
- Example: "free trial" (broad) blocks "trial free", "try for free"

## Common Patterns

**Brand Name Negatives:**
```
Match Type: EXACT or PHRASE
Examples: "nike", "adidas", "competitor brand"
```

**Question Keywords:**
```
Match Type: PHRASE
Examples: "how to", "what is", "why does"
```

**Job Search Terms:**
```
Match Type: PHRASE
Examples: "jobs", "careers", "hiring"
```

**Free/Cheap Seekers:**
```
Match Type: PHRASE
Examples: "free", "cheap", "discount", "coupon"
```

## Tips

- **Always run dry_run: true first** - Preview changes before executing
- Use PHRASE match for most negatives (balances coverage and precision)
- Add negatives at campaign level when they apply broadly
- Add at ad group level for more specific exclusions
- Review search terms report weekly for new negative opportunities
- Group similar negatives (all brand names, all question words, etc.)
- Consider shared negative lists for negatives used across many campaigns
- Document why negatives were added (helps future optimization)
- Re-check search terms after adding negatives to verify they're working
