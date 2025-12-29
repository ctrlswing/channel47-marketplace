# Diagram Examples

Reference examples of ASCII diagrams.

## Flowcharts

### Linear Flow
```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Start  │────▶│ Process │────▶│   End   │
└─────────┘     └─────────┘     └─────────┘
```

### With Decision
```
┌─────────┐     ┌─────────┐
│  Start  │────▶│ Process │
└─────────┘     └────┬────┘
                     │
                     ▼
               ┌───────────┐
               │ Decision? │
               └─────┬─────┘
                     │
         ┌───────────┼───────────┐
         │ Yes       │           │ No
         ▼           │           ▼
    ┌─────────┐      │      ┌─────────┐
    │ Path A  │      │      │ Path B  │
    └────┬────┘      │      └────┬────┘
         │           │           │
         └───────────┴───────────┘
                     │
                     ▼
               ┌─────────┐
               │   End   │
               └─────────┘
```

### Complex Process
```
                    ┌─────────────┐
                    │   Request   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
              ┌────▶│  Validate   │◀────┐
              │     └──────┬──────┘     │
              │            │            │
              │            ▼            │
              │     ┌─────────────┐     │
              │     │   Valid?    │     │
              │     └──────┬──────┘     │
              │       Yes  │  No        │
              │     ┌──────┴──────┐     │
              │     ▼             ▼     │
              │ ┌───────┐   ┌───────┐   │
              │ │Process│   │ Error │───┘
              │ └───┬───┘   └───────┘
              │     │
              │     ▼
              │ ┌───────┐
              └─│ Retry?│
                └───┬───┘
                    │ No
                    ▼
                ┌───────┐
                │  Done │
                └───────┘
```

## Directory Trees

### Basic Tree
```
project/
├── src/
│   ├── index.ts
│   └── utils.ts
├── tests/
│   └── index.test.ts
└── package.json
```

### Detailed Tree
```
my-app/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
├── src/
│   ├── components/
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   └── index.ts
│   │   └── Input/
│   │       ├── Input.tsx
│   │       └── index.ts
│   ├── hooks/
│   │   └── useAuth.ts
│   ├── utils/
│   │   ├── api.ts
│   │   └── helpers.ts
│   ├── App.tsx
│   └── index.tsx
├── public/
│   └── index.html
├── package.json
├── tsconfig.json
└── README.md
```

## Tables

### Simple Table
```
┌──────────┬─────────┬──────────┐
│ Name     │ Status  │ Priority │
├──────────┼─────────┼──────────┤
│ Feature  │ Done    │ High     │
│ Bug Fix  │ WIP     │ Medium   │
│ Docs     │ Pending │ Low      │
└──────────┴─────────┴──────────┘
```

### With Alignment
```
┌──────────────┬─────────────┬──────────┐
│ Feature      │    Status   │ Priority │
├──────────────┼─────────────┼──────────┤
│ Auth         │  ✓ Complete │   High   │
│ API Routes   │ ◐ Progress  │   High   │
│ Unit Tests   │  ○ Pending  │  Medium  │
│ Integration  │  ○ Pending  │   Low    │
└──────────────┴─────────────┴──────────┘
```

### ASCII Only
```
+--------------+-------------+----------+
| Feature      | Status      | Priority |
+--------------+-------------+----------+
| Auth         | Complete    | High     |
| API Routes   | In Progress | High     |
| Unit Tests   | Pending     | Medium   |
+--------------+-------------+----------+
```

## Sequence Diagrams

### Simple Request/Response
```
┌────────┐          ┌────────┐
│ Client │          │ Server │
└───┬────┘          └───┬────┘
    │                   │
    │  GET /users       │
    │──────────────────▶│
    │                   │
    │  200 OK [users]   │
    │◀──────────────────│
    │                   │
```

### Complex Interaction
```
┌────────┐       ┌────────┐       ┌────────┐       ┌────────┐
│ Client │       │  API   │       │ Auth   │       │   DB   │
└───┬────┘       └───┬────┘       └───┬────┘       └───┬────┘
    │                │                │                │
    │ POST /login    │                │                │
    │───────────────▶│                │                │
    │                │ Verify token   │                │
    │                │───────────────▶│                │
    │                │                │ Check user     │
    │                │                │───────────────▶│
    │                │                │                │
    │                │                │ User data      │
    │                │                │◀───────────────│
    │                │ Token valid    │                │
    │                │◀───────────────│                │
    │ 200 OK         │                │                │
    │◀───────────────│                │                │
    │                │                │                │
```

## Architecture Diagrams

### Simple Architecture
```
┌─────────────────────────────────────────┐
│              Load Balancer              │
└────────────────────┬────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
   ┌─────────┐  ┌─────────┐  ┌─────────┐
   │ Server  │  │ Server  │  │ Server  │
   │    1    │  │    2    │  │    3    │
   └────┬────┘  └────┬────┘  └────┬────┘
        │            │            │
        └────────────┼────────────┘
                     │
              ┌──────┴──────┐
              │             │
              ▼             ▼
         ┌────────┐    ┌────────┐
         │ Primary│───▶│Replica │
         │   DB   │    │   DB   │
         └────────┘    └────────┘
```

### Microservices
```
                    ┌─────────────┐
                    │   Gateway   │
                    └──────┬──────┘
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼
┌───────────┐       ┌───────────┐       ┌───────────┐
│  User     │       │  Order    │       │  Product  │
│  Service  │       │  Service  │       │  Service  │
└─────┬─────┘       └─────┬─────┘       └─────┬─────┘
      │                   │                   │
      ▼                   ▼                   ▼
┌───────────┐       ┌───────────┐       ┌───────────┐
│  User DB  │       │ Order DB  │       │Product DB │
└───────────┘       └───────────┘       └───────────┘
```

## Arrow Reference

| Direction | Unicode | ASCII |
|-----------|---------|-------|
| Right | ──▶ | --> |
| Left | ◀── | <-- |
| Up | ▲ | ^ |
| Down | ▼ | v |
| Bidirectional | ◀──▶ | <--> |

## Box Drawing Characters

| Purpose | Characters |
|---------|------------|
| Corners | ┌ ┐ └ ┘ ╔ ╗ ╚ ╝ |
| Lines | ─ │ ═ ║ ━ ┃ |
| T-junctions | ┬ ┴ ├ ┤ ╦ ╩ ╠ ╣ |
| Cross | ┼ ╬ |
| Arrows | ▲ ▼ ◀ ▶ △ ▽ ◁ ▷ |
