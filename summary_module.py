from gemini_client import generate_text

def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational text for quick revision.

Requirements:
- Preserve the core information.
- Remove unnecessary repetition.
- Use simple language.
- Prefer short paragraphs or bullet points.
- Do not add information that is not present in the source.

Text:
{text}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Unable to generate the summary: {exc}"
