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


def log_pass():
    """
    Ввод логина и пароля
    """
    user_login = input('Введите логин: ')
    user_pass = input('Введите пароль: ')
    return user_login, user_pass


conn = sqlite3.connect('new_db')
curs = conn.cursor()
curs.executescript("""DROP TABLE IF EXISTS autorisation;
                      CREATE TABLE IF NOT EXISTS autorisation
                      (login varchar(50), 
                       pass_hash varchar(255), 
                       salt varchar(255));""")
login, passwd = log_pass()
salt = uuid4().hex
pass_hash = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
curs.execute("INSERT INTO autorisation values(?, ?, ?)", (login, pass_hash, salt))
print('Пройдите авторизацию.')
login, passwd = log_pass()
curs.execute("""SELECT login, pass_hash, salt
                FROM autorisation""")
result = curs.fetchall()
is_exist = False
j = -1
for i, val in enumerate(result):
    if login in val:
        is_exist = True
        j = i
if is_exist:
    user = result[j]
    pass_hash = hashlib.sha256(user[2].encode() + passwd.encode()).hexdigest()
    if pass_hash == user[1]:
        print('Авторизация прошла успешно')
    else:
        print('Неверный логин или пароль')
else:
    print('Пользователь с таким логином не найден')
conn.close()
