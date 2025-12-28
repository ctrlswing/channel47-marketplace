# Plugin Skill Consolidation Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Consolidate creative-writing (7→3 skills) and ascii-art (6→2 skills) with progressive documentation loading

**Architecture:** Create new consolidated skills alongside existing ones, add progressive disclosure references, deprecate old skills, update documentation

**Tech Stack:** Markdown (skill files), YAML frontmatter, Claude Code plugin system

---

## Part 1: Creative Writing Plugin

### Task 1: Create writing-patterns.md Reference

**Files:**
- Create: `plugins/creative-writing/skills/write/writing-patterns.md`

**Step 1: Create skills/write directory**

```bash
mkdir -p plugins/creative-writing/skills/write
```

**Step 2: Create writing-patterns.md**

Create `plugins/creative-writing/skills/write/writing-patterns.md` with full AI pattern detection rules:

```markdown
# AI Writing Patterns to Avoid

This reference contains comprehensive AI pattern detection rules.

## Pattern Categories

### 1. Punctuation Overuse

| Pattern | Examples | Why Avoid | Fix |
|---------|----------|-----------|-----|
| Em-dashes | "The solution—which works well—is simple" | Feels mechanical, AI-generated | Use periods, commas, or rewrite |
| Excessive colons | "Here's the key: consistency matters" | Overused transition | Direct statement or "because" |
| Semicolons in casual writing | "It works well; however, there are trade-offs" | Too formal for conversational tone | Split into two sentences |

### 2. Hype Words and Superlatives

**Auto-flag these terms:**
- game-changer, revolutionary, groundbreaking
- cutting-edge, state-of-the-art, next-level
- unlock, unleash, harness, leverage
- robust, scalable, synergy, paradigm
- seamless, effortless, transformative

**Replacement strategy**: Use concrete, specific language
- "game-changer" → "saves 3 hours per week"
- "seamless integration" → "works with existing tools"
- "unlock potential" → "enables new workflows"

### 3. Rhetorical Questions as Transitions

**Pattern**: Questions that aren't genuine curiosity

Examples:
- "But what does this mean?"
- "Why does this matter?"
- "How can we address this?"
- "What's the takeaway?"

**Fix**: Make direct statements or skip transition entirely.

### 4. Generic CTAs and Endings

**Auto-flag:**
- "What are your thoughts?"
- "Let me know in the comments!"
- "What do you think?"
- "I'd love to hear from you"
- "Share your experience below"

**Replacement**: Specific, genuine questions about the content.

### 5. Performative Openings

**Pattern**: Bold declarations without earning them

Examples:
- "As an expert in..."
- "I'm excited to share..."
- "In this post, I'll show you..."
- "Let's dive deep into..."

**Fix**: Start with something real—admission, observation, concrete detail.

### 6. List Addiction

**Pattern**: Bullet points where prose would work better

Flag when:
- Lists under 4 items (should be prose)
- Sequential items (use "first... then... finally")
- Lists every 2-3 paragraphs (disrupts flow)

**Exception**: Technical steps, comparison tables, reference material.

### 7. Header Overload

**Pattern**: H2/H3 headers every 2-3 paragraphs

Flag when:
- Headers break narrative flow
- Could use paragraph breaks instead
- Headers state transitions ("Why This Matters", "The Solution")

**Fix**: Use white space, varied paragraph length for pacing.

## Detection Algorithm

When analyzing content in `clean` mode:

1. Scan for hype words (auto-flag list above)
2. Count em-dashes and colons per 100 words (>2 = flag)
3. Identify rhetorical transition questions
4. Check opening (first 2 sentences for performative patterns)
5. Check ending (last paragraph for generic CTAs)
6. Count lists and headers vs paragraphs
7. Flag specific patterns for removal/replacement

## Quick Reference

**High-priority patterns** (always remove):
- Hype words
- Generic CTAs
- Performative openings
- Rhetorical transition questions

**Medium-priority** (consider context):
- Em-dashes (keep if under 1 per 100 words)
- Lists (keep if technical or >5 items)
- Headers (keep if genuinely organizing distinct sections)

**Low-priority** (judgment call):
- Semicolons in appropriate formal contexts
- Occasional colons for emphasis
```

**Step 3: Verify file created**

```bash
ls -la plugins/creative-writing/skills/write/writing-patterns.md
```

Expected: File exists

**Step 4: Commit**

```bash
git add plugins/creative-writing/skills/write/writing-patterns.md
git commit -m "feat(creative-writing): add writing-patterns reference"
```

---

### Task 2: Create style-guide-loader.md Reference

**Files:**
- Create: `plugins/creative-writing/skills/write/style-guide-loader.md`

**Step 1: Create style-guide-loader.md**

Create `plugins/creative-writing/skills/write/style-guide-loader.md`:

```markdown
# Style Guide Section Loader

Maps operation modes to required style guide sections.

## Section Loading by Mode

### Draft Mode
Load complete style guide:
- Voice Principles
- Structure Guidelines
- Word Choice Standards
- Patterns to Avoid
- Endings
- Quick Reference Checklist

### Edit Mode
Load these sections:
- Voice Principles
- Structure Guidelines
- Word Choice Standards
- Patterns to Avoid
- Quick Reference Checklist

### Opening Mode
Load these sections:
- Voice Principles (especially "Lead with honesty")
- Patterns to Avoid (performative openings)

### Ending Mode
Load these sections:
- Endings
- Patterns to Avoid (generic CTAs)

### Clean Mode
Load pattern detection only:
- Full "Patterns to Avoid" table
- Reference [writing-patterns.md](writing-patterns.md) for comprehensive rules

## Section Extraction Method

Use header matching to extract sections from style guide:

```
Find: ## Voice Principles
Extract: From this header through the line before next ## header
```

If custom style guide doesn't have these exact headers, load full guide.
```

**Step 2: Verify file created**

```bash
ls -la plugins/creative-writing/skills/write/style-guide-loader.md
```

Expected: File exists

**Step 3: Commit**

```bash
git add plugins/creative-writing/skills/write/style-guide-loader.md
git commit -m "feat(creative-writing): add style-guide-loader routing"
```

---

### Task 3: Create /write Skill SKILL.md

**Files:**
- Create: `plugins/creative-writing/skills/write/SKILL.md`

**Step 1: Create SKILL.md with full implementation**

Create `plugins/creative-writing/skills/write/SKILL.md`:

