from src.logger import logger
from src.agent import agent_ask
from datetime import datetime
from typing import Optional
from src.prompt_chaining.schemas import IsEvent, EventDetails, EventConfirmation

TODAY = datetime.now()
DATE_CONTEXT = f"Today is {TODAY.strftime('%A, %B %d, %Y')}."

# Workflow of the function.
def extract_event_info(user_input: str) -> IsEvent:
    """
    LLM call to determine if the event is a calendar event.
    """
    logger.info("[Extracting] Analysing of the event is a calender event.")
    logger.debug(f"[Extracting] Input text {user_input}")

    messages = [
        {
            "role":"system",
            "content": f"{DATE_CONTEXT} Analyze if the text describes a calendar event."
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    response = agent_ask(messages, IsEvent)

    logger.info(f"[Extracting] Extraction Complete. Is Calendar Event: {response.is_calendar_event}; Confidence: {response.confidence_score}.")

    return response

def parse_event_details(description: str) -> EventDetails:
    """
    LLM call to extract specific event details.
    """
    # Log the information
    logger.info("[Parsing] Initiating the event details parsing")

    messages = [
        {
            "role": "system",
            "content": f"{DATE_CONTEXT}. Extract detailed event information. When dates reference 'next Tuesday' or similar relative dates, use this current date as reference."
        },
        {
            "role": "user",
            "content": description
        }
    ]

    # Call the LLM
    response = agent_ask(messages, EventDetails)

    # Log the result
    logger.info(f"[Parsing] Parsed event details. Event name: {response.name}; Event Duration: {response.duration_in_minutes}; Event Date: {response.timestamp}.")
    logger.info(f"[Parsing] Participants: {', '.join(response.participants)}")

    # Return the result
    return response

def generate_confirmation(event_details: EventDetails) -> Optional[EventConfirmation]:
    """
    LLM call to generate the confirmation message.
    """
    logger.info("[Generating] Generating the confirmation message for the user.")

    messages = [
        {
            "role": "system",
            "content": "Generate a natural confirmation message for the event. Sign of with your name; Susie"
        },
        {
            "role": "system",
            "content": str(event_details.model_dump())
        }
    ]

    response = agent_ask(messages, EventConfirmation)

    logger.info(f"[Generating] Confirmation Message Generated. {response}")

    return response

def process_calendar_request(user_input: str) -> Optional[EventConfirmation]:
    logger.info("[Processing] Started processing the calendar event.")

    initial_extration = extract_event_info(user_input)

    logger.info(f"[Processing] Extrated event information. {initial_extration}")

    if (
        not initial_extration.is_calendar_event
        or  initial_extration.confidence_score < 0.7
    ): return None

    logger.info("[Processing] Confirmed that this is a calendar event.")

    event_details = parse_event_details(initial_extration.description)

    logger.info(f"[Processing] Event details parsed {event_details}.")

    confirmation = generate_confirmation(event_details)

    logger.info(f"[Processing] Confirmation message generated {confirmation}.")

    return confirmation