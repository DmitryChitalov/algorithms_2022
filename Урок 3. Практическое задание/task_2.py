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

import mysql.connector
import hashlib


def pass_add(data):
    user_data = input('Введите пароль: ')
    user_data_hash = hashlib.sha512(data + user_data.encode('utf-8')).hexdigest()
    cursor.execute(f"INSERT INTO passwords(password_hash) VALUES ('{user_data_hash}')")
    connect.commit()
    cursor.execute(f"SELECT password_hash FROM passwords WHERE password_hash = '{user_data_hash}'")
    print('В базе данных хранится хэш: ', cursor.fetchone()[0])


def pass_check(data):
    user_data = input('Ещё раз введите пароль: ')
    user_data_hash = hashlib.sha512(data + user_data.encode('utf-8')).hexdigest()
    cursor.execute("SELECT password_hash FROM passwords")
    if user_data_hash == cursor.fetchone()[0]:
        print('Вы ввели правильный пароль')
    else:
        print('Что-то пошло не так')


connect = mysql.connector.connect(user='root',
                                  password='WWtT#@pGS8Fm5qj',
                                  host='127.0.0.1',
                                  database='py_algorithms')

cursor = connect.cursor()

cursor.execute("SELECT salt FROM salt")
salt = cursor.fetchone()[0].encode('utf-8')

pass_add(salt)
pass_check(salt)

connect.close()
