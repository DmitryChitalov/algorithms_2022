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

from uuid import uuid4
import sqlite3
import hashlib

conn = sqlite3.connect('task2.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS passwords (pwd_hash varchar(500))')
cursor.execute('CREATE TABLE IF NOT EXISTS salt (salt varchar(500))')

if salt := tuple(cursor.execute(f"SELECT salt FROM salt limit 1")):
    salt = salt[0][0]
else:
    salt = uuid4().hex
    cursor.execute(f"INSERT INTO salt VALUES ('{salt}')")
    conn.commit()

print('Соль:', salt)

if password := input('Введите пароль:'):
    hashed_string = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    if tuple(cursor.execute(f"SELECT pwd_hash FROM passwords where pwd_hash = '{hashed_string}'")):
        print('Вы ввели правильный пароль, который уже есть в БД.', hashed_string)
    else:
        print(hashed_string)
        if password := input('Введите пароль еще раз для проверки:'):
            if hashlib.sha256(salt.encode() + password.encode()).hexdigest() == hashed_string:
                print('Проверка успешна, пароль записан в БД.', hashed_string)
                cursor.execute(f"INSERT INTO passwords VALUES ('{hashed_string}')")
                conn.commit()
            else:
                print('ОШИБКА! Вы ввели неправильный пароль!')
        else:
            print('Вы не ввели пароль для проверки!')
else:
    print('Пароль не может быть пустым!')

conn.close()
