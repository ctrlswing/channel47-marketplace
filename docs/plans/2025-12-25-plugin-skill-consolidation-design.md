# Plugin Skill Consolidation Design

**Date:** 2025-12-25
**Plugins:** creative-writing, ascii-art
**Goal:** Consolidate granular skills and implement progressive documentation loading

## Problem Statement

Both creative-writing and ascii-art plugins suffer from skill proliferation and inadequate documentation integration:

**Creative Writing Issues:**
- 7 skills with significant overlap (edit-draft vs improve-opening/strengthen-ending)
- Similar operations require users to choose between subtle differences
- Style guide chunking logic duplicated across skills
- No centralized pattern detection reference

**ASCII Art Issues:**
- 6 skills where most are text decoration variants
- Excellent reference docs in `/assets/` but skills don't load them
- Users confused about which skill to use for text styling
- Font and color references unused by skills

**Impact:**
- User confusion and decision paralysis
- LLM struggles to pick optimal skill
- High maintenance burden (changes require updating 7+ files)
- Wasted reference documentation
- Inconsistent implementation across similar skills

## Design Overview

**Consolidation Strategy:**

Creative Writing: **7 → 3 skills**
- `/write` - All content generation and editing (consolidates 5 skills)
- `/review` - Feedback without rewrites (enhanced, stays focused)
- `/configure` - Style guide setup (renamed from generate-style-guide)

ASCII Art: **6 → 2 skills**
- `/text` - All text decoration (logos, banners, boxes, effects)
- `/diagrams` - Structural diagrams (flowcharts, trees, architecture)

**Key Innovation:** Progressive disclosure pattern where skills explicitly reference supporting documentation, loading only what's needed per operation.

## Skill Consolidation Details

### Creative Writing `/write` Skill

**Consolidates:** edit-draft, generate-content, improve-opening, strengthen-ending, remove-ai-tells

**Arguments:**
```yaml
---
name: write
description: Generate or refine written content using style guide principles. Use when writing drafts, editing content, improving openings or endings, or removing AI writing patterns.
args:
  - name: content
    description: Content to edit (paste or @file), or topic for new content
    required: false
  - name: mode
    description: "Operation: draft, edit, opening, ending, clean (default: auto-detect)"
    required: false
    flag: true
  - name: style-guide
    description: Path to custom style guide (overrides default/settings)
    required: false
    flag: true
---
```

**Mode Detection Logic:**
- No content provided → `draft` (generate new)
- Content < 100 words → `opening`
- Content mentions "ending"/"conclusion" → `ending`
- Content has AI patterns → `clean`
- Otherwise → `edit` (full rewrite)

**File Structure:**
```
skills/write/
├── SKILL.md                    # Core workflow and mode detection
├── writing-patterns.md         # AI tells, pattern detection rules
└── style-guide-loader.md       # Which style guide sections per mode
```

**Progressive Disclosure:**
- Core workflow in SKILL.md
- References `writing-patterns.md` for AI pattern detection (loaded in clean mode)
- References `style-guide-loader.md` for section routing
- Loads style guide chunks dynamically based on mode:
  - `draft` → Full guide
  - `edit` → Voice, Structure, Word Choice, Patterns to Avoid
  - `opening` → Voice Principles, Patterns to Avoid
  - `ending` → Endings, Patterns to Avoid
  - `clean` → Full Patterns to Avoid from writing-patterns.md

### Creative Writing `/review` Skill

**Changes:** Enhanced with pattern reference, otherwise stays focused

**Enhancements:**
- Now references `writing-patterns.md` for consistent feedback
- Maintains read-only review approach
- No structural changes to core functionality

### Creative Writing `/configure` Skill

**Changes:** Renamed from `generate-style-guide`, functionality unchanged

**Rationale:** More consistent naming with `/write` and `/review`

### ASCII Art `/text` Skill

**Consolidates:** generate-logo, generate-banner, generate-box, text-effects

