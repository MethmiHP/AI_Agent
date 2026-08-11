import os

from dotenv import load_dotenv
from google import genai

from tools.calculator import add_numbers


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is 25 + 37?",
    config={
        "tools": [add_numbers]
    }
)

print(response.text)