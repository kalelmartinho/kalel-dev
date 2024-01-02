from beanie import Document
from pydantic import BaseModel


class Post(Document, BaseModel):
    """Post model"""

    author: str
    title: str
    content: str
    tags: list[str]
