# Google Ads Plugin Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a complete Google Ads plugin with MCP server, negative keyword discovery agent, GAQL query guide skill, and interactive setup command for performance marketers.

**Architecture:** Copy and trim existing MCP server from `/Users/jackson/mcp/google_ads_mcp` to keep only 2 tools (list accounts, run GAQL). Create one agent for negative keyword discovery, one skill as GAQL reference for the LLM, and one setup command to guide credential configuration. All components use `${CLAUDE_PLUGIN_ROOT}` for portability.

**Tech Stack:** Python 3.10+, FastMCP, Google Ads API, Pydantic, OAuth 2.0

---

## Task 1: Set Up Plugin Structure

**Files:**
- Modify: `plugins/google-ads/.claude-plugin/plugin.json`
- Create: `plugins/google-ads/requirements.txt`
- Create: `plugins/google-ads/agents/.gitkeep`
- Create: `plugins/google-ads/skills/.gitkeep`
- Create: `plugins/google-ads/commands/.gitkeep`

**Step 1: Update plugin.json metadata**

```json
{
  "name": "google-ads",
  "version": "1.0.0",
  "description": "Query Google Ads data using GAQL with OAuth authentication",
  "author": {
    "name": "Jackson",
    "url": "https://channel47.dev"
  },
  "homepage": "https://channel47.dev/plugins/google-ads",
  "repository": "https://github.com/ctrlswing/channel47-marketplace",
  "mcp": {
    "configFile": ".mcp.json"
  },
  "requirements": {
    "python": ">=3.10"
  }
}
```

**Step 2: Create requirements.txt**

```txt
# Google Ads MCP Server Dependencies

# MCP Framework
mcp>=1.2.0

# Google Ads API
google-ads>=28.0.0

# Google Auth
google-auth>=2.32.0
google-auth-oauthlib>=1.2.0
google-auth-httplib2>=0.1.1

# Core dependencies
pydantic>=2.8
httpx>=0.27

# Optional but recommended
python-dotenv>=1.0.1

grpcio>=1.66.0
protobuf>=5.27.0
```

**Step 3: Create directory structure**

Run:
```bash
mkdir -p plugins/google-ads/agents
mkdir -p plugins/google-ads/skills
mkdir -p plugins/google-ads/commands
touch plugins/google-ads/agents/.gitkeep
touch plugins/google-ads/skills/.gitkeep
touch plugins/google-ads/commands/.gitkeep
```

Expected: Directories created

**Step 4: Commit**

```bash
git add plugins/google-ads/.claude-plugin/plugin.json plugins/google-ads/requirements.txt plugins/google-ads/agents/.gitkeep plugins/google-ads/skills/.gitkeep plugins/google-ads/commands/.gitkeep
git commit -m "feat(google-ads): initialize plugin structure with dependencies"
```

---

## Task 2: Copy and Trim MCP Server

**Files:**
- Create: `plugins/google-ads/src/google_ads_mcp.py`
- Verify: `plugins/google-ads/.mcp.json` (already exists)

**Step 1: Copy existing MCP server**

Run:
```bash
cp /Users/jackson/mcp/google_ads_mcp/src/google_ads_mcp.py plugins/google-ads/src/google_ads_mcp.py
```

Expected: File copied (1,714 lines)

**Step 2: Remove specialized input models**

Remove these classes from google_ads_mcp.py (lines ~460-690):
- `CampaignPerformanceInput`
- `KeywordPerformanceInput`
- `SearchTermsInput`
- `AdStatusQueryInput`
- All specialized enums: `CampaignStatus`, `CampaignType`, `AdServingStatus`, `AdApprovalStatus`, `SortOrder`

Keep: `DateRange`, `ResponseFormat`, `RunGoogleAdsGaqlInput`, `ListAccountsInput`

**Step 3: Remove specialized tool functions**

Remove these @mcp.tool functions (lines ~993-1704):
- `campaign_performance`
- `keyword_performance`
- `search_terms`
- `ad_status_overview`
- `describe_google_ads_resource`
- `list_google_ads_resources`

Keep only:
- `run_google_ads_gaql` (lines ~705-742)
- `google_ads_list_accounts` (lines ~755-833)

**Step 4: Verify trimmed file**

Run:
```bash
wc -l plugins/google-ads/src/google_ads_mcp.py
```

