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
from uuid import uuid4
import json
def get_hash():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    hash_password = hashlib.sha256(login.encode() + password.encode()).hexdigest()
    data_users = login, hash_password
    return data_users

def register_users():
    login, reg_hash = get_hash()
    with open('users.json', 'w', encoding='utf-8')as f:
        json.dump(data_users, f)
    return login, reg_hash

def log_in():
    login, reg_hash = get_hash()
    with open('users.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


    hash_checking = hashlib.sha256(data_users[0].encode() + password_again.encode()).hexdigest()
    if hash_checking == data[1]:
        print('Вы ввели верный пароль')
    else:
        print('Пароль неверный')