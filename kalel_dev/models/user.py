from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr
from typing import Annotated


class User(Document, BaseModel):
    """User model

    Admin users can manage posts, projects and users comments
    Non-admin users can only comment and react to posts

    """
    name: str
    email: Annotated[EmailStr, Indexed(str)]
    password_hash: str
    admin: bool