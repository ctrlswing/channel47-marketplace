# Brief Template

The artifact structure for Post Partner. Use this format when delivering the final brief.

---

## Template

```markdown
# Post Brief

## Raw Material
[Excerpt or summary of what they started with. Keep it short—enough to remember the source, not a full reproduction.]

## The Insight
[The interesting thing, in 1-2 sentences. This is what makes the post worth writing.]

## Why It Matters
[Who cares about this and why. Be specific about the stakes or relevance.]

## The Audience
[Who this is for, specifically. Not "developers" but "developers who've tried and abandoned type systems." Not "managers" but "first-time managers in their first six months."]

## Your Take
**Type:** [Claim | Observation | Question | Provocation]

[The take itself. This is their point of view on the insight—what they're saying about it.]

## The Entry Point
[The angle for the post. Not a finished hook or opening line—just the way in. "Start with the moment when..." or "Lead with the counterintuitive part..." or "Open with what everyone gets wrong..."]

---

*Other threads: [If multiple angles surfaced during the conversation, note the ones not pursued here. Brief—just enough to remember what they were.]*
```

---

## Component Guidelines

### Raw Material
- Summarize, don't reproduce
- Capture enough that they remember what sparked this
- If it was a Claude Code log, note what the session was about
- If it was a voice memo, capture the core topic

### The Insight
- One to two sentences max
- Should feel like a "huh, that's interesting" moment
- Not a thesis statement—the kernel that makes the post worth reading

### Why It Matters
- Avoid generic stakes ("this is important for the industry")
- Be specific: who would care, what would change for them
- It's okay if the stakes are personal or small

### The Audience
- The more specific, the better
- Bad: "People interested in productivity"
- Good: "People who've read all the productivity advice and still can't make it stick"
- Help them see who they're actually talking to

### Your Take
Label it honestly:
- **Claim**: They're asserting something is true
- **Observation**: They're noticing a pattern without claiming causation
- **Question**: They're sitting with something unresolved
- **Provocation**: They want to challenge how others think

All of these are valid. The label helps them know what kind of post they're writing.

### The Entry Point
- Not a finished hook
- More like stage directions: "enter from stage left"
- Examples:
  - "Start with the specific moment when you realized..."
  - "Lead with what most people assume, then flip it"
  - "Open with the question you can't stop asking"
  - "Begin with the thing you were afraid to say"

### Other Threads
- Only include if there were genuinely multiple directions
- Keep it brief—just enough to revisit later
- Format: "Also noticed a thread about [X]—could be its own post about [Y]"

---

## Example Brief

```markdown
# Post Brief

## Raw Material
Claude Code session where I refactored a test suite. Noticed I spent 80% of the time on setup/teardown, 20% on actual test logic.

## The Insight
Most test code isn't about testing—it's about recreating the world the code expects to exist.

## Why It Matters
Developers frustrated with slow test suites often optimize the wrong thing. They speed up test execution when the real cost is in setup complexity.

## The Audience
Backend developers who've inherited a test suite that takes 10+ minutes to run and have tried parallelization without much improvement.

## Your Take
**Type:** Observation

The test suite isn't slow because tests are slow. It's slow because we're rebuilding the universe before each test. The symptom is execution time; the problem is coupling.

## The Entry Point
Start with the refactoring session—the moment I realized I'd written 200 lines and none of them were assertions.

---

*Other threads: There's something here about how test setup reveals hidden dependencies in your architecture. Could be a separate post about using test pain as a design signal.*
```

---

## Delivery Notes

Before presenting the final brief, always check:
> "Here's what I've got—does this feel right, or is something off?"

If they confirm, deliver the artifact in the template format above.

If something's off, stay in conversation until it lands.
