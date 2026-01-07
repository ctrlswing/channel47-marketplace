---
name: troubleshooting-gaql-errors
description: Troubleshoot common GAQL query errors, permission issues, and field validation problems. Includes error messages, root causes, and fixes. Use when encountering query errors or unexpected results from the query or mutate tools.
---

# Troubleshooting GAQL Errors

Common Google Ads Query Language errors and how to fix them.

## Syntax Errors

### Error: "Query must start with SELECT"

**Cause:** Query doesn't begin with SELECT keyword or contains mutation keywords.

**Fix:**
```sql
-- ❌ Wrong
FROM campaign WHERE ...

-- ✅ Correct
SELECT campaign.id, campaign.name FROM campaign WHERE ...
```

### Error: "Unexpected token at line X"

**Cause:** Missing comma, parenthesis, or quote.

**Common Issues:**
- Missing comma between fields
- Unclosed quotes in strings
- Missing closing parenthesis in IN clause

**Fix:**
```sql
-- ❌ Wrong (missing comma)
SELECT campaign.id campaign.name FROM campaign

-- ✅ Correct
SELECT campaign.id, campaign.name FROM campaign

-- ❌ Wrong (unclosed quote)
WHERE campaign.name = 'Test Campaign

-- ✅ Correct
WHERE campaign.name = 'Test Campaign'
```

## Field Validation Errors

### Error: "Field X does not exist"

**Cause:** Invalid field name or typo.

**Fix:**
- Check field name spelling (case-sensitive)
- Verify field exists for the resource type
- Check GAQL reference documentation

```sql
-- ❌ Wrong (typo)
SELECT campaign.nam FROM campaign

-- ✅ Correct
SELECT campaign.name FROM campaign
```

**Common Typos:**
- `campaign.nam` → `campaign.name`
- `metrics.cost` → `metrics.cost_micros`
- `metrics.conversion` → `metrics.conversions`

### Error: "Field X cannot be selected with field Y"

**Cause:** Incompatible field combinations. Some fields can't be queried together.

**Common Incompatibilities:**
- Segments fields with non-aggregated metrics
- Resource fields from different resource types
- Date segments with certain ad group fields

**Fix:**
Remove one of the incompatible fields or split into separate queries.

```sql
-- ❌ Wrong (incompatible combination)
SELECT
  segments.date,
  campaign.name,
  ad_group_criterion.keyword.text
FROM campaign

-- ✅ Correct (use keyword_view instead)
SELECT
  segments.date,
  campaign.name,
  ad_group_criterion.keyword.text
FROM keyword_view
```

### Error: "Field X requires segmentation by date"

**Cause:** Metrics field requires `segments.date` to be included.

**Fix:**
Add `segments.date` to SELECT clause and WHERE clause.

```sql
-- ❌ Wrong
SELECT
  campaign.name,
  metrics.cost_micros
FROM campaign

-- ✅ Correct
SELECT
  campaign.name,
  segments.date,
  metrics.cost_micros
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
```

## Resource and FROM Clause Errors

### Error: "Resource X does not exist"

**Cause:** Invalid resource name in FROM clause.

**Fix:**
Use correct resource name from GAQL reference.

**Common Resources:**
- `campaign`
- `ad_group`
- `ad_group_criterion` (for keywords)
- `keyword_view` (for keyword with metrics)
- `search_term_view`
- `campaign_criterion` (for campaign-level criteria)
- `shopping_performance_view`

```sql
-- ❌ Wrong
SELECT campaign.name FROM campaigns

-- ✅ Correct
SELECT campaign.name FROM campaign
```

### Error: "Cannot query X from resource Y"

**Cause:** Trying to query fields that don't belong to the resource.

**Fix:**
Switch to correct resource or use a view that includes both resources.

```sql
-- ❌ Wrong (can't get keyword from campaign resource)
SELECT
  campaign.name,
  ad_group_criterion.keyword.text
FROM campaign

-- ✅ Correct (use keyword_view)
SELECT
  campaign.name,
  ad_group_criterion.keyword.text
FROM keyword_view
```

## WHERE Clause Errors

### Error: "Operator X is not supported for field Y"

**Cause:** Using wrong operator for field type.

**Valid Operators by Type:**
- String fields: `=`, `!=`, `IN`, `NOT IN`, `LIKE`, `NOT LIKE`
- Numeric fields: `=`, `!=`, `>`, `<`, `>=`, `<=`, `IN`, `NOT IN`
- Enum fields: `=`, `!=`, `IN`, `NOT IN`

