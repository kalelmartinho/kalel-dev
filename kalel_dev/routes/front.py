from fastapi import APIRouter, Request

from kalel_dev.core.context import create_context
from kalel_dev.core.enums.page import Page
from kalel_dev.core.front import templates

router = APIRouter()


@router.get("/")
async def index_page(request: Request):
    page = Page.HOME
    hero_context = {
        "greeting": "Hello, I'm Kalel Martinho",
        "hero_description": "I'm a passionate software engineer currently working as a Python Software Engineer at a startup in Brazil.",
    }
    return templates.TemplateResponse("/main.html", create_context(request, page, hero_context))


@router.get("/about")
async def about_page(request: Request):
    page = Page.ABOUT
    return templates.TemplateResponse("/about.html", create_context(request, page))


@router.get("/blog")
async def blog_page(request: Request):
    page = Page.BLOG
    return templates.TemplateResponse("/blog.html", create_context(request, page))


@router.get("/contact")
async def contact_page(request: Request):
    page = Page.CONTACT
    return templates.TemplateResponse("/contact.html", create_context(request, page))


@router.get("/portfolio")
async def portfolio_page(request: Request):
    page = Page.PORTFOLIO
    return templates.TemplateResponse("/portfolio.html", create_context(request, page))



