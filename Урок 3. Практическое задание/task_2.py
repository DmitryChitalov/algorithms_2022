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


def hash_passwd(password):
    salt = uuid4().bytes
    pass_hash = pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return {'pass_hash': pass_hash, 'salt': salt}


def check_passwd(password, s_hash):
    pass_hash = pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(s_hash['salt']), 100000)
    if pass_hash == bytes.fromhex(s_hash['pass_hash']):
        return True
    else:
        return False


if __name__ == '__main__':
    login = input('Имя пользователя: ')
    salt_hash = hash_passwd(input('Введите пароль: '))
    print(f"Хеш пароля: {salt_hash['pass_hash'].hex()}")
    try:
        sqlite_connection = sqlite3.connect('passwd.sqlite')
        cursor = sqlite_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS passwd(
                          id INT PRIMARY KEY, login TEXT UNIQUE, hash TEXT, salt TEXT);
                        """)
        sqlite_connection.commit()
        row = cursor.execute('select hash, salt from passwd where login = ?', [login])
        if row.fetchone() is None:
            cursor.execute('insert into passwd (login, hash, salt) values(?, ?, ?)',
                           [login, salt_hash['pass_hash'].hex(), salt_hash['salt'].hex()])
        else:
            cursor.execute('update passwd set hash = ?, salt = ? where login = ?',
                           [salt_hash['pass_hash'].hex(), salt_hash['salt'].hex(), login])
        sqlite_connection.commit()
        new_pass = input('Введите пароль ещё раз: ')
        cursor.execute('select hash, salt from passwd where login = ?', [login])
        rec = cursor.fetchone()
        print(rec)
        salt_hash['pass_hash'] = rec[0]
        salt_hash['salt'] = rec[1]
        if check_passwd(new_pass, salt_hash):
            print('Пароли совпадают')
        else:
            print('Пароли не совпадают')

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

