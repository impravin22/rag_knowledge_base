from __future__ import annotations

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    app_name: str = Field(default="rag_knowledge_base")
    log_level: str = Field(default="INFO")

    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_", extra="ignore")


class HealthResponse(BaseModel):
    status: str
    name: str
