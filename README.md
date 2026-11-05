# CrewAIpractice

A multi-agent workflow built with [CrewAI](https://www.crewai.com): a **researcher** agent mines a YouTube channel for a topic, then a **writer** agent turns the findings into a Markdown blog post (`new-blogpost.md`).

## Architecture
```
topic ─▶ Researcher (YoutubeChannelSearchTool) ─▶ research_task ─▶ Writer ─▶ write_task ─▶ new-blogpost.md
```
| File | Role |
|---|---|
| `tools.py` | YouTube channel RAG search tool (channel configurable via env) |
| `agents.py` | Researcher and Writer agents (roles, goals, backstories) |
| `tasks.py` | Task definitions; the writer receives the researcher's output as context |
| `crew.py` | Assembles a sequential crew and runs it from the CLI |

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env     # add OPENAI_API_KEY
```

## Run
```bash
python crew.py                                  # default topic
python crew.py "Retrieval-augmented generation" # custom topic
```
The result is printed and saved to `new-blogpost.md`.

## Learning goals
Agent roles/backstories, task context passing, tools, sequential process, memory and caching.
