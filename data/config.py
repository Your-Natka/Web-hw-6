from pathlib import Path

# Абсолютний або відносний шлях до SQLite бази
BASE_DIR = Path(__file__).resolve().parent.parent
DB_NAME = "student.db"
DB_PATH = DB_PATH= BASE_DIR / DB_NAME
