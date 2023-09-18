

# Task_25  Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

my_string = 'a a a b c a a d c d d'

my_list = my_string.split()

my_dict = {}

for i in my_list:
    if i not in my_dict:
        my_dict[i] = 0
        print(i+' ',end='')
    else:
        print(i,end='')
        my_dict[i] += 1  
        print('_' + str(my_dict[i]) +' ',end='')


# user_input = "a a a b c a a d c d d"
# list_input = user_input.split()
# values = list()

# for i in range(len(list_input)):
#     if list_input[i] not in values:
#         values.append(list_input[i])
#     else:
#         values.append(list_input[i])
#         list_input[i] += f"_{values.count(list_input[i]) - 1}"      

# print(" ".join(list_input))



'''/////////////////////////////'''

# Task_27
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


# n = int(input("Enter a number: "))
# max_number = n
# while n > 0:
#     n = int(input("Enter a number: "))
#     if max_number < n:
#         max_number = n
# print(max_number)

'''/////////////'''

#Task_27  Пользователь вводит текст(строка). 
#Словом считается последовательность непробельных символов идущих подряд, слова разделены одним пробелом. 
#Определите, сколько различных слов содержится в этом тексте.

#Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

#Output: 13

#She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# string = input("Введите текст:").lower().split()
# stringA = set(string)
# print(len(stringA))


# user_input = "She sells sea shells on the sea shore The shells \
# that she sells are sea shells I'm sure. So if she sells sea \
# shells on the sea shore I'm sure that the shells are sea \
# shore shells"
# # example output: 19

# list_input = user_input.split()

# for i in range(len(list_input)):
#     list_input[i] = list_input[i].lower()
#     if list_input[i][-1] in [".", ",", "!", "?"]:
#         list_input[i] = list_input[i][:len(list_input[i]) - 1]

# unique_words = set(list_input)
# print(len(unique_words))