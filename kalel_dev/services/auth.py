from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from pydantic import EmailStr
from kalel_dev.core.config import settings

token_serializer = URLSafeTimedSerializer(settings.token_key, salt='temp-token')


def create_temp_token(email: EmailStr) -> str:
    return str(token_serializer.dumps(email))


def verify_temp_token(token: str, max_age: int) -> bool:
    try:
        token_serializer.loads(token, max_age=max_age)
    except SignatureExpired:
        return False
    except BadSignature:
        return False
    return True


async def create_session_cookie(response, email: EmailStr) -> str:
    token = create_temp_token(email)
    response.set_cookie(
        key="Authorization",
        value=token,
        expires=settings.refresh_token_expire,
    )
    return response


