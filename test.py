from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY = os.getenv("gemini_key")
client = genai.Client(api_key=GEMINI_KEY)


def generate_explanation(topic):
    prompt = f"""You are an intelligent and friendly learning assistant designed to help users understand academic topics in a clear and approachable way.

    Given a topic, generate a brief and accurate explanation suitable for students or self-learners.

    Follow these strict guidelines:
    1. Keep the explanation concise — **no more than 5-7 sentences**.
    2. Use simple, **conversational language** while maintaining technical correctness.
    3. Start with a clear definition or high-level overview of the topic.
    4. Include **one key insight or real-world example** if appropriate.
    5. **Avoid excessive jargon, equations, or code** — focus on clarity.
    6. Do **not greet the user**, ask questions, or include motivational phrases.
    7. Your output should be **only the explanation**, with **no headings, bullet points, or extra formatting**.

    Topic: {topic}
    """

    res = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt)

    return res.text
