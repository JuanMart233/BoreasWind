import mysql.connector
import os
from dotenv import load_dotenv

_search_dirs = [
    os.path.dirname(__file__),
    os.path.join(os.path.dirname(__file__), ".."),
    os.path.join(os.path.dirname(__file__), "..", ".."),
    os.path.join(os.path.dirname(__file__), "..", "..", "base"),
]
for _d in _search_dirs:
    _env = os.path.join(os.path.abspath(_d), ".env")
    if os.path.exists(_env):
        load_dotenv(_env)
        break

class Database:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            use_pure=True
        )
