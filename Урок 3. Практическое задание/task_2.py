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

from binascii import hexlify
from hashlib import pbkdf2_hmac
from json import load, dump
from uuid import uuid4


def get_password_hash(passwd, salt):
    p_hash = pbkdf2_hmac(hash_name='sha256',
                         password=passwd.encode('utf-8'),
                         salt=salt.encode(),
                         iterations=100_000)
    return hexlify(p_hash)


def add_new_user(name, password):
    try:
        with open('./БД.json') as db:
            data = load(db)
    except:
        data = {}
    if name in data:
        print('Такой пользователь уже усществует')
    else:
        salt = uuid4().hex
        p_hash = get_password_hash(password, salt)
        with open('./БД.json', 'w+') as db:
            data[name] = [p_hash.decode(), salt]
            dump(data, db, indent=2)


def verify_user(name, password):
    try:
        with open('./БД.json') as db:
            data = load(db)
        salt = data[name][1]
    except KeyError:
        print('Нет такого пользователя')
    except FileNotFoundError:
        print('Файл базы данных не найден')
    else:
        p_hash = get_password_hash(password, salt)
        if p_hash == data[name][0].encode():
            print('Пароль верный!')
        else:
            print('Неправильный пароль')


name = input('Введите логин: ')
password = input('Введите пароль: ')
add_new_user(name, password)
password_2 = input('Введите пароль еще раз: ')
verify_user(name, password_2)
