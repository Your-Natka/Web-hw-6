from data.config import DB_PATH
import sqlite3

def list_subjects():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM subjects;")
        subjects = cursor.fetchall()
    return [s[0] for s in subjects]

if __name__ == "__main__":
    subjects = list_subjects()
    print("Предмети в базі:")
    for subj in subjects:
        print(f"- {subj}")
