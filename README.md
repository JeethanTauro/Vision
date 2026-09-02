# VISION

VISION is a personal AI assistant built around a simple idea: use existing AI coding CLIs as the execution layer and Notion as the persistent workspace.

VISION is currently at **V1**.

## Architecture

VISION is designed to be CLI-agnostic. The same workspace can be operated through multiple AI coding agents:

- **Antigravity CLI (AGY)** — primary CLI, using `GEMINI.md`
- **OpenCode** — alternative CLI, using `AGENTS.md`
- **Codex CLI** — alternative CLI, using `AGENTS.md`

The CLIs provide the agent runtime, model access, filesystem access, and MCP support. VISION's behavior is defined through Markdown instructions and Skills, allowing the same architecture to work across different CLIs.

```text
                  ┌─────────────────────┐
                  │       VISION        │
                  │ Instructions +      │
                  │      Skills         │
                  └──────────┬──────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────▼─────┐  ┌─────▼─────┐  ┌─────▼─────┐
        │    AGY    │  │ OpenCode  │  │   Codex   │
        │ GEMINI.md │  │ AGENTS.md │  │ AGENTS.md │
        └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                         Notion MCP
                             │
                  ┌──────────▼──────────┐
                  │       Notion        │
                  │ Tasks / Calendar /  │
                  │ Memory / Reviews /  │
                  │                     │
                  └─────────────────────┘
```

The purpose of this architecture is also practical: different CLIs provide access to different models, providers, quotas, and free tiers. Instead of making VISION dependent on a single model or CLI, the same workspace can be used across multiple agents.

## Skills

VISION's behavior is separated into focused Skills:

| Skill | Responsibility |
|---|---|
| `tasks-management` | Create, retrieve, update, and complete tasks |
| `calendar-management` | Manage scheduled events |
| `daily-planning` | Build a realistic plan from tasks and calendar |
| `daily-review` | Review the day and maintain daily reviews |
| `session-memory` | Store and retrieve durable context |
| `morning-brief` | Provide a morning overview of tasks and events |
| `quick-capture` | Convert thoughts into tasks or durable memory |
| `focus-recommendation` | Recommend what to work on next |

Skills are stored under:

```text
.agents/skills/
```

Each Skill contains the instructions required for the agent to perform that specific capability.

## Persistence

Notion acts as VISION's persistent data layer.

VISION separates information by purpose:

- **Tasks** — actionable work
- **Calendar** — scheduled events
- **Daily Reviews** — daily reflections
- **Session Memory** — durable context

Notion resource IDs are kept in local configuration rather than hardcoded into the Skills.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/JeethanTauro/vision.git
cd vision
```

### 2. Configure Notion

Create the local Notion configuration:

```text
config/notion.json
```

Add the IDs of your VISION Notion resources:

```json
{
  "root_page_id": "YOUR_ROOT_PAGE_ID",
  "tasks_database_id": "YOUR_TASKS_DATABASE_ID",
  "calendar_database_id": "YOUR_CALENDAR_DATABASE_ID",
  "daily_reviews_page_id": "YOUR_DAILY_REVIEWS_PAGE_ID",
  "session_memory_database_id": "YOUR_SESSION_MEMORY_DATABASE_ID",
  "projects_database_id": "YOUR_PROJECTS_DATABASE_ID"
}
```

This file is local configuration.

### 3. Connect Notion MCP

VISION uses the Notion MCP server for persistent storage and retrieval.

Configure the Notion MCP server for whichever CLI you use.

For example, the project can be used with:

- Antigravity CLI
- OpenCode
- Codex CLI

The CLI handles the model and agent runtime while Notion MCP provides VISION's persistent workspace.

### 4. Run VISION

Enter the repository and start your preferred CLI.

For Antigravity:

```bash
agy
```

For OpenCode:

```bash
opencode
```

For Codex:

```bash
codex
```

The selected CLI loads the appropriate instruction file and Skills from the repository.

## V1

V1 focuses on establishing the core architecture:

- Multiple CLI support
- Notion MCP integration
- Modular Skills
- Task and calendar management
- Daily planning and reviews
- Persistent session memory
- Quick capture and focus recommendations

The goal of V1 is to provide a working foundation before optimizing the architecture further.

## Demo
[Click on this link for the demo](https://youtu.be/rzg6q2zhR8g)

## VISION Mini

Checkout the **`vision-mini`** branch.

VISION Mini aggressively reduces the size of the Markdown instructions and Skills

The current `main` branch remains the full V1 implementation.

