import subprocess
from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager for FastAPI app."""
    try:
        subprocess.run(
            [
                "tailwindcss",
                "-i",
                "kalel_dev/static/src/tw.css",
                "-o",
                "kalel_dev/static/css/main.css",
                "--minify"
            ]
        )
    except:
        print("Error")

    yield