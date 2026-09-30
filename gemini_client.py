import os
from dotenv import load_dotenv

load_dotenv()

try:
    from google import genai
except ImportError:
    genai = None

_client = None

def get_client():
    global _client
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured. Create a .env file from .env.example."
        )

    if genai is None:
        raise RuntimeError(
            "The google-genai package is not installed. Run: pip install -r requirements.txt"
        )

    if _client is None:
        _client = genai.Client(api_key=api_key)

    return _client


def generate_text(prompt: str) -> str:
    client = get_client()
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    response = client.models.generate_content(model=model, contents=prompt)

    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")

    return text.strip()
