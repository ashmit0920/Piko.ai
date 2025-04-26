from fastapi import FastAPI
from gemini import generate_manim_code
import subprocess

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API working!"}


@app.get("/code/{topic}")
async def get_code(topic: str):
    code = generate_manim_code(topic)

    filename = f"{topic}_manim.py"
    with open(filename, "w") as f:
        f.write(code)

    subprocess.Popen(["python", filename],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return {"status": "Code Generated and executed.", "file": filename}