```markdown
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

# Write Skill

Generate new content or refine existing writing using style guide principles.

## Workflow

**Step 1: Load Style Guide**

Check for style guide in this order:
1. `--style-guide` parameter (if provided)
2. `.claude/creative-writing.local.md` custom_style_guide setting
3. Default style guide at `../../default-style-guide.md`

**Step 2: Detect Mode**

If `--mode` not specified, auto-detect:

```
No content provided → draft (generate new)
Content < 100 words → opening
Content mentions "ending"/"conclusion" → ending
Content has AI patterns (check writing-patterns.md) → clean
Otherwise → edit
```

**Step 3: Load Relevant Style Guide Sections**

Read [style-guide-loader.md](style-guide-loader.md) to determine sections needed.

Load specified sections from the style guide using header matching (`## Section Name` through next `##`).

**Step 4: Get or Generate Content**

If no content provided:
```
Paste content to edit, or provide a topic for new draft:
```

Wait for user input.

**Step 5: Execute Mode-Specific Operation**

### Draft Mode
Generate new content from topic:
- Use full style guide
- Focus on honest opening, clear reasoning, genuine ending
- Avoid lists, use prose
- Show trade-offs where relevant

### Edit Mode
Rewrite full content:
- Apply Voice Principles, Structure, Word Choice
- Check against [writing-patterns.md](writing-patterns.md) for AI tells
- Preserve core meaning, upgrade execution
- Vary sentence length, natural paragraphs

### Opening Mode
Refine first 1-3 paragraphs:
- Lead with honesty, not authority
- Remove performative declarations
- Check against Patterns to Avoid
- Set genuine tone for rest of piece

### Ending Mode
Strengthen conclusion:
- Replace generic CTAs with specific questions
- Ensure genuine curiosity, not formality
- Check Endings section of style guide
- Avoid "What do you think?" or "Let me know below!"

### Clean Mode
Remove AI patterns only:
- Load full Patterns to Avoid from [writing-patterns.md](writing-patterns.md)
- Remove em-dashes, excessive colons
- Replace hype words with concrete language
- Fix rhetorical questions as transitions
- Minimal structural changes, focus on pattern removal

**Step 6: Present Results**

Show:

```markdown
## Original
[original content if editing, or "New Draft" if generating]

## Revised
[improved content]

## Key Changes
- [Change 1 with brief reasoning]
- [Change 2 with brief reasoning]
- [Change 3 with brief reasoning]
```

## Error Handling

**Missing style guide**:
```
Couldn't load custom style guide at [path], using default instead.
```

**Short content** (< 50 words):
```
Content seems short. For better results, provide at least a paragraph or two.
```

**No content after prompt**:
```
No content received. Please paste your draft or provide a topic.
```

## Examples

**Generate new content:**
```
/write "The benefits of plugin marketplaces for AI tools"
```

**Edit existing:**
```
/write @draft.md
```

**Improve opening:**
```
/write --mode opening
[paste opening paragraphs]
```

**Remove AI patterns:**
```
/write --mode clean @article.md
```
```

**Step 2: Verify skill structure**

```bash
ls -la plugins/creative-writing/skills/write/
```

Expected: SKILL.md, writing-patterns.md, style-guide-loader.md

**Step 3: Commit**

```bash
git add plugins/creative-writing/skills/write/SKILL.md
git commit -m "feat(creative-writing): add /write consolidated skill"
```

---

### Task 4: Update /review Skill

**Files:**
- Modify: `plugins/creative-writing/skills/review-writing/SKILL.md`

**Step 1: Read existing review-writing skill**

```bash
cat plugins/creative-writing/skills/review-writing/SKILL.md
```

**Step 2: Add reference to writing-patterns.md**

In the workflow section, after loading style guide, add:

```markdown
**Step 2.5: Load Pattern Reference**

Read [../write/writing-patterns.md](../write/writing-patterns.md) for AI pattern detection rules.

Use this to identify:
- Hype words and superlatives
- Em-dash and colon overuse
- Rhetorical transition questions
- Generic CTAs
- Performative openings
```

**Step 3: Verify changes**

```bash
git diff plugins/creative-writing/skills/review-writing/SKILL.md
```

Expected: Shows added reference section

**Step 4: Commit**

```bash
git add plugins/creative-writing/skills/review-writing/SKILL.md
git commit -m "feat(creative-writing): enhance /review with pattern reference"
```

---

### Task 5: Rename /generate-style-guide to /configure

**Files:**
- Move: `plugins/creative-writing/skills/generate-style-guide/` → `plugins/creative-writing/skills/configure/`
- Modify: `plugins/creative-writing/skills/configure/SKILL.md`

**Step 1: Rename directory**

```bash
mv plugins/creative-writing/skills/generate-style-guide plugins/creative-writing/skills/configure
```

**Step 2: Update skill name in SKILL.md frontmatter**

Change:
```yaml
name: generate-style-guide
```

To:
```yaml
name: configure
```

**Step 3: Verify rename**

```bash
ls -la plugins/creative-writing/skills/configure/
cat plugins/creative-writing/skills/configure/SKILL.md | head -10
```

Expected: Directory renamed, name updated in frontmatter

**Step 4: Commit**

```bash
git add plugins/creative-writing/skills/configure/
git add plugins/creative-writing/skills/generate-style-guide/
git commit -m "refactor(creative-writing): rename /generate-style-guide to /configure"
```

---

### Task 6: Add Deprecation Notice to /edit-draft

**Files:**
- Modify: `plugins/creative-writing/skills/edit-draft/SKILL.md`

**Step 1: Read existing skill**

```bash
cat plugins/creative-writing/skills/edit-draft/SKILL.md | head -20
```

**Step 2: Update description in frontmatter**

Change description to:
```yaml
description: "[DEPRECATED] Use /write instead. This skill will be removed in v2.0. Rewrite content to match style guide principles."
```

**Step 3: Add deprecation header after frontmatter**

After the `---` closing, before existing content, add:

```markdown
# ⚠️ DEPRECATED - Use `/write` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/write` with your content:
- `/write "your content here"` (auto-detects edit mode)
- `/write "your content" --mode edit` (explicit edit)

The new `/write` skill consolidates edit-draft, improve-opening, strengthen-ending, and remove-ai-tells into one unified workflow with auto-detection.

---

