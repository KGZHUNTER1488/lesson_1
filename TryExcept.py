'''Try/Except(Исключения)'''

'''try и except - это конструкции для
обработки ошибок в Python.
Иногда в коде могут возникать ошибки,,
которые мешают программе работать. Например,
если ты делишь число на ноль или пытаешься
открыть файл, которого нет, программа сразу выйдет
с ошибкой. Чтобы избежать этого и не ломать прорамму, используется блок try и except.

try - это блок, где ты пишешь кодб который может
вызвать ошибку.

except - это блок, который срабатывает,
если в блоке try возникла ошибка.
Вместо того чтобы программа ломалась,
мы можем обработать ошибку.'''

# try:
#     a = 10
#     b = 0
#     result = a / b
#     print(result)
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
# print('Привет')



# try:
#     num = int(input('Введите число: '))
#     print('Вы ввели не число:', num)
# except ValueError:
#     print('Ошибка! Вы ввели не число.')



# try:
#     a = int(input('Введите первое число: '))
#     b = int(input('Введите второе число: '))
#     result = a / b
#     print('Результат деления:', result)
# except ZeroDivisionError:
#     print('Нельзя делить на ноль!')
# except ValueError:
#     print('Ошибка! Вы ввели не число.')



# try:
#     a = int(input('Введите чисдо: '))
#     result = a * 2
# except ValueError:
#     print('Ошибка! Вы ввели не число.')
# else:
#     print('Результат умножения на 2:', result)
# finally:
#     print('Конец программы.')
'''
Если ошибка не произошла,
сработает блок else и выведет результат.

Блок finally всегда выполнится,
независимо от того, была ли ошибка или нет.'''


#1
try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    result = a / b
    print('Результат деления:', result)
except ZeroDivisionError:
    print('Нельзя делить на ноль!')
except ValueError:
    print('Ошибка! Вы ввели не число.')



#2
while True:
    user_input = input("Введите целое число: ")
    try:
        number = int(user_input)
        break 
    except ValueError:
        print("Ошибка: введите целое число.")


#4
class Calculator:
    def divide(self, a, b):
        try:
            result = a / b
            print(f"Результат деления: {result}")
            return result
        except ZeroDivisionError:
            print("Деление на ноль невозможно.")
            return None

calc = Calculator()

calc.divide(5, 0)  



#5
while True:
    user_input = input("Введите несколько чисел через пробел: ")
    try:
        numbers = list(map(float, user_input.split()))
        print("Вы ввели числа:", numbers)
        break 
    except ValueError:
        print("Введите только числа")



#6
while True:
    user_input = input("Введите строку: ")
    
    if ' ' in user_input:
        parts = user_input.split()
        print("Разделенные части строки:", parts)
    else:
        print("Ошибка: строка не содержит пробела")
