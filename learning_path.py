from gemini_client import generate_text

def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for the topic below.

Topic:
{topic}

Organize the plan from beginner to advanced level.
Include:
- Beginner concepts
- Intermediate concepts
- Advanced concepts
- Suggested order of study
- Approximate timeline
- Practice suggestions
- Useful resource types such as videos, articles, or books

Keep the plan practical and student-friendly.
"""
    try:
        return generate_text(prompt)
    except Exception as exc:
        return f"Unable to generate the learning path: {exc}"
