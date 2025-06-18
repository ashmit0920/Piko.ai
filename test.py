import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


# dir_path = os.path.join("media", "videos", "binary search", "1080p60")
# print("Checking folder:", dir_path)

# if not os.path.isdir(dir_path):
#     print("Folder does not exist")

# files = [f for f in os.listdir(dir_path) if f.endswith(".mp4")]
# print("Found files:", files)

# if not files:
#     print("No MP4s found yet")

app = FastAPI()

app.mount("/videos", StaticFiles(directory="media/videos"), name="videos")


@app.get("/videos/{topic}/{resolution}/file")
def get_generated_video(topic: str, resolution: str):
    dir_path = os.path.join("media", "videos", topic, resolution)
    print("Checking folder:", dir_path)

    if not os.path.isdir(dir_path):
        print("Folder does not exist")

    files = [f for f in os.listdir(dir_path) if f.endswith(".mp4")]
    print("Found files:", files)

    if not files:
        print("No MP4s found yet")

    return {"filename": files[0]}
