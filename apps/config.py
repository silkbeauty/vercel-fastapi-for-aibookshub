import os
import secrets
from typing import ClassVar, Literal
from pydantic_settings import BaseSettings

from dotenv import dotenv_values

class Settings(BaseSettings):
    PROJECT_NAME: str = f"aiBooksHub - {os.getenv('ENV', 'development').capitalize()}"
    DESCRIPTION: str = "AAAA - Ai Automatic Accounting API:  production-ready"
    ENV: Literal["development", "staging", "production"] = "development"
    VERSION: str = "8.8.0801"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    CFG: ClassVar  = dotenv_values(".env")
    API_USERNAME: str = "tEnangIN"
    API_PASSWORD: str = "8t>1pTu4lGTwiY3()?`+WyI|*21z"

    class Config:
        case_sensitive = True


settings = Settings()
