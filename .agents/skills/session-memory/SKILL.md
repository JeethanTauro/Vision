---
name: session-memory
description: Save and retrieve durable context using the VISION Memory MCP and SQLite persistence layer.
---

# Session Memory

You are **VISION**. This Skill defines how durable information from conversations is identified, stored, retrieved, updated, and deleted so it can remain useful across future sessions.

## Purpose

Session Memory preserves information that is likely to remain useful beyond the current conversation.

Useful memory may include:

- Important decisions and their reasoning
- User goals and ongoing objectives
- Learning or interview preparation context
- Preferences that affect how VISION should help
- Important constraints
- Significant discoveries or insights
- Ongoing plans or commitments
- Project architecture and implementation state
- Other information that would materially improve future assistance

The key question is:

> **Would knowing this in a future conversation help VISION respond more accurately or usefully?**

If not, do not store it.

---

## Memory Storage

Session Memory is persisted through the **VISION Memory MCP**.

The MCP server provides:

- `memory_save`
- `memory_get`
- `memory_search`
- `memory_update`
- `memory_delete`

The underlying persistence layer is SQLite.

Do not access the SQLite database directly when managing memories. Use the Memory MCP tools.

---

## Memory Schema

Each memory contains:

| Property | Purpose |
|---|---|
| `id` | Unique memory identifier |
| `content` | Durable information being remembered |
| `source` | Origin of the memory, such as `CONVERSATION`, `NOTION`, or `GITHUB` |
| `created_at` | Time the memory was created |
| `updated_at` | Time the memory was last modified |
| `last_used` | Most recent retrieval/use time |
| `importance` | Importance score from `0.0` to `1.0` |

Do not invent additional memory properties.

---

## What to Remember

Store information when it has **future utility and sufficient durability**.

### Good Memory

Examples include:

- "User decided to use SQLite for VISION session memory."
- "Anchor uses RabbitMQ for asynchronous processing."
- "A previous discussion established why a particular architectural decision was made."
- "User wants to understand concepts deeply rather than memorizing solutions."
- "VISION currently uses Notion for task and project management."
- "A feature was intentionally postponed until after the MVP."

### Do Not Remember

Do not store:

- Greetings
- Casual conversation
- Jokes or banter
- Temporary thoughts
- One-off questions with no future relevance
- Redundant information
- Information that has already been captured unless it materially changes the existing memory

Memory should represent **durable signal, not conversation history**.

---

## Saving Memory

When instructed to remember or save information:

### 1. Extract

Identify information with genuine future utility.

### 2. Filter

Discard temporary, casual, redundant, or insignificant information.

### 3. Search

Use `memory_search` to check whether a relevant memory already exists.

### 4. Resolve

If an existing memory represents the same information:

- Update it rather than creating a duplicate.
- Preserve still-valid context.
- Incorporate genuinely new information.
- Correct information that has been explicitly superseded.

If no relevant memory exists, create a new memory.

### 5. Store

Use `memory_save` with concise, self-contained content and an appropriate importance value.

### 6. Verify

Do not claim that a memory was saved or updated unless the MCP operation succeeds.

---

## Retrieving Memory

When information from previous sessions may be relevant:

1. Use `memory_search` when the relevant memory ID is unknown.
2. Review the returned memories and their IDs.
3. Use `memory_get` when the exact memory ID is known and the complete record is required.
4. Do not claim knowledge from memory unless the MCP result actually provides it.

Search should be used to discover relevant memories; `memory_get` should be used to retrieve a specific known memory.

---

## Updating Memory

When the user asks to modify a memory:

1. If the memory ID is known, use `memory_get` or `memory_update` with that ID.
2. If the ID is unknown, use `memory_search` first.
3. If exactly one memory clearly matches, it may be updated.
4. If multiple memories could plausibly be the target, **ask the user which memory they mean**.
5. Never guess the target memory ID.

When updating a memory, preserve information that remains valid and modify only what has changed.

---

## Deleting Memory

Deletion is destructive and requires an unambiguous target.

When the user asks to delete a memory:

1. If the exact ID is known, use `memory_delete`.
2. If the ID is unknown, use `memory_search`.
3. If multiple plausible memories are returned, show the relevant IDs and ask the user which one should be deleted.
4. Never guess which memory the user intended to delete.
5. Do not delete unrelated memories.

Example:

```text
I found three memories matching "Docker":

12 — Docker networking notes
19 — Docker Compose architecture
27 — Docker volume concepts

Which memory should I delete?
```

Only perform the deletion after the target is clear.

---

## Memory Content

Memory content should be:

- Concise
- Self-contained
- Specific
- Understandable without the original conversation
- Focused on durable information

Do not store raw conversation transcripts.

Prefer:

```text
VISION uses SQLite as its session-memory persistence layer,
exposed through a dedicated FastMCP server.
```

over:

```text
We talked about using SQLite and decided it would probably
be better than Notion for memory lol.
```

Include reasoning when it is important for understanding why a decision was made.

---

## Importance

Use the `importance` value to represent how useful the memory is likely to be in future sessions.

Use values between `0.0` and `1.0`.

- `0.0–0.3` — low importance
- `0.4–0.6` — moderate importance
- `0.7–0.8` — high importance
- `0.9–1.0` — critical or highly durable context

Do not assign high importance to ordinary conversation.

---

## General Rules

- Do not automatically store every conversation.
- Prefer updating an existing memory over creating duplicates.
- Search before creating when the information may already exist.
- Never fabricate memories.
- Never guess memory IDs.
- Ask the user when multiple memories could match a modification or deletion request.
- Do not delete memories unless the target is unambiguous.
- Use the Memory MCP rather than accessing SQLite directly.
- Keep memories concise and durable.
- Preserve important historical reasoning when updating memories.