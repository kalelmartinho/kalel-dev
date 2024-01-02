from beanie import Document
from pydantic import BaseModel


class Comment(Document, BaseModel):
    """Comment model"""

    author: str
    content: str
    post_id: str