# Original Skill Documentation
```

**Step 4: Verify changes**

```bash
git diff plugins/creative-writing/skills/edit-draft/SKILL.md
```

Expected: Shows deprecation notice added

**Step 5: Commit**

```bash
git add plugins/creative-writing/skills/edit-draft/SKILL.md
git commit -m "chore(creative-writing): deprecate /edit-draft skill"
```

---

### Task 7: Add Deprecation to /generate-content

**Files:**
- Modify: `plugins/creative-writing/skills/generate-content/SKILL.md`

**Step 1: Update description in frontmatter**

```yaml
description: "[DEPRECATED] Use /write instead. This skill will be removed in v2.0. Generate content from topics using style guide."
```

**Step 2: Add deprecation header**

```markdown
# ⚠️ DEPRECATED - Use `/write` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/write` with your topic:
- `/write "your topic here"` (auto-detects draft mode)
- `/write --mode draft "your topic"` (explicit draft)

---

# Original Skill Documentation
```

**Step 3: Commit**

```bash
git add plugins/creative-writing/skills/generate-content/SKILL.md
git commit -m "chore(creative-writing): deprecate /generate-content skill"
```

---

### Task 8: Add Deprecation to /improve-opening

**Files:**
- Modify: `plugins/creative-writing/skills/improve-opening/SKILL.md`

**Step 1: Update description in frontmatter**

```yaml
description: "[DEPRECATED] Use /write --mode opening instead. This skill will be removed in v2.0. Improve opening paragraphs."
```

**Step 2: Add deprecation header**

```markdown
# ⚠️ DEPRECATED - Use `/write --mode opening` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/write` with opening mode:
- `/write` then paste opening paragraphs (auto-detects opening mode for short content)
- `/write --mode opening` (explicit opening mode)

---

# Original Skill Documentation
```

**Step 3: Commit**

```bash
git add plugins/creative-writing/skills/improve-opening/SKILL.md
git commit -m "chore(creative-writing): deprecate /improve-opening skill"
```

---

### Task 9: Add Deprecation to /strengthen-ending

**Files:**
- Modify: `plugins/creative-writing/skills/strengthen-ending/SKILL.md`

**Step 1: Update description in frontmatter**

```yaml
description: "[DEPRECATED] Use /write --mode ending instead. This skill will be removed in v2.0. Strengthen conclusion."
```

**Step 2: Add deprecation header**

```markdown
# ⚠️ DEPRECATED - Use `/write --mode ending` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/write` with ending mode:
- `/write` then paste ending with "conclusion" (auto-detects ending mode)
- `/write --mode ending` (explicit ending mode)

---

# Original Skill Documentation
```

**Step 3: Commit**

```bash
git add plugins/creative-writing/skills/strengthen-ending/SKILL.md
git commit -m "chore(creative-writing): deprecate /strengthen-ending skill"
```

---

### Task 10: Add Deprecation to /remove-ai-tells

**Files:**
- Modify: `plugins/creative-writing/skills/remove-ai-tells/SKILL.md`

**Step 1: Update description in frontmatter**

```yaml
description: "[DEPRECATED] Use /write --mode clean instead. This skill will be removed in v2.0. Remove AI writing patterns."
```

**Step 2: Add deprecation header**

```markdown
# ⚠️ DEPRECATED - Use `/write --mode clean` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/write` with clean mode:
- `/write` then paste content with AI patterns (auto-detects clean mode)
- `/write --mode clean @file.md` (explicit clean mode)

---

# Original Skill Documentation
```

**Step 3: Commit**

```bash
git add plugins/creative-writing/skills/remove-ai-tells/SKILL.md
git commit -m "chore(creative-writing): deprecate /remove-ai-tells skill"
```

---

### Task 11: Update Creative Writing README.md

**Files:**
- Modify: `plugins/creative-writing/README.md`

**Step 1: Read existing README**

```bash
cat plugins/creative-writing/README.md
```

**Step 2: Update Skills section**

Replace the Skills section with:

```markdown
## Skills

### Current Skills (v1.1.0+)

- `/write` - Generate or refine content (replaces edit-draft, generate-content, improve-opening, strengthen-ending, remove-ai-tells)
- `/review` - Get feedback without rewrites
- `/configure` - Create personalized style guide (formerly generate-style-guide)

### Deprecated Skills (Removed in v2.0)

<details>
<summary>Click to see deprecated skills</summary>

These skills still work but will be removed in v2.0.0:
- `/edit-draft` → Use `/write` instead
- `/generate-content` → Use `/write` instead
- `/improve-opening` → Use `/write --mode opening`
- `/strengthen-ending` → Use `/write --mode ending`
- `/remove-ai-tells` → Use `/write --mode clean`

</details>
```

**Step 3: Verify changes**

```bash
git diff plugins/creative-writing/README.md
```

Expected: Shows skills section updated

**Step 4: Commit**

```bash
git add plugins/creative-writing/README.md
git commit -m "docs(creative-writing): update README with new skills"
```

---

### Task 12: Update Creative Writing CHANGELOG.md

**Files:**
- Modify: `plugins/creative-writing/CHANGELOG.md`

**Step 1: Read existing changelog**

```bash
cat plugins/creative-writing/CHANGELOG.md | head -30
```

**Step 2: Add v1.1.0 entry at top**

Add this at the top of the changelog:

```markdown
## [1.1.0] - 2025-12-25

### Added
- New `/write` skill consolidating 5 content operations (edit-draft, generate-content, improve-opening, strengthen-ending, remove-ai-tells)
- Progressive disclosure pattern for style guide loading
- `writing-patterns.md` reference file for AI pattern detection
- `style-guide-loader.md` for explicit chunk routing
- Mode auto-detection based on content characteristics

### Changed
- `/configure` renamed from `/generate-style-guide` (old name still works via skill alias)
- `/review` enhanced with writing-patterns.md reference for consistent feedback

### Deprecated
- `/edit-draft` - Use `/write` instead (removed in v2.0.0)
- `/generate-content` - Use `/write` instead (removed in v2.0.0)
- `/improve-opening` - Use `/write --mode opening` (removed in v2.0.0)
- `/strengthen-ending` - Use `/write --mode ending` (removed in v2.0.0)
- `/remove-ai-tells` - Use `/write --mode clean` (removed in v2.0.0)

