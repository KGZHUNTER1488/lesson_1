import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS students(
                    id INTEGER PRINARY REY,
                    name TEXT IF NOT NULL,
                    age INTEGER,
                    email TEXT
               )
               """)

conn.commit()

cursor.execute("INSERT INTO students (name, age, email) VALUES (?,?,?)", ("Азамат", 14, "a@ex.com"))
cursor.execute("UPDATE students SET age = 17 WHERE name = 'Азамат'")
cursor.execute("DELETE FROM students WHERE name = 'Азамат'")

conn.commit()

conn.close()