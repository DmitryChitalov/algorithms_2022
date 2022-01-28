"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
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
import os
from hashlib import sha256
from uuid import uuid4


def load_file():
    fr = open('test.json', 'a+')
    if os.stat("test.json").st_size == 0:
        my_dict = {}
    else:
        fr.seek(0)
        my_dict = json.load(fr)
    fr.close()
    return my_dict


def seek_dict(dct, pas):
    for key, value in dct.items():
        if sha256(value.encode() + pas.encode()).hexdigest() == key:
            return key


def write_file(dct, pas):
    with open('test.json', 'w+') as fw:
        salt = uuid4().hex
        dct[sha256(salt.encode() + pas.encode()).hexdigest()] = salt
        json.dump(dct, fw)
        return sha256(salt.encode() + pas.encode()).hexdigest()


pwd = input('Введите пароль: ')
hash1 = seek_dict(load_file(), pwd)
if hash1:
    print(f'В базе есть строка: {hash1}')
    pwd = input('Введите пароль еще раз: ')
    hash2 = seek_dict(load_file(), pwd)
    if hash2 == hash1:
        print('Пароль верен!')
    else:
        print('Пароль неверен!')
else:
    new_hash = write_file(load_file(), pwd)
    print(f'В базу записан хэш: {new_hash}')
    pwd = input('Введите пароль еще раз: ')
    hash2 = seek_dict(load_file(), pwd)
    if hash2 == new_hash:
        print('Пароль верен!')
    else:
        print('Пароль не совпадает!')
