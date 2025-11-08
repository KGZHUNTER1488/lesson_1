# #1
# print("🔹 Задание 1: Запись в info.txt")
# with open("info.txt", "w", encoding="utf-8") as f:
#     f.write("Алексей\n")
#     f.write("25 лет\n")
#     f.write("Чтение книг\n")

# #2
# print("\n🔹 Задание 2: Содержимое info.txt")
# with open("info.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# #3
# print("🔹 Задание 3: Построчный вывод с номерами")
# with open("info.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines, start=1):
#         print(f"{i}: {line.strip()}")

# #4
# print("🔹 Задание 4: Добавление строки в info.txt")
# with open("info.txt", "a", encoding="utf-8") as f:
#     f.write("Любимая еда: паста\n")

# #5
# print("🔹 Задание 5: Подсчёт строк в info.txt")
# with open("info.txt", "r", encoding="utf-8") as f:
#     line_count = len(f.readlines())
#     print(f"Количество строк: {line_count}")

# #6
# print("🔹 Задание 6: Копирование info.txt в info_copy.txt")
# with open("info.txt", "r", encoding="utf-8") as src:
#     with open("info_copy.txt", "w", encoding="utf-8") as dst:
#         for line in src:
#             dst.write(line)

# #7
# print("🔹 Задание 7: Фильтрация строк из data.txt (только с 'a')")
# with open("data.txt", "w", encoding="utf-8") as f:
#     f.write("apple\nbanana\norange\nkiwi\ngrape\n")

# with open("data.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         if 'a' in line:
#             print(line.strip())

# 8
# print("🔹 Задание 8: Ввод дел и запись в todo.txt")
# with open("todo.txt", "w", encoding="utf-8") as f:
#     for i in range(3):
#         task = input(f"Введите дело {i+1}: ")
#         f.write(task + "\n")

# # Задание 9. Пропуск пустых строк
# print("🔹 Задание 9: Вывод непустых строк из notes.txt")
# with open("notes.txt", "w", encoding="utf-8") as f:
#     f.write("Привет\n\nЭто тест\n\n\nPython лучший\n")

# with open("notes.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         if line.strip():
#             print(line.strip())

# #10
# print("🔹 Задание 10: Журнал посещений log.txt")
# custom_time = input("Введите текущую дату и время (например: 2025-10-13 14:25:00): ")

# with open("log.txt", "a", encoding="utf-8") as f:
#     f.write(f"Пользователь зашёл: {custom_time}\n")

# print("Все входы из log.txt:")
# with open("log.txt", "r", encoding="utf-8") as f:
#     print(f.read())
