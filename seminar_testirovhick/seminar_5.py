# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13

#Задание необходимо решать через рекурсию

# def find_nth_fib(n):
#     if n in [1, 2]:
#         return 1


'''''//////////////////////////////'''

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

# def input_number(msg: str):
#     while True:
#         num = input(msg)
#         if num.isdigit():
#             num = int(num)
#             return num

# amount = input_number("Enter amount of grades you want to input: ")
# grades = [] # list()

# for _ in range(amount):
#     user_input = input_number("Enter a grade: ")
#     grades.append(user_input)

# def max_to_min(arr: list):
#     max_num = max(arr)
#     min_num = min(arr)
#     for i in range(len(arr)):
#         if arr[i] == max_num:
#             arr[i] = min_num
        
# max_to_min(grades)

''''///////'''

# def prime(n):
#     for div in range(2, int(n**0.5)+1):
#         if n%div == 0:
#             return "Not Prime"
#     return "Prime"

# num = int(input("Введите число: "))

# print(prime(num))

# def prime(n):  # решение от преподавателя
#     i = 2
#     flag = True
#     while i < n and flag:
#         if n % i == 0:
#             flag = False
#         i += 1
#     if flag:
#         return 'yes'
#     return 'no'

# n = int(input('Введите число: '))
# print(prime(n))


'''//////////////'''

# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input:    2 -> 3 4
# Output: 4 3

'''1'''
def print_reversed(amount: int):  # Евгений скинул
    if amount == 0:
        return ""
    num = input("Enter a number: ")
    return f"{num} {print_reversed(amount - 1)}".rstrip()[::-1]

'''2'''
def print_reversed(amount: int):  # Евгений скинул - 2
    if amount == 0:
        return ""
    num = input("Enter a number: ")
    return f"{print_reversed(amount - 1)} {num}".lstrip()

'''3'''
def posled(n):  # Решение на семинаре
    if n == 0:
        return ""
    k = input("Введите число: ") 
    return posled(n-1) + ' ' + k

num = int(input ("Введите кол-во чисел: "))
print(posled(num))


def main():
    print("Начало модуля 1")
    figure = rect(10,20) - circle(5) + tri(2,5)
    print(figure)
    print("Конец модуля 1")
    
if __name__ == "__main__":