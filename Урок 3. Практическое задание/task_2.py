import sqlite3
import hashlib
from uuid import uuid4
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


def create_bd():
    """Создание тестовой бд"""
    conn = sqlite3.connect('task_2.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   login TEXT,
                   passwd TEXT,
                   salt TEXT
                   );""")
    conn.commit()
    conn.close()


def reg_user(login, passwd):
    """Регистрация пользователя,
    записывает данные в бд"""
    salt = str(uuid4())
    passwd_hash = hashlib.sha256(
        passwd.encode('utf-8') + salt.encode('utf-8')
    ).hexdigest()
    reg_data = (login, passwd_hash, salt)
    conn = sqlite3.connect('task_2.db')
    cur = conn.cursor()
    cur.execute("""INSERT into users(login, passwd, salt)
                    VALUES(?, ?, ?);""", reg_data)
    conn.commit()
    conn.close()


def check_user(login, passwd):
    """Аутентификация пользователя"""
    conn = sqlite3.connect('task_2.db')
    cur = conn.cursor()
    cur.execute("""SELECT passwd, salt FROM users
                   WHERE login = ?""", (login,))
    res = cur.fetchone()
    conn.close()
    try:
        salt = res[1]
        passwd_2 = input(f'В базе хранится хеш {res[1]}\n'
                         f'Введите пароль еще раз для проверки: ')
        if passwd == passwd_2:
            enter_passwd = hashlib.sha256(
                passwd_2.encode('utf-8') + salt.encode('utf-8')
            ).hexdigest()
            if res[0] == enter_passwd:
                print('Пароль введен верно')
            else:
                print('Неверный пароль')
        else:
            print('Неверный пароль')
    except TypeError:
        print('Такого пользователя не существует!')


if __name__ == '__main__':
    create_bd()

    while True:
        answer = input('\nРегистрация - введите reg\n'
                       'Вход - введите log\n'
                       'Завершить работу - введите exit\n'
                       'Выберите действие: ')
        if answer == 'reg':
            reg_user(input('Придумайте логин: '), input('Придумайте пароль: '))
        elif answer == 'log':
            check_user(input('Введите логин: '), input('Введите пароль: '))
            break
        else:
            break

"""Добавил к изначальному варианту блок try except для функции check_user,
так, как sql запрос может вернуть NULL значение или NoneType для питона, забыл
 про эту особенность, исправляюсь, писал Вам в телеграмме про это, 
 надеюсь ничего страшного?"""
