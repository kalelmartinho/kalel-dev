from fastapi import APIRouter, Request

from kalel_dev.core.context import create_context
from kalel_dev.core.enums.page import Page
from kalel_dev.core.front import templates

page = Page.CONTACT
router = APIRouter()


@router.get("/contact")
async def contact_page(request: Request):

    return templates.TemplateResponse("/contact.html", create_context(request, page))
