from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from kalel_dev.core.config import settings

from kalel_dev.models.post import Post
from kalel_dev.models.page_context import PageContext
from kalel_dev.models.user import User
from kalel_dev.models.comment import Comment
from kalel_dev.models.project import Project


async def init_db():
    db_client = AsyncIOMotorClient(settings.db_url)
    await init_beanie(
        database=db_client.db_name,
        document_models=[
            Post,
            PageContext,
            User,
            Comment,
            Project,
        ]
    )
