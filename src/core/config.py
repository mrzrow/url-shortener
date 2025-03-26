import os

from pathlib import Path
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
BASE = Path(__file__).parent.parent.parent


class DatabaseSettings(BaseModel):
    url: str = os.environ.get('DB_PATH').format(BASE)
    echo: bool = bool(int(os.environ.get('DB_ECHO')))


class Settings(BaseModel):
    api_prefix: str = os.environ.get('API_PATH')
    db: DatabaseSettings = DatabaseSettings()


settings = Settings()
print(settings.db.url)
