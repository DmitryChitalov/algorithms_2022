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

"""Создан конект к БД """
con = sqlite3.connect("algoritms_course.db")
cur = con.cursor()
"""В БД подготовлена таблица с 3 столбцами login, password, birthdate и вставлены данные"""

# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE IF not EXISTS users(login PRIMARY KEY, password, birthdate)")

"""Заполнение базы данными пользователей"""
data = [
    ('User1', '0bb8cc3709270272798e3bbe78bb541be60b96158aa32371d9b99496cb998640', '1982-07-11'),
    ('User2', '73660badc3d2c6611760350b8851d86b38048cb9f57e1b9f1990275d01937ac9', '1983-07-11'),
    ('User3', '874242a94476fbd5037064fd088f679cf75d22d89aa81cedd2d8ab8c5ec5880e', '1983-08-11')]

try:
    cur.executemany("INSERT INTO users VALUES(?, ?, ?)", data)
except sqlite3.IntegrityError:
    print('Выпытаетесь вставить в базу данных запись с login, который уже в Базе данных')
con.commit()


"""Выполнение сравнения введенного пароля и пароля в таблице"""


def check_pasword(login: str, password_try: str):
    """Функция принимает в себя логин и введенный пароль.
    Обращается к базе данных для получения даты рождения пользователя.
    Создает хеш из пароля и соли в виде даты рождения, и выводит его как указано в задании.
    Сравнивает полученный хеш с хешем в базе данных. Если хешы не совпадают, функция вызывается в рекурсии"""
    try:
        sql_query = f"SELECT birthdate FROM users WHERE login = '{login}'"
        result = cur.execute(sql_query)
        users_birthdate = result.fetchone()[0]  # С учетом наличия PrimaryKey ответ должен быть только 1
        password_hash = hashlib.sha256(users_birthdate.encode() + password_try.encode()).hexdigest()
        print(password_hash)  # Обязательно выведите созданный хеш
        sql_query = f"SELECT password FROM users WHERE login = '{login}'"
        result = cur.execute(sql_query)
        db_password = result.fetchone()[0]  # С учетом наличия PrimaryKey ответ должен быть только 1
        if db_password == password_hash:
            print('Вы ввели правильный пароль!')
            exit()
        else:
            check_pasword(login, input('Неверно! Введите пароль еще раз для проверки: '))
    except TypeError:
        print(f'Полльзователь с именем {login} не зарегистрирован')
        exit()


user = 'User1'  # Весь скрипт выполняет из под пользователя User1
password = input(f'Введите пароль для пользователя {user}: ')  # Эта запись для заполнения пароля в Базе данных
check_pasword(user, password)
