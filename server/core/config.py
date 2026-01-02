from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache

class Configuration(BaseSettings):
    APP_NAME: str = "Portfolio"
    ENV: str = Field(default="local")
    DEBUG: bool = False
    DATABASE_URL: str
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

@lru_cache
def get_config() -> Configuration:
    return Configuration()