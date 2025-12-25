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
