# 1. Задайте строки из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте проблем.(Положительные числа)

# stroka = '267 12 963'
# list_1 = stroka.split()
# max = int(list_1[0])
# min = int(list_1[0])
# for i in list_1:
#     if int(i) > max:
#         max = int(i)
#     if int(i) < min:
#         min = int(i)
# print(max)
# print(min)

# 2. Найдите корни квадратного уравнения Ах2 + Вх + С = 0 двумя способами:
#       1) с помощью математических формул нахождения корней квадратного уравнения
#       2) с помощью дополнительных библиотек Python

# a = float(input())
# b = float(input())
# c = float(input())
# D = b ** 2 - 4 * a * c
# if D == 0:
#     print(f'Один корень и он равен = {round(-b/2 * a, 2)}')
# elif D < 0:
#     print('Корней нет')
# else:
#     print(f'Первый корень равен = {round((-b + D ** 0.5) / (2 * a), 2)}')
#     print(f'Второй корень равен = {round((-b - D ** 0.5) / (2 * a), 2)}')

# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# a = int(input())
# b = int(input())
# s = a * b
# while a != b:
#     if a > b:
#         a -= b
#     else: 
#         b -= a
# print(s // a)

# Домашнее задание
# 1_Задача
# Вычислить число c заданной точностью d
# Пример:
# - при d = 3, π = 3.141

# d = int(input('Введите число знаков после запятой: '))
# k = 1
# s = 0
# for i in range(1000000):
#     if i % 2 == 0 :
#         s += 4 / k
#     else:
#         s -= 4 / k
#     k += 2
# print(round(s, d))

# 2_Задача
# Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N. (1 - составное число)

# number = int(input('Введите целое число: '))
# print(f'Простые делители числа: ', end = ' ')
# for i in range(number - 1, 1, -1):
#     count = 0
#     if (number % i == 0):
#         for j in range(i - 1, 1, -1):
#             if (i % j == 0):
#                 count += 1
#         if (count == 0):
#             print(i, end = ' ')

# 3_Задача
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list = input('Введите числа через пробел:\n').split()
# print(f'Исходный список чисел: {list}')
# new_list = []
# [new_list.append(i) for i in list if i not in new_list]
# print(f'Список из неповторяющихся элементов: {new_list}')

# 4_Задача
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# stepenK = int(input('Введите старшую степень многочлена: '))
# string = (' ')
# for i  in range(stepenK,-1,-1):
#         string += str(random.randint(0,100)) + '*' + 'x' + '^' + str(i) + ' ' + '+' + ' '
# result = string[:-6] + ' ' + '=' + ' ' + '0'
# print(result)