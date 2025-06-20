from fastapi import FastAPI, HTTPException
from gemini import generate_manim_code, generate_explanation
import subprocess
from concurrent.futures import ThreadPoolExecutor
import re
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from text_to_speech import generate_audio

app = FastAPI()
executor = ThreadPoolExecutor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    explanation = generate_explanation(topic)
    generate_audio(explanation)

    return {"status": "Manim animation is rendering in background.", "explanation": explanation}

app.mount("/static/videos", StaticFiles(directory="media/videos"), name="videos")
app.mount("/audio", StaticFiles(directory="."), name="audio")


@app.get("/videos/{topic}/{resolution}/file")
def get_generated_video(topic: str, resolution: str):
    dir_path = os.path.join("media", "videos", topic, resolution)
    print("Checking folder:", dir_path)

    if not os.path.isdir(dir_path):
        print("Folder does not exist")
        raise HTTPException(404, "Topic or resolution not found")

    files = [f for f in os.listdir(dir_path) if f.endswith(".mp4")]
    print("Found files:", files)

    if not files:
        print("No MP4s found yet")
        raise HTTPException(404, "No video found")

    return {"filename": files[0]}
