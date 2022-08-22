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
from hashlib import pbkdf2_hmac
from os import urandom
from mysql.connector import connect, Error


"""Решение при помощи json файла"""


def ret_psw_hash(password, salt):
    psw_hash = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
    return psw_hash.hex()


_salt = urandom(32)
psw_1 = input('Введите пароль: ')
with open('psw.json', 'w') as psw_file:
    json.dump(ret_psw_hash(psw_1, _salt), psw_file)

psw_2 = input('Введите пароль ещё раз: ')
with open('psw.json', 'r') as psw_file:
    if json.load(psw_file) == ret_psw_hash(psw_2, _salt):
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели не правильный пароль')


"""Решение при помощи БД"""


try:
    with connect(host="localhost", user="root", password="rootroot", database="testdb") as connection:
        login = input('Введите логин: ')
        with connection.cursor() as cursor:
            cursor.execute("SELECT hash_psw, salt FROM users WHERE login = %s", (login,))
            result = cursor.fetchone()
            psw_1 = input('Введите пароль: ')
            if result:
                if ret_psw_hash(psw_1, result[1]) == result[0]:
                    print('Вы ввели правильный пароль')
                else:
                    print('Вы ввели не правильный пароль')
            else:
                _salt = urandom(32)
                hash_1 = ret_psw_hash(psw_1, _salt)
                psw_2 = input('Введите пароль ещё раз: ')
                hash_2 = ret_psw_hash(psw_2, _salt)
                if hash_2 == hash_1:
                    cursor.execute("INSERT INTO users(login, hash_psw, salt) VALUES (%s, %s, %s)",
                                   (login, hash_1, _salt))
                    connection.commit()
                    print('Вы ввели правильный пароль')
                else:
                    print('Вы ввели не правильный пароль')
except Error as e:
    print(e)