**Arguments:**
```yaml
---
name: text
description: Create ASCII text art including logos, banners, boxes, and text effects. Use when generating headers, decorative text, terminal splash screens, or framed content.
args:
  - name: content
    description: Text to render or content to frame
    required: true
  - name: type
    description: "Output type: logo, banner, box (default: logo)"
    required: false
    flag: true
  - name: style
    description: "Font/border style: standard, block, slant, banner, small, rounded, double, etc."
    required: false
    flag: true
  - name: effect
    description: "Text effect: shadow, 3d, outline, gradient, rainbow, neon"
    required: false
    flag: true
  - name: color
    description: "ANSI color or gradient: red, blue, sunset, ocean, matrix"
    required: false
    flag: true
---
```

**Type Detection:**
- Contains newlines or >50 chars → box
- Multiple words (>2) → banner
- Single word, uppercase → logo
- Default → logo

**File Structure:**
```
skills/text/
├── SKILL.md                 # Core workflow and type routing
├── font-loader.md           # Font file mapping
└── examples/
    ├── logo-examples.md
    ├── banner-examples.md
    └── box-examples.md
```

**Progressive Disclosure:**
- SKILL.md contains workflow and decision tree
- References `assets/fonts/[style].md` for character patterns (loaded on demand)
- References `assets/reference/ansi-colors.md` when color specified
- References `assets/examples/borders.md` for box/banner styles
- Font loader pattern maps style names to asset files

### ASCII Art `/diagrams` Skill

**Consolidates:** generate-diagram, generate-art

**Arguments:**
```yaml
---
name: diagrams
description: Create ASCII diagrams including flowcharts, trees, tables, and architecture visualizations. Use when visualizing flows, hierarchies, data structures, or system architecture.
args:
  - name: description
    description: What to diagram or visualize
    required: true
  - name: type
    description: "Diagram type: flowchart, tree, table, architecture, sequence (default: auto-detect)"
    required: false
    flag: true
  - name: direction
    description: "Layout direction: horizontal, vertical (default: horizontal)"
    required: false
    flag: true
---
```

**Type Detection:**
- Contains "→" or "then" or "after" → flowchart
- Contains "parent/child" or hierarchical indicators → tree
- Contains rows/columns or "|" delimiter → table
- Contains "system/component/service" → architecture
- Contains "user/actor" or temporal sequence → sequence

**File Structure:**
```
skills/diagrams/
├── SKILL.md                    # Core workflow and diagram generation
└── diagram-patterns.md         # Box drawing chars, connectors, layouts
```

**Progressive Disclosure:**
- SKILL.md contains core workflow
- References `diagram-patterns.md` for box drawing characters and layout patterns
- References `assets/examples/diagrams.md` for pattern examples

## Implementation Details

### Creative Writing `/write` Workflow

**Step 1: Load Style Guide**

Check for style guide in priority order:
1. `--style-guide` parameter (if provided)
2. `.claude/creative-writing.local.md` custom_style_guide setting
3. Default style guide at `../../default-style-guide.md`

**Step 2: Detect Mode**

Auto-detect if `--mode` not specified using rules above.

**Step 3: Load Relevant Sections**

Read `style-guide-loader.md` to determine which sections needed for detected mode.

Extract sections using header matching: `## Section Name` through next `##` header.

**Step 4: Get or Generate Content**

If no content provided, prompt user.

**Step 5: Execute Mode-Specific Operation**

Each mode has specialized workflow:
- **Draft:** Generate from scratch using full guide
- **Edit:** Full rewrite with Voice, Structure, Word Choice
- **Opening:** Refine first 1-3 paragraphs for honesty
- **Ending:** Strengthen conclusion with genuine question
- **Clean:** Remove AI patterns using pattern detection rules

**Step 6: Present Results**

Show original, revised, and key changes with reasoning.

### ASCII Art `/text` Workflow

**Step 1: Determine Type**

Auto-detect from content or use `--type` flag.

**Step 2: Load Font or Border Reference**

Read `font-loader.md` to map style to font file:
- standard → `../../assets/fonts/standard.md`
- block → `../../assets/fonts/block.md`
- slant → `../../assets/fonts/slant.md`
- banner → `../../assets/fonts/banner.md`
- small → `../../assets/fonts/small.md`

