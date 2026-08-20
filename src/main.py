from google import genai
from dotenv import load_dotenv
import os

from tools.business_tools import (
    get_halls,
    get_hall_details,
    check_hall_availability
)


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def main():

    user_message = input("Customer: ")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_message,
        config={
            "tools": [
                get_halls,
                get_hall_details,
                check_hall_availability
            ]
        }
    )

    print("\nEventOps AI:")
    print(response.text)


if __name__ == "__main__":
    main()