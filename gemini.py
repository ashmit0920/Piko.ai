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

    The topic for which you need to write manim code is - {topic}
    
    """

    res = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt)

    return res.text
