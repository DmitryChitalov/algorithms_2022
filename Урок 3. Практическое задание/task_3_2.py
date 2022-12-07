"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""


import hashlib
import json

# with open('users.json', 'w', encoding='utf-8') as f:
#     users_data = {}
#     json.dump(users_data, f)


def check_hash():
    users_data = {}
    password = input('Введите пароль: ')
    pass_salt = password[::-1]
    memorised_hash = hashlib.sha256((password + pass_salt).encode(encoding='utf-8')).hexdigest()
    # with open('users.json', 'r', encoding='utf-8') as f:
    #     users_data = json.load(f)
    #     print(type(users_data), users_data)

    with open('users.json', 'w', encoding='utf-8') as f:
        users_data[password] = (pass_salt, memorised_hash)
        json.dump(users_data, f)

    print('В базе даннных хранится строка: ', memorised_hash)

    with open('users.json', 'r', encoding='utf-8') as f:
        users_data = json.load(f)
        # print(type(users_data), users_data)

    duble_password = input('Введите пароль еще раз для проверки: ')
    duble_hash = hashlib.sha256((duble_password + duble_password[::-1]).encode(encoding='utf-8')).hexdigest()

    if duble_hash == users_data[password][1]:
        print(f'Вы ввели правильный пароль: {duble_password}')
    else:
        print(f'Вы ввели неправильный пароль: {duble_password} вместо {password}')




check_hash()
