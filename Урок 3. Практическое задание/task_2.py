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


def password_check(password=input('Придумайте пароль: ')):
    salt = 'my_salt'
    hash_obj = hashlib.sha256(password.encode('utf-8') + salt.encode())
    hex_dig_res = hash_obj.hexdigest()
    with open('hash_file.json', 'w') as f:
        json.dump({'hash': hex_dig_res, 'salt': salt}, f)
    print(hex_dig_res)
    conf_password = input('Введите пароль еще раз для проверки: ')
    hash_obj2 = hashlib.sha256(conf_password.encode('utf-8') + salt.encode())
    hex_dig_res2 = hash_obj2.hexdigest()
    print(hex_dig_res2)
    with open('hash_file.json', 'r') as f:
        res = json.load(f)
    if res['hash'] == hex_dig_res2:
        print('Пароль подтвержден')
    else:
        print('Вы ввели не верный пароль')


password_check()
