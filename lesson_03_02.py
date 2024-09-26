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
from hashlib import pbkdf2_hmac
from uuid import uuid4
import sqlite3


def pass_request():
    user_password = input('Password: ').encode('utf-8')
    return user_password


def hash_creator(salt, password):
    return pbkdf2_hmac('sha256', password, salt, 10000)


def database_saver(login, salt, password_hash):
    conn = sqlite3.connect('hash_database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS hash_db (login, salt, hash)')
    cursor.execute(f'INSERT INTO hash_db VALUES ("{login}", "{salt}", "{password_hash}")')
    conn.commit()
    return print(f'Saved to database: {login}, {salt}, {password_hash}')


def password_check():
    login = input('Login: ')
    salt = uuid4().hex.encode('utf-8')
    print(f'Salt: {salt}')
    password_hash = hash_creator(salt, pass_request())
    print(f'Hash: {password_hash}')
    database_saver(login, salt, password_hash)
    if password_hash == hash_creator(salt, pass_request()):
        print('Пароли совпадают')
    else:
        print('Пароли не совпадают')


password_check()





