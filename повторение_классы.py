class Person:
    def __init__(self, name, age):
        self.name = name

        if age == int(age) and 0 <= age <= 150:
            self.age = 0
        else:
            print('Возраст должен быть менше 150 и больше нуля')

    def greet(self):
        return f"Привет, меня зовут {self.name}, мне {self.age} лет."

e = Person("Алексей", 40, "менеджер")
print(e.greet())   
print(e.work())   