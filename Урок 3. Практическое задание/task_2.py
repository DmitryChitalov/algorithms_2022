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


def create_db():
    db_con = sqlite3.connect('passwd.db')
    cursor = db_con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS passwd(
    login text,
    passwd text)""")
    db_con.commit()
    return db_con, cursor


def set_pass():
    login, pas = input('Введите логин: '), input('Введите пароль: ')
    pas_hesh = sha256(login.encode() + pas.encode()).hexdigest()
    print("В базе данных хранится строка: ", pas_hesh)
    return login, pas_hesh


def check(hesh, log, pas):

    pas_hesh = sha256(log.encode() + pas.encode()).hexdigest()
    if hesh == pas_hesh:
        print("Пароль верный")
    else:
        print("Пароль не верный")




def main():
    con, cur = create_db()
    cur.execute("""INSERT INTO passwd values (?, ?);""", set_pass())
    con.commit()
    login, pas = input('Введите логин: '), input('Введите пароль: ')
    cur.execute("""SELECT passwd FROM passwd where login = ?""", (login,))
    check(cur.fetchone()[0], login, pas)

if __name__ == '__main__':
    main()
