from typing import Annotated

from beanie import Document
from pydantic import BaseModel, HttpUrl


class Project(Document, BaseModel):
    """Project model"""

    name: str
    short_description: str
    description: str
    github_url: Annotated[HttpUrl, str]
