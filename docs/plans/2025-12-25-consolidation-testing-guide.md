# Plugin Skill Consolidation - Testing Guide

## Overview

This document provides manual testing steps for verifying the consolidated skills in both creative-writing and ascii-art plugins.

**Date:** 2025-12-25
**Changes:** v2.0.0 releases for both plugins with breaking changes

## Prerequisites

Ensure the plugins are properly installed and skills are discoverable:

```bash
# Verify plugin directories exist
ls plugins/creative-writing/skills/
ls plugins/ascii-art/skills/
```

Expected output:
- **creative-writing**: configure, review-writing, write
- **ascii-art**: diagrams, text

## Creative Writing Plugin Tests

### Test 1: /write Skill - Draft Mode

**Command:**
```bash
/write "The benefits of progressive disclosure in LLM plugins"
```

**Expected behavior:**
- Auto-detects draft mode (no content provided)
- Loads full style guide
- Generates new content following voice principles
- Output includes honest opening, clear reasoning, genuine ending

**Verification:**
- Content should avoid AI patterns (em-dashes, hype words, performative openings)
- Should be prose, not lists

---

### Test 2: /write Skill - Edit Mode

**Command:**
```bash
/write "This is a game-changer for developers—it's absolutely revolutionary and will unlock massive potential." --mode edit
```

**Expected behavior:**
- Detects edit mode (explicit flag or content >100 words)
- Loads writing-patterns.md reference
- Removes AI patterns: "game-changer", "revolutionary", "unlock", em-dash, hype words
- Preserves core meaning

**Verification:**
- AI patterns should be replaced with concrete language
- No em-dashes or excessive colons

---

### Test 3: /write Skill - Opening Mode

**Command:**
```bash
/write "I'm excited to share this amazing technique with you today!" --mode opening
```

**Expected behavior:**
- Detects opening mode (short content or explicit flag)
- Loads Voice Principles and Patterns to Avoid
- Replaces performative opening with honest admission or observation

**Verification:**
- No "I'm excited to share" or similar performative patterns
- Opening should be genuine, not authoritative

---

### Test 4: /write Skill - Clean Mode

**Command:**
```bash
/write "The solution—which works well—unlocks potential. What's the takeaway? Let me know in the comments!" --mode clean
```

**Expected behavior:**
- Detects clean mode (AI patterns present)
- Loads full writing-patterns.md
- Removes: em-dashes, "unlocks", rhetorical question, generic CTA
- Minimal structural changes

**Verification:**
- All flagged patterns removed
- Content structure mostly preserved

---

### Test 5: /review Skill

**Command:**
```bash
/review "Your content here with some AI patterns—like em-dashes and game-changing hype words."
```

**Expected behavior:**
- Loads writing-patterns.md for pattern detection
- Provides feedback without rewriting
- Identifies specific AI patterns with examples
- Organized in categories: Opening, Reasoning, Structure, Word Choice, Ending, Patterns to Clean, Strengths

**Verification:**
- Feedback includes specific line references
- Notes em-dashes and hype words
- Suggests actionable improvements

---

### Test 6: /configure Skill

**Command:**
```bash
/configure
```

**Expected behavior:**
- Launches interactive questionnaire
- Asks about content formats, tone preferences, audience
- Generates personalized style guide
- Saves to `.claude/creative-writing.local.md`

**Verification:**
- Skill name is "configure" (not "generate-style-guide")
- Prompts are clear and actionable

---

## ASCII Art Plugin Tests

### Test 7: /text Skill - Logo Type

**Command:**
```bash
/text "ACME" --style block
```

**Expected behavior:**
- Auto-detects logo type (single uppercase word)
- Loads font-loader.md
- References ../../assets/fonts/block.md
- Renders logo using block font characters

**Verification:**
- Output uses Unicode block characters (█ ╔ ╗ ╚ ╝)
- Consistent height across letters
- Proper monospace alignment

---

### Test 8: /text Skill - Banner Type

**Command:**
```bash
/text "Welcome to My CLI" --type banner --style rounded
```

**Expected behavior:**
- Auto-detects banner type (multiple words) or uses explicit flag
- Loads banner-examples.md reference
- Creates rounded border with centered text

**Verification:**
- Uses rounded corners (╭ ╮ ╰ ╯)
- Text is centered
- Border is complete

---

### Test 9: /text Skill - Box Type

**Command:**
```bash
/text "Important Notice\nThis is a multi-line message" --type box --style double
```

**Expected behavior:**
- Auto-detects box type (newlines or >50 chars) or uses explicit flag
- Loads box-examples.md reference
- Creates double-border box with multi-line content

**Verification:**
- Uses double borders (╔═╗ ║ ╚═╝)
- Handles newlines correctly
- Proper padding around content

---

### Test 10: /text Skill - Color Support

**Command:**
```bash
/text "SUCCESS" --style block --color green
```

**Expected behavior:**
- Loads ../../assets/reference/ansi-colors.md
- Wraps output with ANSI green color codes
- Renders colored logo

