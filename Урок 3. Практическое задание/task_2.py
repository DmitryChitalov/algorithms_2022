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
from hashlib import sha256


# Функция для извлечения данных
def load_json(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            accounts = json.load(file)
        return accounts
    else:
        return {}


# Функция для хеширования
def hash_password(login, password):
    hash_pass = sha256(password.encode('utf-8') + login.encode('utf-8'))
    return hash_pass.hexdigest()


# Функция создаёт аккаунт и если он существует сообщает об этом и запускается рекурсивно
def create_account():
    print('Создание аккаунта')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    hash_pass = hash_password(login, password)
    print(f'Полученный хеш: {hash_pass}')

    accounts = load_json('accounts.json')

    if accounts.get(login):
        print('Логин занят повторите попытку')
        create_account()

    accounts[login] = hash_pass

    with open('accounts.json', 'w', encoding='utf-8') as file:
        json.dump(accounts, file, indent=4)


# Функция проверки валидности логина и пароля
def check_account():
    print('Проверка аккаунта')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    hash_pass = hash_password(login, password)
    accounts = load_json('accounts.json')

    if accounts.get(login) == hash_pass:
        print('Вы ввели правильный пароль')
    else:
        print('Ввод неверен')


create_account()
check_account()
