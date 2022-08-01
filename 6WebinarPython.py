# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,*,/. Приоритет операций стандартный.
# Пример:
# 2+2 => 4
# 1+2*3 => 7
# 1-2*3 => -5
#  Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
#  1+2*3 => 7
# (1+2)*3 => 9

# expression = input('Введите выражение')
# print(eval(expression))

# Домашнее задание
# 1_Задача
# Пример:
# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# transformation = lambda data: data
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print ('ok')
# else:
#     print ('fail')

# 2_Задача

# from math import pi


# def find_farthest_orbit(list_of_orbits):
#     lst=[round(pi*list_of_orbits[i][0]*list_of_orbits[i][1], 2) if list_of_orbits[i][0]!=list_of_orbits[i][1] else 0 for i in range(len(list_of_orbits))]
#     return list_of_orbits[lst.index(max(lst))]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# 3_Задача

# sym = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

# string = ''
# phrase = input('Введите фразу: ').split()
# for i in range(len(phrase)):
#     if i > 0:
#         string += '_'
#     for j in range(len(phrase[i])):

#         if phrase[i][j] in sym:
#             string += 'a'
#         else:
#             string += phrase[i][j]
# string = string.split('_')

# if len(set(map(lambda s: s.count('a'), string))) == 1:
#     result = 'Парам пам-пам' 
# else:
#     result = 'Пам парам'
# print(result)

# 4_Задача

# def same_by(characteristic, objects):
#     characteristic = True
#     for i in objects:
#         if i % 2 != 0:
#             characteristic = not characteristic
#             break
#     return characteristic


# # values = [1, 2, 3, 4]
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# 5_Задача

# x = int(input('Введите число X: '))
# y = int(input('Введите число Y: '))

# def print_operation_table(operation, num_columns=9, num_rows=9):
#     for col in range(1, num_columns+1):
#         print()
#         for row in range(1, num_rows+1):
#             print(operation(col, row), end='\t')

# print_operation_table(lambda x, y: x*y, x, y)