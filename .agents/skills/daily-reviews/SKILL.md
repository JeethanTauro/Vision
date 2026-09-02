---

name: daily-reviews
description: Create or update a dated Daily Review under VISION's Daily Reviews page.
-------------------------------------------------------------------------------------

# Daily Review

You are VISION. Create/update a concise daily record using relevant Tasks, Calendar events, and conversation context.

## Purpose

Capture:

* Completed/progress
* In-progress/unfinished work
* Important events
* Learnings/discoveries
* Decisions
* Blockers
* Tomorrow's priorities

## Required Content

Before creating, ensure sufficient information exists for all review sections. Infer only when reasonable; otherwise ask for missing information.

User may explicitly specify `no progress`, `no blocker`, `no priority`, etc.; leave that section blank.

## Boundary

Read IDs from `config/notion.json`.

Reviews must be **dated child pages directly under the existing `📅 Daily Reviews` parent page**.

Never:

* Create a Daily Reviews database.
* Create reviews elsewhere.
* Modify unrelated Notion content.

## Naming

Use exactly:

`YYYY-MM-DD — Day`

Create **exactly one review per date**. Update the existing review if one already exists.

## Structure

```markdown
# YYYY-MM-DD — Day

## Summary
[Concise overview]

## Completed
[Meaningful completed work]

## In Progress
[Ongoing work]

## Unfinished
[Important incomplete work]

## Events
[Important events/activities]

## What I Learned
[Important learning/discoveries]

## Decisions
[Important decisions]

## Blockers
[Problems/obstacles]

## Tomorrow
[Priorities/next steps]

## Day Summary
**Productivity:** High / Medium / Low
**Main Focus:** [Primary focus]
**Biggest Win:** [Most significant accomplishment]
**Biggest Blocker:** [Most significant obstacle]
```

Omit/invalidate no section only when the user explicitly indicates it has no content; otherwise gather sufficient information before creation.

## Rules

* Use only relevant Tasks, Calendar, and conversation context.
* Preserve existing review content when updating; modify only information relevant to the review.
* Never invent events, progress, decisions, learnings, blockers, or priorities.
* Never create duplicate reviews.
* Never modify unrelated Notion content.
* Verify Notion success before claiming completion.
