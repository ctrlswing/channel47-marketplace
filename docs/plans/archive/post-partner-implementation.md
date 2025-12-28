# Post Partner Implementation Plan

Replace the `creative-writing` plugin with `post-partner` - a thought partner for turning raw material into posts worth sharing.

---

## Overview

**What changes:**
- Remove `plugins/creative-writing/` entirely (14 files)
- Create `plugins/post-partner/` with new structure
- Update `marketplace.json` to replace creative-writing entry

**Core difference from creative-writing:**
- Creative-writing: Generates/rewrites content for you
- Post-partner: Guides you through thinking, outputs a brief (not the post itself)

---

## File Structure

```
plugins/post-partner/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── skills/
│   └── post/
│       ├── SKILL.md                  # Main skill definition
│       ├── conversation-guide.md     # Reference for adaptive conversation moves
│       └── brief-template.md         # Brief artifact structure
├── README.md                         # Plugin documentation
├── GETTING_STARTED.md                # User guide
├── CHANGELOG.md                      # Version history
└── LICENSE                           # MIT License
```

---

## Implementation Tasks

### Phase 1: Remove Creative Writing Plugin

1. **Delete `plugins/creative-writing/` directory**
   - All 14 files removed

2. **Update `marketplace.json`**
   - Remove creative-writing entry
   - Add post-partner entry with new metadata

---

### Phase 2: Create Plugin Infrastructure

3. **Create `.claude-plugin/plugin.json`**
   ```json
   {
     "name": "post-partner",
     "version": "1.0.0",
     "description": "A thought partner for turning raw material into posts worth sharing",
     "author": {
       "name": "Jackson",
       "url": "https://channel47.dev"
     },
     "homepage": "https://channel47.dev/plugins/post-partner",
     "repository": "https://github.com/ctrlswing/channel47-marketplace",
     "license": "MIT",
     "keywords": ["writing", "posts", "content", "thinking", "briefs"]
   }
   ```

4. **Create `LICENSE`** (MIT)

---

### Phase 3: Create Main Skill

5. **Create `skills/post/SKILL.md`**

   Core elements from design doc:

   **YAML Frontmatter:**
   ```yaml
   ---
   name: post
   description: Turn raw material (logs, transcripts, drafts, ideas) into a post brief through guided conversation
   args:
     - name: material
       description: Raw material - Claude Code log, transcript, draft, or idea (paste or @file)
       required: false
   ---
   ```

   **Workflow Sections:**

   a. **Input Assessment**
      - Dense material (logs, transcripts) → Surface 1-2 candidate insights
      - Sparse material (rough idea) → Ask opening question
      - Draft post → Skip to pressure testing

   b. **Adaptive Conversation**
      - Track what's established vs open
      - Available moves: surface insight, pressure test, offer candidate, reflect back, ask deeper, challenge gently, sit back
      - Read conversational tempo (short answers = do more lifting; riffing = stay back)

   c. **The Take Question**
      - If assertive: "What's the claim you're making?"
      - If exploratory: "What are you noticing that others might miss?"
      - If uncertain: "What question are you sitting with?"
      - If reactive: "What do you want people to reconsider?"

   d. **Brief Components** (destination, not path)
      - Raw material (excerpt/summary)
      - The insight (1-2 sentences)
      - Why it matters (who cares, why)
      - The audience (specific)
      - Your take (labeled: claim/observation/question/provocation)
      - The entry point (angle, not finished hook)

   e. **Edge Cases**
      - No post here: Recognize and exit gracefully
      - Multiple threads: Surface options, let user pick, note others for later

   f. **Before Delivery**
      - Check: "Here's what I've got—does this feel right, or is something off?"
      - If off → stay in conversation
      - If confirmed → deliver artifact

6. **Create `skills/post/conversation-guide.md`**

   Reference document for conversation behaviors:
   - Tone: Peer slightly further along, not coach/editor/cheerleader
   - No "Great!" or "Love that" - reactions earned
   - Direct questions, not softened
   - Comfortable saying "I don't think that's the interesting part"
   - Comfortable saying "That's it—that's the post"
   - Signals for "no post here" (redirecting, shorter answers, explicit uncertainty)
   - Exit language: "I'm not sure there's a post here yet..."