For banners/boxes, reference example files.

**Step 3: Load Color Reference (if specified)**

If `--color` flag provided:
Read `../../assets/reference/ansi-colors.md`
Extract ANSI codes for requested color or gradient.

**Step 4: Render Base Output**

Type-specific rendering:
- **Logo:** Use character patterns from font file
- **Banner:** Create top/bottom borders with centered text
- **Box:** Frame multi-line content with complete border

**Step 5: Apply Effects (if specified)**

Apply visual effects based on `--effect`:
- shadow, 3d, outline, gradient, rainbow, neon, glitch, retro

**Step 6: Apply Colors**

Wrap output with ANSI color codes (solid or gradient).

**Step 7: Output Result**

Display in code block for proper monospace formatting.

### ASCII Art `/diagrams` Workflow

**Step 1: Parse Description**

Extract diagram structure from natural language:
- Identify nodes/entities
- Identify relationships/connections
- Detect hierarchy or sequence

**Step 2: Detect Diagram Type**

Auto-detect or use `--type` flag.

**Step 3: Load Diagram Patterns**

Read `diagram-patterns.md` for:
- Box drawing characters for selected style
- Connector symbols (arrows, lines)
- Layout rules for diagram type

Reference `../../assets/examples/diagrams.md` for examples.

**Step 4: Generate Diagram**

Type-specific generation:
- **Flowchart:** Boxes with directional arrows
- **Tree:** Hierarchical structure with branches
- **Table:** Grid with headers and rows
- **Architecture:** System components with heavy borders
- **Sequence:** Actors with message flow over time

**Step 5: Apply Box Style**

Use box drawing characters from `diagram-patterns.md`:
- simple: ┌─┐ │ └─┘
- double: ╔═╗ ║ ╚═╝
- rounded: ╭─╮ │ ╰─╯
- heavy: ┏━┓ ┃ ┗━┛

**Step 6: Output Result**

Display in code block.

## Supporting Files

### writing-patterns.md

Comprehensive AI pattern detection reference containing:

**Pattern Categories:**
1. Punctuation overuse (em-dashes, colons, semicolons)
2. Hype words (game-changer, revolutionary, unlock, leverage)
3. Rhetorical questions as transitions
4. Generic CTAs and endings
5. Performative openings
6. List addiction
7. Header overload

**Detection Algorithm:**
- Auto-flag hype words from comprehensive list
- Count punctuation patterns per 100 words
- Identify rhetorical transition questions
- Check opening/ending for generic patterns
- Analyze list/header density

**Replacement Strategy:**
- Concrete language instead of hype words
- Direct statements instead of rhetorical questions
- Specific questions instead of generic CTAs

### style-guide-loader.md

Maps operation modes to required style guide sections:

| Mode | Sections Loaded |
|------|-----------------|
| draft | Full guide |
| edit | Voice, Structure, Word Choice, Patterns to Avoid, Quick Reference |
| opening | Voice Principles, Patterns to Avoid |
| ending | Endings, Patterns to Avoid |
| clean | Patterns to Avoid only (from writing-patterns.md) |

**Section Extraction Method:**
Use header matching to extract sections between `##` markers.

### font-loader.md

Maps font style names to asset file paths:

| Style | File | Best For |
|-------|------|----------|
| standard | assets/fonts/standard.md | Classic ASCII, general use |
| block | assets/fonts/block.md | Bold impact, splash screens |
| slant | assets/fonts/slant.md | Dynamic, modern appearance |
| banner | assets/fonts/banner.md | Simple, hash-based letters |
| small | assets/fonts/small.md | Compact, space-constrained |

### diagram-patterns.md

Box drawing character sets and layout patterns:

**Character Sets:**
- Simple: ┌─┐ │ └─┘
- Double: ╔═╗ ║ ╚═╝
- Rounded: ╭─╮ │ ╰─╯
- Heavy: ┏━┓ ┃ ┗━┛
- ASCII-only: +-+ | +-+

