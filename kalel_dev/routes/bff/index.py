from fastapi import APIRouter, Request
from kalel_dev.core.front import templates

router = APIRouter()


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("/main.html", {"request": request})
