from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    cookie_exp: int = 60 * 60 * 24
    token_key: str = "secret"

    db_user: str = ""
    db_password: str = ""
    db_host: str = "localhost"
    db_port: int = 27017
    db_name: str = ""
    db_url: str = f"mongodb://{db_host}:{db_port}"


settings = Settings()
