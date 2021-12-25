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


def to_hash(salt, string):
    return sha256(salt.encode() + string.encode()).hexdigest()


def add_user(login, password):
    data = {}
    if not data.get(login):
        data[login] = to_hash(login, password)
        print(f'Your hash: {data[login]}')
        with open('result.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
    else:
        print('Current user already exists!')


def log_in(login, password):
    with open('result.json', 'r', encoding='utf-8') as f:
        data_json = json.load(f)
    password = to_hash(login, password)
    if data_json.get(login) and data_json[login] == password:
        print('Welcome!')
    else:
        print('Something wrong...')


if __name__ == '__main__':
    user = input('Input your login: ')
    passwd = input('Input your password: ')
    add_user(user, passwd)
    check_pass = input('Check your password: ')
    log_in(user, check_pass)
