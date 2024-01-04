from fastapi import APIRouter, Request

from kalel_dev.core.context import create_context
from kalel_dev.core.enums.page import Page
from kalel_dev.core.front import templates

page = Page.HOME
router = APIRouter()


@router.get("/")
async def index(request: Request):
    hero_context = {
        "greeting": "Hello, I'm Kalel Martinho",
        "hero_description": "I'm a passionate software engineer currently working as a Python Software Engineer at a startup in Brazil.",
    }
    return templates.TemplateResponse("/main.html", create_context(request, page, hero_context))
