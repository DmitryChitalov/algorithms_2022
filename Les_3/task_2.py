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


from getpass import getpass
from mysql.connector import connect, Error
from hashlib import sha256
import uuid


def hash_password(password, pepper):
    return sha256(pepper.encode('utf-8') + password.encode('utf-8')).hexdigest()


def check_password(hash_password, user_password, pepper):
    return hash_password == sha256(pepper.encode('utf-8') + user_password.encode('utf-8')).hexdigest()


def insert_to_database(hash_pass, salt):
    insert_passwords = """
            INSERT INTO passwords (hash, salt)
            VALUES ( %s, %s )"""
    with connection.cursor() as cursor:
        data_insert = [(hash_pass, salt)]
        cursor.executemany(insert_passwords, data_insert)
        connection.commit()


try:
    with connect(
            host="localhost",
            user=input("Имя пользователя: "),
            password=getpass("Пароль: "),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE DATABASE IF NOT EXISTS passwords_database""")
            cursor.execute("""USE passwords_database""")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS passwords (
                id SERIAL PRIMARY KEY,
                hash VARCHAR(255) COMMENT 'Хэш пароля',
                salt VARCHAR(255));
                """)
        first_password = input('Введите пароль: ')
        salt = uuid.uuid4().hex
        hashed_password = hash_password(first_password, salt)
        print('Хэш, отправленный в базу данных: ', hashed_password)
        insert_to_database(hashed_password, salt)
        second_password = input('Введите пароль еще раз для проверки: ')
        if check_password(hashed_password, second_password, salt):
            print('Вы ввели правильный пароль')
        else:
            print('Пароли не совпадают')
except Error as e:
    print(e)
