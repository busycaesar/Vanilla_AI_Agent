from pydantic import BaseModel, Field

## Data Models for each working stage.

## 1. Making sure that the query talks about an event.
class IsEvent(BaseModel):
    description: str = Field(
        description="Raw description of the event."
    )
    is_calendar_event: bool = Field(
        description="Does this query describes a calendar event."
    )
    confidence_score: float = Field(
        description="Confidence score between 0 and 1."
    )

## 2. Extracting the event details from the query.
class EventDetails(BaseModel):
    name: str = Field(
        description="Name of the event."
    )
    timestamp: str = Field(
        description="Date and time."
    )
    duration_in_minutes: int = Field(
        description="Duration in mintues."
    )
    participants: list[str] = Field(
        description="List of all the participants."
    )

class EventConfirmation(BaseModel):
    confiration_message: str = Field(
        description="Natural language confirmation message."
    )
    calendar_link: str = Field(
        description="Calendar link if applicable."
    )