Deprecated skills will be removed in v2.0.0 (minimum 4 weeks from this release).
```

**Step 3: Verify changes**

```bash
git diff plugins/creative-writing/CHANGELOG.md
```

Expected: Shows v1.1.0 entry added

**Step 4: Commit**

```bash
git add plugins/creative-writing/CHANGELOG.md
git commit -m "docs(creative-writing): add v1.1.0 changelog entry"
```

---

## Part 2: ASCII Art Plugin

### Task 13: Create font-loader.md Reference

**Files:**
- Create: `plugins/ascii-art/skills/text/font-loader.md`

**Step 1: Create skills/text directory**

```bash
mkdir -p plugins/ascii-art/skills/text
```

**Step 2: Create font-loader.md**

Create `plugins/ascii-art/skills/text/font-loader.md`:

```markdown
# Font Reference Loader

Maps font style names to font definition files.

## Font File Mapping

| Style Name | File Path | Best For |
|------------|-----------|----------|
| standard | ../../assets/fonts/standard.md | Classic ASCII art, general use |
| block | ../../assets/fonts/block.md | Bold impact, splash screens |
| slant | ../../assets/fonts/slant.md | Dynamic, modern appearance |
| banner | ../../assets/fonts/banner.md | Simple, hash-based letters |
| small | ../../assets/fonts/small.md | Compact, space-constrained |

## Loading Instructions

When `--style` is specified:
1. Look up the style name in the mapping above
2. Read the corresponding font file for character patterns
3. Use those patterns to render the text

## Font File Structure

Each font file contains character definitions:

```
# [Font Name]

## A
[ASCII pattern for letter A]

## B
[ASCII pattern for letter B]

...
```

Extract the pattern for each character in the input text and assemble into the logo.

## Default Behavior

If no `--style` specified: Use standard font.

If style not found in mapping: Show error and list available styles.
```

**Step 3: Verify file created**

```bash
ls -la plugins/ascii-art/skills/text/font-loader.md
```

Expected: File exists

**Step 4: Commit**

```bash
git add plugins/ascii-art/skills/text/font-loader.md
git commit -m "feat(ascii-art): add font-loader reference"
```

---

### Task 14: Create text skill example files

**Files:**
- Create: `plugins/ascii-art/skills/text/examples/logo-examples.md`
- Create: `plugins/ascii-art/skills/text/examples/banner-examples.md`
- Create: `plugins/ascii-art/skills/text/examples/box-examples.md`

**Step 1: Create examples directory**

```bash
mkdir -p plugins/ascii-art/skills/text/examples
```

**Step 2: Create logo-examples.md**

Create `plugins/ascii-art/skills/text/examples/logo-examples.md`:

```markdown
# Logo Examples

Reference examples for ASCII text logos.

## Standard Style

```
  ____  _                 _
 / ___|| | __ _ _   _  __| | ___
| |    | |/ _` | | | |/ _` |/ _ \
| |___ | | (_| | |_| | (_| |  __/
 \____|_|\__,_|\__,_|\__,_|\___|
```

## Block Style

```
 ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗
██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝
██║     ██║     ███████║██║   ██║██║  ██║█████╗
██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝
╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗
 ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
```

## Slant Style

```
   ________                __
  / ____/ /___ ___  ______/ /__
 / /   / / __ `/ / / / __  / _ \
/ /___/ / /_/ / /_/ / /_/ /  __/
\____/_/\__,_/\__,_/\__,_/\___/
```

## Banner Style

```
#####  #        #    #     # ##### ######
#    # #       # #   #     # #    # #
#    # #      #   #  #     # #    # #####
#    # #     #######  #   #  #    # #
#    # #     #     #   # #   #    # #
#####  ##### #     #    #    ##### ######
```

## Small Style

```
 ___ _                _
/ __| |__ _ _  _ __ _| |___
\__ \ / _` | || / _` | / -_)
|___/_\__,_|\_,_\__,_|_\___|
```
```

**Step 3: Create banner-examples.md**

Create `plugins/ascii-art/skills/text/examples/banner-examples.md`:

```markdown
# Banner Examples

Reference examples for decorative banners.

## Simple Border

```
┌─────────────────────────────────┐
│      Welcome to My CLI          │
└─────────────────────────────────┘
```

## Double Border

```
╔═════════════════════════════════╗
║      Welcome to My CLI          ║
╚═════════════════════════════════╝
```

## Rounded Border

```
╭─────────────────────────────────╮
│      Welcome to My CLI          │
╰─────────────────────────────────╯
```

## Heavy Border

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Welcome to My CLI          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Stars Border

```
*************************************
*      Welcome to My CLI           *
*************************************
```
```

**Step 4: Create box-examples.md**

Create `plugins/ascii-art/skills/text/examples/box-examples.md`:

```markdown
# Box Examples

Reference examples for content boxes.

## Simple Box

```
┌─────────────────────────────┐
│ Important Notice            │
│                             │
│ This is a multi-line        │
│ message in a box.           │
└─────────────────────────────┘
```

## Double Box

```
╔═════════════════════════════╗
║ Important Notice            ║
║                             ║
║ This is a multi-line        ║
║ message in a box.           ║
╚═════════════════════════════╝
```

## Rounded Box

```
╭─────────────────────────────╮
│ Important Notice            │
│                             │
│ This is a multi-line        │
│ message in a box.           │
╰─────────────────────────────╯
```

## Heavy Box (for warnings)

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ⚠️  WARNING                  ┃
┃                             ┃
┃ This action cannot be       ┃
┃ undone.                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```
```

**Step 5: Verify files created**

```bash
ls -la plugins/ascii-art/skills/text/examples/
```

Expected: All three example files exist

**Step 6: Commit**

```bash
git add plugins/ascii-art/skills/text/examples/
git commit -m "feat(ascii-art): add text skill example references"
```

---

### Task 15: Create /text Skill SKILL.md

**Files:**
- Create: `plugins/ascii-art/skills/text/SKILL.md`

**Step 1: Create SKILL.md**

Create `plugins/ascii-art/skills/text/SKILL.md`:

```markdown
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
    description: "Text effect: shadow, 3d, outline, gradient, rainbow, neon, glitch, retro"
    required: false
    flag: true
  - name: color
    description: "ANSI color or gradient: red, blue, yellow, green, cyan, magenta, sunset, ocean, matrix"
    required: false
    flag: true
  - name: width
    description: Maximum character width (default: 80)
    required: false
    flag: true
---

# ASCII Text Art

Create decorative ASCII text including logos, banners, boxes, and effects.

## Workflow

**Step 1: Determine Type**

