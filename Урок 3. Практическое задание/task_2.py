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

import hashlib
import sqlite3 as sql
from uuid import uuid4

dbname = "passwordDB.sql"
connectdb = sql.connect(dbname)

with connectdb:
    cur = connectdb.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS "passwordCash" ("password" STRING UNIQUE, "cache" STRING)')
    try:
        cur.execute(f'INSERT INTO "passwordCash" (password, cache) VALUES ("cache_salt", "{str(uuid4())}" )')
    except sql.IntegrityError:
        pass
    finally:
        connectdb.commit()


def connector_db(password):
    with connectdb:
        cur = connectdb.cursor()
        cur.execute(f'SELECT "cache" FROM "passwordCash" WHERE password = "{password}"')
        data = cur.fetchall()
        return str(data[0][0]) if data else None


def cache_value():
    salt = connector_db('cache_salt')
    return str(salt[0][0])


def connect_db_rw(password: str, cache: str):
    with connectdb:
        cur = connectdb.cursor()
        try:
            cur.execute(f"INSERT INTO passwordCash VALUES ('{password}','{cache}')")
        except sql.IntegrityError:
            print("Этот пароль уже в  DB")
            return None

        connectdb.commit()


def proxy(password, salt):
    return hashlib.sha256(password.encode() + salt.encode()).hexdigest()


def hash_go():
    password = input('Введите пароль для записи в BD: ')
    password_in = proxy(password, cache_value())
    print(f'CASH в БАЗЕ ДАННЫХ: {password_in}')
    db_cache = connector_db(password)
    if not db_cache:
        connect_db_rw(password, password_in)

    password = input("Введите пароль еще раз для проверки:: ")
    password_in = proxy(password, cache_value())
    db_cache = connector_db(password)

    if password_in == db_cache:
        print("Вы ввели правильный пароль")
        return
    print("Вы ввели  не правильный пароль")


hash_go()
