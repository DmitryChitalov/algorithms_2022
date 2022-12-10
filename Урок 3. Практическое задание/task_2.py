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

import sqlite3
from hashlib import sha256

with sqlite3.connect('datebase.db') as db:
    cursor = globals()
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name VARCHAR,
    user_password TEXT)
    """)


def hash_func(salt, password):
    hash_generator = sha256(salt.encode() + password.encode()).hexdigest()
    print('Сгенерирован hash пароля\n', hash_generator)
    return hash_generator


def register():
    print('регистрация аккаунта')
    user_name = input('name: ')
    user_password = input('pass: ')
    hash_pass = hash_func(user_name, user_password)
    con = sqlite3.connect('datebase.db')

    try:
        cursor.execute(""" SELECT user_name FROM users WHERE user_name=?""", [user_name])
        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO users VALUES (NULL, ?, ?)', (user_name, hash_pass))
            print('Ваш аккаунт зарегистрирован в базе данных')
            db.commit()
            enter_acc()
        else:
            print('такой аккаунт уже есть')
            enter_acc()
    except sqlite3.Error:
        if con: con.rollback()
        print('ошибка запроса!')
    finally:
        if con: con.close()


def enter_acc():
    print('вход в аккаунт')
    con = sqlite3.connect('datebase.db')
    name = input('name: \n')
    passw = input('password: \n')
    hash_pass = hash_func(name, passw)
    try:
        cursor.execute("""SELECT user_name FROM users WHERE user_name = ?""", [name])
        if cursor.fetchone() is None:
            print('такого аккаунта не существует, пожалуйста зарегистрируйтесь')
            register()
        else:
            cursor.execute(""" SELECT user_password FROM users WHERE user_password = ?""", [hash_pass])
            if cursor.fetchone() is None:
                print('неверно введён пароль')
                enter_acc()
            else:
                print('вход успешно выполнен!')
    except sqlite3.Error:
        if con: con.rollback()
        print('ошибка запроса!')
    finally:
        if con: con.close()


enter_acc()

with sqlite3.connect('datebase.db') as db:
    for result in cursor.execute('SELECT * FROM users'):
        print(*result)
