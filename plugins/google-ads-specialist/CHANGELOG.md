# Changelog

All notable changes to the Google Ads Specialist Plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.1.0] - 2026-01-07

### Changed

**Distribution Model:**
- MCP server now distributed as npm package `@channel47/google-ads-mcp`
- Server auto-installed via npx when plugin is activated
- No manual server installation required
- Server version independent of plugin version

**Plugin Structure:**
- Removed `server/` directory from plugin
- Skills remain in plugin (`skills/` directory)
- Hook validation remains in plugin (`.claude/hooks/`)
- Plugin now focused on skills and documentation

**Configuration:**
- `.mcp.json` updated to use `npx @channel47/google-ads-mcp@latest`
- Environment variables still configured at plugin level
- No changes to OAuth setup process

**Documentation:**
- Updated README for npm distribution model
- Updated GETTING_STARTED with npx workflow
- Added links to npm package and server repository

### Technical Details

**NPM Package:**
- Package name: `@channel47/google-ads-mcp`
- Distribution: npm registry
- Auto-installation: `npx -y @channel47/google-ads-mcp@latest`
- Independent versioning: Server v1.0.0, Plugin v3.1.0

**Plugin Changes:**
- Removed dependencies from package.json (handled by npm package)
- Removed server-related npm scripts
- Version bumped to 3.1.0 (minor - backward compatible)

**Benefits:**
- ✅ Automatic server updates (using @latest)
- ✅ No npm install needed for plugin users
- ✅ Smaller plugin download size
- ✅ Faster plugin updates (skills-only)
- ✅ Independent server development cycle

### Migration from 3.0.0

**No action required for users:**
- Environment variables unchanged
- Skills unchanged
- Workflow unchanged

