import os
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URI: str
    DATABASE_URL: bool

    class Config:
        env = os.environ["APP_CONFIG_FILE"]
        env_file = Path(__file__).parent.parent / f"config/{env}.env"
        case_sensitive = True
