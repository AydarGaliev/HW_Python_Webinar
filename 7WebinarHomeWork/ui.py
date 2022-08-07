from Logger import input_data, print_data, put_data, delete_data

def interface():
    print('Привет, это телефонный справочник. Выберите действие: \n'
            '1. Записать данные(2 варианта)\n'
            '2. Удалить данные\n'
            '3. Изменить данные\n'
            '4. Вывести данные\n')
    command = int(input("Введите номер функции: "))

    while command < 1 or command > 4:
        print('Нет подходящих вариантов.')
        command = int(input('Введите номер варианта: '))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    else:
        print_data()