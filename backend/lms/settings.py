from dotenv import load_dotenv
from os import getenv
from pathlib import Path


class Config:

    def __init__(self):
        load_dotenv("../.env")
        self.SECRET_KEY = getenv('SECRET_KEY')
        self.SQLALCHEMY_DATABASE_URI = f"{getenv('DATABASE_ENGINE')}://{getenv('DATABASE_USER')}:{getenv('DATABASE_PASSWORD')}@{getenv('DATABASE_HOST')}/{getenv('DATABASE_NAME')}"


PROJECT_DIR = Path(__file__).resolve().parent
BASE_DIR = PROJECT_DIR.parent
GLOBAL_DIR = BASE_DIR.parent

MEDIA_ROOT = GLOBAL_DIR / "media"

MEDIA_URL = "/media/"

STATIC_ROOT = PROJECT_DIR / "static"

STATIC_URL = "/static/"
