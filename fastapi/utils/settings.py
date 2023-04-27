import os
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int

    class Config:
        env = os.environ["APP_CONFIG_FILE"]
        env_file = Path(__file__).parent.parent / f"config/{env}.env"
        case_sensitive = True


settings = Settings()