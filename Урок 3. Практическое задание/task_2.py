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
from uuid import uuid4
from hashlib import pbkdf2_hmac


def hash_passwd(password: str, salt=uuid4().bytes):
    pass_hash = pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return pass_hash, salt


class PasswordChecker:

    def __init__(self):
        self.login = ''
        self.connection = sqlite3.connect('passwd.sqlite')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS passwd(id INT PRIMARY KEY, login TEXT UNIQUE, hash TEXT, salt TEXT);"""
        )
        self.connection.commit()

    def check_passwd(self, password: str):
        self.cursor.execute('select hash, salt from passwd where login = ?', [self.login])
        rec = self.cursor.fetchone()
        original_hash = rec[0]
        salt = rec[1]
        input_hash, _ = hash_passwd(password, bytes.fromhex(salt))
        return input_hash == bytes.fromhex(original_hash)

    def close_connection(self):
        if (self.connection):
            self.cursor.close()

    def find_user(self, login: str, pass_hash: bytes, salt: bytes):
        self.login = login
        cursor = self.connection.cursor()
        row = cursor.execute('select hash, salt from passwd where login = ?', [login])
        if row.fetchone() is None:
            cursor.execute(
                'insert into passwd (login, hash, salt) values(?, ?, ?)',
                [login, pass_hash.hex(), salt.hex()]
            )
        else:
            cursor.execute(
                'update passwd set hash = ?, salt = ? where login = ?',
                [pass_hash.hex(), salt.hex(), login]
            )
        self.connection.commit()


if __name__ == '__main__':
    pass_checker = PasswordChecker()
    login = input('Имя пользователя: ')
    pass_hash, salt = hash_passwd(input('Введите пароль: '))
    try:
        pass_checker.find_user(login, pass_hash, salt)
        new_pass = input('Введите пароль для проверки: ')
        print('Верно' if pass_checker.check_passwd(new_pass) else 'Не верно')

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        pass_checker.close_connection()
