import sqlite3

conn = sqlite3.connect('school_v2.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        subject TEXT,
        experience INTEGER
    )
""")

conn.commit()

cursor.execute("INSERT INTO teachers (name, subject, experience) VALUES (?, ?, ?)", ("Иванов Иван", "Математика", 10))
cursor.execute("INSERT INTO teachers (name, subject, experience) VALUES (?, ?, ?)", ("Петрова Анна", "Русский язык", 7))
cursor.execute("INSERT INTO teachers (name, subject, experience) VALUES (?, ?, ?)", ("Сидоров Алексей", "Физика", 5))

conn.commit()

cursor.execute("UPDATE teachers SET experience = 8 WHERE name = 'Сидоров Алексей'")

cursor.execute("DELETE FROM teachers WHERE name = 'Петрова Анна'")

conn.commit()
conn.close()