From `--type` flag or auto-detect from content:
- Contains newlines or >50 chars → box
- Multiple words (>2) → banner
- Single word, uppercase → logo
- Default → logo

**Step 2: Load Font or Border Reference**

Read [font-loader.md](font-loader.md) to map `--style` to font file.

For logos:
- standard → [../../assets/fonts/standard.md](../../assets/fonts/standard.md)
- block → [../../assets/fonts/block.md](../../assets/fonts/block.md)
- slant → [../../assets/fonts/slant.md](../../assets/fonts/slant.md)
- banner → [../../assets/fonts/banner.md](../../assets/fonts/banner.md)
- small → [../../assets/fonts/small.md](../../assets/fonts/small.md)

For banners/boxes, reference:
- [examples/banner-examples.md](examples/banner-examples.md)
- [examples/box-examples.md](examples/box-examples.md)

**Step 3: Load Color Reference (if specified)**

If `--color` flag provided, read:
[../../assets/reference/ansi-colors.md](../../assets/reference/ansi-colors.md)

Extract ANSI codes for the requested color or gradient.

**Step 4: Render Base Output**

### Logo Type
- Use character patterns from loaded font file
- Render each character with proper spacing
- Maintain consistent height across all characters
- Apply width constraints if specified

### Banner Type
- Choose border style (simple, double, rounded, heavy, ascii, dashed, dotted, stars)
- Create top border, content line, bottom border
- Center or left-align text based on width
- Reference border patterns from banner-examples.md

### Box Type
- Create complete frame around content
- Support multi-line content with proper wrapping
- Optional title in top border
- Reference box patterns from box-examples.md

**Step 5: Apply Effects (if specified)**

Read effect specifications and apply:
- shadow: Add drop shadow beneath characters
- 3d: Extrude characters for depth
- outline: Hollow outlined letters
- gradient/rainbow: Apply color gradations
- neon: Add glow effect with bright colors
- glitch: Distort with cyberpunk style
- retro: Vintage terminal aesthetic

**Step 6: Apply Colors (if specified)**

Wrap output with ANSI color codes:
- Solid colors: Single code wraps entire output
- Gradients: Apply color progression across lines or characters

**Step 7: Output Result**

Display in code block for proper monospace formatting:

\`\`\`
[ASCII art output]
\`\`\`

## Error Handling

**Empty text**:
```
Please provide text to render.
```

**Unsupported characters**:
```
Some characters couldn't be rendered. ASCII art works best with A-Z, 0-9, and common punctuation.
```

**Text too long for width**:
```
Text exceeds width limit. Try --style small or --width 120, or break into multiple lines.
```

**Unknown style**:
```
Style '[style]' not recognized. Available: standard, block, slant, banner, small (for logos) or simple, double, rounded, heavy (for banners/boxes).
```

## Examples

**Generate logo:**
```
/text "Claude Code" --type logo --style block
```

**Create banner:**
```
/text "Welcome!" --type banner --style rounded --color cyan
```

**Frame content in box:**
```
/text "Important Notice\nThis is a multi-line message" --type box --style double --color red
```

**Add effects:**
```
/text "NEON" --style block --effect neon --color matrix
```

**Constrain width:**
```
/text "Long Application Name" --style small --width 60
```

## Tips

- **Logos**: Use block style for maximum impact, small for space constraints
- **Banners**: Rounded style for friendly tone, heavy for warnings
- **Boxes**: Double borders for emphasis, simple for general use
- **Effects**: Combine with colors for enhanced visual impact
- **Width**: 80 chars fits most terminals, 120 for wide displays
```

**Step 2: Verify skill structure**

```bash
ls -la plugins/ascii-art/skills/text/
```

Expected: SKILL.md, font-loader.md, examples/ directory

**Step 3: Commit**

```bash
git add plugins/ascii-art/skills/text/SKILL.md
git commit -m "feat(ascii-art): add /text consolidated skill"
```

---

### Task 16: Create diagram-patterns.md Reference

**Files:**
- Create: `plugins/ascii-art/skills/diagrams/diagram-patterns.md`

**Step 1: Create skills/diagrams directory**

```bash
mkdir -p plugins/ascii-art/skills/diagrams
```

**Step 2: Create diagram-patterns.md**

Create `plugins/ascii-art/skills/diagrams/diagram-patterns.md`:

```markdown
# Diagram Pattern Reference

Box drawing characters and layout patterns for ASCII diagrams.

## Box Drawing Character Sets

### Simple (default)
```
Corners: ┌ ┐ └ ┘
Lines:   ─ │
T-joins: ├ ┤ ┬ ┴
Cross:   ┼
```

### Double
```
Corners: ╔ ╗ ╚ ╝
Lines:   ═ ║
T-joins: ╠ ╣ ╦ ╩
Cross:   ╬
```

### Rounded
```
Corners: ╭ ╮ ╰ ╯
Lines:   ─ │
T-joins: ├ ┤ ┬ ┴
Cross:   ┼
```

### Heavy
```
Corners: ┏ ┓ ┗ ┛
Lines:   ━ ┃
T-joins: ┣ ┫ ┳ ┻
Cross:   ╋
```

### ASCII-only (maximum compatibility)
```
Corners: + + + +
Lines:   - |
T-joins: + + + +
Cross:   +
```

## Arrow and Connector Symbols

### Horizontal Arrows
```
Right:  ─▶ ──▶ ───▶ ────▶
Left:   ◀─ ◀── ◀─── ◀────
Both:   ◀──▶ ◀───▶
```

### Vertical Arrows
```
Down:   │
        ▼

Up:     ▲
        │

Both:   ▲
        │
        ▼
```

### Diagonal Connectors
```
Tree branches:
  └── child
  ├── child

Flow splits:
     ┌─▶ path1
  ───┤
     └─▶ path2
```

## Layout Patterns

### Flowchart Node Spacing

**Horizontal layout:**
```
[Node width: 10-20 chars]
[Spacing between nodes: 4-6 chars]

┌──────────┐     ┌──────────┐     ┌──────────┐
│  Node A  │────▶│  Node B  │────▶│  Node C  │
└──────────┘     └──────────┘     └──────────┘
```

**Vertical layout:**
```
[Vertical spacing: 1 blank line]

┌──────────┐
│  Node A  │
└──────────┘
      │
      ▼
