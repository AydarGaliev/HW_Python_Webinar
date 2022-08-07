import Operator as option
from cmath import *

def first():
    firstnum = complex(input('Введите первое число: '))
    return firstnum

def second():
    secondnum = complex(input('Введите второе число: '))
    return secondnum

def selectoperation():
    global operation
    operation = (input(f'Выбор операции: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Ошибка операции')

def res(firstnum, secondnum):
    if  operation == '+':
        res = secondnum + firstnum
        result = res
        return result
    elif operation == '-':
        res = secondnum - firstnum
        result = res
        return result
    elif operation == '*':
        res = secondnum * firstnum
        result = res
        return result
    elif operation == '/':
        res = secondnum / firstnum
        result = res
        return result
    else:
        print('Ошибка')

def mainterminal():
    global file
    x = first()
    while True:
        y = second()
        oper = selectoperation()
        result = res(x, y)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'Result {x} {oper} {y} = {result}\n')
        print(f'Результат {x} {oper} {y} = {result}' )
        break