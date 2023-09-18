my_dict = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров', 4: 'Смит'}

my_dict[2] = 'Никитин'
my_dict[5] = my_dict[1]
del my_dict[1]

print(my_dict)

my_dict = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров', 4: 'Смит'}

my_dict[5] = my_dict.pop(3)