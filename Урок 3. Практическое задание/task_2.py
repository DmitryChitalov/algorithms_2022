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
import hashlib
from uuid import uuid4


passwd_hash = {}

try:
    with open('passwd_hash.json', 'x', encoding='utf-8') as f:
        json.dump(passwd_hash, f)

except FileExistsError:
    pass

finally:
    with open('passwd_hash.json', 'r', encoding='utf-8') as f:
        passwd_hash = json.load(f)

login = input('Введите логин: ')
password = input('Введите пароль: ')


def get_hash(password):
    salt = uuid4().hex
    key = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    print(f'В базе данных хранится строка: {key}')
    passwd_hash[login] = [salt, key]
    with open('passwd_hash.json', 'w', encoding='utf-8') as f:
        json.dump(passwd_hash, f)


get_hash(password)

new_password = input('Введите пароль еще раз для проверки: ')


def password_verification(new_password):
    with open('passwd_hash.json', 'r', encoding='utf-8') as f:
        passwd_hash = json.load(f)

    new_key = hashlib.sha256(passwd_hash[login][0].encode() + new_password.encode()).hexdigest()

    if new_key == passwd_hash[login][1]:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели неправильный пароль')



password_verification(new_password)
