# Task_10
# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

'''Colorada'''
# n = int(input('Введите общее количество монеток на столе: '))
# print('Введите 0, если монета лежит вверх решкой. \nВведите 1, если монета лежит вверх гербом')
# countTails = 0
# countArms = 0

# for i in range(n):
#     coin = int(input('Какой стороной лежит монета?\n'))
#     if coin == 0:
#         countTails += 1
#     elif coin == 1:
#         countArms += 1
#     # else:
#     #     break
#     #     print('Введены неверные данные! Введите 0 или 1!')
# print(f'Необходимо перевернуть {min(countTails, countArms)} монет')


# entered_list = input("Введите список чисел, разделенных пробелом: ").split()
# print("Введенный список:", entered_list)

# num_list = list(map(int, entered_list))
# print("Список чисел: ", num_list)
# print("Сумма списка:", sum(num_list))


# eagle = 0
# tails = 0

# coins = [0, 1]
# for i in range(coins):
#     if int(coins) == 0:
#         eagle += 1
#     if (coins) == 1:
#         tails += 1
# #print (f'всего монет {eagle, tails}')

# if coins > tails:
#     res = tails
# if tails > coins:
#     res = coins

#     print(res)

# import random

# from random import randint

# amount_coin = int(input('введите количество монет: '))

# m = 0
# k = 0
# coins = [0, 1]
# for i in range(amount_coin):
#     random.shuffle(coins)
#     print(f'все монеты{coins}')
#     if int(coins[0]) == 0:
#         k += 1
#     if int(coins[0]) == 1:
#         m += 1
# print(f'всего монет {m, k}')

# if m > k:
#     ans = k
# else:
#     ans = m

# print(f"минимальное количество монет, которые нужно перевернуть: {ans}")



# n = int(input('Введите число монеток: '))
# from random import randint
# a, b = 0, 0
# for i in range(n):
#     temp = randint(0, 1)
#     print(temp, end=' ')
#     if temp > 0: a += 1
#     else: b += 1
# print()
# if a > b:
#     print(f'Нужно перевернуть {b} монеток')
# else:
#     print(f'Нужно перевернуть {a} монеток')

# Task_12
# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

# summ = 5
# prod = 6
# i = 1
# temp = 0
# while i < prod:
#     temp = summ - i
#     if temp + i == summ and temp * i == prod:
#         break
#     i += 1
# print(i, temp)



# Task_14
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

# n = 10
# i = 1
# while i < n:
#     print(i)
#     i = i * 2


# def min_flips(coins):
#     num_flips = 0

# head_count = coins.count('H')
# tail_count = coins.count('T')
# # Если все монетки повернуты одной стороной, возвращаем 0
# # if head_count == 0 or tail_count == 0:
# # print(0)

# # Если повернутых монеток гербом больше, переворачиваем их вверх
# if head_count > tail_count:
#     for coin in coins:
#         if coin == 'T':
#             num_flips += 1
# # Если повернутых монеток решкой больше, переворачиваем их вверх              
# else:
#     for coin in coins:
#         if coin == 'H':
#             num_flips += 1

# # return num_flips
# coins = ['H', 'T', 'H', 'H', 'T', 'T']
# min_flips_needed = min_flips(coins)
# print("Минимальное количество монет, которые нужно перевернуть:", min_flips_needed