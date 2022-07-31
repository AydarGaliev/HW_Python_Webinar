# 1. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i - 1]. Найдите это число.
# 
# with open('1.txt', 'r', encoding = 'utf-8') as file:
#     arr = file.readlines()
#     arr = [int(i) for i in arr[0].split()]
#     for i in range(1, len(arr)):
#         if arr[i] - 1 != arr[i - 1]:
#             print((arr[i-1] + arr[i]) // 2)
# 
# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# 
# nums = [1, 5, 2, 3, 4, 6, 1, 7]
# def get_up (nums):
#     ups = []
#     for i in range(len(nums)):
#         if nums[i] == max(nums[: i + 1:]) and nums[i] not in ups:
#             ups.append(nums[i])
#     return ups
# print(get_up(nums))
# 
# 3. Напишите программу, удалающую из текста все слова, содержащие "абв"
# 
# Длинный код
# stroka = input().split()
# arr = [i for i in stroka if 'абв' not in i.lower()]
# new_str = ' '.join(arr)
# print(new_str)
# 
# Короткий код
# print(''.join(input().lower().split('абв')))
# print(' '.join([i for i in input().lower().split() if 'абв' not in i]))
# print(' '.join([i for i in input().split() if 'абв' not in i.lower()]))

# Домашнее задание
# 1_Задача
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""

# from random import randint as rnd

# def motion(candies, get):
#     while True:
#         player = int(input(f'Возьмите со стола конфеты не более {get}: '))
#         if player <= get and player > 0:
#             break
#     if (candies-player) < 0:
#         print(f'Вы взяли оставшееся количество конфет со стола: {candies}')
#     else:
#         print(f'Вы взяли количество конфет со стола: {player}')
#     candies -= player
#     return candies

# candy = 2021
# print(f'На столе лежат конфеты в количестве {candy}')
# take = int(input('Определите максимально допустимое количество конфет за ход: '))
# lot = 'ваш' if rnd(1, 2) == 1 else 'бота'
# print(f'Жеребьёвка: Первый ход {lot}')

# while candy > 0:
#     if lot == 'ваш':
#         rem = motion(candy, take)
#         candy = rem
#         if candy <= 0:
#             win = 'Игрок'
#         print(f'Конфет на столе осталось: {candy}')
#     bot = candy % (take+1)
#     if (candy-bot) < 0:
#         print(f'Бот взял оставшееся количество конфет со стола: {candy}')
#     else:
#         print(f'Бот взял количество конфет со стола: {bot}')
#     candy -= bot
#     if candy <= 0:
#         win = 'Бот'
#     print(f'Конфет на столе осталось: {candy}')

#     if lot != 'ваш':
#         rem = motion(candy, take)
#         candy = rem
#         if candy <= 0:
#             win = 'Игрок'
#         print(f'Конфет на столе осталось: {candy}')
# print(f'Победитель: {win}')

# 2_Задача
# Создайте программу для игры в ""Крестики-нолики""

# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
#       print("-" * 13)

# def take_input(player_move):
#    valid = False
#    while not valid:
#       answer = input("Куда поставим " + player_move + "? ")
#       try:
#          answer = int(answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if answer >= 1 and answer <= 9:
#          if(str(board[answer - 1]) not in "XO"):
#             board[answer - 1] = player_move
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_position = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_position:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def game(board):
#     count = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if count % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         count += 1
#         if count > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if count == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# game(board)
# input("Нажмите Enter для выхода!")

# 3_Задача
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def encode_message(message):
#     encoded_string = ""
#     i = 0
#     while (i <= len(message)-1):
#         count = 1
#         ch = message[i]
#         j = i
#         while (j < len(message)-1):     
#             if (message[j] == message[j + 1]): 
#                 count = count + 1
#                 j = j + 1
#             else: 
#                 break
#         encoded_string = encoded_string + str(count) + ch
#         i = j + 1
#     return encoded_string

# def decode(our_message):
#     decoded_message = ""
#     i = 0
#     j = 0
#     while (i <= len(our_message) - 1):
#         run_count = int(our_message[i])
#         run_word = our_message[i + 1]
#         for j in range(run_count):
#             decoded_message = decoded_message + run_word
#             j = j + 1
#         i = i + 2
#     return decoded_message

# our_message = "AuuBBBCCCCCCcccccCCCCCCCCCA. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных"
# encoded_message = encode_message(our_message)
# decoded_message = decode(encoded_message)
# print("Исходный текст: [" + our_message + "]")
# print("Текст после кодировки: [" + encoded_message +"]")
# print("Текст после дешифровки: [" + decoded_message +"]")