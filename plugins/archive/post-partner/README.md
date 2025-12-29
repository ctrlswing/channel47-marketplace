# Post Partner

A thought partner for turning raw material into posts worth sharing.

## What It Does

Post Partner guides you through the thinking behind a post without writing it for you. You bring the raw material—a Claude Code log, voice memo transcript, draft, or rough idea. The tool helps you find the interesting part, pressure test whether it matters, and land on what you actually want to say.

The output is a **brief**—not the post itself. The brief holds your thinking so you can write the post now or later.

## The Problem

Current options for turning ideas into posts are unsatisfying. You either do all the thinking yourself—which is slow and often results in ideas dying in drafts—or you hand it to an LLM and get back something that feels hollow. The output might be technically correct but it doesn't feel like yours.

Post Partner sits in the middle. It's a structured conversation that draws the post out of you. The model does real work—surfacing insights, proposing audiences, pressure testing claims—but you stay in control of the actual thinking. The words end up being yours.

## Installation

```bash
claude plugin install channel47-marketplace/post-partner
```

## Quick Start

```bash
/post
```

Then paste your raw material—a log, transcript, draft, or idea. The conversation adapts to what you bring:

- **Dense material** (logs, transcripts): Surfaces candidate insights for you to react to
- **Sparse material** (rough ideas): Asks questions to draw out more context
- **Draft posts**: Skips straight to pressure testing what you're trying to say

## What You Get

A brief containing:

- **Raw material** — What you started with
- **The insight** — The interesting thing, in 1-2 sentences
- **Why it matters** — Who cares and why
- **The audience** — Who this is for, specifically
- **Your take** — Labeled as claim, observation, question, or provocation
- **The entry point** — The angle for your post

You can write immediately or queue up ten briefs and pick which one to write when you have the energy.

## How It Works

The model knows where it needs to end up (a complete brief) but how it gets there adapts to you:

- If you say "the interesting part is X"—it skips excavation and moves to pressure testing
- If you're circling and uncertain—it stays in exploration mode longer
- If something you say later changes the insight—it adjusts
- If you go quiet—it does more lifting; if you're riffing—it stays out of your way

Sometimes there's no post. That's fine. The tool makes it easy to exit without feeling like failure.

## What It's Not

Post Partner is explicitly **not a content generator**. It's a thinking tool that produces clarity, not copy. The brief is proof you did the thinking. The post is yours to write.

## License

MIT
