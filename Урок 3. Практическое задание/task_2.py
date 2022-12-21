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


def getpass():
    password = input('Введите пароль: ')
    with open('salt_file.json', 'r') as f:
        salt_dict = json.load(f)
    salt = salt_dict['salt']
    hash_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    print(f'В базе данных хранится строка: {hash_password}')
    password_comparison = input('Введите пароль еще раз для проверки: ')
    hash_password_comparison = hashlib.sha256((password_comparison + salt).encode('utf-8')).hexdigest()
    if hash_password == hash_password_comparison:
        print('Вы ввели правильный пароль')
        with open('passwords.json', 'w') as f:
            json.dump({'password': hash_password}, f)
    else:
        print('Вы ввели неправильный пароль')

    return 0


getpass()