**For developers:**
- Server code now at [github.com/channel47/google-ads-mcp-server](https://github.com/channel47/google-ads-mcp-server)
- Plugin code remains in marketplace repository
- Test locally by pointing `.mcp.json` to local server build

## [3.0.0] - 2026-01-07

### 🚨 BREAKING CHANGES

Complete architectural redesign from 13 specialized tools to 3 core tools with progressive disclosure via skills.

**Removed Tools:**
- `get_performance`
- `search_terms_report`
- `find_wasted_spend`
- `quality_score_analysis`
- `budget_pacing`
- `shopping_product_status`
- `shopping_performance`
- `performance_by_dimension`
- `add_negative_keywords`
- `adjust_bids`
- `update_campaign_status`

**Tool Changes:**
- `run_gaql_query` → `query` (renamed)
- All functionality now accessible via `query` and `mutate` tools with skill guidance

### Added

**Core Tools (3):**
- `list_accounts`: List accessible Google Ads accounts (unchanged)
- `query`: Execute any GAQL SELECT query (renamed from run_gaql_query)
- `mutate`: Execute write operations via GoogleAdsService.Mutate (new)

**Skills (9):**
- `atomic-campaign-performance`: Campaign metrics query patterns
- `atomic-search-terms-report`: Search query analysis patterns
- `atomic-wasted-spend-analysis`: Wasted spend identification
- `atomic-quality-score-audit`: Quality Score analysis
- `atomic-budget-pacing`: Budget utilization analysis
- `atomic-add-negative-keywords`: Negative keyword mutations with checklist
- `atomic-adjust-bids`: Bid adjustment patterns
- `playbook-account-health-audit`: 6-step comprehensive audit workflow
- `troubleshooting-gaql-errors`: GAQL error troubleshooting guide

**Hook System:**
- PreToolUse hook validates skill reference before query/mutate operations
- Prevents hallucinated queries by requiring skill consultation
- Exempts list_accounts (safe enumeration)
- Fail-open design prevents workflow breakage

**Build System:**
- `build.js`: Creates plugin and standalone-skills distributions
- NPM scripts: `npm run build`, `npm run publish-to-marketplace`
- Plugin manifest (`.claude-plugin/plugin.json`)

**Documentation:**
- Complete README rewrite for 3-tool architecture
- Updated GETTING_STARTED with skills usage
- Comprehensive skill documentation (~1,400 lines)

### Changed

- Server code reduced from 718 lines to 199 lines (~72% reduction)
- Package name: `google-ads-specialist` (matches marketplace plugin)
- Query tool blocks mutation keywords (CREATE, UPDATE, REMOVE)
- All write operations now use `mutate` tool with dry_run default
- Progressive disclosure: domain knowledge in skills, not tool definitions

### Technical Details

**Server Architecture:**
- Minimal 3-tool MCP server
- Mutation blocking in query tool
- GoogleAdsService.Mutate wrapper for writes
- Dry run validation (default: true)

**Skills Architecture:**
- Flat directory structure with prefix naming
- YAML frontmatter for metadata
- 80-120 lines per atomic skill
- 250-850 lines for playbooks
- Supporting files for complex workflows

**Hook Architecture:**
- Python validation script (99 lines)
- JSON settings configuration
- Transcript scanning for skill references
- Clear deny/allow feedback

### Migration Guide

**From v2.x to v3.0:**

1. **Install v3.0.0** via marketplace or manual build
2. **Update workflow:** Reference skills before operations
3. **Use query tool:** Replace specialized tools with GAQL from skills
4. **Use mutate tool:** Replace write operations with mutation patterns from skills

**Example Migration:**

Before (v2.x):
```javascript
// Used specialized tool
{
  "tool": "get_performance",
  "level": "campaign",
  "date_range": "LAST_30_DAYS"
}
```

After (v3.0):
```javascript
// Reference skill, then use query tool
// 1. Claude reads atomic-campaign-performance skill
// 2. Claude constructs GAQL:
{
  "tool": "query",
  "query": "SELECT campaign.name, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_30_DAYS"
}
```

### Benefits

- **Simpler:** 3 tools instead of 13
- **More Flexible:** Any GAQL query possible via query tool
- **Better Learning:** Skills teach proper patterns
- **Safer:** Hook validation prevents hallucinated queries
- **More Maintainable:** 72% less server code
- **Better UX:** Progressive disclosure via readable skill files
- Added Resources section to README

### Milestone

**Manifest 100% Complete!** All 14 tools, 5 prompts, and 2 resources are now implemented.

---

## [2.3.0] - 2024-12-31

### Added - Phase 4: Write Operations

Phase 4 adds write capabilities with comprehensive safety features.

**New Tools:**

- `add_negative_keywords`: Add negative keywords to campaigns or ad groups
  - Bulk addition support with validation
  - Conflict detection (duplicate negatives, positive keyword blocking)
  - Campaign-level and ad group-level targeting
  - Dry run mode (default: true for safety)

- `adjust_bids`: Modify bids for keywords, product groups, or ad groups
  - Multiple adjustment types: SET, INCREASE_PERCENT, DECREASE_PERCENT, INCREASE_AMOUNT, DECREASE_AMOUNT
  - Automatic current bid lookup for percentage/amount adjustments
  - Max/min bid caps and floors
  - Large change warnings (>50% change)
  - Dry run mode (default: true for safety)

- `update_campaign_status`: Enable, pause, or set budgets for campaigns
  - Status changes (ENABLED/PAUSED)
  - Budget updates with shared budget detection
  - Warning when pausing converting campaigns
  - Dry run mode (default: true for safety)

**Infrastructure:**

- New `server/utils/mutations.js` module:
  - `executeMutations()`: Execute Google Ads mutate operations
  - `buildNegativeKeywordOperation()`: Build negative keyword criterion
  - `buildBidAdjustmentOperation()`: Build bid adjustment with calculation
  - `buildCampaignUpdateOperation()`: Build status/budget updates
  - `checkNegativeConflicts()`: Detect conflicts before adding negatives
  - `validateBidChange()`: Validate bid adjustments with limits

**Safety Features:**

- All write operations default to `dry_run: true`
- Conflict detection prevents blocking positive keywords
- Large change warnings for significant bid adjustments
- Shared budget detection and warnings
- Reversibility documentation in all responses

### Changed

- Server version updated to 2.3.0
- Manifest version updated to 2.3.0
- Updated README with write operation documentation
- Updated security section to reflect dry_run defaults

---

## [2.2.0] - 2024-12-31

### Added - Phase 3: Shopping & Segmentation

Phase 3 adds essential e-commerce support and dimensional analysis tools.

**New Tools:**

- `shopping_product_status`: Check Merchant Center feed health and product disapprovals
  - Product status filtering (ALL, DISAPPROVED, PENDING, APPROVED, NOT_ELIGIBLE)
  - Issue categorization with severity levels
  - Automatic Merchant Center ID detection
  - Actionable recommendations per issue type
  - Campaign exposure impact analysis

- `shopping_performance`: Product-level performance for Shopping campaigns
  - Segmentation by product_item_id, title, brand, category, or custom labels
  - Full e-commerce metrics (ROAS, CPA, conversion rate, avg order value)
  - Performance tier classification (top_performer, profitable, break_even, underperforming, wasted_spend)
  - Top performers and wasted spend identification
  - Automated optimization recommendations

- `performance_by_dimension`: Segment performance by time, device, location, or audience
  - Hour of day analysis with peak/off-peak identification
  - Day of week performance patterns
  - Device comparison (mobile, desktop, tablet)
  - Geographic performance by country, region, city, or metro
  - Audience segment performance
  - Automated insights with bid adjustment recommendations

**GAQL Templates:**

- `SHOPPING_PRODUCT_STATUS`: Product feed health and disapproval data
- `SHOPPING_PERFORMANCE`: Product-level Shopping metrics with flexible segmentation
- `PERFORMANCE_BY_HOUR`: Hour of day performance
- `PERFORMANCE_BY_DAY_OF_WEEK`: Day of week performance
- `PERFORMANCE_BY_DEVICE`: Device-segmented performance
- `PERFORMANCE_BY_GEO`: Geographic performance data
- `PERFORMANCE_BY_AUDIENCE`: Audience segment performance

**Prompts Updated:**

- `weekly_account_review`: Now includes shopping feed health and device analysis
- `shopping_optimization`: Fully functional with product, brand, and category analysis
- `competitive_analysis`: Now includes hour and day performance patterns

### Changed

- Server version updated to 2.2.0
- Extended `buildQuery` function for Phase 3 template placeholders
- Updated prompts with tool usage instructions

---

## [2.1.0] - 2024-12-31

### Added - Phase 2: Quality & Budget Analysis

Phase 2 adds three powerful analysis tools and the prompts infrastructure.

**New Tools:**

- `quality_score_analysis`: Analyze Quality Score distribution with component breakdown
  - QS component analysis (expected CTR, ad relevance, landing page experience)
  - Grouping by keyword, ad_group, campaign, or weakest component
  - Estimated monthly savings calculation based on potential QS improvements
  - Filter for keywords at or below configurable QS threshold

- `auction_insights`: Competitive analysis showing auction dynamics
  - Campaign, ad group, and keyword level insights
  - Competitor domain identification with impression share
  - Position metrics (overlap rate, position above rate, outranking share)
  - Top-of-page and absolute top-of-page rates
  - Automated insights generation

- `budget_pacing`: Budget utilization and spend pacing analysis
  - MTD spend vs expected spend calculation
  - Pacing ratio and status (on_track, underspending, overspending, limited_by_budget)
  - Days until budget exhaustion projection
  - Shared budget grouping and analysis
  - Recommended budget surfacing

**Prompts Infrastructure:**

- New `server/prompts/templates.js` with template engine
- `ListPrompts` and `GetPrompt` MCP handlers in `server/index.js`
- Argument validation and default value support
- 5 prompt templates defined:
  - `quick_health_check`: Fast daily account monitoring
  - `weekly_account_review`: Comprehensive weekly review
  - `negative_keyword_mining`: Find and add negative keywords
  - `shopping_optimization`: Shopping campaign deep-dive
  - `competitive_analysis`: Competitive landscape analysis

**GAQL Templates:**

- `QUALITY_SCORE_ANALYSIS`: QS metrics with all three components
- `AUCTION_INSIGHTS_CAMPAIGN`: Campaign-level competitive metrics
- `AUCTION_INSIGHTS_AD_GROUP`: Ad group-level competitive metrics
- `AUCTION_INSIGHTS_KEYWORD`: Keyword-level competitive metrics
- `CAMPAIGN_BUDGET`: Budget and spend data with recommendations
- `CAMPAIGN_DAILY_SPEND`: Daily spend for pacing calculations

### Changed

- Server version updated to 2.1.0
- Added `prompts` capability to MCP server
- Extended `buildQuery` function for new template placeholders

---

## [2.0.0] - 2024-12-30

### Changed - Phase 1 Rebuild (BREAKING)

Complete architectural rebuild with modular structure for maintainability and distribution.

**Breaking Changes:**
- Server is now read-only (analysis tools only)
- Response format changed to include standardized metadata
- Tool names and parameters updated for consistency

**New Architecture:**
- Modular tool structure (one tool per file)
- Shared utilities for auth, validation, response formatting
- Hybrid GAQL template system for query construction
- Progressive migration path for future phases

### Added

**Tools:**
- `get_performance`: Multi-level performance reporting (campaign, ad group, keyword, product group)
- `search_terms_report`: Search query analysis with performance data
- `find_wasted_spend`: Smart waste detection with dynamic CPA-based thresholds

**Prompts:**
- `quick_performance_check`: Daily account health monitoring
- `search_term_deep_dive`: Negative keyword opportunity analysis
- `campaign_performance_comparison`: Performance comparison and optimization

### Removed

**Tools (deferred to Phase 2+):**
- `run_gaql_query`: Advanced users - coming in phase 3
- `add_negative_keywords`: Write operation - coming in phase 2
- `adjust_bids`: Write operation - coming in phase 2
- `update_campaign_status`: Write operation - coming in phase 2
- `quality_score_analysis`: Coming in phase 2
- `auction_insights`: Coming in phase 2
- `budget_pacing`: Coming in phase 2
- `performance_by_dimension`: Coming in phase 2
- `shopping_product_status`: Coming in phase 2
- `shopping_performance`: Coming in phase 2

**Prompts (deferred until required tools available):**
- `weekly_account_review`
- `negative_keyword_mining`
- `shopping_optimization`
- `competitive_analysis`
- `quick_health_check`

### Migration Notes

For users upgrading from 1.0.0:

1. **Response format changed**: All tools now return structured responses with `success`, `summary`, `data`, and `metadata` fields
2. **Environment variables unchanged**: Same OAuth credentials required
3. **Read-only focus**: Phase 1 focuses on analysis; write operations return in phase 2
4. **Tool parameter changes**: Review manifest.json for updated parameter names

### Technical Details

- Modular architecture: `server/tools/`, `server/utils/`, `server/auth.js`
- Standardized error handling with MCP error codes
- Template-based GAQL query construction
- Smart threshold calculation for waste detection (2x CPA or $50 fallback)

---

## [1.0.0] - 2025-12-25

### Added

- Initial release of Google Ads MCP Server as Node.js MCPB bundle
- **Tools**:
  - `run_google_ads_gaql`: Execute any GAQL query for data retrieval
  - `google_ads_list_accounts`: List accessible accounts under MCC
- **Features**:
  - OAuth 2.0 authentication with refresh token
  - Read-only safety enforcement (blocks mutation operations)
  - Response truncation at 25,000 characters
  - Comprehensive error handling with query context
  - Debug logging to stderr
  - Timeout management (2 minute default)
- **MCPB Compliance**:
  - Manifest version 0.3
  - User configuration schema for credentials
  - Platform compatibility (darwin, win32, linux)
  - Node.js 18+ runtime requirement
- **Documentation**:
  - README with usage examples and GAQL reference
  - GETTING_STARTED guide for setup
  - Inline JSDoc comments

### Migrated From

- Python implementation in `plugins/google-ads/src/google_ads_mcp.py`
- Maintains feature parity with Python version
- Uses same environment variable names for easy migration
