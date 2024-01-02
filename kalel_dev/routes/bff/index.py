from fastapi import APIRouter, Request

from kalel_dev.core.context import create_context
from kalel_dev.core.enums.page import Page
from kalel_dev.core.front import templates

page = Page.HOME
router = APIRouter()


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("/main.html", create_context(request, page))
