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

import mysql.connector
from mysql.connector import Error
from hashlib import sha256


def log_in():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    hash_pswd = sha256(f'{login}{password}'.encode()).hexdigest()
    return login, hash_pswd


login, hash_pswd = log_in()
print(hash_pswd)
conn = mysql.connector.connect(host='localhost',
                               database='regist',
                               user='root',
                               password='01021994')
cursor = conn.cursor()
user_log = (login, hash_pswd)
try:
    cursor.execute("insert into users (login, pass) values (%s, %s)", user_log)
except Error:
    print('Такой пользователь уже существует')
else:
    conn.commit()
    pas2 = input('Введите пароль еще раз для проверки: ')
    hash_pswd2 = sha256(f'{login}{pas2}'.encode()).hexdigest()

    cursor.execute("select pass from users where login = %s", (login,))
    result = cursor.fetchone()
    if result[0] == hash_pswd2:
        print(hash_pswd)
        print(result)
        print(hash_pswd2)
        print('Вы ввели правильный пароль')
    else:
        print(hash_pswd)
        print(result)
        print(hash_pswd2)
        print('Вы ввели неправильный пароль')
conn.close()

