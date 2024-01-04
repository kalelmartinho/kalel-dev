from fastapi import APIRouter

from .bff import index_router, contact_router


def get_bff_router():
    bff_router = APIRouter()
    bff_router.include_router(index_router)
    bff_router.include_router(contact_router)
    return bff_router


def get_api_router():
    api_router = APIRouter()
    return api_router
