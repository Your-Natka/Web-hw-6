from data.config import DB_PATH
import sqlite3

def get_subjects():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM subjects")
        return [row[0] for row in cursor.fetchall()]

if __name__ == "__main__":
    subjects = get_subjects()
    print("Список предметів у базі:")
    for subject in subjects:
        print(subject)