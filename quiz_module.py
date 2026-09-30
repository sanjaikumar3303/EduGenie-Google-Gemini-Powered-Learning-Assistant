import json
import re
from gemini_client import generate_text

def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()

def generate_quiz(passage: str) -> dict:
    prompt = f"""
Create exactly 3 multiple-choice questions from the passage below.

Rules:
- Each question must have exactly 4 options.
- Provide one correct answer.
- Make distractors plausible.
- Return ONLY valid JSON.
- JSON format:
{{
  "questions": [
    {{
      "question": "Question text",
      "options": ["A", "B", "C", "D"],
      "answer": "Correct option text"
    }}
  ]
}}

Passage:
{passage}
"""
    try:
        raw = generate_text(prompt)
        data = json.loads(clean_json_block(raw))

        questions = data.get("questions", [])
        if len(questions) != 3:
            raise ValueError("The model did not return exactly 3 questions.")

        for item in questions:
            if len(item.get("options", [])) != 4:
                raise ValueError("Each question must contain 4 options.")
            if item.get("answer") not in item["options"]:
                raise ValueError("Correct answer must match one option.")

        return {"questions": questions}
    except Exception as exc:
        return {"questions": [], "error": f"Quiz generation failed: {exc}"}
