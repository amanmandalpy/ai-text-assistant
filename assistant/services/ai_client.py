import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()


def get_ai_client():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured.")

    client = OpenAI(api_key=api_key)

    return client
