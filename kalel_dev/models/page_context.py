from beanie import Document
from pydantic import BaseModel
from kalel_dev.core.enums.page import Page
from typing import Annotated


class PageContext(Document, BaseModel):
    """PageContext model"""

    page: Annotated[Page, str]
    context: dict