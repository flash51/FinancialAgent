# Agents Practice

This repository is a small collection of Python experiments for building LLM-powered agents using OpenRouter-compatible APIs. It explores simple chat interactions, tool calling, streaming responses, and agent loops with safe filesystem/command access.

## What this project contains

The code in this repo demonstrates several patterns:

- Basic OpenRouter chat completion calls
- Reusable agent loops with message history
- Function-calling tools that the model can invoke
- Safe local command execution inside the project workspace
- Reading workspace files as tool results
- MCP-style extension points for external tools/services
- Resume/CV extraction and structured output experiments

## Repository structure

- `chatAgent.py` — simple interactive chat session using OpenRouter
- `chatAgentLoop.py` — single-request example with a basic loop pattern
- `chatAgentLoopWithTool.py` — tool-calling example with a custom horoscope function
- `chatAgentLoopWithTool1.py` — reasoning-enabled chat example
- `completeChatAgent.py` — more complete streaming agent with command/file tools
- `completeChatAgentWithMcp.py` — extended agent with MCP server hooks
- `cvDetailsExtraction.py` — agent-driven extraction flow for CV/resume content
- `structureOutput.py` — structured output experiment with schema-driven responses
- `resume.txt` — sample resume text used for extraction/testing
- `src/agentspractice/` — package scaffolding
- `pyproject.toml` — Python project metadata and dependencies

## Getting started

### Prerequisites

- Python 3.14+ (as declared in `pyproject.toml`)
- An OpenRouter API key

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

If you use `uv`, the project also includes `uv.lock` and can be used with the standard `uv` workflow.

### Set your API key

```bash
export OPENROUTER_API_KEY="your-api-key"
```

## Running the examples

### Basic chat

```bash
python chatAgent.py
```

### Streamed tool-enabled agent

```bash
python completeChatAgent.py
```

### Agent with MCP-style integration

```bash
python completeChatAgentWithMcp.py
```

### CV/resume extraction

```bash
python cvDetailsExtraction.py
```

## Notes on safety and behavior

Several example agents intentionally include a limited tool layer:

- file reads are restricted to the repository workspace
- destructive shell commands are blocked
- commands still require user confirmation before execution

This makes the examples useful for learning about safe tool use, but they are not a full production security model.

## Typical use cases

These scripts are designed to experiment with:

- agent orchestration patterns
- function calling and structured tool use
- OpenRouter integration with multiple models
- resume/knowledge extraction workflows
- prompt + tool chaining for coding assistants

## Disclaimer

This repo is primarily a learning and experimentation space. It is not a packaged product, service, or production deployment system.