```sql
-- ❌ Wrong (LIKE on numeric field)
WHERE metrics.cost_micros LIKE '1000000'

-- ✅ Correct
WHERE metrics.cost_micros >= 1000000

-- ❌ Wrong (> on enum)
WHERE campaign.status > 'ENABLED'

-- ✅ Correct
WHERE campaign.status = 'ENABLED'
```

### Error: "DURING operator requires date literal"

**Cause:** Invalid date range format.

**Valid Date Ranges:**
- `TODAY`
- `YESTERDAY`
- `LAST_7_DAYS`
- `LAST_14_DAYS`
- `LAST_30_DAYS`
- `LAST_90_DAYS`
- `THIS_MONTH`
- `LAST_MONTH`

```sql
-- ❌ Wrong
WHERE segments.date DURING LAST_MONTH

-- ✅ Correct (use THIS_MONTH or LAST_MONTH)
WHERE segments.date DURING LAST_30_DAYS

-- For custom ranges, use BETWEEN
WHERE segments.date BETWEEN '2024-01-01' AND '2024-01-31'
```

## Permission Errors

### Error: "User does not have permission"

**Cause:** Insufficient account access or missing OAuth scopes.

**Fixes:**
1. Verify account access in Google Ads UI
2. Check if account is linked to MCC
3. Ensure OAuth token has correct scopes
4. Verify `GOOGLE_ADS_LOGIN_CUSTOMER_ID` is set correctly

### Error: "Customer not found" or "Invalid customer ID"

**Cause:** Wrong customer ID format or insufficient access.

**Fixes:**
- Customer ID should be 10 digits without dashes
- Verify ID in Google Ads UI (top right corner)
- If using MCC, set `login_customer_id` to MCC ID

```
-- ❌ Wrong
customer_id: "123-456-7890"

-- ✅ Correct
customer_id: "1234567890"
```

## Mutation Errors

### Error: "Mutation operations not allowed in query tool"

**Cause:** Trying to use CREATE, UPDATE, or REMOVE keywords in query tool.

**Fix:**
Use the `mutate` tool instead of `query` tool for write operations.

### Error: "dry_run validation failed"

**Cause:** Invalid mutation operation structure.

**Common Issues:**
- Missing required fields
- Invalid resource names
- Incorrect field values
- Constraint violations

**Fix:**
Review the error message details and fix the operation structure. Always test with `dry_run: true` first.

## Performance and Limit Errors

### Error: "Query exceeds maximum limit"

**Cause:** Requesting too many rows (max 10,000 per query).

**Fix:**
Add or reduce LIMIT clause.

```sql
-- ❌ May exceed limit
SELECT * FROM campaign WHERE segments.date DURING LAST_90_DAYS

-- ✅ Correct
SELECT * FROM campaign WHERE segments.date DURING LAST_90_DAYS LIMIT 1000
```

### Error: "Query timeout"

**Cause:** Query is too complex or requesting too much data.

**Fixes:**
- Add more specific WHERE filters
- Reduce date range
- Reduce number of fields selected
- Add LIMIT clause
- Break into smaller queries

## Common Pitfalls

### Micros Fields

**Remember:** Cost and bid fields are in micros (1/1,000,000 of currency unit).

```sql
-- To find campaigns spending more than $50:
WHERE metrics.cost_micros >= 50000000  -- Not 50!
```

### Status Filters

**Remember:** Include status filter to avoid REMOVED entities.

```sql
-- ✅ Always filter status
WHERE campaign.status IN ('ENABLED', 'PAUSED')
```

### Case Sensitivity

**Remember:** GAQL is case-sensitive for field names.

```sql
-- ❌ Wrong
SELECT Campaign.Name FROM campaign

-- ✅ Correct
SELECT campaign.name FROM campaign
```

## Debugging Tips

1. **Start simple:** Begin with basic query and add complexity gradually
2. **Check field names:** Verify exact spelling and case in GAQL reference
3. **Test with small date range:** Use LAST_7_DAYS for testing
4. **Add LIMIT:** Always include LIMIT during testing
5. **Read error messages carefully:** Google provides specific line/column numbers
6. **Check resource compatibility:** Ensure all fields belong to the FROM resource
7. **Validate resource names:** Use resource name format from mutations (customers/X/...)

## Reference Links

- [GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
- [GAQL Grammar](https://developers.google.com/google-ads/api/docs/query/grammar)
- [Field Compatibility](https://developers.google.com/google-ads/api/fields/v16/overview)
- [Google Ads API Errors](https://developers.google.com/google-ads/api/docs/errors)
