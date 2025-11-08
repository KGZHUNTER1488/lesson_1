import sqlite3

class User:
    def __init__(self, user_id, name, email):
        self._id = user_id
        self.name = name
        self.email = email


class BankAccount:
    def __init__(self, acc_id, user_id, number, balance, acc_type):
        self._id = acc_id
        self.user_id = user_id
        self._balance = balance
        self.number = number
        self.acc_type = acc_type

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    pass


class CreditAccount(BankAccount):
    def withdraw(self, amount):
        if self._balance - amount >= -10000:
            self._balance -= amount
            return True
        return False

class BankSystem:
    def __init__(self):
        self.conn = sqlite3.connect("bank.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                account_number TEXT,
                balance REAL,
                account_type TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        self.conn.commit()

    def create_user(self, name, email):
        self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()

    def create_account(self, user_id, acc_type):
        number = f"ACC{user_id}{len(self.get_accounts()) + 1}"
        self.cursor.execute(
            "INSERT INTO accounts (user_id, account_number, balance, account_type) VALUES (?, ?, ?, ?)",
            (user_id, number, 0.0, acc_type)
        )
        self.conn.commit()

    def get_accounts(self):
        self.cursor.execute("SELECT * FROM accounts")
        return self.cursor.fetchall()

    def get_account_by_id(self, acc_id):
        self.cursor.execute("SELECT * FROM accounts WHERE id=?", (acc_id,))
        return self.cursor.fetchone()

    def update_balance(self, acc_id, balance):
        self.cursor.execute("UPDATE accounts SET balance=? WHERE id=?", (balance, acc_id))
        self.conn.commit()

    def create_obj(self, acc):
        acc_id, user_id, number, balance, acc_type = acc
        if acc_type == "savings":
            return SavingsAccount(acc_id, user_id, number, balance, acc_type)
        else:
            return CreditAccount(acc_id, user_id, number, balance, acc_type)

    def deposit(self, acc_id, amount):
        acc = self.get_account_by_id(acc_id)
        if acc:
            obj = self.create_obj(acc)
            obj.deposit(amount)
            self.update_balance(acc_id, obj.get_balance())

    def withdraw(self, acc_id, amount):
        acc = self.get_account_by_id(acc_id)
        if acc:
            obj = self.create_obj(acc)
            if obj.withdraw(amount):
                self.update_balance(acc_id, obj.get_balance())
                return True
        return False

def main():
    bank = BankSystem()

    while True:
        print('1. Создать пользователя')
        print('2. Открыть счёт')
        print('3. Пополнить счёт')
        print('4. Снять деньги')
        print('5. Показать все счета')
        print('6. Выход')
        c = input("Выбор: ")

        if c == "1":
            name = input("Имя: ")
            email = input("Email: ")
            bank.create_user(name, email)
            print("✅ Пользователь создан.")

        elif c == "2":
            user_id = int(input("ID пользователя: "))
            t = input("Тип счёта (savings/credit): ")
            if t not in ("savings", "credit"):
                print("Неверный тип.")
                continue
            bank.create_account(user_id, t)
            print("Счёт открыт.")

        elif c == "3":
            acc_id = int(input("ID счёта: "))
            amount = float(input("Сумма пополнения: "))
            bank.deposit(acc_id, amount)
            print("Счёт пополнен.")

        elif c == "4":
            acc_id = int(input("ID счёта: "))
            amount = float(input("Сумма снятия: "))
            if bank.withdraw(acc_id, amount):
                print("Деньги сняты.")
            else:
                print("Недостаточно средств или превышен лимит.")

        elif c == "5":
            accounts = bank.get_accounts()
            if not accounts:
                print("Нет счетов.")
            else:
                print("\nВсе счета:")
                for a in accounts:
                    print(f"ID={a[0]} | user_id={a[1]} | №{a[2]} | баланс={a[3]:.2f} | тип={a[4]}")

        elif c == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")

main()