Expected: Approximately 750-800 lines (removed ~950 lines)

Run:
```bash
grep -c "@mcp.tool" plugins/google-ads/src/google_ads_mcp.py
```

Expected: 2 (only list_accounts and run_gaql)

**Step 5: Test MCP server loads**

Run:
```bash
cd plugins/google-ads
python -c "import src.google_ads_mcp; print('MCP server loaded successfully')"
```

Expected: "MCP server loaded successfully" (no import errors)

**Step 6: Commit**

```bash
git add plugins/google-ads/src/google_ads_mcp.py
git commit -m "feat(google-ads): add trimmed MCP server with 2 core tools"
```

---

## Task 3: Copy Setup Scripts

**Files:**
- Create: `plugins/google-ads/scripts/generate_refresh_token.py`
- Create: `plugins/google-ads/scripts/test_auth.py`

**Step 1: Copy token generation script**

Run:
```bash
cp /Users/jackson/mcp/google_ads_mcp/scripts/generate_refresh_token.py plugins/google-ads/scripts/
```

Expected: Script copied

**Step 2: Copy auth test script**

Run:
```bash
cp /Users/jackson/mcp/google_ads_mcp/scripts/test_auth.py plugins/google-ads/scripts/
```

Expected: Script copied

**Step 3: Verify scripts work**

Run:
```bash
python plugins/google-ads/scripts/test_auth.py --help 2>&1 | head -1
```

Expected: Script runs (may show error about missing env vars, which is OK)

**Step 4: Commit**

```bash
git add plugins/google-ads/scripts/
git commit -m "feat(google-ads): add OAuth setup and testing scripts"
```

---

## Task 4: Create GAQL Query Guide Skill

**Files:**
- Create: `plugins/google-ads/skills/gaql-query-guide/skill.md`

**Step 1: Create skill directory**

Run:
```bash
mkdir -p plugins/google-ads/skills/gaql-query-guide
```

Expected: Directory created

**Step 2: Write skill content**

Create `plugins/google-ads/skills/gaql-query-guide/skill.md`:

```markdown
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
```

**Step 3: Verify skill file**

Run:
```bash
cat plugins/google-ads/skills/gaql-query-guide/skill.md | head -5
```

Expected: Shows frontmatter with name and description

**Step 4: Commit**

```bash
git add plugins/google-ads/skills/gaql-query-guide/
git commit -m "feat(google-ads): add GAQL query guide skill for LLM reference"
```

---

## Task 5: Create Negative Keyword Hunter Agent

**Files:**
- Create: `plugins/google-ads/agents/negative-keyword-hunter/agent.md`

**Step 1: Create agent directory**

Run:
```bash
mkdir -p plugins/google-ads/agents/negative-keyword-hunter
```

Expected: Directory created

**Step 2: Write agent content**

Create `plugins/google-ads/agents/negative-keyword-hunter/agent.md`:

```markdown
---
name: negative-keyword-hunter
description: Analyze search terms to identify negative keyword opportunities and wasted spend
triggerWords:
  - negative keywords
  - wasted spend
  - search terms analysis
  - negative keyword opportunities
  - search term performance
color: red
tools:
  - run_google_ads_gaql
  - google_ads_list_accounts
---

# Negative Keyword Hunter Agent

You are a specialized agent for identifying negative keyword opportunities in Google Ads campaigns. Your goal is to analyze search term performance and recommend negative keywords to add, prioritizing by wasted spend.

## Workflow

### Step 1: Discover Customer Account

If customer_id not provided by user:
1. Use `google_ads_list_accounts` tool to list all accessible accounts
2. Present list to user with account names and IDs
3. Ask: "Which account would you like to analyze?"
4. Store the customer_id for subsequent queries

### Step 2: Gather Analysis Parameters

Ask the user:
1. **Date range** - Default: LAST_30_DAYS (options: LAST_7_DAYS, LAST_14_DAYS, LAST_30_DAYS, LAST_MONTH)
2. **Minimum spend threshold** - Default: $10 (filter out search terms below this cost)
3. **Campaign filter** (optional) - Specific campaign ID to analyze, or "all campaigns"

### Step 3: Query Search Term Performance

Use the GAQL query guide skill (@gaql-query-guide) to construct the query.

Execute this GAQL query using `run_google_ads_gaql` tool:

```sql
SELECT
  search_term_view.search_term,
  campaign.id,
  campaign.name,
  ad_group.id,
  ad_group.name,
  segments.keyword.info.text,
  segments.keyword.info.match_type,
  metrics.cost_micros,
  metrics.clicks,
  metrics.conversions,
  metrics.conversions_value,
  metrics.impressions,
  metrics.ctr
