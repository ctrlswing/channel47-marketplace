# Getting Started with Post Partner

## First Use

Start with whatever you've got:

```bash
/post
```

Then share your raw material. The conversation adapts based on what you bring.

### From a Claude Code Log

Paste or reference the log. Post Partner will surface what it notices:

```
/post @.claude/logs/session-2024-01-15.md
```

> "Here's what I'm noticing: you spent most of this session fighting the type system, then had a breakthrough when you stopped trying to make it 'correct' and made it 'useful' instead. There might be something there about the difference between correctness and usefulness in developer tools. Does that land, or is the interesting part somewhere else?"

### From a Voice Memo Transcript

Paste the transcript. Expect the tool to find threads:

```
/post
[paste transcript]
```

> "There might be two threads here—one about why you stopped reading business books, one about what you learned from the last one you actually finished. Want to pick one?"

### From a Rough Idea

Just describe it. The tool will ask questions to draw out more:

```
/post
I've been thinking about how every productivity system eventually becomes a source of guilt
```

> "What happened recently that made you think about this?"

### From a Draft Post

If you've already written something, the tool skips excavation and goes straight to pressure testing:

```
/post @drafts/type-safety-post.md
```

> "Here's what I think you're saying: type systems are sold as 'catching bugs' but their real value is making refactoring safe. The argument works, but you're hedging in paragraph 3—'some might argue' weakens the claim. What are you actually worried about?"

## What to Expect

### The Conversation

Post Partner isn't a questionnaire. It responds to what's actually happening:

- If you're on a roll, it stays back
- If you're stuck, it offers something concrete to react to
- If you're circling, it reflects back what it's hearing
- If you say something that changes earlier conclusions, it adjusts

The vibe is a peer who's slightly further along in the craft—someone who'll push back, but from interest, not authority.

### The Take Question

At some point you'll figure out your take—what you're actually saying about the insight. Post Partner frames this based on how you've been talking:

- If you've been assertive: "What's the claim you're making?"
- If you've been exploratory: "What are you noticing that others might miss?"
- If you've been uncertain: "What question are you sitting with?"
- If you've been reactive: "What do you want people to reconsider?"

All valid. The brief labels your take by type so you know what kind of post you're writing.

### Before You Get the Brief

The tool checks before delivering:

> "Here's what I've got—does this feel right, or is something off?"

If something's off, stay in the conversation. If it lands, you get the artifact.

## The Brief

Your output looks like this:

```markdown
# Post Brief

## Raw Material
[What you started with]

## The Insight
[The interesting thing, 1-2 sentences]

## Why It Matters
[Who cares and why]

## The Audience
[Who this is for, specifically]

## Your Take
**Type:** Observation

[Your point of view on the insight]

## The Entry Point
[The angle—not a hook, just the way in]

---

*Other threads: [Angles you didn't pursue, if any]*
```

You can write immediately, or queue it up and write later. The brief holds your thinking.

## When There's No Post

Sometimes the idea isn't ready. That's fine.

If you keep redirecting, if your answers get shorter, if you say "I don't know"—the tool notices:

> "I'm not sure there's a post here yet—might just be something you're still chewing on. Want to drop it for now, or keep pulling at it?"

If you exit, no brief. Just:

> "Parked this thread—raw material saved if you want to come back to it."

No failure. Not everything becomes a post.

## Tips

- **Bring real material.** Logs and transcripts work better than abstract ideas because there's more to notice.
- **React honestly.** If something doesn't land, say so. The conversation adjusts.
- **Don't perform certainty.** "I'm not sure" is useful information.
- **The brief is the goal.** You can ask for a draft opening line, but the value is in the thinking you did, not text the tool generates.
