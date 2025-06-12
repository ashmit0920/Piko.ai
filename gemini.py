from google import genai
import os
from dotenv import load_dotenv
from markdownify import markdownify as md
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()

GEMINI_KEY = os.getenv("gemini_key")

client = genai.Client(api_key=GEMINI_KEY)

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local(
    "manim_index", embedding_model, index_name="index", allow_dangerous_deserialization=True)

# Convert a user topic into a more helpful query for searching Manim documentation.


def generate_search_query(topic: str) -> str:
    base_phrases = [
        f"How to animate {topic} using Manim",
        f"How to visually represent {topic} in Manim",
        f"Manim example for {topic}",
        f"Which Manim objects or animations are useful for {topic}",
        f"How to create a scene about {topic} in Manim"
    ]
    return " | ".join(base_phrases)


def generate_manim_code(topic):
    search_query = generate_search_query(topic)
    docs = vectorstore.similarity_search(
        search_query, k=3)  # get top 3 relevant chunks
    context_text = "\n".join([doc.page_content for doc in docs])

    prompt = f"""Manim is a python library used to generate mathematical/scientific/programming animations. You need to write python code using python's Manim library, to generate beautiful and aesthetic animations about a given topic.
    
    Below is relevant reference information from the official Manim documentation:
    ---
    {context_text}
    ---
    
    STRICTLY follow the guidelines below while writing the manim code -
    
    1. Your response should strictly ONLY CONTAIN THE PYTHON CODE and nothing else, no intro or outro lines or any descriptions.
    2. The output should be purely text, do not use code block formats (like ```python```). 
    3. Do not write any comments in the code and use proper indentation to make sure it works correctly. 
    4. In the code, keep the required Class name exactly the same as topic name.
    5. Do not use classes like Tex() or MathTex() which requires the user to download external dependencies (Latex in this example).
    6. REMEMBER THAT YOU ARE NOT RESTRICTED to the API reference provided above, IT IS JUST ADDITIONAL CONTEXT TO AVOID SYNTAX ERRORS. YOU ARE FREE TO WRITE MANIM CODE OTHER THAN THE REFERENCES PROVIDED ABOVE.

    The topic for which you need to write manim code is - {topic}. Ideate on how a good and well-explained animation should look like, along with text and annotations in the animation - and write code for it accordingly.
    The animation should atleast be around 15-20 seconds, there's no upper limit write as much code as needed.
    
    """

    res = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt)

    return res.text


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
