"""Application configuration."""

import os
from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database
    database_url: str = "postgresql://user:password@localhost/room_api"
    
    # Environment
    python_env: str = "development"
    log_level: str = "INFO"
    
    # API
    api_title: str = "Room API"
    api_version: str = "1.0.0"
    api_description: str = "CRUD REST API for room management"

    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    """Get application settings.
    
    Returns:
        Settings: Cached application settings instance.
    """
    return Settings()
