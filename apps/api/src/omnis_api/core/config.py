from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration."""

    app_name: str = "OMNIS API"
    app_version: str = "0.1.0"
    api_prefix: str = "/api/v1"
    debug: bool = False
    environment: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="OMNIS_",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()
