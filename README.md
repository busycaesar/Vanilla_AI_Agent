# Agent Without Framework

## Description

A learning project to understand how AI agents work under the hood, built with pure Python and the OpenAI SDK directly, no agent frameworks (no LangChain, LangGraph, CrewAI, etc.).

## Tech Stack

![Image Alt](https://skillicons.dev/icons?i=python)

## Features

- Manual tool-calling loop: model requests a tool call, Python dispatches it, result is fed back to the model
- Tool definitions and dispatch handled with plain Python, no framework abstractions
- Structured output via a Pydantic schema instead of a framework's output parser
- Prompt chaining: a multi-step LLM pipeline where each call's structured output gates and feeds the next

## Project Structure

- `src/prompt_chaining/` — calendar-scheduling example: chains extract → parse → confirm LLM calls to turn a natural-language request into a calendar event
- `src/tool_calling/` — weather / knowledge-base example: manual tool-calling loop with two dispatchable tools and structured output

## AI Configuration

- SDK: `openai`
- Model: `gpt-4o-mini`

## How to run the project?

1. Copy `.env.example` to `.env` and fill in the values
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r req.txt`
4. Run an example from the repo root:
   - Prompt chaining: `python -m src.prompt_chaining.main`
   - Tool calling: `python -m src.tool_calling.main`

## Author

[Dev J. Shah](https://github.com/busycaesar)
