from fastapi import FastAPI
from gemini import generate_manim_code
import subprocess
from concurrent.futures import ThreadPoolExecutor
import re
import asyncio

app = FastAPI()
executor = ThreadPoolExecutor()


def find_scene_class_name(code: str) -> str:
    # extract the manim scene class name from the code

    match = re.search(r'class\s+(\w+)\s*\(.*Scene.*\)\s*:', code)
    if match:
        return match.group(1)
    else:
        return None


def run_manim(file_path: str, class_name: str):
    # run the manim CLI cmd to generate video
    try:
        process = subprocess.Popen(
            ["manim", "-pqh", file_path, class_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate()
        # print("STDOUT:\n", stdout)
        print("STDERR:\n", stderr)

    except Exception as e:
        print(f"Error running Manim: {e}")


@app.get("/")
def home():
    return {"message": "API working!"}


@app.get("/code/{topic}")
async def generate_and_run_code(topic: str):

    code = generate_manim_code(topic)

    file_path = f"generated/{topic}.py"
    with open(file_path, "w") as f:
        f.write(code)

    # Find the class name
    class_name = find_scene_class_name(code)
    if not class_name:
        return {"status": "Failed", "reason": "No Manim Scene class found."}

    # Run Manim asynchronously
    loop = asyncio.new_event_loop()
    loop.run_in_executor(executor, run_manim, file_path, class_name)

    return {"status": "Manim animation is rendering in background.", "file": file_path, "scene": class_name}