**Arrow/Connector Symbols:**
- Horizontal: ─▶ ◀─ ◀──▶
- Vertical: │▼ ▲│
- Diagonal: └── ├──

**Layout Patterns:**
- Flowchart node spacing
- Tree branch structures
- Table column auto-sizing
- Architecture layer grouping
- Sequence diagram lifelines

## Migration Strategy

### Phase 1: Non-Breaking Addition (v1.1.0 / v1.2.0)

Add new consolidated skills alongside existing ones.

**Creative Writing Structure:**
```
skills/
├── write/                    # NEW
├── review/                   # UPDATED
├── configure/                # RENAMED
├── edit-draft/              # DEPRECATED
├── generate-content/        # DEPRECATED
├── improve-opening/         # DEPRECATED
├── strengthen-ending/       # DEPRECATED
└── remove-ai-tells/         # DEPRECATED
```

**ASCII Art Structure:**
```
skills/
├── text/                     # NEW
├── diagrams/                 # NEW
├── generate-logo/           # DEPRECATED
├── generate-banner/         # DEPRECATED
├── generate-box/            # DEPRECATED
├── generate-diagram/        # DEPRECATED
├── generate-art/            # DEPRECATED
└── text-effects/            # DEPRECATED
```

### Phase 2: Deprecation Notices

Add deprecation warnings to old skills:

```yaml
---
name: edit-draft
description: "[DEPRECATED] Use /write instead. This skill will be removed in v2.0. Rewrite content to match style guide principles."
---

# ⚠️ DEPRECATED - Use `/write` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/write` with your content:
- `/write "your content here"` (auto-detects edit mode)
- `/write "your content" --mode edit` (explicit edit)
```

**Deprecation Mappings:**

Creative Writing:
- `/edit-draft` → `/write` (auto-detects edit mode)
- `/generate-content` → `/write` (auto-detects draft mode)
- `/improve-opening` → `/write --mode opening`
- `/strengthen-ending` → `/write --mode ending`
- `/remove-ai-tells` → `/write --mode clean`

ASCII Art:
- `/generate-logo` → `/text` (auto-detects logo type)
- `/generate-banner` → `/text --type banner`
- `/generate-box` → `/text --type box`
- `/text-effects` → `/text --effect [effect-name]`
- `/generate-diagram` → `/diagrams`
- `/generate-art` → `/diagrams` (for structural art) or `/text` (for decorative)

### Phase 3: Documentation Updates

**README.md Changes:**

```markdown
## Skills

### Current Skills (v1.1.0+)

- `/write` - Generate or refine content
- `/review` - Get feedback without rewrites
- `/configure` - Create personalized style guide

### Deprecated Skills (Removed in v2.0)

<details>
<summary>Click to see deprecated skills</summary>

- `/edit-draft` → Use `/write` instead
- `/generate-content` → Use `/write` instead
- `/improve-opening` → Use `/write --mode opening`
- `/strengthen-ending` → Use `/write --mode ending`
- `/remove-ai-tells` → Use `/write --mode clean`
</details>
```

**CHANGELOG.md Entry:**

```markdown
## [1.1.0] - 2025-MM-DD

### Added
- New `/write` skill consolidating 5 content operations
- Progressive disclosure for style guide loading
- `writing-patterns.md` reference for AI pattern detection
- `style-guide-loader.md` for explicit chunk routing

### Changed
- `/configure` renamed from `/generate-style-guide`
- `/review` enhanced with pattern references

### Deprecated
- `/edit-draft`, `/generate-content`, `/improve-opening`,
  `/strengthen-ending`, `/remove-ai-tells`
