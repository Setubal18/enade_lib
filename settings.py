import os
from pathlib import Path  # python3 only

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

MONGO_URI = os.getenv('MONGO_URI')
DATABASE = os.getenv('DATABASE')
COLLECTION = os.getenv('COLLECTION')
