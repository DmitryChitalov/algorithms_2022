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
import json


def registration_user(salt, user, password):
    data_base = open("data_base.csv", "w")
    users = {}
    hash_password = sha256(salt.encode() + password.encode()).hexdigest()
    users[user] = {
        'salt': salt,
        'password': hash_password
    }
    data_base.write(json.dumps(users))
    data_base.close()
    print(f'В базе данных хранится строка: {hash_password}')


def authorization_user(salt, name, user_auth_password):
    with open("data_base.csv", 'r') as db:
        base = json.load(db)
    authorization_hash_password = sha256(salt.encode() + user_auth_password.encode()).hexdigest()
    if authorization_hash_password == base.get(name).get('password'):
        print('Вы ввели правильный пароль')
        db.close()
    else:
        print('Вы ввели не правильный пароль')
        db.close()


user_name = input('Введите имя пользователя: ')
user_password = input('Введите пароль: ')
registration_user('соль-соленая', user_name, user_password)
user_auth_password = input('Введите пароль для авторизации: ')
authorization_user('соль-соленая', user_name, user_auth_password)
