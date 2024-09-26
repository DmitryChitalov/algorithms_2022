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
import sqlite3
from uuid import uuid4

"""
Создание таблицы:
CREATE TABLE passwords (
	hash TEXT NOT NULL,
	salt TEXT NOT NULL
);
"""


def db_save_password(hash, salt):
    conn = sqlite3.connect('passwords.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO passwords (hash, salt)
        VALUES ('{hash}', '{salt}')
    """)
    conn.commit()
    conn.close()


def db_get_password():
    conn = sqlite3.connect('passwords.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT hash, salt
        FROM passwords
        LIMIT 1 
    """)
    password_hash, salt = cursor.fetchone()
    conn.close()
    return password_hash, salt


def db_remove_password():
    conn = sqlite3.connect('passwords.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"""
        DELETE
        FROM passwords
    """)
    conn.commit()
    conn.close()


def create_password():
    password_string = input('Придумайте новый пароль: ')
    salt = uuid4().hex
    password_hash = hashlib.sha256(salt.encode() + password_string.encode()).hexdigest()
    print(password_hash)
    db_save_password(password_hash, salt)


def check_password():
    entered_password_string = input('Введите ваш пароль: ')
    password_hash, salt = db_get_password()
    entered_password_hash = hashlib.sha256(salt.encode() + entered_password_string.encode()).hexdigest()
    print(entered_password_hash)
    return entered_password_hash == password_hash


if __name__ == '__main__':
    create_password()
    print(check_password())
    db_remove_password()
