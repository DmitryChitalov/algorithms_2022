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

# Хранение в файле
# import hashlib
# import uuid
# import sqlite3
#
# password = input('Введите пароль: ')
# salt = str(uuid.uuid4())
# res = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
# print(f'Хэш пароля:{res}')
#
#
# with open('password.json', 'w')as f:
#     f.write(f'user_1 - {res}')
#
# with open('password.json', 'r')as f:
#     pass_check = input('Введите пароль еще раз для проверки: ')
#     user_pass = f.read()
#     if user_pass[9:] == hashlib.sha256(salt.encode() + pass_check.encode('utf-8')).hexdigest():
#         print('Вы ввели правильный пароль')
#     else:
#         print('Вы ввели неправильный пароль')




# Хранение в БД

from hashlib import sha256
from os.path import join, dirname
from sqlite3 import connect, OperationalError, IntegrityError


class HashClass:
    def __init__(self):
        self.db_obj = join(dirname(__file__), "db_hash.sqlite")
        self.conn = connect(self.db_obj)
        self.crs = self.conn.cursor()

    def create_table(self):

        create_stmt = "CREATE TABLE user_info (user_login VARCHAR(255)" \
                      "unique, user_password varchar(255));"

        try:
            self.crs.execute(create_stmt)
        except OperationalError:
            print('Таблица уже существует')
        else:
            self.conn.commit()
            print('Операция прошла успешно, таблица добавлена в БД')

    @staticmethod
    def get_hash():
        login = input('Введите логин: ')
        passwd = input('Введите пароль: ')
        hash_obj = sha256(login.encode() + passwd.encode()).hexdigest()
        return login, hash_obj

    def register(self):

        login, reg_hash = self.get_hash()
        insert_stmt = "INSERT INTO user_info (user_login, user_password)" \
                      "VALUES (?, ?)"

        user_info = (login, reg_hash)

        try:
            self.crs.execute(insert_stmt, user_info)
        except IntegrityError:
            print('Вы уже есть в базе, выполните вход')
        else:
            self.conn.commit()
            print('Операция прошла успешно, вы зарегистрировались')


    def log_in(self):

        login, check_hash = self.get_hash()
        select_stmt = "SELECT user_password FROM user_info WHERE user_login = ?"
        self.crs.execute(select_stmt, (login,))

        out_hash = self.crs.fetchone()

        if check_hash == out_hash[0]:
            print('Вы вошли')
        else:
            print('Вы ввели неправильный пароль')

network = HashClass()
network.create_table()
network.register()
network.log_in()