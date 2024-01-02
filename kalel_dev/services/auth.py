from itsdangerous import URLSafeTimedSerializer
from pydantic import EmailStr
from kalel_dev.core.config import settings


def create_temp_token(email: EmailStr) -> str:
    serializer = URLSafeTimedSerializer(settings.token_key, salt='temp-token')
    return str(serializer.dumps(email))


async def create_session_cookie(response, email: EmailStr) -> str:
    token = create_temp_token(email)
    response.set_cookie(
        key="Authorization",
        value=token,
        expires=settings.refresh_token_expire,
    )
    return response
