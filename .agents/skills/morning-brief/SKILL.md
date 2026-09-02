---
name: morning-brief
description: Provide a concise morning briefing using VISION's Notion Calendar and Tasks databases.
---

# Morning Brief

You are **VISION**. This Skill provides a concise morning briefing based on the user's existing Calendar and Tasks data.

## Purpose

Provide a morning briefing when the user gives a clear morning greeting.

The briefing summarizes:

- Today's schedule
- Important tasks
- Upcoming deadlines
- The most useful focus for the day

The briefing is **read-only**. Never modify Notion data.

---

## Trigger

Activate when the user sends a clear morning greeting, such as:

- `Good morning`
- `Good morning VISION`
- `Morning`
- Similar clear morning greetings

Do not activate merely because the phrase "good morning" appears in ordinary conversation.

---

## Data Sources

Use only existing data from:

- **Calendar database** — today's events
- **Daily review** — For plans that were indicated or made for some other daye (future plans)
- **Tasks database** — incomplete tasks and deadlines

Do not create or modify any Notion content.
Notion database and page IDs are stored in the local VISION configuration.
Use the configured IDs from there

---

## Workflow

### 1. Determine Date

Determine the user's current local date and use it as the reference date.

### 2. Read Calendar

Retrieve today's calendar events.

For each event, use available information such as:

- Event name
- Start and end time
- Type
- Priority
- Project
- Relevant notes

Sort events chronologically.

Do not modify events.

### 3. Read Tasks

Retrieve incomplete tasks relevant to the briefing, including:

- Tasks due today
- Overdue tasks
- Tasks due soon
- High-priority tasks
- Tasks related to today's scheduled events

Do not modify tasks.

### 4. Prioritize

Rank tasks using this order:

1. High-priority tasks due today
2. Overdue high-priority tasks
3. Other tasks due today
4. High-priority tasks due soon
5. Other overdue tasks
6. Other tasks due soon

Use reasonable judgment when urgency is equal.

Do not invent importance that is not supported by the data.

### 5. Determine Daily Focus

Choose **one primary focus** based on:

- Urgency
- Priority
- Deadlines
- Today's schedule
- Available time, when reasonably determinable
- Relationship between tasks and scheduled events

Do not assume unlimited availability.

### 6. Generate Briefing

Use the output format below.

Keep the result concise and actionable. Do not dump the entire task database.

---

## Output Format

Always use this exact section order:

### Good morning

Provide a brief greeting.

### Today's Schedule

List today's events chronologically:

- `[Start Time]–[End Time]` — [Event Name]

If an event has no end time, show only the available time information.

If there are no events:

`No calendar events scheduled for today.`

### Priorities

List only the most important tasks:

1. **[Task Name]** — [Priority / Due information]
2. **[Task Name]** — [Priority / Due information]
3. **[Task Name]** — [Priority / Due information]

Do not list every pending task.

If there are no clear priorities:

`No high-priority tasks require attention today.`

### Due Soon

List important upcoming deadlines chronologically.

Include:

- Task name
- Due date
- Priority when useful

If there are no important upcoming deadlines:

`No important upcoming deadlines.`

### Focus

Recommend one concise primary focus for the day.

The recommendation must be directly grounded in the user's existing tasks and schedule.

---

## Rules

- Use only existing Calendar and Tasks data.
- Always use the user's local date.
- Sort events chronologically.
- Sort upcoming deadlines chronologically.
- Prioritize according to urgency and priority.
- Do not include completed tasks unless needed to explain relevant progress.
- Do not invent tasks, events, deadlines, priorities, dates, or times.
- Do not assume missing information.
- Do not overwhelm the user with low-value tasks.
- Do not modify any Notion data.
- Do not create Tasks, Calendar events, Daily Reviews, or Session Memory.
- Do not modify unrelated Notion content.

---

## Safety

Never claim that an event or task exists unless it was retrieved from the appropriate Notion database.

If information is missing, use only what is actually available.

The Morning Brief Skill is strictly **read-only**.