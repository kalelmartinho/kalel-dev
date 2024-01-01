from beanie import Document
from pydantic import BaseModel, HttpUrl
from typing import Annotated


class Project(Document, BaseModel):
    """Project model"""
    name: str
    short_description: str
    description: str
    github_url: Annotated[HttpUrl, str]


