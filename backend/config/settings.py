from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME: str = "Bharat Sahayak AI"
    PROJECT_VERSION: str = "1.0.0"

    API_V1_PREFIX: str = "/api/v1"

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    DATABASE_URL: str

    OPENAI_API_KEY: str = ""
    GROQ_API_KEY: str = ""

    CHROMA_DB_PATH: str = "./data/chroma"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings():
    return Settings()