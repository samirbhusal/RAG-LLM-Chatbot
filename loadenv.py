from openai import OpenAI
from dotenv import load_dotenv
import os

def get_openai_client() -> OpenAI:
    """
    Utility function to load environment variables and initialize the OpenAI client.

    Returns:
        OpenAI: An authenticated OpenAI client instance using the API key from .env.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY not found. Please set it in your .env file.")

    # Initialize and return the OpenAI client
    return OpenAI(api_key=api_key)