FROM search_term_view
WHERE segments.date DURING [DATE_RANGE]
  AND metrics.cost_micros > [THRESHOLD_MICROS]
ORDER BY metrics.cost_micros DESC
LIMIT 500
```

**Note:** Convert threshold to micros (multiply by 1,000,000). Example: $10 → 10000000

If campaign filter provided, add:
```sql
  AND campaign.id = [CAMPAIGN_ID]
```

**Parameters:**
- Set `use_streaming: false` (result set typically <500 rows)
- Parse JSON response from tool

### Step 4: Analyze Results

For each search term in results, calculate:

1. **Cost** = metrics.cost_micros ÷ 1,000,000
2. **Conversions** = metrics.conversions
3. **Conversion Value** = metrics.conversions_value
4. **CVR** = (conversions ÷ clicks) × 100 if clicks > 0, else 0
5. **ROAS** = conversion_value ÷ cost if cost > 0, else None

**Identify negative keyword candidates** if any of these conditions are met:
- **Zero conversions** with cost ≥ threshold
- **Very low CVR** (<0.5%) AND cost ≥ threshold × 2
- **ROAS** < 1.0 (optional, only if conversion value is tracked)

For each candidate, capture:
- Search term
- Matched keyword
- Match type (helps determine negative keyword level)
- Campaign name
- Ad group name
- Cost (wasted spend)
- Clicks
- Conversions
- Recommendation (campaign-level negative, ad group-level negative, or phrase match negative)

### Step 5: Present Recommendations

Generate a markdown report with this structure:

```markdown
# Negative Keyword Opportunities

**Account:** [customer_id]
**Period:** [date_range]
**Minimum Spend:** $[threshold]
**Total Search Terms Analyzed:** [count]
**Negative Keyword Candidates:** [candidate_count]
**Total Wasted Spend:** $[sum_of_candidate_costs]

---

## Executive Summary

- Found [candidate_count] search terms with $[wasted_spend] in wasted budget
- Top opportunity: "[top_term]" wasted $[cost] with zero conversions
- Estimated monthly savings if implemented: $[projected_savings]

---

## High Priority (>$50 wasted)

[For each candidate with cost > $50, grouped by campaign:]

### Campaign: [campaign_name]

**Total Wasted in Campaign:** $[campaign_total]

#### 1. "[search_term]"
- **Wasted Spend:** $[cost]
- **Clicks:** [clicks] | **Conversions:** [conversions]
- **Matched Keyword:** [keyword_text] ([match_type])
- **Ad Group:** [ad_group_name]
- **Recommendation:** Add as [campaign/ad group/phrase match] negative keyword
- **Rationale:** [Zero conversions with significant spend / Low CVR with high cost]

[Continue for all high-priority candidates...]

---

## Medium Priority ($10-$50 wasted)

[Same structure as above, for candidates with $10-$50 spend]

---

## Implementation Guide

To add these negative keywords:

1. **Campaign-level negatives:** Apply to entire campaign (recommended for brand/irrelevant terms)
2. **Ad group-level negatives:** Apply only to specific ad group (for granular control)
3. **Match types:**
   - Exact match negative: [search term] - blocks only this exact query
   - Phrase match negative: "search term" - blocks queries containing this phrase
   - Broad match negative: search term - blocks related variations

**Priority order:** Start with high-priority candidates (>$50 wasted) first for maximum impact.

---

## Next Steps

