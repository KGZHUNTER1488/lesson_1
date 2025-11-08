#1
#a

#2
#b

#3
#b

#4
#b

#5
#b

#6
#b

#7
#b

#8
#a

#9
#b

#10
#b

#11
#b

#12
#b

#13
#b

#14
#a

#15
#b

#16
#b

#17
#c

#18
#c

#19
#a

#20
#a

#21
#a

#22
#a

#23
#a

#24
#d

#25
#a

#26
#a

#27
#b

#28
#b

#29
#a

#30
#a

#31
def get_list(lst):
    total = sum(lst)
    print(total)

get_list([1, 2, 3, 4, 5])

#32
def get_stroka(stroka):
    return stroka[::-1]

print(get_stroka('hello')) 

#33
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
while i < len(a):
    if a[i] % 2 == 0:
        a.pop(i)
    else:
        i += 1

print(a)


#34
students = {
    'Алиса': 85,
    'Боб': 78,
    'Катя': 91,
    'Дима': 67,
    'Ева': 95
}

for name in students.keys():
    score = students[name]
    if score > 80:
        print(name, score)

#35
a = -37
if a / a and a / 1 and a > 0:
    print('Yes')
else:
    print('No')

#36
def max(*args):
    print(max(args))

max(1, 2, 3, 4, 5, 6, 7, 8, 9)

#37
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"Марка: {self.brand}, Год выпуска: {self.year}")

car1 = Car("Toyota", 2020)
car1.display_info()