from fastapi import APIRouter
from .front import router as front_router


def get_bff_router():
    bff_router = APIRouter()
    bff_router.include_router(front_router)
    return bff_router


def get_api_router():
    api_router = APIRouter()
    return api_router
