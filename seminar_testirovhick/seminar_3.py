# Task_19
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# my_list = [1, 2, 3, 4, 5, 6]

# k = int(input('Input a index correction: ')) % len(my_list)

# for i in range(k):
#     my_list.insert(0, my_list.pop())

# print(my_list)

'''/////////////////////////////'''

# Task_17
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

'''//////////'''
# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# count = set(list_1)

# print(len(count))

'''/////////'''
# numbers = [1, 1, 2, 0, -1, 3, 4, 4] # type = list
# numbers = list()
# amount = int(input("Enter amount of values you want to input: "))
# for _ in range(amount):
#     numbers.append(int(input("Enter a value: ")))
# print(len(set(numbers)))


'''//////////'''
# numbers = [1, 1, 2, 0]
# numbers = list()
# amount = int(input("Enter am....: "))
# for _ in range(amount):

'''//////'''

# input = [1, 1, 2, 0, -1, 3, 4, 4]
# print('Уникальных:', len(set(input)))



# Task_21
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит


# lst_obj = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#            {"VII": "S005"}, {"V": "S009"}, {" VIII": "S007"}]

# set_obj = set()
# for dict_el in lst_obj:
#     for val in dict_el.values():
#         set_obj.add(val)

# print(set_obj)

# user_input = [
#     {'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, 
#     {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, 
#     {'VIII': 'S007'}  
# ]

# my_set = set()
# for dictionary in user_input:
#     for value in dictionary.values():
#         my_set.add(value)
    
# print(my_set)    #  или print(set())


'''//////////////////'''
# Task_23
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

#numbers = [0, -1, 5, 2, 3]

amount = int(input("Enter amount of number you want to insert: "))
numbers = list()
for _ in range(amount):
    numbers.append(int(input("Enter a number: ")))
count = 0
for i in range(1, len(numbers)):
    if numbers[i - 1] < numbers[i]:
        count += 1

print(f"{numbers}, amount of numbers: {count}")

