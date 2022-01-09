import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.resolve()
ENV_PATH = Path(BASE_DIR, ".env")
load_dotenv(ENV_PATH)
TG_API_KEY = os.getenv("TG_API_KEY")
TG_BOT_NAME = os.getenv("TG_BOT_NAME")
