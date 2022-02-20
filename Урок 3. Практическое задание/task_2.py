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
from hashlib import sha256
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

def create_table(con):
    cursor = con.cursor()
    cursor.execute("CREATE TABLE user_info (user_login varchar(255), user_password varchar(255))")
    con.commit()

def get_hash():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    hash_obj = sha256(login.encode() + password.encode()).hexdigest()
    return login, hash_obj

def reg (con):
    login, reg_hash = get_hash()
    vel = (login, reg_hash)
    cursorObj = con.cursor()
    cursorObj.execute ("INSERT INTO user_info (user_login, user_password) VALUES (?, ?)" , vel)
    con.commit()


def log_in(con):

    login, check_hash = get_hash()
    cursorObj = con.cursor()
    sql_select_query = """SELECT user_password FROM user_info WHERE user_login = ?"""
    cursorObj.execute(sql_select_query, (login,))
    out_hash = cursorObj.fetchall()
    if check_hash == out_hash[0][0]:
        print('это Вы!')
    else:
        print("Вы ввели неверный пароль или еще не регались")


con = sql_connection()
# create_table(con)
# reg (con)
log_in(con)