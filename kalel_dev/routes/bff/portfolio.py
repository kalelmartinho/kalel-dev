from fastapi import APIRouter, Request

from kalel_dev.core.context import create_context
from kalel_dev.core.enums.page import Page
from kalel_dev.core.front import templates

page = Page.PORTFOLIO
router = APIRouter()


@router.get("/portfolio")
async def portfolio_page(request: Request):

    return templates.TemplateResponse("/portfolio.html", create_context(request, page))
