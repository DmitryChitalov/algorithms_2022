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


def password_hesh(login):
    password = input('Введите пароль: ')
    pass_hash = hashlib.sha256(password.encode() + login.encode()).hexdigest()
    print(f'В базе данных хранится строка: {pass_hash}')
    with open("hash.json", "w") as w_file:
        json.dump(pass_hash, w_file)
    password = input('Введите пароль повторно, для проверки: ')
    pass_hash = hashlib.sha256(password.encode() + login.encode()).hexdigest()
    with open("hash.json", "r") as r_file:
        database_hash = json.load(r_file)
    if database_hash == pass_hash:
        print('Вы ввели правильный пороль')
    else:
        print('Вы ввели неправильный пороль')


log = input('Введите логин: ')
password_hesh(log)