- Deprecated skills removed in v2.0.0
```

### Phase 4: Version Timeline

**Creative Writing:**
- v1.0.0 → v1.1.0 (add new, deprecate old)
- v1.1.0 → v2.0.0 (remove deprecated)

**ASCII Art:**
- v1.1.0 → v1.2.0 (add new, deprecate old)
- v1.2.0 → v2.0.0 (remove deprecated)

**Deprecation Period:** Minimum 4 weeks between v1.x and v2.0

## Testing Strategy

### Phase 1: Unit Testing

**Creative Writing Tests:**

Mode Detection:
- Auto-detect draft from topic
- Auto-detect opening from short content
- Auto-detect ending from conclusion markers
- Auto-detect clean from AI patterns
- Explicit mode override

Style Guide Loading:
- Custom style guide via flag
- Settings-based style guide
- Default fallback
- Missing guide error handling

Reference File Loading:
- `writing-patterns.md` in clean mode
- `style-guide-loader.md` routing
- Section extraction accuracy

Error Handling:
- No content provided
- Very short content
- Empty content

**ASCII Art Tests:**

Type Detection:
- Auto-detect logo, banner, box
- Explicit type override

Font/Style Loading:
- Each font style (standard, block, slant, banner, small)
- Each border style (simple, double, rounded, heavy)
- Font loader mapping accuracy

Color Loading:
- Solid colors
- Gradient colors
- No color specified

Effect Application:
- Individual effects
- Combined effects and colors

Width Constraints:
- Within limit
- Exceeds limit

Error Handling:
- Unknown styles
- Empty text
- Unsupported characters

**Diagram Tests:**

Type Detection:
- Each diagram type auto-detection
- Explicit type override

Pattern Loading:
- diagram-patterns.md loading
- Example reference loading

Box Styles:
- Each style (simple, double, heavy, rounded)

Direction:
- Horizontal and vertical layouts

Parsing:
- Complex structures
- Multi-level hierarchies
- Branching flows

Error Handling:
- Unclear structures
- Too many nodes
- Empty descriptions

### Phase 2: Integration Testing

Plugin Discovery:
- New skills auto-discovered
- Old skills marked deprecated

Settings Integration:
- Local settings respected
- Flag overrides settings

File References:
- Relative paths resolve correctly
- Missing files handled gracefully

Cross-skill:
- Multiple skills in same session
- Old and new skills coexist

### Phase 3: User Acceptance Testing

**Creative Writing Scenarios:**

Blog Post Workflow:
1. Generate draft with `/write "topic"`
2. Review with `/review`
3. Refine opening with `/write --mode opening`
4. Clean patterns with `/write --mode clean`
5. Final review

Custom Style Guide:
1. Create with `/configure`
2. Use with `/write --style-guide path`
3. Verify custom application

Quick Edits:
1. Paste content to `/write`
2. Auto-detect mode
3. Single-step improvement

**ASCII Art Scenarios:**

CLI Splash Screen:
1. Logo with `/text "App" --style block --color cyan`
2. Banner with `/text "Version" --type banner --style rounded`
3. Frame with `/text "Notice" --type box --color green`

Documentation Diagrams:
1. Architecture with `/diagrams "Web → API → DB" --type architecture`
2. Flowchart with `/diagrams "Input → Process → Save"`
3. Tree with `/diagrams "Project > Frontend, Backend"`

Combined Effects:
1. Neon logo with `/text "NEON" --effect neon --color matrix`
2. 3D banner with `/text "ANNOUNCE" --effect 3d --color sunset`

**Regression Tests:**

Old Skill Parity:
- Compare outputs from old vs new skills
- Verify equal or better quality
- Confirm no lost functionality

Edge Cases:
- Very long text
- Special characters
- Empty inputs
- Complex structures

### Phase 4: Performance Testing

Reference File Loading:
- Style guide chunk loading times (< 100ms)
- Font file loading times (< 50ms)
- Concurrent skill usage

Token Efficiency:
- Compare context size old vs new
- Mode-specific loading efficiency
- Target: 20-40% token reduction

## Implementation Plan

### Week 1: Creative Writing Plugin

**Day 1-2: Create `/write` skill**
- Write SKILL.md with mode detection
- Create writing-patterns.md reference
- Create style-guide-loader.md routing

**Day 3: Update `/review` and `/configure`**
- Enhance review with pattern refs
- Rename generate-style-guide to configure

**Day 4: Add deprecation notices**
- Update old skill descriptions
- Add migration instructions
- Update README.md

**Day 5: Unit testing**
- Test mode detection
- Test style guide loading
- Test reference file loading

### Week 2: ASCII Art Plugin

**Day 1-2: Create `/text` skill**
- Write SKILL.md with type detection
- Create font-loader.md reference
- Create example files

**Day 3: Create `/diagrams` skill**
- Write SKILL.md with type detection
- Create diagram-patterns.md reference

**Day 4: Add deprecation notices**
- Update old skill descriptions
- Add migration instructions
- Update README.md

**Day 5: Unit testing**
- Test type detection
- Test asset loading
- Test diagram generation

### Week 3: Integration & UAT

**Day 1-2: Integration testing**
- Plugin discovery
- Settings integration
- File references
- Cross-skill usage

**Day 3-4: User acceptance testing**
- Real-world workflows
- Custom configurations
- Edge cases

**Day 5: Performance testing**
- Loading times
- Token efficiency
- Concurrent usage

### Week 4: Release & Migration

**Day 1: Release v1.1.0 / v1.2.0**
- Deploy with new and deprecated skills
- Update marketplace listings
- Publish changelogs

**Day 2-3: Monitor & feedback**
- Track usage patterns
- Gather user feedback
- Document issues

**Day 4-5: Plan v2.0.0**
- Review migration success
- Plan deprecation removal
- Update documentation

### Week 8: Remove Deprecated Skills

**Release v2.0.0:**
- Remove deprecated skills
- Final documentation updates
- Announcement and migration guide

## Success Metrics

**User Experience:**
- Reduced decision time (fewer skills to choose from)
- Improved skill discovery (clearer descriptions)
- Faster workflows (consolidated operations)

**Code Quality:**
- Reduced duplication (shared references)
- Easier maintenance (fewer files to update)
- Better documentation integration (progressive disclosure)

**Performance:**
- 20-40% token reduction (selective loading)
- Faster reference loading (< 100ms per chunk)
- No regression in output quality

**Adoption:**
- 80%+ users migrate to new skills within 4 weeks
- Minimal support requests during transition
- Positive feedback on consolidated approach

## Risks & Mitigations

**Risk:** Users resist change, continue using old skills
**Mitigation:**
- Clear deprecation notices with migration paths
- Extended deprecation period (4 weeks minimum)
- Documentation showing benefits of new skills

**Risk:** Auto-detection fails, wrong mode selected
**Mitigation:**
- Conservative detection rules
- Always allow explicit `--mode` override
- Log mode selection for debugging

**Risk:** Reference files don't load correctly
**Mitigation:**
- Thorough path testing in integration phase
- Graceful fallback if files missing
- Clear error messages

**Risk:** Lost functionality during consolidation
**Mitigation:**
- Regression testing against old skills
- UAT with real workflows
- Feature parity checklist

**Risk:** Performance regression from file loading
**Mitigation:**
- Performance testing with baselines
- Optimize file reading
- Monitor token usage

## Future Enhancements

**Post-v2.0 Improvements:**

1. **Caching:** Cache loaded reference files for session duration
2. **Templates:** Add template system for common content types
3. **Presets:** Named presets combining mode + style + guide
4. **Analytics:** Track mode usage to optimize defaults
5. **Validation:** Pre-flight validation of reference file structure

**Potential New Skills:**

Creative Writing:
- `/compare` - Compare writing against style guide (read-only analysis)
- `/iterate` - Multi-round refinement workflow

ASCII Art:
- `/animate` - Generate animation frames
- `/compose` - Combine multiple ASCII elements into scenes

## Conclusion

This consolidation achieves:
- **Simplified UX:** 7→3 and 6→2 skills reduces cognitive load
- **Better Documentation:** Progressive disclosure integrates existing references
- **Easier Maintenance:** Centralized patterns and routing logic
- **Improved Performance:** Selective loading reduces token usage
- **Consistent Quality:** Shared references ensure consistency

The migration strategy balances user convenience (extended deprecation) with code maintainability (eventual removal of old skills).

Progressive disclosure pattern establishes a foundation for future skill development, where supporting documentation is treated as a first-class concern rather than an afterthought.
