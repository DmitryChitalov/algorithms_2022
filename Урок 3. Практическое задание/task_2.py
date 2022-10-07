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

import os
import json
from uuid import uuid4
import hashlib
salt = uuid4().hex

def get_hash(password):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()

def password_compare():
    password = input('Введите пароль: ')
    hash1 = get_hash(password)
    with open('password.json', 'r+', encoding='utf-8') as my_password:
        json.dump(hash1, my_password, ensure_ascii=False)
    file = open('password.json', 'r+', encoding='utf-8')
    print(f'В базе данных хранится строка: {hash1}')
    for i in file:
        password2 = input('Введите пароль еще раз для проверки: ')
        hash2 = get_hash(password2)
        result_hash = i.replace('"', '')
        print(f'Хэш: {result_hash}')
        if hash2 == result_hash:
            return 'Вы ввели правильный пароль'
        else:
            print('Пароли не совпадают. Попробуйте еще.')
            return password_compare()
    file.close()

print(password_compare())