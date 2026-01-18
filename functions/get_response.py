from google.genai import types
from config import SYSTEM_PROMPT
from functions import schema

def get_response(client, model, messages):
    return client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[schema.available_functions],
            ),
    )