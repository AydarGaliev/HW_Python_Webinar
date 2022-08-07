from AddContacts import AddName, AddSurname, AddPhone, AddPost

def input_data():
    name = AddName()
    surname = AddSurname()
    phone = AddPhone()
    post = AddPost()
    var = int(input("В каком варианте вы хотите записать даные?"
                    "1 вариант: построчно, 2 вариант через ';'"
                    "Выберите номер варианта:"))
    while var != 1 and var != 2:
        print('Нет подходящих вариантов.')
        var = int(input('Введите номер варианта: '))
    if var == 1:
        with open('first_variant_contacts.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{post}\n')
    else:
        with open('second_variant_contacts.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{post}\n')

def print_data():
    print('Вывожу данные для вас из 1-ого файла\n')
    with open('first_variant_contacts.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        print(''.join(data_first))
    print('Вывожу данные для вас из 2-ого файла\n')
    with open('second_variant_contacts.csv', 'r', encoding='utf-8') as file:
        data_second = ''.join(file.readlines())
        print(*data_second)
    return data_first, data_second

def put_data():
    print('Из какого файла вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Нет подходящих вариантов.')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        print("Какую именно запись по счёту хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        print(f'Именить данную запись\n{data_first[number_journal - 1]}')
        name = AddName()
        surname = AddSurname()
        phone = AddPhone()
        post = AddPost()
        data_first = data_first[:number_journal] + [f'{name};{surname};{phone};{post}\n'] + \
            data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения сохранены.')
    else:
        print("Какую именно запись по счёту хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        print(f'Именить данную запись\n{data_second[number_journal - 1]}')
        name = AddName()
        surname = AddSurname()
        phone = AddPhone()
        post = AddPost()
        data_second = data_second[:number_journal] + f'{name};{surname};{phone};{post}\n' + \
            data_second[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(data_second)
        print('Изменения сохранены.')

def delete_data():
    print('Из какого файла вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Нет подходящих вариантов.')
        number_file = int(input('Введите номер файла: '))
    
    if number_file == 1:
        print("Какую именно запись по счёту хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения сохранены.')
    else:
        print("Какую именно запись по счёту хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения сохранены.')