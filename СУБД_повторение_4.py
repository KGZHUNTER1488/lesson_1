import sqlite3

conn = sqlite3.connect('bank_2.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT,
    amount INTEGER,
    type TEXT
)
""")

conn.commit()

cursor.execute("INSERT INTO clients (name, balance) VALUES ('Али', 10000)")
cursor.execute("INSERT INTO clients (name, balance) VALUES ('Малика', 5000)")
cursor.execute("INSERT INTO clients (name, balance) VALUES ('Тимур', 7000)")

conn.commit()

cursor.execute("SELECT * FROM clients")
for client in cursor.fetchall():
    print(client)

cursor.execute("UPDATE clients SET balance = balance + 2000 WHERE name='Али'")

cursor.execute("INSERT INTO transactions (client_name, amount, type) VALUES ('Малика', 2000, 'withdraw')")
cursor.execute("INSERT INTO transactions (client_name, amount, type) VALUES ('Али', 2000, 'deposit')")

conn.commit()

cursor.execute("SELECT * FROM transactions")
for transaction in cursor.fetchall():
    print(transaction)

cursor.execute("DELETE FROM clients WHERE balance < 6000")
conn.commit()

cursor.execute("SELECT * FROM clients")
for client in cursor.fetchall():
    print(client)

conn.close()