"""Application configuration settings."""

from functools import lru_cache
from typing import List

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Base application settings loaded from environment variables."""

    api_v1_prefix: str = "/api/v1"
    project_name: str = "Dividend Tracker"

    database_url: str = Field(
        ...,
        description="Database connection URL compatible with SQLAlchemy.",
        env="DATABASE_URL",
    )

    aws_region: str = Field("us-east-1", env="AWS_REGION")
    s3_bucket_name: str = Field(..., env="S3_BUCKET_NAME")

    allowed_origins: List[str] = Field(default_factory=lambda: ["http://localhost:3000"])

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Return cached application settings."""

    return Settings()  # type: ignore[arg-type]
