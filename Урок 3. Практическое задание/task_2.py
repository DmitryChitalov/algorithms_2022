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
import os
import sqlite3

class Pass():
    def __init__(self):
        self.login = ''
        self.psw = ''
        self.salt = ''
        self.hsh = ''
        self.db_filename = 'task_2.db'
        self.conn = ''
        self.currsor = ''

        self.openDb()

    def setPassword(self):
        self.login = input('Укажите логин: ')
        if self.loginDb(self.login):
            self.psw = input('Введите пароль: ')
            self.salt = self.login
            self.hsh = hashlib.sha256(self.psw.encode('utf-8') + self.salt.encode('utf-8')).hexdigest()
            self.conn.executescript(f"INSERT INTO pass (login, salt, hsh) VALUES ('{self.login}', '{self.salt}', '{self.hsh}');")
            print(f'Новый пользователь {self.login} зарегистрирован. Его данные (для проверки примера): ')
            self.viewPassword()

        else:
            print(f'Пользователь {self.login} уже есть. Считанные из базы данных данные пользователя:')
            self.viewPassword()
            self.autorizedDb()

    def viewPassword(self):
        print(f'Введенный пароль: {self.psw}')
        print(f'Сгенерированная соль: {self.salt}')
        print(f'Сгенерированный хеш с солью: {self.hsh}')

    def openDb(self):
        db_exists = not os.path.exists(self.db_filename)
        self.conn = sqlite3.connect(self.db_filename)
        self.cursor = self.conn.cursor()
        if db_exists:
            print('No schema exists.')
            self.conn.executescript(""" 
                CREATE TABLE pass (
	                login text primary key,
	                salt text,
	                hsh text
                ); """)
        else:
            print('DB exists.')

    def viewDb(self):
        self.cursor.execute(f'SELECT * FROM pass;')
        print('В базе данных есть пользователи: ')
        for row in self.cursor.fetchall():
            login, salt, hsh = row
            print(login)

    def loginDb(self, login):
        self.cursor.execute(f"SELECT * FROM pass WHERE login='{login}';")
        l = self.cursor.fetchall()
        for row in l:
            self.login, self.salt, self.hsh = row
        if len(l) > 0:
            return False
        else:
            return True

    def autorizedDb(self):
        psw = input(f'Введите пароль для существующего пользователя {self.login}: ')
        hsh = hashlib.sha256(psw.encode('utf-8') + self.salt.encode('utf-8')).hexdigest()
        if hsh == self.hsh:
            print('Вы ввели правильный пароль')
        else:
            print('Вы ввели не правильный пароль')



p = Pass()
p.setPassword()
p.viewDb()