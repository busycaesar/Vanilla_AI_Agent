from pydantic import BaseModel, Field

class WeatherResponse(BaseModel):
    temperature: float = Field(
        description="The current temperature in celsius for the given coordinates."
    )
    response: str = Field(
        description="A natural language response to the user's question."
    )

class KBResponse(BaseModel):
    answer: str = Field(
        description="This is the answer to the user's question."
    )
    source: int = Field(
        description="This is the record id of the answer."
    )