1. Review recommendations above
2. Verify terms are truly irrelevant (check landing pages, business goals)
3. Add negatives in Google Ads UI or via API
4. Re-run this analysis in 7 days to measure impact
5. Consider adding regex patterns for common irrelevant terms
```

**Output Format:**
- Use markdown for readability
- Bold key metrics
- Group by campaign for easy implementation
- Sort by wasted spend (highest first)
- Limit to top 50 candidates to avoid overwhelming output

### Step 6: Offer Follow-Up Actions

After presenting the report, ask:

"Would you like me to:
1. Export this list as CSV for bulk upload to Google Ads?
2. Analyze a different campaign or date range?
3. Drill deeper into a specific search term pattern?
4. Generate a GAQL query to add these as negative keywords via API?"

## Edge Cases

**No search term data:**
- "No search term data found for this period. This could mean:
  - Account is too new (needs at least 7 days of data)
  - No Search campaigns are running
  - Search campaigns have no impressions/clicks"

**All search terms converting:**
- "Great news! All search terms above the $[threshold] threshold are converting. Your targeting appears to be very efficient."

**Very large result set:**
- If >500 candidates, focus report on top 50 by wasted spend
- Mention: "Showing top 50 of [total_count] candidates. Recommend starting with these highest-impact opportunities."

## Success Metrics

Track these for the user:
- Number of negative keyword candidates identified
- Total wasted spend recovered
- Average cost per wasted search term
- Campaign(s) with highest waste

## Remember

- Convert all cost values from micros (÷ 1,000,000) for display
- Match type determines negative keyword level (broad match keywords need broader negatives)
- Focus on high-impact terms first (>$50 wasted)
- Provide actionable recommendations, not just data
- Group by campaign for easier implementation
```

**Step 3: Verify agent file**

Run:
```bash
cat plugins/google-ads/agents/negative-keyword-hunter/agent.md | head -10
```

Expected: Shows frontmatter with name, description, triggerWords, color, tools

**Step 4: Commit**

```bash
git add plugins/google-ads/agents/negative-keyword-hunter/
git commit -m "feat(google-ads): add negative keyword hunter agent"
```

---

## Task 6: Create Interactive Setup Command

**Files:**
- Create: `plugins/google-ads/commands/setup.md`

**Step 1: Write command content**

Create `plugins/google-ads/commands/setup.md`:

