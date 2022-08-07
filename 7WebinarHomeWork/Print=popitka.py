# def OpenContactList():
#     file1 = open('Contacts.txt', 'r', encoding='utf-8')
#     while True:
#         line = file1.readline()
#         if not line:
#             break
#         print(line.strip(),'\n')

# def OpenContList():
#     with open('Contacts.txt', 'r', encoding='utf-8') as data:
#         read_data = data.read()
#         print(f'\n')
#         print(f'{read_data}\n')
#         print()
#         for row in data:
#             print(f'\n{row}\n')