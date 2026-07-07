from src.config import client
import json

def agent_run(messages, response_format, tools, call_function):
    # Passing the message to the model.
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        # Passing the list of tools that LLM has access to in order to help answer the question of the user.
        tools=tools,
    )

    # Executing the tools suggested by the model and appending the results into the message.
    for tool_call in completion.choices[0].message.tool_calls:
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        messages.append(completion.choices[0].message)

        # Executing the function that model ask to run by passing the parameters.
        result = call_function(name, args)

        # Appending the function result into the messages.
        messages.append(
            {"role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result)}
        )

    response = agent_ask(messages, response_format)

    return response

def agent_ask(messages, response_format):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=messages,
      #  tools=tools,
        # Passing the format in which the response is required.
        response_format=response_format,
    )

    return completion.choices[0].message.parsed