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