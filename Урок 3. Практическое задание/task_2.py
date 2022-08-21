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


login = 'User1'
# password = '123'
password = input(f'Введите пароль для пользователя {login}: ')
birthdate = '1982-07-11'
password_hash = hashlib.sha256(login.encode()+password.encode()).hexdigest()


"""Создан конект к БД """
con = sqlite3.connect("algoritms_course.db")
cur = con.cursor()

"""в БД подготовлена таблица с 3 столбцами login, password, birthdate и вставлены данные"""

# cur.execute("DROP TABLE IF EXISTS users")
"""
cur.execute("CREATE TABLE IF not EXISTS users(login PRIMARY KEY, password, birthdate)")
data = [
    ('User1', '449ec036afd1132942a51a0dffad469ec64d042ee421f9e910a0f39ad0081012', '1982-07-11'),
    ('User2', 'c5d7e2513116e20ea5554e60dfd170bb20c50d383aa08fd77bbf3d2174139dcc', '1983-07-11'),
    ('User3', 'ce2b7842122a1c98e3f6cfec1df9dfb41dc79fa70fa45bd84158c2d43515a41f', '1983-08-11')]

try:
    cur.executemany("INSERT INTO users VALUES(?, ?, ?)", data)
except sqlite3.IntegrityError:
    print('Выпытаетесь вставить в базу данных запись с login, который уже в Базе данных')
con.commit()
"""

"""Выполнение сравнения"""
sql_query = f"SELECT password FROM users WHERE login = '{login}'"
res = cur.execute(sql_query)
db_answer = res.fetchone()[0]  # С учетом наличия PrimaryKey ответ должен быть только 1

if db_answer == password_hash:
    print('Вы ввели правильный пароль')
else:
    print('Пароли не совпадают')
