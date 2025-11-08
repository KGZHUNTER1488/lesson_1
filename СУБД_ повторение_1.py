import sqlite3

conn = sqlite3.connect('library_v2.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("""
    CREATE TABLE books(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        year INTEGER,
        available BOOLEAN
    )
""")

cursor.execute("INSERT INTO books (title, author, year, available) VALUES (?, ?, ?, ?)", ("Как играть в роблокс", "Ринат", 2025, 1))
cursor.execute("INSERT INTO books (title, author, year, available) VALUES (?, ?, ?, ?)", ("Как играть на ноутбуке с нулем зарядки", "Давид", 2023, 0))
cursor.execute("INSERT INTO books (title, author, year, available) VALUES (?, ?, ?, ?)", ("Капитанская дочка", "Пушкин", 1993, 1))
cursor.execute("UPDATE books SET year = 2024 WHERE title = 'Как играть в роблокс'")
cursor.execute("DELETE FROM books WHERE title = 'Как играть в роблокс'")

for row in cursor.execute("SELECT * FROM books"):
    print(row)

cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("""
    CREATE TABLE students(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        grade INTEGER
    )
""")

students = [
    ("Азамат", 14, 5),
    ("Мадина", 12, 4),
    ("Рустам", 13, 3),
    ("Айгуль", 15, 5),
    ("Тимур", 11, 2)
]
cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students)
cursor.execute("UPDATE students SET age = age + 1")
cursor.execute("DELETE FROM students WHERE age < 13")

for student in cursor.execute("SELECT * FROM students WHERE grade > 4"):
    print(student)

cursor.execute("DROP TABLE IF EXISTS movies")
cursor.execute("""
    CREATE TABLE movies(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        genre TEXT,
        year INTEGER,
        rating REAL
    )
""")

cursor.execute("INSERT INTO movies (title, genre, year, rating) VALUES (?, ?, ?, ?)", ("Интерстеллар", "Фантастика", 2014, 9.0))
cursor.execute("INSERT INTO movies (title, genre, year, rating) VALUES (?, ?, ?, ?)", ("Дюна", "Фантастика", 2021, 8.3))
cursor.execute("INSERT INTO movies (title, genre, year, rating) VALUES (?, ?, ?, ?)", ("Оппенгеймер", "Драма", 2023, 9.1))
cursor.execute("UPDATE movies SET rating = 9.2 WHERE title = 'Оппенгеймер'")

for movie in cursor.execute("SELECT * FROM movies WHERE rating > 8.5"):
    print(movie)

conn.commit()
conn.close()
