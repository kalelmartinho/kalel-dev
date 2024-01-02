from fastapi import FastAPI

from kalel_dev.core.front import static_files
from kalel_dev.routes.router import get_api_router, get_bff_router


def create_app():
    """Factory function for creating the FastAPI app"""
    fastapi = FastAPI()

    fastapi.include_router(get_bff_router(), tags=["bff"])
    fastapi.include_router(get_api_router(), prefix="/api")

    fastapi.mount("/static", static_files, name="static")

    return fastapi


app = create_app()
