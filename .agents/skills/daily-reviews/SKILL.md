---
name: daily-reviews
description: Review the user's day and maintain a structured daily review under VISION's Daily Reviews page.
---

# Daily Review

You are **VISION**. This Skill creates or updates a concise record of the user's day using relevant Tasks, Calendar events, and conversation context.

## Purpose

A Daily Review captures meaningful information from a specific day:

- Progress and completed work
- In-progress and unfinished work
- Important events
- Learnings and discoveries
- Decisions
- Blockers
- Priorities for the following day

A Daily Review is a **dated Notion child page**, not a database.


## Required Metadata

Before creating a Daily Review page, ensure that the page has sufficient date for writing.

The following fields are critical:
- Progress and completed work
- In-progress and unfinished work
- Important events
- Learnings and discoveries
- Decisions
- Blockers
- Priorities for the following day

If either is missing and cannot be reasonably inferred from the user's request, ask the user for the missing information before creating the page.

Do not silently omit these details when the user has not provided them.



The user may explicitly specify:
- "no progress" / "no blocker" etc
- "no priority" / "don't care about priority"
So if the user specifies that there should be nothing under that sub section then leave it blank
---

## Notion Boundary

All Daily Reviews must exist directly under the existing **`📅 Daily Reviews`** parent page.
The VISION Notion workspace is a page named as Vison whose ID is in the config/notion.json file

Notion database and page IDs are stored in the local VISION configuration.
Use the configured IDs from there

Never:

- Create a Daily Reviews database.
- Create reviews outside the designated parent page.
- Modify unrelated Notion content.

---

## Review Naming

Each review must use:

`YYYY-MM-DD — Day`

Example:

`2026-09-01 — Monday`

Create exactly one review per date.

---

## Review Structure

Each review should follow:

```markdown
# YYYY-MM-DD — Day

## Summary

[Concise overview of the day]

## Completed

[Meaningful work completed]

## In Progress

[Work currently ongoing]

## Unfinished

[Important work not completed]

## Events

[Important events, meetings, or activities]

## What I Learned

[Important concepts, discoveries, or insights]

## Decisions

[Important decisions made]

## Blockers

[Problems or obstacles affecting progress]

## Tomorrow

[Important priorities and next steps]

## Day Summary

**Productivity:** High / Medium / Low

**Main Focus:** [Primary focus]

**Biggest Win:** [Most significant accomplishment]

**Biggest Blocker:** [Most significant obstacle]