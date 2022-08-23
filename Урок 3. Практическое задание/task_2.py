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
from pathlib import Path
import hashlib


def make_database():
    try:
        sql_connection = sqlite3.Connection('database.db')
        cursor = sql_connection.cursor()

        ddl_script = """
            DROP TABLE IF EXISTS users;
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                login VARCHAR NOT NULL,
                pass_hash VARCHAR(64) NOT NULL,
            UNIQUE (login)
            );
        """

        cursor.executescript(ddl_script)
        cursor.close()
    except sqlite3.Error:
        raise
    finally:
        if sql_connection:
            sql_connection.close()


def db_init():
    db_path = Path.cwd() / 'database.db'
    if not db_path.exists():
        make_database()


def check_login(login):
    try:
        sql_connection = sqlite3.Connection('database.db')
        cursor = sql_connection.cursor()

        cursor.execute('SELECT login FROM users WHERE login = ?', [login])
        if cursor.fetchone() is not None:
            return True
        return False

    except sqlite3.Error:
        raise
    finally:
        if sql_connection:
            sql_connection.close()


def check_passwd(passwd, login):
    try:
        sql_connection = sqlite3.Connection('database.db')
        cursor = sql_connection.cursor()

        pass_encoded = (passwd + login).encode(encoding='utf-8')
        pass_hash = hashlib.sha256(pass_encoded).hexdigest()

        cursor.execute('SELECT pass_hash FROM users WHERE login = ?', [login])
        db_hash = cursor.fetchone()[0]

        if db_hash == pass_hash:
            return True
        return False

    except sqlite3.Error:
        raise
    finally:
        if sql_connection:
            sql_connection.close()


def add_user(login, passwd):
    try:
        sql_connection = sqlite3.Connection('database.db')
        cursor = sql_connection.cursor()

        pass_encoded = (passwd + login).encode(encoding='utf-8')
        pass_hash = hashlib.sha256(pass_encoded).hexdigest()

        cursor.execute('INSERT INTO users (login, pass_hash) VALUES (?,?)', (login, pass_hash))
        sql_connection.commit()

    except sqlite3.Error:
        raise
    finally:
        if sql_connection:
            sql_connection.close()


def main():
    try:
        db_init()

        while True:
            user_login = input('Введите логин: ').lower()
            if user_login == '':
                print('Логин не может быть пустым!')
            else:
                break

        while True:
            user_passwd = input('Введите пароль: ')
            if user_passwd == '':
                print('Пароль не может быть пустым!')
            else:
                break

        if not check_login(user_login):
            print('Пользователь не найден!')
            while True:
                answer = input(f'Зарегистрировать пользователя {user_login} как нового? (y/n): ')
                if answer == 'y':
                    add_user(user_login, user_passwd)
                    print(f'Пользователь {user_login} зарегистрирован')
                    return
                elif answer == 'n':
                    return
                else:
                    print('Введено неверное значение!')

        if check_passwd(user_passwd, user_login):
            print(f'Пользователь {user_login} авторизован')
        else:
            print('Введен неверный пароль!')

    except sqlite3.Error as e:
        print(f'Ошибка SQLite: {e}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
