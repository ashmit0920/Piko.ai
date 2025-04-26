from fastapi import FastAPI
from gemini import generate_manim_code
import subprocess
import asyncio
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()
executor = ThreadPoolExecutor()


def run_manim_code(code: str):
    try:
        exec(code)

    except Exception as e:
        print(f"Error while running generated code: {e}")


@app.get("/")
def home():
    return {"message": "API working!"}


@app.get("/code/{topic}")
async def generate_and_run_code(topic: str):

    code = generate_manim_code(topic)

    loop = asyncio.get_event_loop()
    loop.run_in_executor(executor, run_manim_code, code)

    return {"status": "Code Generated and executed in background."}
