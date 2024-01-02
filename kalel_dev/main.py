from fastapi import FastAPI

from kalel_dev.core.front import static_files
from kalel_dev.routes.router import get_api_router, get_bff_router


def create_app():
    """Factory function for creating the FastAPI app"""
    fast_api = FastAPI()

    fast_api.include_router(get_bff_router(), tags=["bff"])
    fast_api.include_router(get_api_router(), prefix="/api")

    fast_api.mount("/static", static_files, name="static")

    return fast_api


app = create_app()

