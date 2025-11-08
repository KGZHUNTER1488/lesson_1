'''8. Контекстный менеджер "with", работа с файлами;

Файл - это место где хранятся данные (текст, числа, код, и т.д).
в Python мы можем **читать** и **записывать**
файды с помошью встроенных функций.
'''

# file = open('text.txt', 'r', encoding='utf-8')
# text = file.read()
# file.close()
# print(file)

# with open('text.txt', 'r', encoding='utf-8') as file:
#     text = file.read
#     print(text)

# with open('text.txt', 'r', encoding='UTF=8') as file:
#     line1 = file.readline()
#     line2 = file.readline()
#     line3 = file.readline()

#     print(line1)
#     print(line2)
#     print(line3)

# try:
#     with open('text.txt', 'r', encoding='UTF=8') as file:
#         lines = file.readlines()
#         print(lines)

#         if not lines:
#             print('Файл пуст. Добавь в него текст!')
#         else:
#             for i, line in enumerate(lines, start=1):
#                 print(f'Строка {i}:', line.strip())
# except FileExistsError:
#     print('Файл "text.txt" не найден! Убедись, что он в той же папке, что и программа')

# with open('text.txt', 'w', encoding='utf-8') as file:
#     file.write('Привет мир!\n')
#     file.write('Python - класный язык.')

# with open('text.txt', 'w', encoding='utf-8') as file:
#     file.write('\nДобавлена новая строка')

# pen('text.txt', 'r', encoding='utf-8') as file:
#     file.write('\nДобавлена новая строка')

# Запись в файл (режим "w" — запись, файл перезаписывается)
# with open("text.txt", "w", encoding="utf-8") as file:
#     file.write("Привет, мир!\n")
#     file.write("Python — классный язык.")

# Добавление строки в конец файла (режим "a" — добавление)
# with open("text.txt", "a", encoding="utf-8") as file:
#     file.write("\nДобавлена новая строка.")

# Чтение и добавление (режим "r+")
# with open("text.txt", "r+", encoding="utf-8") as file:
#     text = file.read()
#     file.write("\nНовая запись в конец.")

# Построчное чтение файла
# with open("text.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())

# Запись списка строк
# lines = ["Первая строка\n", "Вторая строка\n", "Третья строка\n"]
# with open("text.txt", "w", encoding="utf-8") as file:
#     file.writelines(lines)

# Подсчёт количества строк в файле
# with open("text.txt", "r", encoding="utf-8") as file:
#     count = 0
#     for line in file:
#         count += 1
#     print("Количество строк:", count)

# Копирование содержимого одного файла в другой
# with open("text.txt", "r", encoding="utf-8") as source:
#     with open("copy.txt", "w", encoding="utf-8") as target:
#         for line in source:
#             target.write(line)

