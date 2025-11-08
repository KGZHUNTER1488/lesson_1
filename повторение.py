# #1
# name = "Даниел"       
# age = 14                 
# height = 1.66                    
# is_student = True             

# print("Имя:", name, "Тип:", type(name))
# print("Возраст:", age, "Тип:", type(age))
# print("Рост:", height, "Тип:", type(height))
# print("Учусь в школе:", is_student, "Тип:", type(is_student))

# #2
# text = "  Hello, World!  "
# text = text.strip()
# text = text.lower()
# text = text.replace(",", "-")

# print(text, len(text))

# #3
# num = int(input('Введите число: '))

# if num == 0:
#     print('Это ноль')
# elif num % 2 == 0:
#     print('Чётное')
# else:
#     print('Нечётное')

# #4
# for i in range(1, 11):
#     print(i**2)
    
# sum = 0
# i = 1

# while i <= 100:
#     sum += i
#     i += 1

# print(sum)

# #5
# # Исходный список
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# print(fruits[0])
# print(fruits[-1])

# fruits[1] = "orange"
# fruits.append("grape")
# fruits.remove("kiwi")
# fruits.sort()

# print(fruits)

# #6
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(numbers[:5])
# print(numbers[-3:])
# print(numbers[0::2])
# print(numbers[::-1])

# #7
# my_tuple = (10, 20, 30)
# print("Исходный кортеж:", my_tuple)

# #my_tuple[1] = 99  

# my_list = list(my_tuple)
# my_list[1] = 99
# my_new_tuple = tuple(my_list)

# print("Изменённый кортеж:", my_new_tuple)

#8
# book = {
#     "title": "1984",
#     "author": "George Orwell",
#     "year": 1949
# }

# print("Название:", book["title"])
# print("Автор:", book["author"])

# book["pages"] = 328

# del book["year"]

# if "author" in book:
#     print("Ключ 'author' есть в словаре")
# else:
#     print("Ключ 'author' отсутствует в словаре")

# print(book)

# #9
# def greet(name):
#     print(f"Привет, {name}!")

# greet("Аня")
# greet("Максим")
# greet("Елена")

# #10
# def numbers(numbers):
#     original = numbers
#     filter = []
#     for num in numbers:
#         if num % 2 == 0:
#             filter.append(num)
    
#     if filter:
#         a = sum(filter) / len(filter)
#     else:
#         a = None
    
#     return {
#         "original": original,
#         "filtered": filter,
#         "average": a
#     }

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# result = numbers(nums)
# print(result)
