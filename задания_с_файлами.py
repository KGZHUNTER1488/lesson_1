# #1
# with open("data.txt", "r", encoding="utf-8") as f:
#     first_line = f.readline()
#     print(first_line.strip())

# #2
# with open("text.txt", "r", encoding="utf-8") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     line3 = f.readline()

# print(line1.strip())
# print(line2.strip())
# print(line3.strip())

# #3
# with open("story.txt", "r", encoding="utf-8") as f:
#     raskaz = f.read()
#     print(raskaz)

# #4
# with open("notes.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     count = len(lines)
#     print(count)

# #5
# with open("words.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

# #6
# with open("data.txt", "r", encoding="utf-8") as f:
#     for i, line in enumerate(f, start=1):
#         print(f"{i}: {line.strip()}")

# #7
# with open("words.txt", "r", encoding="utf-8") as f:
#     words = f.read().split()
#     longest = max(words, key=len)
#     print("Самое длинное слово:", longest)

# #8
# with open("text.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#     print("Количество символов:", len(text))

# #9
# with open("messages.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         if "привет" in line.lower():
#             print(line.strip())

# #10
# with open("original.txt", "r", encoding="utf-8") as f:
#     content = f.read()

# with open("copy.txt", "w", encoding="utf-8") as f:
#     f.write(content)

# #11
# with open("article.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#     words = text.split()
#     print("Количество слов:", len(words))

# #12
# long_count = 0

# with open("notes.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         stripped = line.strip()
        
#         if len(stripped) > 20:
#             long_count += 1
        
#         if stripped and stripped[0].lower() == "а":
#             print(stripped)

# print(long_count)

# #13
# with open("names.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         if len(line) > 0 and (line[0] == "А" or line[0] == "а"):
#             print(line, end="")

# #14
# count_errors = 0
# with open("log.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         if "ошибка" in line.lower():
#             count_errors += 1
# print("Количество строк с 'ошибка':", count_errors)

# #15
# vowels = "аеёиоуыэюя"
# count_vowels = 0

# with open("text.txt", "r", encoding="utf-8") as f:
#     text = f.read().lower()
#     for char in text:
#         if char in vowels:
#             count_vowels += 1

# print("Количество гласных:", count_vowels)

##16
# with open("data.txt", "w", encoding="utf-8") as f:
#     f.write("Python\n")
#     f.write("Java\n")
#     f.write("С#\n")

# with open("data.txt", "r", encoding="utf-8") as f1:
#     with open("filtered.txt", "w", encoding="utf-8") as f2:
#         for line in f1:
#             if "Python" in line:
#                 print(line.strip())
#                 f2.write(line)


# #17
# with open("lines.txt", "w", encoding="utf-8") as f:
#     f.write("одна\n")
#     f.write("очень длинная строка здесь\n")
#     f.write("коротко\n")

# with open("lines.txt", "r", encoding="utf-8") as f:
#     lines = [line.strip() for line in f if line.strip()]
#     shortest = min(lines, key=len)
#     print("17: Самая короткая строка:", shortest)


# #18
# with open("story.txt", "r", encoding="utf-8") as f:
#     words = f.read().lower().replace(".", "").replace(",", "").split()
#     unique = set(words)
#     print("18: Уникальных слов:", len(unique))

# #19
# with open("messy.txt", "w", encoding="utf-8") as f:
#     f.write("\nПривет\n\nЭто пример\n\n\nБез пустых строк\n")

# with open("messy.txt", "r", encoding="utf-8") as src, open("clean.txt", "w", encoding="utf-8") as dst:
#     for line in src:
#         if line.strip():
#             dst.write(line)


# #20
# with open("text.txt", "w", encoding="utf-8") as f:
#     f.write("В тексте есть ошибка. Еще одна ошибка найдена.")
# with open("text.txt", "r", encoding="utf-8") as f:
#     text = f.read().replace("ошибка", "исправлено")
# with open("new_text.txt", "w", encoding="utf-8") as f:
#     f.write(text)