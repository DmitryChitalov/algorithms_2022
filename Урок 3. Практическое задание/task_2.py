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

from hashlib import sha256
from uuid import uuid4
import json

password = input('Enter your password: ')

salt = uuid4().hex


def do_hash(pas, sal):
    return sha256(sal.encode() + pas.encode()).hexdigest()


def password_hash(pas, sal):
    hash_file = open('pas_hash.csv', 'w')
    pas_hash = do_hash(pas, sal)
    users_pas = {pas: {'hash': pas_hash, 'salt': sal}}
    hash_file.write(json.dumps(users_pas))
    hash_file.close()
    print(f'The string is stored in the database: {pas_hash}')
    new_pass = input('Enter your password again: ')
    with open('pas_hash.csv', 'r') as fr:
        base = json.load(fr)
    new_pass_hash = do_hash(new_pass, base[pas]['salt'])
    if base[pas]['hash'] == new_pass_hash:
        print('Correct password')
    else:
        print('Incorrect password')


password_hash(password, salt)