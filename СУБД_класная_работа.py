import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        year INTEGER
    )
""")

conn.commit()

cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", ("Мастер и Маргарита", "Булгаков", 1967))
cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", ("Война и мир", "Толстой", 1869))
cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", ("Преступление и наказание", "Достоевский", 1866))

conn.commit()

cursor.execute("UPDATE books SET year = 1968 WHERE title = 'Мастер и Маргарита'")

cursor.execute("DELETE FROM books WHERE title = 'Война и мир'")

conn.commit()
conn.close()
