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


class BaseSql:
    conn = None
    cursor = None

    def __init__(self, path):
        try:
            self.conn = sqlite3.connect(path)
        except sqlite3.DatabaseError as err:
            print("Error: ", err)
        else:
            self.cursor = self.conn.cursor()  # курсор лучше переопределять каждый раз или можно использовать один?

    def close(self):
        try:
            self.conn.close()
        except sqlite3.DatabaseError as err:
            print("Error: ", err)

    def truncate(self, table_ref):
        try:
            self.cursor.execute(f'delete from {table_ref}')
        except sqlite3.DatabaseError as err:
            print("Error: ", err)
        else:
            self.conn.commit()

    def insert_users(self, dict):
        for key, value in dict.items():
            try:
                self.cursor.execute(f'insert into users values (\"{key}\", \"{value}\")')
            except sqlite3.DatabaseError as err:
                print("Error: ", err)
            else:
                self.conn.commit()

    def select_users(self, login):
        try:
            self.cursor.execute(f'select * from users where login = (\"{login}\")')
            return self.cursor.fetchall()
        except sqlite3.DatabaseError as err:
            print("Error: ", err)


base = BaseSql('pass.db')
base.truncate('users')
dct = {'Иванов': 'lakjsdflkj3', 'Петров': 'asdfasdf3'}
base.insert_users(dct)

while True:
    login = input('Введите пользователя, для выхода введите 0: ')
    if login == '0':
        break
    pass_user = input('Введите пароль: ')

    res = base.select_users(login)
    if len(res) == 0:
        print(f'Нет пользователя {login} добавим в базу.')
        hex = hashlib.sha256(login.encode() + pass_user.encode()).hexdigest()
        base.insert_users({login: hex})
        print(f'Пользователь добавлен: {base.select_users(login)}')
        print(f' Еще раз расчитаем хеш {hashlib.sha256(login.encode() + pass_user.encode()).hexdigest()}')

    else:
        print(f'Пользователь {login} есть в базе. Хеш: {res[0][1]}')
        rep = input('Введите пароль еще раз для проверки: ')
        hex_rep = hashlib.sha256(login.encode() + rep.encode()).hexdigest()
        if res[0][1] == hex_rep:
            print(f'Вы ввели правильный пароль.')
        else:
            print(f'Вы ввели неправильный пароль.')

base.close()
