from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # -------------------------------
    # Project Information
    # -------------------------------
    PROJECT_NAME: str = "Bharat Sahayak AI"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = (
        "AI-powered multilingual government scheme assistant"
    )

    API_V1_PREFIX: str = "/api/v1"

    # -------------------------------
    # Security
    # -------------------------------
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # -------------------------------
    # Database
    # -------------------------------
    DATABASE_URL: str

    # -------------------------------
    # AI Providers
    # -------------------------------
    OPENAI_API_KEY: str = ""
    GROQ_API_KEY: str = ""

    # -------------------------------
    # Vector Database
    # -------------------------------
    CHROMA_DB_PATH: str = "./data/chroma"

    # -------------------------------
    # CORS
    # -------------------------------
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    # -------------------------------
    # Logging
    # -------------------------------
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()