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
import mysql.connector


# DROP DATABASE IF EXISTS python;
# CREATE DATABASE python;
# USE python;
#
# DROP TABLE IF EXISTS users;
# CREATE TABLE users (
# 	user_name VARCHAR(255) NOT NULL PRIMARY KEY,
#   pass_word VARCHAR(255) NOT NULL);

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='master',
    database='python')

my_cur = connection.cursor()

def insert_password():
    user_name = input('Введите логин: ')
    pass_word = input('Введите пароль: ')
    my_cur.execute(f"INSERT INTO users values ('{user_name}',"
                   f"'{hashlib.sha256(user_name.encode() + pass_word.encode()).hexdigest()}')")
    connection.commit()
    print("Данные добавлены в базу данных")


insert_password()


def req_pass_word():
    user_name = input('Введите логин: ')
    pass_word = input('Введите пароль: ')
    pass_word_hash = hashlib.sha256(user_name.encode() + pass_word.encode()).hexdigest()
    my_cur.execute(f'SELECT pass_word FROM users where user_name = "{user_name}"')
    if my_cur.fetchone()[-1] == pass_word_hash:
        print('Пароли совпадают')
    else:
        print('Пароли не совпадают')


req_pass_word()
