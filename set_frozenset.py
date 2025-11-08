'''set_frozenset'''

# num = {1, 2, 3, 3, 2, 1}

# print(num)

# num1 = set({1, 2, 3, 4, 5, 7, 5, 7, 5, 6, 6, 1})

# print(num1)

# num2 = set()
# print(num2)
# print(type(num2))

# num3 = {1, 2}
# num3.add(3)
# num3.remove(2) # удаляет 2, если нет - ошибка
# num3.discard(5) # удаляет 5, если нет - НЕТ ошибки
# num3.clear()
# print(num3)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a | b) #Обьеденение (все элементы из обоих)

# print(a & b) #Пересечение (только общие)

# print(a - b) #Разность (только у первого)

# print(a ^ b) #Симетрическая разность (уникальное, без общих)


# lst = set([1, 2, 2, 3, 3, 3])

# lst = [1, 2, 2, 3, 3, 3]
# lst2 = set(lst)


# s = {1, 2, 3}
# s.update([5, 6])
# #s.pop()
# x = s.copy()
# print(x)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}


# # print(a | b) #Обьеденение (все элементы из обоих)
# print(a.union(b))

# # print(a & b) #Пересечение (только общие)
# print(a.intersection(b))

# # print(a - b) #Разность (только у первого)
# print(a.difference(b))

# # print(a ^ b) #Симетрическая разность (уникальное, без общих)
# print(a.symmetric_difference(b))

# num1 = frozenset([1, 2, 3])
# print(type(num1))
# print(num1)

# a = frozenset({1, 2, 3, 4})
# b = frozenset({3, 4, 5, 6})e

# print(a | b)



#1
a = {1, 2, 2, 3, 4, 4, 5}

print(a)

#2
a.add(10)

a.remove(2)

a.discard(100)

# a.remuve(2) # удаляет 2, если нет - ошибка
# a.discard(100) # удаляет 5, если нет - НЕТ ошибки

#3
b = {10, 20, 30}

b.clear()

#4
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}

print(x | y)

print(x & y)

print(x - y)

print(x ^ y)

#5
