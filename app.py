from fastapi import FastAPI
from gemini import generate_manim_code

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API working!"}


@app.get("/code/{topic}")
def get_code(topic: str):
    return generate_manim_code(topic)
