from src.logger import logger
from src.prompt_chaining.workflow import process_calendar_request

user_input = "Let's schedule a 1h team meeting next Tuesday at 2pm with Alice and Bob to discuss the project roadmap."
# user_input = "Can you send an email to Alice and Bob to discuss the project roadmap?"

logger.info(f"[Main] {user_input}")

result = process_calendar_request(user_input)

logger.info(f"[Main] Calendar request is processed. {result}")

if result:
    print(f"Confirmation {result.confiration_message}.")
    if result.calendar_link:
        print(f"Calendar Link", result.calendar_link)
else:
    print("The content does not appear to be a calendar event.")