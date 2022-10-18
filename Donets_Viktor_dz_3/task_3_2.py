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

from sqlite3 import connect, OperationalError, IntegrityError


class HashClass:
    def __init__(self):
        self.db = 'test.sqlite'
        self.conn = connect(self.db)
        self.cursor = self.conn.cursor()


    def create_table(self):
        create_tbl = "CREATE TABLE users (user_login varchar(255)" \
                      "unique, user_password varchar(255));"
        try:
            self.cursor.execute(create_tbl)
        except OperationalError:
            print('Таблица существует')
        else:
            self.conn.commit()


    @staticmethod
    def get_hash():
        login = input('Введите Ваш login: ')
        password = input('Введите Ваш password: ')
        hash_object = sha256(login.encode() + password.encode()).hexdigest()
        return login, hash_object


    def registration(self):
        login, registration_hash = self.get_hash()
        insert_user = "INSERT INTO users (user_login, user_password)" \
                      "VALUES (?, ?)"
        user_info = (login, registration_hash)
        try:
            self.cursor.execute(insert_user, user_info)
        except IntegrityError:
            print('Ваш login и password существует')
        else:
            self.conn.commit()
            print('Вы, зарегистрированы')


    def account_login(self):
        login, check_hash = self.get_hash()
        select_user = "SELECT user_password FROM users " \
                      "WHERE user_login = ?"
        self.cursor.execute(select_user, (login,))
        out_hash = self.cursor.fetchone()
        if check_hash == out_hash[0]:
            print('Вы, вошли')
        else:
            print('Вы, ввели не правильный пароль!!!')


results = HashClass()
results.create_table()
results.registration()
results.account_login()