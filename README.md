# VISION

VISION is a personal AI assistant built around a simple idea: use existing AI coding CLIs as the execution layer, with specialized MCP servers providing persistent capabilities.

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
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
           ┌─────▼─────┐      ┌─────▼─────┐      ┌─────▼─────┐
           │    AGY    │      │ OpenCode  │      │   Codex   │
           │ GEMINI.md │      │ AGENTS.md │      │ AGENTS.md │
           └─────┬─────┘      └─────┬─────┘      └─────┬─────┘
                 │                  │                  │
                 └──────────────────┼──────────────────┘
                                    │
                         ┌──────────▼──────────┐
                         │         MCP         │
                         └───────┬───────┬─────┘
                                 │       │
                    ┌────────────▼─┐   ┌─▼──────────────┐
                    │  Notion MCP  │   │ Memory MCP     │
                    └──────┬───────┘   └───────┬────────┘
                           │                   │
                    ┌──────▼──────┐     ┌──────▼──────┐
                    │   Notion    │     │    SQLite   │
                    │             │     │              │
                    │ Tasks       │     │ Session      │
                    │ Calendar    │     │ Memory       │
                    │ Reviews     │     │              │
                    │ Projects    │     │              │
                    └─────────────┘     └──────────────┘
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
| `session-memory` | Store and retrieve durable cross-session context |
| `morning-brief` | Provide a morning overview of tasks and events |
| `quick-capture` | Convert thoughts into tasks or durable memory |
| `focus-recommendation` | Recommend what to work on next |

Skills are stored under:

```text
.agents/skills/
```

Each Skill contains the instructions required for the agent to perform that specific capability.

## Persistence

VISION uses different persistence layers based on the type of information:

- **Notion** — Tasks, Calendar, Daily Reviews, and Projects
- **SQLite** — Session Memory

Notion operations are exposed through the **Notion MCP**.

Session Memory is exposed through the **VISION Memory MCP**, which provides:

- `memory_save`
- `memory_get`
- `memory_search`
- `memory_update`
- `memory_delete`

Notion resource IDs are kept in local configuration rather than hardcoded into Skills.

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
}
```

This file contains local configuration and should not be committed with personal resource IDs.

### 3. Setup venv
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### 4. Configure MCP

VISION uses MCP servers for its external capabilities.

Configure the following for your preferred CLI:

- **Notion MCP** — manages VISION's Notion workspace.
- **VISION Memory MCP** — manages SQLite-backed session memory.

The CLI handles the model and agent runtime while the MCP servers provide VISION's persistent capabilities.

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

## MCP config
### For opencode (vision/opencode.json)
```json
{
  "mcpServers": {
    "notion": {
      "serverUrl": "https://mcp.notion.com/mcp"
    },
    "vision-memory": {
      "command": "/home/<username>/Desktop/vision/.venv/bin/python3",
      "args": [
        "/home/<username>/Desktop/vision/memory/memory_mcp.py"
      ]
    }
  }
}
```

### For antigravity (vision/.agents/mcp_config.json)
```json
{
  "mcpServers": {
    "notion": {
      "serverUrl": "https://mcp.notion.com/mcp"
    },
    "vision-memory": {
      "command": "/home/<username>/Desktop/vision/.venv/bin/python3",
      "args": [
        "/home/<username>/Desktop/vision/memory/memory_mcp.py"
      ]
    }
  }
}
```

### For codex ( ~/.codex/config.toml)
```toml
[mcp_servers.vision-memory]
command = "/home/<username>/Desktop/vision/.venv/bin/python3"
args = ["/home/<username>/Desktop/vision/memory/memory_mcp.py"] 
```

The selected CLI loads the appropriate instruction file and Skills from the repository.
## Demo

[Watch the VISION demo](https://youtu.be/rzg6q2zhR8g)

## VISION Mini

Check out the **`vision-mini`** branch.

VISION Mini aggressively reduces the size of the Markdown instructions and Skills to investigate how little context VISION actually needs while maintaining reliable agent behavior.

The current `main` branch remains the full V1 implementation and serves as the baseline for comparison.
