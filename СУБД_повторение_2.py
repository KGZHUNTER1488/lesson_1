import sqlite3

conn = sqlite3.connect('bank.db')
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

cursor.execute("INSERT INTO clients (name, balance) VALUES ('Али', 10000)")
cursor.execute("INSERT INTO clients (name, balance) VALUES ('Малика', 5000)")
cursor.execute("INSERT INTO clients (name, balance) VALUES ('Тимур', 7000)")

conn.commit()

print('Клиенты до перевода:')
cursor.execute('SELECT * FROM clients')
clients = cursor.fetchall()
for client in clients:
    print(client)

cursor.execute("UPDATE clients SET balance = balance - 2000 WHERE name='Малика'")
cursor.execute("UPDATE clients SET balance = balance + 2000 WHERE name='Али'")

conn.commit()


print('Транзакции:')
cursor.execute('SELECT * FROM transactions')
transactions = cursor.fetchall()
for transaction in transactions:
    print(transaction)

cursor.execute('DELETE FROM clients WHERE balance < 6000')

conn.commit()

print('\nКлиенты после')
cursor.execute('SELECT * FROM clients')
clients = cursor.fetchall()
for client in clients:
    print(client)

conn.close()