---
name: session-memory
description: Manage durable cross-session context using VISION Memory MCP.
---

# Session Memory

Store information that will materially improve future conversations. Do not store casual, temporary, redundant, or one-off information.

## Use Memory For

- Important decisions and their reasoning
- Long-term goals and plans
- Stable preferences
- Project architecture and state
- Important constraints
- Significant discoveries or learning

Memory should represent **durable signal, not conversation history**.

## Tools

Use the VISION Memory MCP:

- `memory_save` — create a memory
- `memory_search` — find relevant memories
- `memory_get` — retrieve a specific memory by ID
- `memory_update` — modify a memory by ID
- `memory_delete` — delete a memory by ID

SQLite is the underlying persistence layer. Never access it directly; use the MCP tools.

## Rules

### Save

Before saving:

1. Extract only durable information.
2. Search for an existing related memory.
3. Update an existing memory instead of creating a duplicate.
4. Otherwise save a concise, self-contained memory.
5. Use an importance value from `0.0` to `1.0`.

### Retrieve

Use `memory_search` when the ID is unknown. Use `memory_get` when the exact ID is known.

### Update / Delete

If the ID is unknown, search first.

If multiple memories could match, show the relevant IDs and **ask the user which one they mean**.

Never guess a memory ID or delete an ambiguous result.

### Content

Memories must be concise, specific, self-contained, and understandable without the original conversation.

Do not store raw conversation transcripts.

Only claim a memory was saved, updated, or deleted after the MCP operation succeeds.