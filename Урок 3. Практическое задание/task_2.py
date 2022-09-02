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
from hashlib import pbkdf2_hmac
from binascii import hexlify
from uuid import uuid4
import csv


def get_key(str, salt):
    res_hash = hexlify(
        pbkdf2_hmac(hash_name='sha256',
                    password=str.encode('utf-8'),
                    salt=salt.encode('utf-8'),
                    iterations=100)
    )
    res_hash.decode('utf-8')
    return res_hash


mod = int(input('Введите - 1  id для сохранения пользователей и паролей или 2. - для проверки пароля пользователя: '))

if mod == 1:
    with open("data.csv", 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'salt', 'key'])
        writer.writeheader()
        inp_mod = 1
        while inp_mod !=0:
            id = input('Введите id пользователя: ')
            passw = input('Введите пароль: ')
            salt = uuid4().hex
            key = get_key(passw, salt).decode('utf-8')
            print(type(salt),salt)
            print(type(key),key)
            writer.writerow({'id': id, 'salt': salt, 'key': key})


            inp_mod = int(input('Для продолжения нажмите любую клавишу, для выхода - 0: '))


if mod == 2:
    id = input ('Введите id пользователя: ')

    passw_to_check = input('Введите пароль для проверки: ')
    with open("data.csv", 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['id'] == id:
                salt = row['salt']
                key = row ['key']
    key_new = get_key(passw_to_check, salt).decode('utf-8')

    if key_new == key:
        print('Пароль введен верно')
    else:
        print('Пароль неверный')
