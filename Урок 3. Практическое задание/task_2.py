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

import json
import hashlib
from binascii import hexlify


def data_base(dct=None):
    if dct is not None:
        with open('db.json', 'w') as file_w:
            json.dump(dct, file_w)
    try:
        with open('db.json', encoding='utf-8') as file_r:
            db = json.load(file_r)
    except FileNotFoundError:
        db = {}
    return db


def authorization(login):
    db = data_base()

    if login not in db:
        print(f'{login} не зарегистрирован.\nРегистрация:')
        password = input('Введите новый пароль: ')
        pas_obj = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), login.encode('utf-8'), 100000)
        pas_key = hexlify(pas_obj)

        db[login] = pas_key.decode()
        db = data_base(db)  # обновляем бд
        print(f'В базу данных записана строка: {db[login]}')
    else:
        print(f'{login} есть в базе данных: {db[login]}')

    password = input('Введите пароль для входа: ')
    pas_obj = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), login.encode('utf-8'), 100000)
    pas_key = hexlify(pas_obj)
    if pas_key.decode() == db[login]:
        print('Вход')
    else:
        print('Вы ввели неправильный пароль')


authorization(input('Логин: '))
