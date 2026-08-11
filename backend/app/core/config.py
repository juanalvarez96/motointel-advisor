from functools import lru_cache
from typing import Literal 
from pydantic_settings import BaseSettings, SettingsConfigDict

RepositoryBackend = Literal["memory", "dynamodb"]


class Settings(BaseSettings):
    app_name: str = "MotoIntel Advisor API"
    environment: str = "local"
    repo_backend: RepositoryBackend = "memory"
    dynamodb_table_name: str = "motointel-advisor-dev-knowledge"
    aws_region: str = "eu-west-1"

    model_config = SettingsConfigDict(
        env_prefix="MOTOINTEL_",
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
