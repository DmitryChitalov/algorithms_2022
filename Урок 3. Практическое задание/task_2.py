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


def db_password_check(password): #Проверка пароля в БД
    db_connection = sqlite3.connect('db_password.sqlite').cursor()
    sql_password_request = '''
        SELECT hash FROM users;
    '''
    if password == db_connection.execute(sql_password_request).fetchall()[0][0]:
        db_connection.close()
        return True
    db_connection.close()
    return False


def db_password_add(password_hash):  #Запись в БД хешей.
    db_connection = sqlite3.connect('db_password.sqlite')
    cursor = db_connection.cursor()
    sql_password = f"INSERT INTO users (hash)VALUES ('{password_hash}');"
    cursor.execute(sql_password)
    db_connection.commit()
    db_connection.close()


def authorization():
    password = input('Введите пароль: ')
    password_hash = hashlib.sha256((password + 'salt').encode('utf-8')).hexdigest()
    db = sqlite3.connect('db_password.sqlite')
    db_connection = sqlite3.connect('db_password.sqlite').cursor()
    sql_table_create_request = '''
    CREATE TABLE IF NOT EXISTS users (
    hash VARCHAR(50)
    );
    '''
    db_connection.execute(sql_table_create_request)
    db_password_add(password_hash)
    print(f'В базе данных хранится строка: {password_hash}')
    second_password = hashlib.sha256(
       (input('Введите пароль еще раз для проверки: ') + 'salt').encode('utf-8')).hexdigest()
    if db_password_check(second_password):
        db.close()
        return 'Вы ввели правильный пароль'
    db.close()
    return 'Вы ввели неправильный пароль'


if __name__ == '__main__':
    print(authorization())