┌──────────┐
│  Node B  │
└──────────┘
```

### Tree Node Spacing

**Binary tree:**
```
        Root
         │
    ┌────┴────┐
    │         │
  Left      Right
    │         │
 ┌──┴──┐   ┌─┴──┐
 │     │   │    │
 L1   L2   R1   R2
```

**Wide tree:**
```
           Root
            │
  ┌─────┬───┴───┬─────┐
  │     │       │     │
Child1 Child2 Child3 Child4
```

### Table Column Sizing

**Auto-sizing algorithm:**
1. Measure longest content in each column
2. Add 2 chars padding (1 each side)
3. Minimum width: 8 chars
4. Maximum width: 30 chars (truncate with ...)

**Example:**
```
Content: "Name", "Alice" → Column width: 7
Content: "Description", "A very long..." → Column width: 20 (truncated)

┌─────────┬────────────────────┐
│  Name   │    Description     │
├─────────┼────────────────────┤
│  Alice  │ A very long desc...│
└─────────┴────────────────────┘
```

### Architecture Layer Grouping

**Horizontal layers:**
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Presentation Layer       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
              │
              ▼
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         Business Layer          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
              │
              ▼
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          Data Layer             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

**Vertical layers:**
```
┌─────────┐  ┌─────────┐  ┌─────────┐
│  Web UI │  │   API   │  │ Database│
│         │─▶│ Gateway │─▶│         │
└─────────┘  └─────────┘  └─────────┘
```

### Sequence Diagram Lifelines

```
Actor spacing: 12-15 chars between actors

  ActorA        ActorB        ActorC
    │             │             │
    │──message───▶│             │
    │             │──request───▶│
    │             │◀──response──│
    │◀──result────│             │
    │             │             │
```

## Decision Nodes

### Diamond (compact):
```
     ┌─yes─▶
  ◇──┤
     └─no──▶
```

### Box (clear):
```
┌──────────┐
│ condition│
│   met?   │
└──┬───┬───┘
   │   │
  yes  no
   │   │
   ▼   ▼
```

## Rendering Guidelines

1. **Consistent spacing**: Maintain uniform gaps between elements
2. **Alignment**: Ensure boxes and connectors align properly
3. **Balance**: Center nodes when possible, avoid cramming
4. **Clarity**: Prefer readability over density
5. **Width**: Aim for 80 chars total width, max 120 for complex diagrams
6. **Labels**: Keep node labels concise (10-15 chars), truncate if needed
7. **Whitespace**: Use blank lines to separate diagram sections
```

**Step 3: Verify file created**

```bash
ls -la plugins/ascii-art/skills/diagrams/diagram-patterns.md
```

Expected: File exists

**Step 4: Commit**

```bash
git add plugins/ascii-art/skills/diagrams/diagram-patterns.md
git commit -m "feat(ascii-art): add diagram-patterns reference"
```

---

### Task 17: Create /diagrams Skill SKILL.md

**Files:**
- Create: `plugins/ascii-art/skills/diagrams/SKILL.md`

**Step 1: Create SKILL.md**

Create `plugins/ascii-art/skills/diagrams/SKILL.md`:

```markdown
---
name: diagrams
description: Create ASCII diagrams including flowcharts, trees, tables, and architecture visualizations. Use when visualizing flows, hierarchies, data structures, or system architecture.
args:
  - name: description
    description: What to diagram or visualize (natural language description)
    required: true
  - name: type
    description: "Diagram type: flowchart, tree, table, architecture, sequence (default: auto-detect)"
    required: false
    flag: true
  - name: direction
    description: "Layout direction: horizontal, vertical (default: horizontal for flowcharts, vertical for trees)"
    required: false
    flag: true
  - name: style
    description: "Box style: simple, double, rounded, heavy (default: simple)"
    required: false
    flag: true
---

# ASCII Diagrams

Create structural diagrams for visualizing flows, hierarchies, and architectures.

## Workflow

**Step 1: Parse Description**

Extract diagram structure from natural language:
- Identify nodes/entities
- Identify relationships/connections
- Detect hierarchy or sequence
- Extract labels and annotations

**Step 2: Detect Diagram Type**

If `--type` not specified, auto-detect:
- Contains "→" or "then" or "after" → flowchart
- Contains "parent/child" or "under" or hierarchical structure → tree
- Contains rows/columns or tabular data → table
- Contains "system" or "component" or "service" → architecture
- Contains "user/actor" or temporal sequence → sequence

**Step 3: Load Diagram Patterns**

Read [diagram-patterns.md](diagram-patterns.md) for:
- Box drawing characters for the selected style
- Connector symbols
- Layout rules for the diagram type

Reference examples:
[../../assets/examples/diagrams.md](../../assets/examples/diagrams.md)

**Step 4: Generate Diagram by Type**

### Flowchart
```
Parse: Node1 → Node2 → Node3 (conditional) → Node4

Render:
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  Node1   │────▶│  Node2   │────▶│  Node3   │────▶│  Node4   │
└──────────┘     └──────────┘     │  (cond)  │     └──────────┘
                                  └──────────┘
```

Layout rules:
- Horizontal: nodes side-by-side with arrows between
- Vertical: nodes stacked with downward arrows
- Decisions: diamond or labeled box with multiple exits
- Use connector arrows: ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ ▶ ▼

### Tree
```
Parse: Root > Child1, Child2 > Grandchild1, Grandchild2

Render:
         Root
          │
    ┌─────┴─────┐
    │           │
  Child1     Child2
    │           │
    │      ┌────┴────┐
    │      │         │
Grandchild1  Grandchild2
```

Layout rules:
- Root at top (or left for horizontal)
- Branches use ├ ┤ └ ┘ ┬ ┴ │ ─
- Balanced spacing for visual clarity
- Align children under parents

### Table
```
Parse: Header1, Header2, Header3 | Row1Col1, Row1Col2, Row1Col3

Render:
┌───────────┬───────────┬───────────┐
│  Header1  │  Header2  │  Header3  │
├───────────┼───────────┼───────────┤
│ Row1Col1  │ Row1Col2  │ Row1Col3  │
├───────────┼───────────┼───────────┤
│ Row2Col1  │ Row2Col2  │ Row2Col3  │
└───────────┴───────────┴───────────┘
```

Layout rules:
- Calculate column widths from content
- Header row with separator
- Align text (left, right, center) as appropriate
- Use box drawing: ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘ │ ─

### Architecture
```
Parse: Frontend → API Gateway → Backend Services → Database

