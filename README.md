# Agent Without Framework

## Description

A learning project to understand how AI agents work under the hood, built with pure Python and the OpenAI SDK directly, no agent frameworks (no LangChain, LangGraph, CrewAI, etc.).

## Tech Stack

![Image Alt](https://skillicons.dev/icons?i=python)

## Features

- Manual tool-calling loop: model requests a tool call, Python dispatches it, result is fed back to the model
- Tool definitions and dispatch handled with plain Python, no framework abstractions
- Structured output via a Pydantic schema instead of a framework's output parser

## AI Configuration

- SDK: `openai` (used directly, no agent framework)
- Model: `gpt-4o-mini`

## How to run the project?

1. Copy `.env.example` to `.env` and fill in the values
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r req.txt`
4. Run `python main.py`

## Author

[Dev J. Shah](https://github.com/busycaesar)
