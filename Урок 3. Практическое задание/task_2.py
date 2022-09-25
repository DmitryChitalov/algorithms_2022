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

from hashlib import sha256
import json


def salt():
    return sha256('static salt'.encode('utf-8')).hexdigest()


def compare_to_hash(p, login):
    with open('pswd.json', 'r') as f:
        p_list = json.load(f)
    p = sha256(p.encode('utf-8')).hexdigest() + salt()
    return p in p_list[login]


def write_hash(p, login):
    data = {login: sha256(p.encode('utf-8')).hexdigest() + salt()}
    with open('pswd.json', 'w') as f:
        json.dump(data, f)


def get_hashed(login):
    with open('pswd.json', 'r') as f:
        return json.load(f)[login]


def pswd(login='login'):
    plain_pswd = input('Enter the password: ')
    write_hash(plain_pswd, login)

    print(f'DB contains {get_hashed(login)}')
    if compare_to_hash(input('Type your password again: '), login):
        return f'The password is correct'
    else:
        return f'Wrong password'


print(pswd())

