from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Finance Quiz"
    app_env: str = "development"
    debug: bool = True

    host: str = "0.0.0.0"
    port: int = 8000

    secret_key: str

    database_url: str

    telegram_bot_token: str = ""

    webhook_url: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()