Render:
┏━━━━━━━━━━━┓     ┏━━━━━━━━━━━┓     ┏━━━━━━━━━━━━━━━┓     ┏━━━━━━━━━━┓
┃ Frontend  ┃────▶┃    API    ┃────▶┃    Backend    ┃────▶┃ Database ┃
┃   (React) ┃     ┃  Gateway  ┃     ┃   Services    ┃     ┃ (Postgres┃
┗━━━━━━━━━━━┛     ┗━━━━━━━━━━━┛     ┗━━━━━━━━━━━━━━━┛     ┗━━━━━━━━━━┛
```

Layout rules:
- System components in boxes (heavy borders for emphasis)
- Arrows show data/control flow
- Optional: add labels on arrows
- Support for layers (vertical grouping)

### Sequence
```
Parse: User → System: login | System → Database: verify | Database → System: success

Render:
  User         System       Database
    │            │              │
    │───login───▶│              │
    │            │───verify────▶│
    │            │◀──success────│
    │◀──token────│              │
```

Layout rules:
- Actors/systems as headers
- Vertical lifelines (│)
- Horizontal arrows for messages (───▶)
- Return arrows (◀───)
- Time flows top to bottom

**Step 5: Apply Box Style**

If `--style` specified, use corresponding box drawing characters from diagram-patterns.md:
- simple: ┌─┐ │ └─┘
- double: ╔═╗ ║ ╚═╝
- rounded: ╭─╮ │ ╰─╯
- heavy: ┏━┓ ┃ ┗━┛

**Step 6: Output Result**

Display in code block:

\`\`\`
[Diagram output]
\`\`\`

## Error Handling

**Unclear structure**:
```
Couldn't parse diagram structure clearly. Try being more explicit:
- "A → B → C" for flowcharts
- "Parent > Child1, Child2" for trees
- "Col1, Col2 | Row1Val1, Row1Val2" for tables
```

**Too complex**:
```
Diagram has [N] nodes which may not render well. Consider:
- Breaking into multiple diagrams
- Simplifying to key components
- Using --direction horizontal for better fit
```

**Missing connections**:
```
Some nodes appear disconnected. Verify relationships are specified.
```

## Examples

**Flowchart:**
```
/diagrams "User clicks button → Validate input → Save to database → Show success message"
```

**Tree:**
```
/diagrams "Company > Engineering, Sales > Frontend Team, Backend Team, Customer Success" --type tree
```

**Architecture:**
```
/diagrams "Web App → Load Balancer → App Servers → Cache Layer → Database" --type architecture --style heavy
```

**Table:**
```
/diagrams "Feature, Status, Owner | Dark Mode, Complete, Alice | Search, In Progress, Bob" --type table
```

**Sequence:**
```
/diagrams "User → API: get data, API → DB: query, DB → API: results, API → User: response" --type sequence --direction vertical
```

## Tips

- **Flowcharts**: Keep to 5-7 nodes per diagram for clarity
- **Trees**: Balance depth vs. breadth (max 4 levels recommended)
- **Tables**: Use for structured data, not complex relationships
- **Architecture**: Show high-level components, not every detail
- **Sequence**: Order matters - specify temporal flow clearly
- **Direction**: Horizontal for wide diagrams, vertical for deep ones
- **Style**: Heavy borders for architecture, simple for flowcharts
```

**Step 2: Verify skill structure**

```bash
ls -la plugins/ascii-art/skills/diagrams/
```

Expected: SKILL.md, diagram-patterns.md

**Step 3: Commit**

```bash
git add plugins/ascii-art/skills/diagrams/SKILL.md
git commit -m "feat(ascii-art): add /diagrams consolidated skill"
```

---

### Task 18: Add Deprecation to ASCII Art Skills

**Files:**
- Modify: `plugins/ascii-art/skills/generate-logo/SKILL.md`
- Modify: `plugins/ascii-art/skills/generate-banner/SKILL.md`
- Modify: `plugins/ascii-art/skills/generate-box/SKILL.md`
- Modify: `plugins/ascii-art/skills/text-effects/SKILL.md`
- Modify: `plugins/ascii-art/skills/generate-diagram/SKILL.md`
- Modify: `plugins/ascii-art/skills/generate-art/SKILL.md`

**Step 1: Deprecate /generate-logo**

Update frontmatter description and add header:

```yaml
description: "[DEPRECATED] Use /text instead. This skill will be removed in v2.0. Generate ASCII text logos."
```

Add header:
```markdown
# ⚠️ DEPRECATED - Use `/text` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/text` for logos:
- `/text "MyApp"` (auto-detects logo type)
- `/text "MyApp" --type logo --style block`

---

# Original Skill Documentation
```

**Step 2: Deprecate /generate-banner**

```yaml
description: "[DEPRECATED] Use /text --type banner instead. This skill will be removed in v2.0. Create decorative banners."
```

Header:
```markdown
# ⚠️ DEPRECATED - Use `/text --type banner` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/text` with banner type:
- `/text "Welcome!" --type banner --style rounded`

---

# Original Skill Documentation
```

**Step 3: Deprecate /generate-box**

```yaml
description: "[DEPRECATED] Use /text --type box instead. This skill will be removed in v2.0. Wrap content in ASCII boxes."
```

Header:
```markdown
# ⚠️ DEPRECATED - Use `/text --type box` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/text` with box type:
- `/text "Notice\nMulti-line" --type box --style double`

---

# Original Skill Documentation
```

**Step 4: Deprecate /text-effects**

```yaml
description: "[DEPRECATED] Use /text --effect instead. This skill will be removed in v2.0. Apply text effects."
```

Header:
```markdown
# ⚠️ DEPRECATED - Use `/text --effect [name]` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/text` with effect parameter:
- `/text "NEON" --effect neon --color matrix`

---

# Original Skill Documentation
```

**Step 5: Deprecate /generate-diagram**

```yaml
description: "[DEPRECATED] Use /diagrams instead. This skill will be removed in v2.0. Create ASCII diagrams."
```

Header:
```markdown
# ⚠️ DEPRECATED - Use `/diagrams` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**: Use `/diagrams`:
- `/diagrams "A → B → C" --type flowchart`

---

# Original Skill Documentation
```

**Step 6: Deprecate /generate-art**

```yaml
description: "[DEPRECATED] Use /diagrams or /text instead. This skill will be removed in v2.0. Generate ASCII art."
```

Header:
```markdown
# ⚠️ DEPRECATED - Use `/diagrams` or `/text` Instead

This skill is deprecated and will be removed in v2.0.0.

**Migration**:
- For structural art (diagrams, flows): Use `/diagrams`
- For decorative art (text, logos): Use `/text`

---

# Original Skill Documentation
```

**Step 7: Commit all deprecations**

```bash
git add plugins/ascii-art/skills/generate-logo/SKILL.md
git add plugins/ascii-art/skills/generate-banner/SKILL.md
git add plugins/ascii-art/skills/generate-box/SKILL.md
git add plugins/ascii-art/skills/text-effects/SKILL.md
git add plugins/ascii-art/skills/generate-diagram/SKILL.md
git add plugins/ascii-art/skills/generate-art/SKILL.md
git commit -m "chore(ascii-art): deprecate old skills"
```

---

### Task 19: Update ASCII Art README.md

**Files:**
- Modify: `plugins/ascii-art/README.md`

**Step 1: Read existing README**

```bash
cat plugins/ascii-art/README.md
```

**Step 2: Update Features/Skills section**

Replace the skills table with:

```markdown
## Features

### Current Skills (v1.2.0+)

| Skill | Description |
|-------|-------------|
| `/text` | Create ASCII text art - logos, banners, boxes, and effects (replaces generate-logo, generate-banner, generate-box, text-effects) |
| `/diagrams` | Create diagrams - flowcharts, trees, tables, architecture (replaces generate-diagram, generate-art) |

### Deprecated Skills (Removed in v2.0)

<details>
<summary>Click to see deprecated skills</summary>

These skills still work but will be removed in v2.0.0:
- `/generate-logo` → Use `/text` instead
- `/generate-banner` → Use `/text --type banner`
- `/generate-box` → Use `/text --type box`
- `/text-effects` → Use `/text --effect [name]`
- `/generate-diagram` → Use `/diagrams`
- `/generate-art` → Use `/diagrams` or `/text`

</details>
```

**Step 3: Verify changes**

```bash
git diff plugins/ascii-art/README.md
```

Expected: Shows features section updated

**Step 4: Commit**

```bash
git add plugins/ascii-art/README.md
git commit -m "docs(ascii-art): update README with new skills"
```

---

### Task 20: Update ASCII Art CHANGELOG.md

**Files:**
- Modify: `plugins/ascii-art/CHANGELOG.md`

**Step 1: Add v1.2.0 entry**

Add this at the top of the changelog:

```markdown
## [1.2.0] - 2025-12-25

### Added
- New `/text` skill consolidating 4 text operations (generate-logo, generate-banner, generate-box, text-effects)
- New `/diagrams` skill consolidating 2 diagram operations (generate-diagram, generate-art)
- Progressive disclosure pattern for asset file loading
- `font-loader.md` reference mapping styles to font files
- `diagram-patterns.md` reference for box drawing characters and layouts
- Example reference files for logos, banners, and boxes
- Type auto-detection based on content characteristics

### Changed
- Font files now explicitly referenced by skills (progressive disclosure)
- Color references now loaded on-demand when --color specified

### Deprecated
- `/generate-logo` - Use `/text` instead (removed in v2.0.0)
- `/generate-banner` - Use `/text --type banner` (removed in v2.0.0)
- `/generate-box` - Use `/text --type box` (removed in v2.0.0)
- `/text-effects` - Use `/text --effect [name]` (removed in v2.0.0)
- `/generate-diagram` - Use `/diagrams` (removed in v2.0.0)
- `/generate-art` - Use `/diagrams` or `/text` (removed in v2.0.0)

Deprecated skills will be removed in v2.0.0 (minimum 4 weeks from this release).
```

**Step 2: Commit**

```bash
git add plugins/ascii-art/CHANGELOG.md
git commit -m "docs(ascii-art): add v1.2.0 changelog entry"
```

---

## Part 3: Final Steps

### Task 21: Create Consolidated Commit

**Step 1: Verify all changes staged**

```bash
git status
```

Expected: Clean working tree, all changes committed

**Step 2: Review commit log**

```bash
git log --oneline -20
```

Expected: See all individual commits from tasks 1-20

**Step 3: Create summary of changes**

Document what was accomplished:
- Creative writing: 3 new files, 7 deprecations, 2 doc updates
- ASCII art: 7 new files, 6 deprecations, 2 doc updates

---

### Task 22: Test New Skills (Manual Verification)

**This task requires manual testing - provide test commands**

**Creative Writing Tests:**

```bash
# Test /write skill exists
/skill list | grep write

# Test mode auto-detection
/write "test topic"  # Should detect draft mode

# Test style guide loading
/write @test-content.md --mode clean

# Test review enhancement
/review @test-content.md

# Test configure rename
/configure
```

**ASCII Art Tests:**

```bash
# Test /text skill exists
/skill list | grep text

# Test type auto-detection
/text "TEST"  # Should detect logo type

# Test font loading
/text "TEST" --style block

# Test diagrams skill
/diagrams "A → B → C"

# Test diagram type detection
/diagrams "Root > Child1, Child2" --type tree
```

**Step 1: Document test results**

Create `docs/plans/test-results.md` with outcomes of manual tests.

**Step 2: Commit test documentation**

```bash
git add docs/plans/test-results.md
git commit -m "docs: add manual test results for consolidated skills"
```

---

## Execution Summary

**Total Tasks:** 22
**Estimated Time:** 4-6 hours

**Files Created:**
- Creative Writing: 3 new files (writing-patterns.md, style-guide-loader.md, write/SKILL.md)
- ASCII Art: 7 new files (font-loader.md, 3 example files, diagram-patterns.md, text/SKILL.md, diagrams/SKILL.md)

**Files Modified:**
- Creative Writing: 7 skill deprecations, 2 doc updates (README, CHANGELOG)
- ASCII Art: 6 skill deprecations, 2 doc updates (README, CHANGELOG)

**Git Commits:** 22 individual commits (one per task)

---

## Next Steps

After completing this plan:

1. **Manual Testing:** Test all new skills thoroughly
2. **User Documentation:** Update GETTING_STARTED.md files if needed
3. **Version Tagging:** Tag releases (creative-writing v1.1.0, ascii-art v1.2.0)
4. **Marketplace Update:** Update marketplace listings
5. **Monitor Feedback:** Track user adoption and issues
6. **Plan v2.0:** Schedule deprecated skill removal (4+ weeks out)
