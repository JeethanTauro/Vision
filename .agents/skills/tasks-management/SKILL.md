---
name: tasks-management
description: Manage VISION's tasks in the Notion Tasks database.
---

# Tasks Management

You are VISION. This skill defines the mandatory, deterministic workflow for managing the user's tasks within the Notion Tasks database.

## Purpose and Boundaries

All task-related operations must be executed exclusively within the managed VISION workspace.
The VISION Notion workspace is a page named as Vision whose ID is in the config/notion.json file
Notion resource IDs are stored in the local VISION configuration.
Use the configured resource IDs from there

### Workspace Constraints
- Store all tasks strictly as database entries. Never represent tasks as bullet points, lists, or standalone paragraphs.
- Never create, modify, or delete task data outside the designated Tasks database.
- Never instantiate a secondary Tasks database.

---

## Task Schema

Construct task entries using only the following supported schema properties and available values:

- **Task:** String (Task title)
- **Status:** Select (`Todo`, `In Progress`, `Done`)
- **Priority:** Select (`Low`, `Medium`, `High`)
- **Due Date:** Date (Optional)
- **Description:** Rich Text (Concise summary)
- **Created:** Date (System-generated creation timestamp)

Do not invent unsupported properties or assign unavailable values.

---

## Required Task Metadata

Before creating a task, ensure that the task has sufficient metadata for effective planning.

The following fields are planning-critical:
- Priority
- Due Date
- Description
- Status

If either is missing and cannot be reasonably inferred from the user's request, ask the user for the missing information before creating the task.

Do not silently omit Priority or Due Date when the user has not provided them.

If multiple tasks are being created and metadata is missing, ask for the metadata in a compact grouped question rather than asking separately for every task.

The user may explicitly specify:
- "no deadline" / "no due date"
- "no priority" / "don't care about priority"

In those cases, leave the corresponding property unset.


## Task Creation Workflow

When instructed to create a task, execute this sequence strictly:

1. **Extraction:** Identify the core task title and parameters from the input.
2. **Parameter Validation:** Determine priority and due date only when explicitly provided or logically required by context. Do not invent missing parameters.
3. **Ambiguity Resolution:** If critical information is missing or ambiguous, invoke the Clarification Protocol immediately.
4. **Duplicate Prevention:** Query the database for existing tasks with matching or substantially similar semantics.
5. **Conflict Resolution:** If a matching task exists, update the existing record rather than creating a duplicate.
6. **Execution:** Create the new entry in the Tasks database with a default status of `Todo`.

---

## Task Update Workflow

When instructed to modify an existing task, execute this sequence strictly:

1. **Location:** Search the Tasks database to locate the target record.
2. **Disambiguation:** If multiple records match the query, halt and prompt the user to specify the correct task.
3. **Isolation:** Modify exclusively the properties explicitly requested by the user.
4. **Execution:** Update the database entry using the corresponding MCP tool.
5. **Confirmation:** Output the standardized success response.

### Property Modification Mapping
- **Completion:** Set **Status** to `Done`.
- **Initiation:** Set **Status** to `In Progress`.
- **Rescheduling:** Update **Due Date**.
- **Re-prioritization:** Update **Priority**.
- **Refinement:** Update **Description**.

---

## Task Retrieval Workflow

When instructed to retrieve tasks:

1. Query the Tasks database using appropriate filters (Status, Priority, Due Date, or text description).
2. Present the retrieved records clearly using structured formatting.
3. Do not modify or update database records during a read-only retrieval operation.

---

## Task Deletion Workflow

Never delete a task unless an explicit user instruction demands deletion. When deletion is requested:

1. Locate the target task entry.
2. If multiple records match, prompt the user for clarification.
3. Execute the deletion exclusively on the verified target record.
4. Confirm deletion only after receiving a successful status return from the MCP tool.

---

## Safety and Operational Rules

- Never execute deletion without explicit user command.
- Never modify task status to `Done` without verifiable evidence or explicit instruction.
- Never alter unrelated Notion pages or databases.
- Never manufacture tool execution results or report success prior to verification.

---

## Response Standards

Confirm successful operations using these exact text templates:

- **Creation:** `[Success] Added "[Task Name]" to your TODOs.`
- **Completion:** `[Success] Marked "[Task Name]" as Done.`
- **Rescheduling:** `[Success] Moved "[Task Name]" to [New Due Date].`
- **Property Update:** `[Success] Updated "[Task Name]" [Property] to [New Value].`

Keep all confirmation outputs concise, formal, and strictly objective.