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


def hash_password(passw, login):
    with open('hash_and_salt.json', 'w') as sv:
        passw1 = bytes(passw, encoding='utf-8')
        salt = bytes(login, encoding='utf-8')
        hash1 = hashlib.sha256(salt + passw1).hexdigest()
        dict_js = {'salt': login, 'hash_pass': hash1}
        json.dump(dict_js, sv)
        print(f"В базе данных храница строка: {hash1}")
    return dict_js


def check_hash(passw):
    with open('hash_and_salt.json', 'r') as sv2:
        dec_js = json.load(sv2)
        passw2 = bytes(passw, encoding='utf-8')
        salt = bytes(dec_js['salt'], encoding='utf-8')
        hash2 = hashlib.sha256(salt + passw2).hexdigest()
        if dec_js['hash_pass'] == hash2:
            print('Вы ввели верный пароль')
        else:
            print('Не верный пароль')


hash_password(input('Введите пароль: '), input('Введите логин: '))
check_hash(input('Введите пароль повторно: '))