import sqlite3
from data.config import DB_PATH

def create_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # Таблиця груп
        cur.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """)

        # Таблиця студентів
        cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            group_id INTEGER,
            FOREIGN KEY (group_id) REFERENCES groups (id)
        );
        """)

        # Таблиця викладачів
        cur.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL
        );
        """)

        # Таблиця предметів
        cur.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        );
        """)

        # Таблиця оцінок
        cur.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            grade INTEGER NOT NULL CHECK(grade BETWEEN 1 AND 100),
            date_of TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (subject_id) REFERENCES subjects (id)
        );
        """)

        conn.commit()
        print("✅ Таблиці створено успішно!")

if __name__ == "__main__":
    create_tables()
