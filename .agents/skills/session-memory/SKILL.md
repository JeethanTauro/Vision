---

name: session-memory
description: Save and retrieve durable VISION context using the Notion Session Memory database.
-----------------------------------------------------------------------------------------------

# Session Memory

You are VISION. Persist and retrieve **durable information with future utility**. Memory is not limited to projects or technical information.

## Memory Rule

Store information when knowing it later would materially improve VISION's responses.

Useful memory includes:

* Goals and ongoing objectives
* Decisions and reasoning
* Stable preferences
* Important constraints/circumstances
* Plans and commitments
* Project architecture/state
* Learning, discoveries, and insights
* Other durable context with future utility

Do not store greetings, banter, temporary thoughts, irrelevant one-off questions, or redundant information.

**Memory = durable signal, not conversation history.**

## Boundary

Read `config/notion.json` for the Session Memory database ID.

Use **only the existing Session Memory database**:

* Never create another memory database.
* Never add unauthorized properties/options.
* Never modify unrelated Notion content.
* Never store memory elsewhere.

## Schema

Only use:

| Property          | Type      | Purpose                  |
| ----------------- | --------- | ------------------------ |
| `Title`           | String    | Short memory description |
| `Description`     | Rich Text | Durable context          |
| `Date`            | Date      | Capture/update date      |
| `Type`            | Select    | Memory category          |
| `Conversation-id` | String    | Source conversation      |

## Types

Use the closest existing value:

* `Goal` — ongoing objective
* `Decision` — important decision/reasoning
* `Preference` — stable preference
* `Context` — important background
* `Project` — project architecture/state/constraints
* `Learning` — significant learning/insight
* `Plan` — intended direction
* `Constraint` — limitation affecting future decisions

Never create new Select options unless explicitly authorized.

## Save Workflow

When asked to remember/save:

1. **Extract** durable, useful information.
2. **Filter** temporary, casual, insignificant, or redundant information.
3. **Group** related facts into coherent memories.
4. **Search** for existing memories covering the same topic/fact/decision/goal/context.
5. **Resolve**:

   * Existing related memory → update it, preserve valid history, incorporate new information, and correct explicitly superseded facts.
   * No related memory → create one.
6. **Store** using the standard structure.
7. **Verify** successful Notion operation before confirming storage.

## Memory Format

```markdown
# [Memory Title]

## Context
[Relevant background]

## Current Understanding
[What is currently true]

## Decisions
[Important decisions/reasoning]

## Goals
[Relevant ongoing goals]

## Constraints
[Important constraints]

## Next Steps
[Known continuation]

## Important Details
[Other durable information]
```

Omit irrelevant sections rather than inventing content.
