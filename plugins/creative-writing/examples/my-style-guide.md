# My Technical Writing Style Guide

Generated for technical blog posts and documentation.

## Voice Principles

**Be direct and honest**
Skip marketing speak. If something is complex, say so.

> Good: "This approach requires understanding async/await. If you're new to asynchronous programming, check out [resource] first."
> Avoid: "Our revolutionary async solution makes everything simple!"

**Show your work**
Walk through the reasoning with code examples.

> Good: "I tried using callbacks initially. Here's what that looked like: [code]. The problem was nested callbacks became hard to follow. So I switched to promises: [code]."
> Avoid: "Promises are better than callbacks."

**Acknowledge limitations**
Every approach has trade-offs.

> Good: "This pattern simplifies state management but adds bundle size. For small apps, the trade-off might not be worth it."
> Avoid: "This pattern solves all state management problems."

## Structure Guidelines

**Short paragraphs (2-4 sentences)**
Keep ideas focused. Break complex concepts into smaller chunks.

**Heavy use of code examples**
Show, don't just tell. Every concept needs an example.

**Lists are fine for reference material**
Tutorials and guides should use prose. API docs and quick references can use lists.

## Word Choice Standards

**Technical accuracy over simplicity**
Use correct technical terms. Define them if needed, but don't dumb down.

> Good: "The event loop processes the callback queue when the call stack is empty."
> Avoid: "The computer does one thing at a time."

**Concrete examples from real projects**
Reference actual use cases.

> Good: "When I built the dashboard component, I needed to fetch data from three APIs. Here's how I handled that..."
> Avoid: "Imagine you need to fetch data from multiple sources."

## Patterns to Avoid

| Pattern | Why It Fails |
|---------|--------------|
| "Simply" or "just" | Minimizes complexity, frustrates readers |
| "Obviously" | Makes readers feel dumb if it's not obvious |
| Tutorials without error cases | Real code fails; show how to handle it |
| Examples without context | Show where this fits in the larger app |
| Marketing hyperbole | Technical readers skip it |

## Endings

End with next steps or further reading. Make it actionable.

> Good: "Try implementing this in your project. If you run into issues with [specific edge case], here's a GitHub discussion thread: [link]"
> Avoid: "Hope this helps! Let me know if you have questions."

## Quick Reference Checklist

1. Did I show code examples for every concept?
2. Did I walk through my reasoning, not just state conclusions?
3. Did I acknowledge when something is actually complex?
4. Did I include error handling in code examples?
5. Did I link to resources for prerequisites?
6. Did I use precise technical terms?
