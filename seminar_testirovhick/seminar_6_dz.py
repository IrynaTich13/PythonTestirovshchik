# Task_30: 
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


# a = int(input('Введите первый элемент арифметической прогрессии: '))
# d = int(input('ВВедите разность между ее членами: '))
# n = int(input('Введите количество членов прогрессии: '))

# def rec(n):
#     if n ==0:
#         return 0
#     return a + d*(n-1)

# my_list = []              
# for i in range(1,n+1):
#     my_list.append(rec(i))
# print(*my_list)



# Task_32:
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


# import random

# n = int(input('Задайте количество элементов массива: '))
# my_list = []
# for i in range(n):
#     my_list.append(random.randint(-10, 10))
# print(my_list)

# min_num = int(input('Задайте минимальный элемент диапазона: '))
# max_num = int(input('Задайте максимальный элемент диапазона: '))

# for i in range(len(my_list)):
#     if min_num <= my_list[i] <= max_num:
#         print(i, end=' ')