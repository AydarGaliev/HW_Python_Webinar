#_1 задача
# a, b = map(int, input().split())
# a = int(input())
# b = int(input())
# if a * a == b or b ** 2 == a:
#     print('yes')
# else:
#     print('no')

#_2 задача
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# max_number = a
# if max_number < b:
#     max_number = b
# if max_number < c:
#     max_number = c
# if max_number < d:
#     max_number = d
# if max_number < e:
#     max_number = e
# print(max_number)
#вариант 2
# a = list(map(int, input().split()))
# max_number = a[0]
# for i in a:
#     if i > max_number:
#         max_number = i
# print(max_number)

#_3 задача
# n = int(input('Введите число: '))
# print(*range(-n, n + 1))
# вариант 2
# n = int(input('Введите число: '))
# for i in range(-n, n + 1):
#     print(i, end=' ')

#_4 задача
# n = float(input('Введите число: '))
# print(int(n * 10) % 10)

#_5 задача
# n = int(input())
# if((n % 5 == 0 and n % 10 == 0) or (n % 15 == 0)) and n % 30 != 0:
#     print('yes')
# else:
#    print('no')

# Домашнее задание
# 1_Задача
# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# a = int(input('Введите число: '))
# if((a == 6) or (a == 7)):
#     print('Да')
# else:
#     print('Нет')

# 2_Задача
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# def statement(x, y, z):
#     print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
#     return (not (x or y or z)) == (not x and not y and not z)
# if(statement(0, 0, 0) and statement(0, 0, 1) and statement(0, 1, 0) and 
# statement(0, 1, 1) and statement(1, 0, 0) and statement(1, 0, 1) and
# statement(1, 1, 0) and statement(1, 1, 1)):
#     print("Истина")
# else:
#     print("Ложь")

# 3_Задача
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# def inputKoord(x):
#     a = [0] * x
#     for i in range(x):
#         is_C = False
#         while not is_C:
#             try:
#                 number = float(input(f"Введите {i+1} координату: "))
#                 a[i] = number
#                 is_C = True
#                 if a[i] == 0:
#                     is_C = False
#                     print("Координата не должно быть равна 0.")
#             except ValueError:
#                 print("Ты ошибся. Вводить надо числа!")
#     return a