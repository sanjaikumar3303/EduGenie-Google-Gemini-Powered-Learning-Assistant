from gemini_client import generate_text

def explain_topic(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational assistant.

Explain this topic in simple, beginner-friendly language:
{topic}

Use this structure when appropriate:
1. Simple definition
2. Main idea
3. Important points
4. Simple example
5. Short recap

Keep the explanation clear and not unnecessarily long.
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Unable to generate the explanation: {exc}"
