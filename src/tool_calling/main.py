from src.agent import agent_run
from src.tool_calling.schemas import WeatherResponse, KBResponse
from src.tool_calling.tools import tools, call_function

# Set the WEATHER True for letting the agent use the tool. Additionally, set the KNOWLEDGE_BASE true to see how the agent retrieves the knowledge from external source.
WEATHER = False
KNOWLEDGE_BASE = True

if WEATHER:
    system_prompt = "You are a helpful weather assistant."
    user_query = "Whats the weather like in Paris today?"
elif KNOWLEDGE_BASE:
    system_prompt = "You are a helpful assistant that answers questions from the knowledge base about our e-commerce store."
    user_query = "What is the return policy?"
else:
    raise ValueError("No mode selected: set WEATHER or KNOWLEDGE_BASE to True.")

messages = [
            {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": user_query,
        },
]

final_response = agent_run(messages, WeatherResponse if WEATHER else KBResponse if KNOWLEDGE_BASE else None, tools, call_function)

print(final_response)