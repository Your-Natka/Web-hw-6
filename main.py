from data.config import DB_PATH
import sqlite3

# Підключення до бази
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Показати всі таблиці для контролю
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Таблиці в базі:", cursor.fetchall())
    
conn.close()


def execute_query(query_path, params=None):
    with open(query_path, 'r', encoding='utf-8') as f:
        query = f.read()
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Таблиці в базі:", tables)

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
    
    return results


if __name__ == "__main__":
    # Запит 1
    results = execute_query('sql/query_01.sql')
    print("5 студентів із найбільшим середнім балом:")
    for row in results:
        print(row)

    # Запит 2
    subject = "Біолог"  # ← або будь-який інший із твоїх предметів
    results = execute_query('sql/query_02.sql', {"subject_name": subject})
    print(f"Студент із найвищим середнім балом з предмета '{subject}':")
    for row in results:
        print(row)

    # Запит 3
    subject = "Біолог"
    results = execute_query('sql/query_03.sql', {"subject_name": subject})
    print(f"Середній бал у групах з предмета '{subject}':")
    for row in results:
        print(row)

    # Запит 4
    results = execute_query('sql/query_04.sql')
    print("\nСередній бал на потоці:")
    for row in results:
        print(row)

    # Запит 5
    teacher = "Давид Петренко"  # 🔁 змінити на ім'я з бази
    results = execute_query('sql/query_05.sql', {"teacher_name": teacher})
    print(f"\nКурси, які читає викладач {teacher}:")
    for row in results:
        print(row)

    # Запит 6
    group = "Група 1"  # 🔁 змінити на назву групи з бази
    results = execute_query('sql/query_06.sql', {"group_name": group})
    print(f"\nСтуденти у групі {group}:")
    for row in results:
        print(row)

    # Запит 7
    subject = "Біолог"         # 🔁 предмет
    group = "Група 1"          # 🔁 група
    results = execute_query('sql/query_07.sql', {"group_name": group, "subject_name": subject})
    print(f"\nОцінки студентів групи {group} з предмета {subject}:")
    for row in results:
        print(row)

    # Запит 8
    teacher = "Давид Петренко"  # 🔁 ім’я викладача
    results = execute_query('sql/query_08.sql', {"teacher_name": teacher})
    print(f"\nСередній бал, який ставив викладач {teacher}:")
    for row in results:
        print(row)

    # Запит 9
    student = "Зорян Арсенич"  # 🔁 ім’я студента
    results = execute_query('sql/query_09.sql', {"student_name": student})
    print(f"\nКурси, які відвідує студент {student}:")
    for row in results:
        print(row)

    # Запит 10
    student = "Зорян Арсенич"     # 🔁 ім’я студента
    teacher = "Давид Петренко"    # 🔁 ім’я викладача
    results = execute_query('sql/query_10.sql', {"student_name": student, "teacher_name": teacher})
    print(f"\nКурси, які студенту {student} читає викладач {teacher}:")
    for row in results:
        print(row) 

         