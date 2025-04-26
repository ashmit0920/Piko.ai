from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY = os.getenv("gemini_key")

client = genai.Client(api_key=GEMINI_KEY)


def generate_manim_code(topic):
    prompt = f"Manim is a python library used to generate mathematical/scientific/programming animations. You need to write python code using python's Manim library, to generate beautiful and aesthetic animations about a given code. Your response should strictly ONLY CONTAIN THE PYTHON CODE and nothing else, no intro or outro lines or any descriptions. The output should be purely text, do not use code block formats (like ```python```). Do not write any comments in the code and use proper indentation to make sure it works correctly. In the code, keep the required Class name exactly the same as topic name. The topic for which you need to write manim code is - {topic}"
    res = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt)

    return res.text
