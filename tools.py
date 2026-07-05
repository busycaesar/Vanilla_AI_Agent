import requests
import json

# Tool for the agent to get the weather at the specificed coordinates.
def get_weather(latitude: float, longitude: float) -> float:
    """
    Fetch the current temperature (°C) for a given latitude/longitude
    using the free Open-Meteo API.

    Args:
        latitude: Latitude of the location.
        longitude: Longitude of the location.

    Returns:
        Current temperature in Celsius.

    Raises:
        requests.HTTPError: If the API request fails.
        KeyError: If the expected data is missing from the response.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    return data["current_weather"]["temperature"]

def search_knowledge_base(question: str):
    """
    Load the whole knowledge based from the json file.
    """
    with open("kb.json", "r") as f:
        return json.load(f)

# Declaring the list of tools and required arguments, to assist the LLM.
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for the provided longitude and latitude coordinates.",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"},
                },
                "required": ["latitude", "longitude"],
                "additionalProperties": False,
            },
            "strict": True
        }
    },
        {
        "type": "function",
        "function": {
            "name": "search_knowledge_base",
            "description": "Load the whole knowledge based from the json file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                },
                "required": ["question"],
                "additionalProperties": False,
            },
            "strict": True
        }
    }
]

# Executes the function by passing the arguments.
def call_function(name, args):
    if name == "get_weather":
        return get_weather(**args)
    elif name == "search_knowledge_base":
        return search_knowledge_base(**args)