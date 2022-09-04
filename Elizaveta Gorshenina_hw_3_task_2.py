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
import hashlib
import uuid


connection = sqlite3.connect('authorisation.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS 'logs_and_pass';")
cursor.execute("CREATE TABLE IF NOT EXISTS 'logs_and_pass' (logins varchar(255), passwords varchar(255));")
connection.commit()
my_login = input('Введите логин: ')
my_pass = input('Введите пароль: ')
salt = uuid.uuid4().hex
my_pass_hash = hashlib.sha256(my_pass.encode('utf-8') + salt.encode('utf-8')).hexdigest()
print('Хеш пароля: ', my_pass_hash)
cursor.execute("INSERT INTO 'logs_and_pass' VALUES (?, ?);", (my_login, my_pass_hash))
connection.commit()
my_pass_rep = input('Введите пароль повторно: ')
my_pass_rep_hash = hashlib.sha256(my_pass_rep.encode('utf-8') + salt.encode('utf-8')).hexdigest()
print('Хеш повторно введенного пароля: ', my_pass_rep_hash)
cursor.execute("SELECT 'logs_and_pass'.passwords FROM 'logs_and_pass' WHERE 'logs_and_pass'.logins = ?;", (my_login,))
if my_pass_rep_hash == cursor.fetchone()[0]:
    print('Вы ввели правильный пароль.')
connection.close()
