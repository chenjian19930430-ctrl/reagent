"""App configuration."""
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "ReAgent"
    VERSION: str = "0.1.0"
    DEBUG: bool = False
    DATABASE_URL: str = "postgresql+asyncpg://reagent:reagent@localhost:5432/reagent"
    REDIS_URL: str = "redis://localhost:6379/0"
    CORS_ORIGINS: List[str] = ["http://localhost:3000","http://localhost:5173"]
    LLM_API_KEY: str = ""
    LLM_BASE_URL: str = "https://api.deepseek.com/v1"
    LLM_MODEL: str = "deepseek-chat"
    DOUYIN_APP_ID: str = ""
    KUAISHOU_APP_ID: str = ""
    XIAOHONGSHU_APP_ID: str = ""
    WECHAT_VIDEO_APP_ID: str = ""
    WECHAT_CORP_ID: str = ""
    WECHAT_CORP_SECRET: str = ""
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
