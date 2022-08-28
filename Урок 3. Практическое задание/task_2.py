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
from uuid import uuid4
import hashlib
import sqlite3
import os

file = 'db_pass.sqlite'
if os.path.isfile(file):
    print('true')
else:
    open(file, 'a').close()
    print('f')
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE pass_hash (
        id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        login VARCHAR (20) UNIQUE,
        pass  VARCHAR (90),
        salt  VARCHAR (50) 
    );
    """)
    conn.close()


def registration(login, passw):
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    salt = uuid4().hex
    hash_obj = hashlib.sha512(passw.encode('utf-8') + salt.encode('utf-8'))
    # print(hash_obj)
    cursor.execute("""INSERT INTO pass_hash ( login, pass, salt) VALUES
           (:login,:pass,:salt);""", {"login":login, "pass": hash_obj.hexdigest(), "salt": salt})
    conn.commit()
    conn.close()


def check_login(login, registr=None):
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    cursor.execute("select login from pass_hash")
    res = []
    for i in cursor.fetchall():
        res.append(i[0])
    # print(res, login)
    if login in res:
        if registr is None:
            check_pass = input('введите пароль')
            check_password(login, check_pass)
        else:
            print('такой логин существует, выберите другой')
            income()
    else:
        if registr is not None:
            check_pass = input('введите пароль')
            check_pass1 = input('введите пароль ещё раз')
            if check_pass1 == check_pass:
                registration(login, check_pass)
            else:
                print('пароли не совпадают!')
                income()
        else:
            print('такого логина не существует, проверьте себя или пройдите регистрацию')
            income()
    conn.close()


def check_password(login, passw):
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    cursor.execute("select pass, salt from pass_hash where login=:log;", {"log": login})
    results1 = cursor.fetchall()
    # print(results1)
    salt_bd = results1[0][1]
    # print(results1)
    # print(salt_bd)
    # print((hashlib.sha512(passw.encode('utf-8') + salt_bd.encode('utf-8'))).hexdigest())
    if (hashlib.sha512(passw.encode('utf-8') + salt_bd.encode('utf-8'))).hexdigest() == results1[0][0]:
        print(' вы авторизованы')
        conn.close()
    else:
        print('пароль не верен!')
        income()
        conn.close()


def income():
    sost = int(input('добро пожаловать. \nвведите 1 для авторизации, \n2 для регистрации, \n0 для выхода'))
    if sost == 0:
        return
    elif sost == 2:
        check_login(input('введите логин'), True)
    elif sost == 1:
        check_login(input('введите логин'))
    else:
        print('неверная команда!')
        income()


income()

"""
для проверки {логин:пароль} : {'abc':123, '147':147, 'qwerty':123456}
"""
