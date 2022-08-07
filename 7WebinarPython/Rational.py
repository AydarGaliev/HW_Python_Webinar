import Operator as option

def first():
    firstnum = float(input('Введите первое число: ').replace(',', '.'))
    return firstnum

def second():
    secondnum = float(input('Введите второе число: ').replace(',', '.'))
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
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('Ошибка')

def mainterminal():
    global file
    x = first()
    while True:
        y = second()
        oper = selectoperation()
        resust = res(x, y)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'Result {x} {oper} {y} = {resust}\n')
        print(f'Результат {x} {oper} {y} = {resust}' )
        break