7. **Create `skills/post/brief-template.md`**

   Artifact structure template:
   ```markdown
   # Post Brief

   ## Raw Material
   [Excerpt or summary of starting material]

   ## The Insight
   [The interesting thing, 1-2 sentences]

   ## Why It Matters
   [Who cares and why]

   ## The Audience
   [Who this is for, specifically]

   ## Your Take
   **Type:** [Claim | Observation | Question | Provocation]

   [The take itself]

   ## The Entry Point
   [The angle—not a finished hook, just the way in]

   ---

   ## Other Threads (if applicable)
   [Brief notes on alternative angles for future consideration]
   ```

---

### Phase 4: Documentation

8. **Create `README.md`**
   - What it does (thought partner, not content generator)
   - The problem it solves (hollow AI output vs slow solo thinking)
   - Installation
   - Quick start example
   - What you get (the brief)
   - Positioning: "The brief is proof you did the thinking"

9. **Create `GETTING_STARTED.md`**
   - First use examples by material type:
     - Claude Code log
     - Voice memo transcript
     - Rough idea
     - Draft post
   - What to expect in the conversation
   - How briefs work (queue them up, write later)
   - Exiting gracefully when there's no post

10. **Create `CHANGELOG.md`**
    ```markdown
    # Changelog

    ## [1.0.0] - 2024-XX-XX

    ### Added
    - Initial release
    - `/post` skill for guided post brief creation
    - Adaptive conversation based on input type
    - Support for multiple input formats (logs, transcripts, drafts, ideas)
    - Brief artifact with structured components
    - Graceful exit for "no post here" scenarios
    ```

---

### Phase 5: Registry Update

11. **Update `marketplace.json`**

    Replace creative-writing entry:
    ```json
    {
      "name": "post-partner",
      "source": "./plugins/post-partner",
      "description": "A thought partner for turning raw material into posts worth sharing",
      "version": "1.0.0",
      "author": {
        "name": "Jackson"
      },
      "category": "writing",
      "tags": ["writing", "posts", "content", "thinking", "briefs", "social"]
    }
    ```

---

## Key Design Decisions

### 1. Single Skill (`/post`) vs Multiple Skills

**Decision:** Single `/post` skill

**Rationale:**
- The design doc describes one unified flow, not separate operations
- The conversation adapts to input—no need for user to pick modes
- Simpler mental model: one command, one purpose

### 2. Reference Files

**Decision:** Two reference files (`conversation-guide.md`, `brief-template.md`)

**Rationale:**
- Keeps SKILL.md focused on workflow
- Conversation guide loaded for tone/behavior reference
- Brief template ensures consistent artifact structure
- Progressive disclosure pattern from other plugins

### 3. No Settings File

**Decision:** No `post-partner.local.md.template`

**Rationale:**
- Post Partner is intentionally opinionated
- The conversation adapts to you in real-time
- No persistent preferences needed
- Can revisit if users request customization

### 4. Brief as Markdown Artifact

**Decision:** Output brief as markdown in conversation

**Rationale:**
- Design doc says "artifact containing the post brief"
- User can copy, save, or queue it
- No file creation needed (matches philosophy of not over-engineering)

---

## Validation Criteria

Before marking complete:

- [ ] `/post` invokes correctly with no arguments
- [ ] `/post @file` works with file reference
- [ ] Pasted material is handled appropriately
- [ ] Dense material triggers insight surfacing
- [ ] Sparse material triggers opening question
- [ ] Draft material skips to pressure testing
- [ ] Conversation adapts to user tempo
- [ ] Brief delivered after confirmation
- [ ] "No post here" exit works gracefully
- [ ] Multiple threads surfaced when present
- [ ] Tone matches design doc (peer, not coach)

---

## Files to Create (Total: 8)

| File | Purpose |
|------|---------|
| `.claude-plugin/plugin.json` | Plugin manifest |
| `skills/post/SKILL.md` | Main skill definition |
| `skills/post/conversation-guide.md` | Tone and behavior reference |
| `skills/post/brief-template.md` | Artifact structure |
| `README.md` | Plugin overview |
| `GETTING_STARTED.md` | User guide |
| `CHANGELOG.md` | Version history |
| `LICENSE` | MIT license |

## Files to Delete (Total: 14)

All files in `plugins/creative-writing/`

## Files to Modify (Total: 1)

`marketplace.json` - Replace creative-writing entry with post-partner
