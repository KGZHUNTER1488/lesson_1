import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clothes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL
)
""")

clothes_data = [
    ('Футболка Nike', 'Футболка', 2500),
    ('Куртка Adidas', 'Куртка', 7200),
    ('Джинсы Levi’s', 'Джинсы', 4800),
    ('Кроссовки Puma', 'Обувь', 5600),
    ('Худи H&M', 'Толстовка', 3300)
]

for item in clothes_data:
    cursor.execute("INSERT INTO clothes (name, category, price) VALUES (?, ?, ?)", item)

conn.commit()

while True:
    print("\n1 - Все товары")
    print("2 - Инфо о товаре")
    print("3 - Добавить товар")
    print("4 - Изменить цену товара")
    print("5 - Удалить товар")
    print("6 - Выход")

    choice = input("Ваш выбор: ")

    if choice == "1":
        cursor.execute("SELECT * FROM clothes")
        for r in cursor.fetchall():
            print(r)

    elif choice == "2":
        item_id = input("ID: ")
        cursor.execute("SELECT * FROM clothes WHERE id = ?", (item_id,))
        item = cursor.fetchone()
        if item:
            print(item)
        else:
            print("Товар не найден.")

    elif choice == "3":
        name = input("Название: ")
        category = input("Категория: ")
        price = float(input("Цена: "))
        cursor.execute("INSERT INTO clothes (name, category, price) VALUES (?, ?, ?)", (name, category, price))
        conn.commit()
        print("Добавлено!")

    elif choice == "4":
        item_id = input("ID товара для изменения цены: ")
        new_price = float(input("Новая цена: "))
        cursor.execute("UPDATE clothes SET price = ? WHERE id = ?", (new_price, item_id))
        conn.commit()
        print("Цена обновлена!")

    elif choice == "5":
        item_id = input("ID товара для удаления: ")
        cursor.execute("DELETE FROM clothes WHERE id = ?", (item_id,))
        conn.commit()
        print("Товар удалён!")

    elif choice == "6":
        print("Выход из программы...")
        break

    else:
        print("Неправильный ввод. Попробуйте снова.")

conn.close()