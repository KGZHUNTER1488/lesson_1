import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    balance INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    product_name TEXT,
    amount INTEGER
)
""")

cursor.execute("INSERT INTO customers (name, balance) VALUES ('Айдан', 10000)")
cursor.execute("INSERT INTO customers (name, balance) VALUES ('Руслан', 8000)")
cursor.execute("INSERT INTO customers (name, balance) VALUES ('Диана', 12000)")

cursor.execute("INSERT INTO products (name, price) VALUES ('Ноутбук', 7000)")
cursor.execute("INSERT INTO products (name, price) VALUES ('Наушники', 3000)")
cursor.execute("INSERT INTO products (name, price) VALUES ('Мышь', 1500)")

conn.commit()

cursor.execute("SELECT * FROM customers")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT balance FROM customers WHERE name='Диана'")
balance_diana = cursor.fetchone()[0]
cursor.execute("SELECT price FROM products WHERE name='Ноутбук'")
price_notebook = cursor.fetchone()[0]
if balance_diana >= price_notebook:
    new_balance = balance_diana - price_notebook
    cursor.execute("UPDATE customers SET balance=? WHERE name='Диана'", (new_balance,))
    cursor.execute("INSERT INTO purchases (customer_name, product_name, amount) VALUES ('Диана', 'Ноутбук', ?)", (price_notebook,))

cursor.execute("SELECT balance FROM customers WHERE name='Руслан'")
balance_ruslan = cursor.fetchone()[0]
cursor.execute("SELECT price FROM products WHERE name='Наушники'")
price_headphones = cursor.fetchone()[0]
if balance_ruslan >= price_headphones:
    new_balance = balance_ruslan - price_headphones
    cursor.execute("UPDATE customers SET balance=? WHERE name='Руслан'", (new_balance,))
    cursor.execute("INSERT INTO purchases (customer_name, product_name, amount) VALUES ('Руслан', 'Наушники', ?)", (price_headphones,))

conn.commit()

cursor.execute("SELECT * FROM purchases")
for row in cursor.fetchall():
    print(row)

cursor.execute("DELETE FROM customers WHERE balance < 5000")
conn.commit()

cursor.execute("SELECT * FROM customers")
for row in cursor.fetchall():
    print(row)

conn.close()