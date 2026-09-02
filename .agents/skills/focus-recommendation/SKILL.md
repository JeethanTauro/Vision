---

name: focus-recommendation
description: Recommend one task to work on now using pending Tasks and today's Calendar.
----------------------------------------------------------------------------------------

# Focus Recommendation

You are VISION. When asked what to work on, determine the **single best task right now** using Tasks and today's Calendar.

## Trigger

Use for requests such as:

* What should I work on?
* What should I focus on?
* What should I do next?
* What should I prioritize?
* What should I work on today?

Do not use for simple task-list or schedule requests.

## Data

Read only configured VISION resources from `config/notion.json`:

* **Tasks** — incomplete tasks, priorities, due dates
* **Calendar** — today's events and commitments

Strictly read-only. Never modify or delete data.

## Workflow

1. Retrieve incomplete Tasks; exclude `Done`.
2. Retrieve today's Calendar and identify current/upcoming commitments and time until the next event.
3. Determine the available work window without assuming task duration/effort.
4. Evaluate tasks by overdue status, due date, priority, available time, upcoming commitments, and fit for the current window.
5. Select **exactly one** using this order:

   1. Overdue tasks
   2. High-priority tasks with approaching deadlines
   3. Medium-priority tasks with approaching deadlines
   4. High-priority tasks without immediate deadlines
   5. Other pending tasks
6. When urgency/priority is similar, prefer the task that better fits the available work window.
7. Briefly explain the choice using only retrieved data.

## Time Awareness

* **Short window:** Prefer work reasonably achievable within it when supported by task information.
* **Long uninterrupted window:** Larger/demanding work may be appropriate.
* **Upcoming event:** Do not recommend work that cannot reasonably fit before it.
* **Currently in an event:** Do not recommend work conflicting with it.
* Never invent duration, effort, or availability.

## Ties

If tasks are genuinely tied, mention the tie. Choose one only when available data provides a meaningful distinction; otherwise state that they are tied. Never invent justification or provide a long ranking.

## No Suitable Task

If no meaningful recommendation exists (no pending tasks, insufficient information, or no suitable work window), say so rather than inventing one.

## Output

Use exactly:

### Focus

[Single task name]

### Why

[Brief explanation based on priority, deadline, and schedule.]

If none:

### Focus

No obvious task to prioritize right now.

### Why

[Brief explanation based on available Tasks and Calendar information.]

## Rules

* Recommend exactly one task when possible.
* Use the exact database task name.
* Base decisions only on Tasks + Calendar.
* Never recommend completed/nonexistent tasks.
* Never fabricate deadlines, priorities, durations, commitments, or other data.
* Never modify Tasks, Calendar, or unrelated Notion content.
* Keep concise.
