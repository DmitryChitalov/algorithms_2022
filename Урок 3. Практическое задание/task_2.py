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

"""
Прошу строго не судит данный код, это мой первы опыт взаимодействия с БД при помощи Питоши)
Алгоритм создает БД mysql с единственной таблицей users, в которой 3 колонки: id, login, password_hash.
При создании хеша пароля, "солил" при помощи логина. Данный код можно дорабатывать безконечно, проводить кучу 
проверок и сравнений, но надо вовремя останавливаться)) Поставленную зачачу код решает!
"""

from mysql.connector import connect, Error
import hashlib


def query_mysql_select(query_script):
    try:
        with connect(host="localhost", user='root', password='drifting69', ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query_script)
                result = cursor.fetchall()
                return result
    except Error as e:
        print(e)


def query_mysql_transact(query_script):
    try:
        with connect(host="localhost", user='root', password='drifting69', ) as connection:
            with connection.cursor() as cursor:
                for el in query_script:
                    cursor.execute(el)
                connection.commit()
    except Error as e:
        print(e)


def create_db():
    db_drop = 'DROP DATABASE IF EXISTS test_hm'
    db_create = 'CREATE DATABASE test_hm'
    db_use = 'USE test_hm'
    db_table_create = """
    CREATE TABLE users (
        id SERIAL PRIMARY KEY, 
        login VARCHAR(250) UNIQUE,
        password_hash VARCHAR(250)
    )"""
    db_init_command = [db_drop, db_create, db_use, db_table_create]
    query_mysql_transact(db_init_command)


def show_db():
    db_show = 'SELECT id, login, password_hash FROM test_hm.users'
    result = query_mysql_select(db_show)
    for el in result:
        print(el)


def create_user():
    print('Создание пользователя')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    user_hash = hashlib.sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest()
    query_insert = f"INSERT INTO test_hm.users (login, password_hash) VALUES ('{login}', '{user_hash}')"
    query_mysql_transact([query_insert])


def autorize():
    print('Авторизация пользователя.')
    login = input('Введите имя пользователя: ')
    # Вынимаем из БД хеш пароля
    query_select = f"SELECT password_hash FROM test_hm.users WHERE login = '{login}'"
    from_db_hash = query_mysql_select(query_select)
    password = input('Введите пароль: ')
    # Вычисляем хеш по введенному логину и паролю
    user_hash = hashlib.sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest()
    print('Авторизация пройденна !') if from_db_hash[0][0] == user_hash else \
        print('Непраильное имя пользователя или пароль!')


# Создадим БД:
create_db()
# Создадим нового пользователя
create_user()
create_user()
create_user()
# Прочитаем созданную таблицу users
show_db()
autorize()
