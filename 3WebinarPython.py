# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# 1 задача
# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# import time

# print(int(str(time.time_ns())[-5] + str(time.time_ns())[-4] + str(time.time_ns())[-3])) #1 вариант

# for i in range(10):
#     time.sleep(0.1)
#     if i % 2 == 0:
#         print(int(str(time.time_ns())[-5] + str(time.time_ns())[-4] + str(time.time_ns())[-3]))
#     else:
#         print(int(str(time.time_ns())[-4] + str(time.time_ns())[-3])) #2 вариант

# 2 задача
# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# def SearchList(arr, number):
#     # for i in arr:
#     #     if i == str(number):
#     #         return 'yes'
#     #     return 'no'  # 1 вариант

#     # if str(number) not in arr:
#     #     return 'yes'
#     # return 'no'      # 2 вариант (с проверкой на отсутствие числа)

# list_1 = ['hello', '12', 'red', '567']
# print(SearchList(list_1, 567))

# 3 задача
# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# def SearchElem(arr, element):
#     count = 0
#     # for i in arr:
#     #     if i == element:
#     #         count += 1
#     #     if count == 2:
#     #         return 'yes'
#     # return 'no'           # 1 вариант
#     for i in range(len(arr)):
#         if arr[i] == element:
#             count += 1
#         if count == 2:
#             return f'yes: {i + 1}'
#     return 'no'             # 2 вариант (с выводом позиции второго входа)

# print(SearchElem(['qwerty', 'asd', 'zxc', 'qwerty', 'ertqwe'], 'qwerty'))

# Домашнее задание

# 1 Задача
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]

# def sum_elem (list):
#     result = 0
#     for i in range (len(list)):
#         if i % 2 != 0 :
#             result += list[i]
#     return result

# print(sum_elem(list))

# 2 Задача
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import math

# list = [2, 3, 4, 5, 6]

# def multiple(list):
#     composition = []
#     for i in range(int(math.ceil(len(list)/2))):
#         composition += {list[i]*list[-(i+1)]}
#     return composition

# print(multiple(list))

# 3 Задача
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import math

# list = [1.1, 1.2, 3.1, 5, 10.01]

# def numberList(a):
#     for i in range(len(a)):
#         a[i] = round(a[i]-math.floor(a[i]), 2)

# def difference(a):
#     maximum = a[0]
#     minimum = a[0]
#     for i in range(len(a)):
#         if maximum < a[i]:
#             maximum = a[i]
#         elif minimum > a[i] and a[i] != 0:
#             minimum = a[i]
#     return maximum-minimum

# numberList(list)
# print(difference(list))

# 4 Задача
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# numbers = int(input('Введите число: '))

# def binar(a):
#     result = ''
#     while a > 0:
#         result = str(a % 2) + result
#         a = a // 2
#     return result

# print(binar(numbers))