from beanie import Document
from pydantic import BaseModel, EmailStr
from typing import Annotated


class Message(Document, BaseModel):
    """Message model for contact form"""

    name: str
    email: Annotated[EmailStr, str]
    phone: str
    subject: str

