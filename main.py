from agent import agent_run

user_query = "Whats the weather like in Paris today?"

messages = [
            {"role": "system", "content": "You are a helpful weather assistant."},
        {
            "role": "user",
            "content": user_query,
        },
]

final_response = agent_run(messages)

print(final_response)