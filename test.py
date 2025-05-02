import time
import re
import asyncio
from concurrent.futures import ThreadPoolExecutor
import subprocess

executor = ThreadPoolExecutor()

classname = "strings_in_programming"


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
        print("STDOUT:\n", stdout)
        print("STDERR:\n", stderr)

    except Exception as e:
        print(f"Error running Manim: {e}")


# loop = asyncio.new_event_loop()
# loop.run_in_executor(executor, run_manim,
#                      "generated/strings_in_programming.py", classname)

future = executor.submit(
    run_manim, "generated/test_string.py", "test_string")
