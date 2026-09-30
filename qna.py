from gemini_client import generate_text

def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, a student-friendly educational assistant.

Answer the following question accurately and concisely.
Explain the answer in simple language suitable for a learner.
Use examples when they make the concept clearer.
Do not invent facts.

Question:
{question}
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Unable to generate the answer: {exc}"