```markdown
---
description: Interactive guide for setting up Google Ads API credentials
---

# Google Ads Setup Wizard

This command guides you through configuring OAuth credentials for the Google Ads plugin.

## Phase 1: Prerequisites Check

First, let me verify your environment:

**Checking Python version...**

Run: `python3 --version`

Expected: Python 3.10 or higher

If Python not found or version too old:
- Install Python 3.10+ from https://python.org
- Restart Claude Code after installation

**Checking plugin dependencies...**

Run: `pip show google-ads mcp pydantic 2>/dev/null | grep Name`

If any missing:
```bash
pip install -r ${CLAUDE_PLUGIN_ROOT}/requirements.txt
```

Expected: All dependencies installed successfully

**Checking setup scripts...**

Run: `ls ${CLAUDE_PLUGIN_ROOT}/scripts/*.py`

Expected: Shows generate_refresh_token.py and test_auth.py

---

## Phase 2: Google Cloud Project Setup

I'll walk you through setting up your Google Cloud project and OAuth credentials.

### Have you created a Google Cloud project?

**If NO:**
1. Go to https://console.cloud.google.com/
2. Click "Select a project" → "New Project"
3. Name it (e.g., "Google Ads API")
4. Click "Create"

**If YES:** ✓ Great, let's continue.

### Have you enabled the Google Ads API?

**If NO:**
1. In Google Cloud Console, go to "APIs & Services" → "Library"
2. Search for "Google Ads API"
3. Click on it and press "Enable"
4. Wait for enablement to complete

**If YES:** ✓ API is ready.

### Have you created OAuth 2.0 credentials?

**If NO:**
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. If prompted, configure OAuth consent screen:
   - User type: External
   - App name: "Google Ads MCP"
   - User support email: your email
   - Developer contact: your email
   - Click "Save and Continue" through remaining screens
   - **Important:** Publish the app (don't leave in Testing mode or tokens expire in 7 days)
4. Back to Create OAuth client ID:
   - Application type: "Desktop app"
   - Name: "Google Ads MCP Client"
   - Click "Create"
5. **Download JSON** - Click "DOWNLOAD JSON" button
6. Save file as `client_secrets.json`

**If YES:** ✓ You should have a client_secrets.json file.

### Where did you save client_secrets.json?

Please provide the full path to your client_secrets.json file:

**[Wait for user input]**

**Validating file...**

Run: `test -f "[USER_PROVIDED_PATH]" && echo "File exists" || echo "File not found"`

Expected: "File exists"

**Copying to plugin scripts directory...**

Run: `cp "[USER_PROVIDED_PATH]" ${CLAUDE_PLUGIN_ROOT}/scripts/client_secrets.json`

Expected: File copied successfully

---

## Phase 3: Google Ads Developer Token

### Do you have a Google Ads developer token?

**If NO:**
1. Sign in to your Google Ads **MCC (Manager) account**
2. Click "Tools & Settings" (wrench icon)
3. Under "Setup", click "API Center"
4. Apply for developer token
5. Fill out the application form
6. **Important:** You need at least "Basic" access for production use
7. Wait for approval (can take 1-2 business days)

**If YES:** ✓ Great!

### What is your developer token?

Paste your developer token here:

**[Wait for user input]**

**Validating format...**

Basic validation: Token should be alphanumeric, typically 22 characters

**Stored temporarily:** dev_tok...*** (last 3 chars masked)

---

## Phase 4: MCC Account ID

### What is your MCC (Manager) account ID?

Your MCC account ID is found in Google Ads:
- Top right corner, click on the customer ID
- Look for the Manager account (has sub-accounts beneath it)
- Format: 123-456-7890 or 1234567890

Paste your MCC account ID here:

**[Wait for user input]**

**Validating format...**

Expected: 10 digits (dashes optional)

**Formatted:** [1234567890] (dashes removed)

---

## Phase 5: Generate Refresh Token

Now I'll run the OAuth flow to generate a refresh token.

**About to run:** `python ${CLAUDE_PLUGIN_ROOT}/scripts/generate_refresh_token.py`

This script will:
1. Open a URL for you to authorize the app
2. Redirect you to a URL after authorization
3. Ask you to paste that redirect URL back

**Ready? Let's start the OAuth flow.**

Run: `cd ${CLAUDE_PLUGIN_ROOT}/scripts && python generate_refresh_token.py`

**Follow the instructions in the terminal:**

1. Copy the URL that appears
2. Open it in your browser
3. Sign in with the Google account that has access to your MCC
4. Click "Allow" to grant permissions
5. You'll be redirected to a URL starting with `http://localhost` or `urn:ietf:wg:oauth:2.0:oob`
6. Copy the ENTIRE redirect URL
7. Paste it back into the terminal

**Expected output:**
```
Your refresh token is: 1//0abc123...xyz
```

**Refresh token generated successfully!**

Stored temporarily: 1//...*** (masked)

---

## Phase 6: Configuration Summary

Here's your complete Google Ads configuration:

```
Developer Token:     dev_tok...***
MCC Account ID:      1234567890
Client ID:           123...apps.googleusercontent.com
Client Secret:       GOC...***
Refresh Token:       1//...***
```

**These credentials will be saved to your Claude Code settings.**

---

## Phase 7: Save to Settings

I'll guide you to save these environment variables.

### Where do you want to save these credentials?

**Options:**

1. **User-level** (recommended) - `~/.claude/settings.json`
   - Available to all projects on this machine
   - Best for personal use

2. **Project-level** - `.claude/settings.json`
   - Shared with team via git (⚠️ NOT recommended for secrets)
   - Use this only for non-sensitive project settings

3. **Local project** - `.claude/settings.local.json`
   - This project only, this machine only
   - Not shared via git (gitignored)
   - Good for project-specific secrets

**Your choice:** [Wait for user input: user/project/local]

**Based on your choice, add these to your settings file:**

File to edit: `~/.claude/settings.json` (or project/local based on choice)

Add this JSON (merge with existing content if file exists):

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "[ACTUAL_TOKEN]",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "[ACTUAL_MCC_ID]",
    "GOOGLE_ADS_CLIENT_ID": "[ACTUAL_CLIENT_ID]",
    "GOOGLE_ADS_CLIENT_SECRET": "[ACTUAL_CLIENT_SECRET]",
    "GOOGLE_ADS_REFRESH_TOKEN": "[ACTUAL_REFRESH_TOKEN]"
  }
}
```

**Would you like me to open the settings file for you?**

If YES:
Run: `code ~/.claude/settings.json` (or other editor based on availability)

If NO:
"Please manually edit the file at [path] and add the JSON above."

**After you've saved the settings file, respond with 'done'.**

[Wait for user confirmation]

---

## Phase 8: Verification

**Important: Restart Claude Code now for settings to take effect.**

After restarting, let's verify your configuration works:

Run: `cd ${CLAUDE_PLUGIN_ROOT}/scripts && python test_auth.py`

**Expected output:**
```
✓ Authentication successful!
✓ Connected to Google Ads API
✓ MCC Account: [Your MCC Name] (1234567890)
```

**If successful:**
```
🎉 Setup complete! Your Google Ads plugin is ready to use.

Try it out:
- "List my Google Ads accounts"
- "Find negative keyword opportunities for account 1234567890"
```

**If failed:**

Common issues and fixes:

### Error: "invalid_grant"
**Cause:** Refresh token is invalid or expired
**Fix:**
- Re-run this setup wizard: `/setup`
- Make sure OAuth consent screen is "Published" (not "Testing")
- Testing mode tokens expire after 7 days

### Error: "invalid_client"
**Cause:** Client ID or Client Secret is incorrect
**Fix:**
- Double-check these values in Google Cloud Console
- Re-run setup wizard and carefully copy credentials

### Error: "Developer token only approved for test accounts"
**Cause:** Developer token has Test access, not Basic/Standard
**Fix:**
- Go to Google Ads API Center
- Apply for Basic or Standard access
- Wait for approval

### Error: "Permission denied"
**Cause:** Authenticated user doesn't have access to MCC account
**Fix:**
- Verify MCC account ID is correct
- Ensure the Google account you authorized has at least Read-only access to the MCC
- Try authorizing with a different Google account that has access

### Error: "Customer not found"
**Cause:** MCC account ID is incorrect
**Fix:**
- Verify the MCC account ID in Google Ads
- Make sure you're using the Manager account ID, not a sub-account

---

## Support

Need help?
- Documentation: https://channel47.dev/plugins/google-ads
- Re-run setup: `/setup`
- Test credentials: `python ~/.claude/plugins/google-ads/scripts/test_auth.py`
```

**Step 2: Verify command file**

Run:
```bash
cat plugins/google-ads/commands/setup.md | head -5
```

Expected: Shows frontmatter with description

**Step 3: Commit**

```bash
git add plugins/google-ads/commands/setup.md
git commit -m "feat(google-ads): add interactive setup command"
```

---

## Task 7: Update Documentation

**Files:**
- Modify: `plugins/google-ads/README.md`
- Modify: `plugins/google-ads/GETTING_STARTED.md`
- Modify: `plugins/google-ads/CHANGELOG.md`

**Step 1: Update README.md**

Replace content in `plugins/google-ads/README.md`:

```markdown
# Google Ads MCP Plugin

Query Google Ads data using GAQL with OAuth authentication.

## Quick Start

1. Install the plugin:
   ```bash
   /plugin install google-ads@channel47
   ```

2. Run setup wizard:
   ```bash
   /setup
   ```

3. Try it out:
   ```
   "List my Google Ads accounts"
   "Find negative keyword opportunities for account 1234567890"
   ```

## What's Included

- **MCP Server** - Two essential tools:
  - List all accessible Google Ads accounts
  - Execute any GAQL query for custom analysis

- **Agent** - Negative Keyword Hunter
  - Analyzes search terms to identify wasted spend
  - Recommends negative keywords to add
  - Prioritizes by budget impact

- **Skill** - GAQL Query Guide
  - Reference for constructing effective queries
  - Field compatibility rules
  - Common query patterns

- **Command** - `/setup`
  - Interactive credential configuration wizard

## Requirements

- Python 3.10+
- Google Ads account with MCC access
- Google Cloud project with Ads API enabled
- OAuth 2.0 credentials

## Documentation

- [Getting Started Guide](GETTING_STARTED.md) - Detailed setup walkthrough
- [Changelog](CHANGELOG.md) - Version history

## Support

Visit [channel47.dev/plugins/google-ads](https://channel47.dev/plugins/google-ads) for examples and guides.
```

**Step 2: Update GETTING_STARTED.md**

Replace content in `plugins/google-ads/GETTING_STARTED.md`:

```markdown
# Getting Started with Google Ads Plugin

This guide walks through the complete setup process for the Google Ads plugin.

## Prerequisites

### 1. Google Ads Account
- MCC (Manager) account with access to sub-accounts
- At least Read-only access level

### 2. Google Cloud Project
- Create project at https://console.cloud.google.com/
- Enable Google Ads API
- Create OAuth 2.0 credentials (Desktop app type)
- **Important:** Publish OAuth consent screen (don't leave in Testing mode)

### 3. Developer Token
- Apply for token in Google Ads: Tools & Settings > Setup > API Center
- Basic or Standard access level required

## Installation

Install the plugin from the channel47 marketplace:

```bash
/plugin install google-ads@channel47
```

## Configuration

Run the interactive setup wizard:

```bash
/setup
```

The wizard will:
1. Check Python and dependencies
2. Guide you through obtaining OAuth credentials
3. Help generate a refresh token
4. Provide configuration for your settings.json

**Manual Setup Alternative:**

If you prefer to configure manually, add these to `~/.claude/settings.json`:

```json
{
  "env": {
    "GOOGLE_ADS_DEVELOPER_TOKEN": "your_developer_token",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID": "1234567890",
    "GOOGLE_ADS_CLIENT_ID": "your_oauth_client_id",
    "GOOGLE_ADS_CLIENT_SECRET": "your_oauth_client_secret",
    "GOOGLE_ADS_REFRESH_TOKEN": "your_refresh_token"
  }
}
```

**Restart Claude Code** after updating settings.

## Verification

Test your configuration:

```bash
python ~/.claude/plugins/google-ads/scripts/test_auth.py
```

Or simply try:
```
"List my Google Ads accounts"
```

## Usage Examples

### Account Discovery
```
"List all my Google Ads accounts"
"Show me accounts under my MCC"
```

### Negative Keyword Discovery
```
"Find negative keyword opportunities for account 1234567890"
"Analyze search terms for wasted spend in the last 30 days"
"Show me search terms with zero conversions for account 1234567890"
```

### Custom GAQL Queries
```
"Run this GAQL query for account 1234567890:
SELECT campaign.name, metrics.cost_micros, metrics.conversions
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC"
```

### Using the Agent
The negative keyword hunter agent triggers automatically when you mention:
- "negative keywords"
- "wasted spend"
- "search terms analysis"

Or invoke directly:
```
"Run the negative keyword hunter for account 1234567890"
```

## Troubleshooting

### "Missing required environment variables"
- Ensure all 5 environment variables are set in settings.json
- Restart Claude Code after updating settings

### "invalid_grant" during authentication
- Your refresh token expired
- Re-run the setup wizard to generate a new token
- Check that OAuth consent screen is "Published" (not "Testing")

### "Developer token only approved for test accounts"
- Apply for Basic or Standard access in Google Ads API Center
- Test accounts have limited functionality

### "Permission denied"
- Verify MCC account ID is correct (10 digits, no dashes)
- Ensure authenticated user has access to the MCC account

## Rate Limits

Google Ads API has rate limits:
- **Basic Access**: 15,000 operations per day
- **Standard Access**: 40 operations per second

The MCP server uses efficient querying patterns to stay within limits.

## Next Steps

- Try the negative keyword hunter on your accounts
- Learn GAQL query patterns for custom analysis
- Set up recurring checks for search term optimization

For more examples and guides, visit [channel47.dev/plugins/google-ads](https://channel47.dev/plugins/google-ads)
```

**Step 3: Update CHANGELOG.md**

Replace content in `plugins/google-ads/CHANGELOG.md`:

```markdown
# Changelog

## [1.0.0] - 2024-12-21

### Added
- Initial release
- MCP server with 2 core tools (list accounts, run GAQL)
- Negative keyword hunter agent for wasted spend analysis
- GAQL query guide skill for LLM reference
- Interactive `/setup` command for OAuth credential configuration
- Python scripts for token generation and auth testing
- Comprehensive documentation (README, GETTING_STARTED)

### Technical Details
- Trimmed MCP server from 8 tools to 2 essential tools
- OAuth 2.0 authentication with refresh token
- Support for Python 3.10+
- Compatible with Google Ads API v28+
```

**Step 4: Verify documentation**

Run:
```bash
wc -l plugins/google-ads/README.md plugins/google-ads/GETTING_STARTED.md plugins/google-ads/CHANGELOG.md
```

Expected: README ~60 lines, GETTING_STARTED ~140 lines, CHANGELOG ~20 lines

**Step 5: Commit**

```bash
git add plugins/google-ads/README.md plugins/google-ads/GETTING_STARTED.md plugins/google-ads/CHANGELOG.md
git commit -m "docs(google-ads): update documentation for v1.0.0 release"
```

---

## Task 8: Final Verification

**Step 1: Verify plugin structure**

Run:
```bash
tree -L 3 plugins/google-ads -I '__pycache__|*.pyc'
```

Expected output:
```
plugins/google-ads/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json
├── agents/
│   └── negative-keyword-hunter/
│       └── agent.md
├── commands/
│   └── setup.md
├── scripts/
│   ├── generate_refresh_token.py
│   └── test_auth.py
├── skills/
│   └── gaql-query-guide/
│       └── skill.md
├── src/
│   └── google_ads_mcp.py
├── CHANGELOG.md
├── GETTING_STARTED.md
├── README.md
└── requirements.txt
```

**Step 2: Verify MCP server tools count**

Run:
```bash
grep -c "@mcp.tool" plugins/google-ads/src/google_ads_mcp.py
```

Expected: 2

**Step 3: Verify all markdown files have valid frontmatter**

Run:
```bash
for file in plugins/google-ads/agents/*/agent.md plugins/google-ads/skills/*/skill.md plugins/google-ads/commands/*.md; do
  echo "Checking $file"
  head -1 "$file" | grep -q "^---$" && echo "✓ Valid frontmatter" || echo "✗ Missing frontmatter"
done
```

Expected: All show "✓ Valid frontmatter"

**Step 4: Test Python imports**

Run:
```bash
cd plugins/google-ads && python -c "
import sys
sys.path.insert(0, 'src')
import google_ads_mcp
print('✓ MCP server imports successfully')
print(f'✓ Tools defined: {len([attr for attr in dir(google_ads_mcp.mcp) if not attr.startswith(\"_\")])}')
"
```

Expected:
```
✓ MCP server imports successfully
✓ Tools defined: 2
```

**Step 5: Verify .mcp.json configuration**

Run:
```bash
cat plugins/google-ads/.mcp.json | python -m json.tool
```

Expected: Valid JSON with:
- `mcpServers.google-ads.command` = "python"
- `mcpServers.google-ads.args` includes "${CLAUDE_PLUGIN_ROOT}/src/google_ads_mcp.py"
- All 5 environment variables defined in `env`

**Step 6: Final commit**

```bash
git add -A
git status
```

Expected: Working directory clean (all changes committed)

If any uncommitted changes:
```bash
git commit -m "chore(google-ads): final verification and cleanup"
```

---

## Testing Checklist

Before marking complete, verify:

- [ ] Plugin structure matches design (agents/, skills/, commands/, src/, scripts/)
- [ ] MCP server has exactly 2 tools (list_accounts, run_gaql)
- [ ] MCP server imports without errors
- [ ] All markdown files have valid YAML frontmatter
- [ ] Agent triggers on correct keywords (negative keywords, wasted spend, etc.)
- [ ] Skill provides comprehensive GAQL reference
- [ ] Setup command guides through all 8 phases
- [ ] Documentation is complete (README, GETTING_STARTED, CHANGELOG)
- [ ] requirements.txt includes all dependencies
- [ ] All commits follow conventional commit format

---

## Post-Implementation Tasks

After completing this plan:

1. **Test the plugin end-to-end:**
   - Install in Claude Code: `/plugin install google-ads@channel47`
   - Run setup: `/setup`
   - Test agent: "Find negative keyword opportunities"
   - Test GAQL: "List my accounts"

2. **Update marketplace README:**
   - Add Google Ads plugin to main README.md
   - Link to channel47.dev/plugins/google-ads

3. **Create example queries:**
   - Document 5-10 common GAQL queries for users
   - Add to plugin documentation or website

4. **Monitor for issues:**
   - Test with real Google Ads accounts
   - Verify OAuth flow works on different machines
   - Check agent output quality with various data sets

## Notes

- All file paths use absolute paths from project root
- ${CLAUDE_PLUGIN_ROOT} is used in runtime configuration (.mcp.json, commands)
- Cost values must be converted from micros (÷ 1,000,000) for display
- OAuth tokens expire if consent screen is in "Testing" mode - must be "Published"
- Agent prioritizes by wasted spend for maximum impact
