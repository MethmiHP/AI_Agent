import os

from google import genai
from dotenv import load_dotenv


load_dotenv()


class EventOpsAgent:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(
            api_key=api_key
        )

    def ask(self, message: str) -> str:

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=message
        )

        return response.text