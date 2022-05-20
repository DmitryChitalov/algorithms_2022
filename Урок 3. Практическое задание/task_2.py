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
from uuid import uuid4


def password_verification():
    salt = uuid4().hex
    password = input('Введите пароль: ')
    hash_obj = hashlib.sha256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    with open('login_password.json', 'w', encoding='utf-8') as f:
        json.dump([salt, hash_obj], f)
    with open('login_password.json', 'r', encoding='utf-8') as f:
        hash_pass = json.load(f)
        print(f'В базе данных хранится строка: {hash_pass[1]}')
        replay_password = input('Введите пароль еще раз для проверки: ')
        if hash_pass[1] == \
                hashlib.sha256(hash_pass[0].encode('utf-8') + replay_password.encode('utf-8')).hexdigest():
            # print(hash_pass.get(replay_password))
            return 'Вы ввели правильный пароль'
        else:
            return 'Введен неверный пароль'


print(password_verification())
