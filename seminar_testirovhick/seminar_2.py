# Task_9
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

# n = int(input('Введите число: '))
# count = 1
# fact = 1
# while count <= n:
#     fact = fact * count
#     count += 1
# print(fact)
'''///////////'''
# while True:
#     fact_request = input("Enter a number for factorial: ")
#     if fact_request.isdigit():
#         fact_request = int(fact_request)
#         break
    
#     else:
#         print("Please, enter a number")

# fact = 1
# count = 1
# while count <= fact_request:
#     fact *= count
#     count += 1

# print(fact)

'''//////////////////////////'''

# Task_11
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

# a = int(input('Введите натуральное число больше единицы: '))

# fib_1 = 0
# fib_2 = 1
# index = 2

# while a > fib_2:
#     temp = fib_2
#     fib_2 += fib_1
#     fib_1 = temp
#     index += 1
# if a == fib_2:
#         print(index)
# else: print(-1)

# if a == 0:
#       print(1)

    # elif a == 0:
    #     print(1)

'''//////////'''

# def find_fibonacci_index(n: int) -> int:
#     if n == 0:
#         return 1
#     if n == 1:
#         return 2
    
#     fib_1 = 0
#     fib_2 = 1
#     index = 2
#     while n > fib_2:
#         temp = fib_2
#         fib_2 += fib_1
#         fib_1 = temp
#         index += 1
        
#     if n == fib_2:
#         return index
    
#     return -1

# print(find_fibonacci_index(9))


'''//////////////////////////'''

# Task_13
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 ->


# days = int(input("Введите температуру: "))
# count = 0
# current_count = 0

# for i in range(days) :
#     temperatue = int(input('Inpt a temp of this day: '))

#     if temperatue > 0 :
#         current_count += 1
#     elif current_count > count :
#         count = current_count
#         current_count = 0
#     else :
#         current_count = 0

# if current_count > count :
#     count = current_count

# print('result is ', count)


'''////////////////////////////////////'''

amount = int(input("Enter amount of watermelons: "))
weight = int(input("Enter weight of a watermelon: "))
min_weight = weight
max_weight = weight
for _ in range(1, amount):
    weight = int(input("Enter weight of a watermelon: "))
    
    if weight > max_weight:
                max_weight = weight
            
    if weight < min_weight:
        min_weight = weight
        
print(f"min = {min_weight}, max = {max_weight}")



''''///////////////////////////////'''

# days = int(input('Input a quantity of days: '))
# count = 0
# current_count = 0

# for i in range(days) :
#     temperature = int(input('Input a temp of this day: '))

#     if temperature > 0 :
#         current_count += 1
#     else :
#         if current_count > count :
#             count = current_count
#         current_count = 0

# if current_count > count :
#     count = current_count

# print('result is', count)



