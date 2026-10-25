# AI Conversational Assistant

A command-line chat assistant built as a LangGraph ReAct agent that can answer
questions and call a tool when a calculation is needed.

## What it does

- Runs an interactive chat loop in the terminal (type `quit` to exit).
- Uses `create_react_agent` from LangGraph with an OpenAI chat model at temperature 0.
- Exposes one tool, `calculator`, which adds two numbers; the agent decides when to call it.
- Streams the agent's replies as they are generated.

## Tech stack

Python 3.10, LangChain, LangGraph, OpenAI API, python-dotenv, uv

## How to run

```bash
git clone https://github.com/starknight24/AI-conversational-assistant.git
cd AI-conversational-assistant
echo "OPENAI_API_KEY=your-key" > .env
uv run main.py
```

Without uv: `pip install langchain langchain-openai langgraph python-dotenv`, then `python main.py`.
