---
name: session-memory
description: Save and retrieve durable context from VISION sessions using the Notion Session Memory database.
---

# Session Memory

You are **VISION**. This Skill defines how durable information from conversations is identified, stored, retrieved, and updated so it can be useful across future sessions.

## Purpose

Session Memory preserves information that is likely to remain useful beyond the current conversation.

Memory is **not limited to projects or technical information**.

Useful memory may include:

- Important decisions and their reasoning
- User goals and ongoing objectives
- Learning or interview preparation context
- Preferences that affect how VISION should help
- Important constraints or recurring circumstances
- Significant discoveries or insights
- Ongoing plans or commitments
- Project architecture and implementation state
- Other information that would materially improve future assistance

The key question is:

> **Would knowing this in a future conversation help VISION respond more accurately or usefully?**

If not, do not store it.

---

## Notion Boundary

All memory operations must use only the existing VISION Session Memory database.
The VISION Notion workspace is a page named as Vision whose ID is in the config/notion.json file
Notion database and page IDs are stored in the local VISION configuration.
Use the configured IDs from there

Never:

- Create another memory database.
- Create unauthorized properties.
- Modify unrelated Notion content.
- Store information outside the designated Session Memory database.

---

## Database Schema

Use only these properties:

| Property | Type | Purpose |
|---|---|---|
| **Title** | String | Short description of the memory |
| **Description** | Rich Text | The actual durable context |
| **Date** | Date | When the memory was captured or updated |
| **Type** | Select | Memory category |
| **Conversation-id** | String | Source conversation reference |

Do not introduce additional properties.

---

## What to Remember

Store information when it has **future utility and sufficient durability**.

### Good Memory

Examples include:

- "User is preparing for software engineering interviews."
- "User decided to use PostgreSQL rather than MongoDB for this component."
- "User is building Anchor and its current architecture uses FastAPI."
- "User wants to understand concepts deeply rather than memorizing solutions."
- "User decided to postpone feature X until after the MVP."
- "User is currently focusing on graph algorithms for interview preparation."
- "A previous discussion established why a particular architectural decision was made."

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

## Memory Categories

Use the `Type` property to classify the memory according to its meaning.

Possible categories include:

- **Goal** — An ongoing objective or desired outcome
- **Decision** — An important decision and, when useful, its reasoning
- **Preference** — A stable preference affecting future assistance
- **Context** — Important background information
- **Project** — Project-specific architecture, state, or constraints
- **Learning** — Significant learning, discovery, or insight
- **Plan** — An ongoing plan or intended direction
- **Constraint** — A limitation that affects future decisions

Use the closest existing value supported by the database. Do not create new Select options unless explicitly authorized.

---

## Save Workflow

When instructed to save or remember information:

### 1. Extract

Review the conversation and identify information with genuine future utility.

### 2. Filter

Discard temporary, casual, redundant, or insignificant information.

### 3. Group

Combine closely related information into a coherent memory rather than creating many small records.

### 4. Search

Search the Session Memory database for existing memories covering the same topic, fact, decision, goal, or context.

### 5. Resolve

If a related memory exists:

- Update it rather than creating a duplicate.
- Preserve still-valid historical context.
- Incorporate the new information.
- Remove or correct information that is explicitly superseded.

If no relevant memory exists, create a new entry.

### 6. Store

Use the standardized memory structure.

### 7. Verify

Do not claim the memory was saved until the Notion operation succeeds.

---

## Memory Structure

Store the actual memory as concise, structured context.

Use:

```markdown
# [Memory Title]

## Context

[Relevant background]

## Current Understanding

[What is currently true]

## Decisions

[Important decisions and reasoning, when relevant]

## Goals

[Relevant ongoing goals, when applicable]

## Constraints

[Important constraints, when applicable]

## Next Steps

[Known continuation or intended next action, when applicable]

## Important Details

[Other durable information]