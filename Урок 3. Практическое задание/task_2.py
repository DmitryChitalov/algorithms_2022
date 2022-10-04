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
import sys
import os


def hash_function(input_string, input_solt):
    hash_obj = hashlib.sha256(input_solt.encode() + input_string.encode())
    return hash_obj.hexdigest()

def new_user_creation(name):
    print(f' New User  - creating ... ')
    inp_passw = input('please enter your password: ')
    os.remove('logins.bak')
    os.rename('logins.json', 'logins.bak')
    logins[inp_login] = hash_function(inp_passw, name)
    print(f'    New Hash generated from Password     : {logins[inp_login]} stored to logins.json file')
    with open('logins.json', 'w', encoding='utf-8') as file_out:
        json.dump(logins, file_out)
    print(f' New User  - created ')


def test_file():
    credential_data = {
        "vlad": 1234567,
        "Ann": 23456,
        "Serge": 87654}
    with open('logins.json', 'w') as outfile:
        json.dump(credential_data, outfile)


if __name__ == '__main__':
    if not os.path.isfile('logins.json'):
        test_file()
    print('')
    inp_login = input('please enter your login: ')

    with open('logins.json', 'r', encoding='utf-8') as f:
        logins = json.load(f)

    if inp_login in logins:
        inp_passw = input('please enter your password: ')
        print(f'    Hash generated from Password     : {hash_function(inp_passw, inp_login)}')
        print(f'    Stored hash for user {inp_login} : {logins[inp_login]}')
        if hash_function(inp_passw, inp_login) == logins[inp_login]:
            print(f' -- Authentication success -- ')
            sys.exit(0)
        else:
            print(f' -- Authentication fails -- ')
            sys.exit(0)
    else:
        new_user_creation(inp_login)


# Script listing:
#
# please enter your login: Maria
#  New User  - creating ...
# please enter your password: Maria123
#     New Hash generated from Password     : 6d2026baa2ac715db0b0af25da9612ff77b365f95c7c3d5ec5e2e02ae75f475b stored to logins.json file
#  New User  - created
#
# Process finished with exit code 0
#
# please enter your login: Maria
# please enter your password: maria222
#     Hash generated from Password     : 2c3c2dcafb130f58659b081a6d9a293430255805da4b4bc096f39733f4d4f224
#     Stored hash for user Maria : 6d2026baa2ac715db0b0af25da9612ff77b365f95c7c3d5ec5e2e02ae75f475b
#  -- Authentication fails --
#
# Process finished with exit code 0
#
#
# please enter your login: Maria
# please enter your password: Maria123
#     Hash generated from Password     : 6d2026baa2ac715db0b0af25da9612ff77b365f95c7c3d5ec5e2e02ae75f475b
#     Stored hash for user Maria : 6d2026baa2ac715db0b0af25da9612ff77b365f95c7c3d5ec5e2e02ae75f475b
#  -- Authentication success --
#
# Process finished with exit code 0