**Verification:**
- Logo appears in green (if terminal supports ANSI colors)
- Color codes don't break formatting

---

### Test 11: /diagrams Skill - Flowchart

**Command:**
```bash
/diagrams "User clicks button → Validate input → Save to database → Show success"
```

**Expected behavior:**
- Auto-detects flowchart type (contains "→" or "then")
- Loads diagram-patterns.md
- Creates horizontal flowchart with arrows

**Verification:**
- Uses box drawing: ┌─┐ │ └─┘ ────▶
- Nodes aligned properly
- Arrows connect nodes

---

### Test 12: /diagrams Skill - Tree

**Command:**
```bash
/diagrams "Company > Engineering, Sales > Frontend Team, Backend Team" --type tree
```

**Expected behavior:**
- Auto-detects tree type (hierarchical structure) or uses explicit flag
- Loads diagram-patterns.md
- Creates vertical tree structure

**Verification:**
- Root at top
- Branches use ├ ┤ └ ┘ ┬ ┴ │ ─
- Children aligned under parents

---

### Test 13: /diagrams Skill - Table

**Command:**
```bash
/diagrams "Feature, Status, Owner | Dark Mode, Complete, Alice | Search, In Progress, Bob" --type table
```

**Expected behavior:**
- Auto-detects table type (contains "|" separators)
- Calculates column widths
- Creates table with header separator

**Verification:**
- Uses box drawing: ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘ │ ─
- Columns properly sized
- Header row separated

---

### Test 14: /diagrams Skill - Architecture

**Command:**
```bash
/diagrams "Frontend → API Gateway → Backend Services → Database" --type architecture --style heavy
```

**Expected behavior:**
- Uses heavy borders (┏━┓ ┃ ┗━┛) for emphasis
- Shows data flow with arrows
- System components in boxes

**Verification:**
- Heavy borders applied
- Components clearly separated
- Flow direction clear

---

## Regression Tests

### Test 15: Verify Deprecated Skills Removed

**Commands:**
```bash
ls plugins/creative-writing/skills/edit-draft 2>/dev/null
ls plugins/creative-writing/skills/generate-content 2>/dev/null
ls plugins/ascii-art/skills/generate-logo 2>/dev/null
```

**Expected output:**
All commands should return "No such file or directory"

**Verification:**
- Old skill directories completely removed
- No orphaned files

---

### Test 16: Verify Reference Files Exist

**Commands:**
```bash
ls plugins/creative-writing/skills/write/writing-patterns.md
ls plugins/creative-writing/skills/write/style-guide-loader.md
ls plugins/ascii-art/skills/text/font-loader.md
ls plugins/ascii-art/skills/diagrams/diagram-patterns.md
```

**Expected output:**
All files exist

**Verification:**
- Reference files are readable
- Content is well-formatted

---

## Performance Tests

### Test 17: Progressive Disclosure Efficiency

**Objective:** Verify that skills only load necessary documentation

**Method:**
1. Monitor skill execution with verbose logging if available
2. Verify that:
   - /write only loads sections specified by mode
   - /text only loads font files when --style specified
   - /diagrams only loads patterns for detected diagram type

**Verification:**
- Token usage is reasonable
- No unnecessary file loading

---

## Documentation Tests

### Test 18: README Accuracy

**Commands:**
```bash
cat plugins/creative-writing/README.md | grep -E "/(write|review|configure)"
cat plugins/ascii-art/README.md | grep -E "/(text|diagrams)"
```

**Expected output:**
- creative-writing README shows 3 skills: /write, /review, /configure
- ascii-art README shows 2 skills: /text, /diagrams

**Verification:**
- No references to deprecated skills
- Examples use new skill names

---

### Test 19: CHANGELOG Completeness

**Commands:**
```bash
cat plugins/creative-writing/CHANGELOG.md | head -50
cat plugins/ascii-art/CHANGELOG.md | head -50
```

**Expected output:**
- Both show v2.0.0 release dated 2025-12-25
- Breaking changes section lists removed skills
- Migration instructions provided

**Verification:**
- Version numbers match
- Migration paths clear

---

## Summary

**Total Tests:** 19
**Categories:**
- Creative Writing: 6 tests
- ASCII Art: 8 tests
- Regression: 2 tests
- Performance: 1 test
- Documentation: 2 tests

**Pass Criteria:**
- All functionality tests execute without errors
- Auto-detection works correctly
- Reference files load properly
- Documentation is accurate
- No deprecated skills remain

**Report Issues:**
Document any failures with:
- Test number and name
- Expected vs. actual behavior
- Error messages
- Environment details

---

## Next Steps After Testing

1. **If all tests pass:**
   - Tag releases: creative-writing v2.0.0, ascii-art v2.0.0
   - Update marketplace listings
   - Document migration guide for existing users

2. **If tests fail:**
   - Document failures
   - Create issues for each failure
   - Fix and re-test
   - Update this testing guide with lessons learned
