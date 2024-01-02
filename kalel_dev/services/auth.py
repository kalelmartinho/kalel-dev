from itsdangerous import URLSafeTimedSerializer
from pydantic import EmailStr
from kalel_dev.core.config import settings


def create_temp_token(email: EmailStr) -> str:
    serializer = URLSafeTimedSerializer(settings.token_key, salt='temp-token')
    return str(serializer.dumps(email))