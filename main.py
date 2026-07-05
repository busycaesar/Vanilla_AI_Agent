from agent import agent_run
from schemas import WeatherResponse, KBResponse

# system_prompt = "You are a helpful weather assistant."

# user_query = "Whats the weather like in Paris today?"

system_prompt = "You are a helpful assistant that answers questions from the knowledge base about our e-commerce store."

user_query = "What is the return policy?"

messages = [
            {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": user_query,
        },
]

final_response = agent_run(messages, KBResponse)

print(final_response)