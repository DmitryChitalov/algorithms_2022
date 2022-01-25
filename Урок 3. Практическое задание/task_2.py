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

import hashlib
import json
from uuid import uuid4



def hash_pass():
    data_base = open('save_pass', 'w')
    passwd = input('Введите пароль: ')
    salt = uuid4().hex
    hashAndSalt = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
    data_base.write(json.dumps(hashAndSalt))
    print(f'В базе данных хранится строка:{hashAndSalt}')
    new_passwd = input('Введите пароль еще раз для проверки: ')
    salt = uuid4().hex
    new_hashAndSalt = hashlib.sha256(salt.encode() + new_passwd.encode()).hexdigest()
    if hashAndSalt == new_hashAndSalt:
        print('Вы ввели правельый пароль')
    else:
        print('Пароль не верный')
    return hash_pass()


hash_pass()

