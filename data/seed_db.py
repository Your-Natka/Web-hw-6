import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta
from data.config import DB_PATH

fake = Faker()

NUM_GROUPS = 3
NUM_STUDENTS = 50
NUM_TEACHERS = 5
NUM_SUBJECTS = 8
MAX_GRADES_PER_STUDENT = 20

def seed_data():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        # Створення груп
        groups = [f"Група {i+1}" for i in range(NUM_GROUPS)]
        cur.executemany("INSERT INTO groups (name) VALUES (?)", [(g,) for g in groups])

        # Створення викладачів
        teachers = [fake.name() for _ in range(NUM_TEACHERS)]
        cur.executemany("INSERT INTO teachers (full_name) VALUES (?)", [(t,) for t in teachers])

        # Отримання ID викладачів
        cur.execute("SELECT id FROM teachers")
        teacher_ids = [row[0] for row in cur.fetchall()]

        # Створення предметів
        subjects = [fake.job() for _ in range(NUM_SUBJECTS)]
        subjects_data = [(name, random.choice(teacher_ids)) for name in subjects]
        cur.executemany("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", subjects_data)

        # Отримання ID груп
        cur.execute("SELECT id FROM groups")
        group_ids = [row[0] for row in cur.fetchall()]

        # Створення студентів
        students = [(fake.name(), random.choice(group_ids)) for _ in range(NUM_STUDENTS)]
        cur.executemany("INSERT INTO students (full_name, group_id) VALUES (?, ?)", students)

        # Отримання ID студентів і предметів
        cur.execute("SELECT id FROM students")
        student_ids = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT id FROM subjects")
        subject_ids = [row[0] for row in cur.fetchall()]

        # Створення оцінок
        grades = []
        for student_id in student_ids:
            for _ in range(random.randint(10, MAX_GRADES_PER_STUDENT)):
                subject_id = random.choice(subject_ids)
                grade = random.randint(60, 100)
                date_of = fake.date_between(start_date='-6m', end_date='today')
                grades.append((student_id, subject_id, grade, date_of))

        cur.executemany("""
            INSERT INTO grades (student_id, subject_id, grade, date_of)
            VALUES (?, ?, ?, ?)
        """, grades)

        conn.commit()
        print("✅ Базу даних заповнено випадковими даними!")

if __name__ == "__main__":
    seed_data()

