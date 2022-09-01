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

from hashlib import sha256
from peewee import *

conn = SqliteDatabase('py_hash.db')


class Logs(Model):
    id = AutoField(column_name='id')
    login = CharField(column_name='Login', unique=True)
    password_hash = CharField(column_name='Password_hash')

    class Meta:
        database = conn


def do_hash(salt, password):
    return sha256(salt.encode() + password.encode()).hexdigest()


def registration():
    log = input('Введите логин: ')
    try:
        Logs.get(Logs.login == log)
        print('Вы ввели уже существующий логин, попробуйте ещё раз. ')
    except DoesNotExist:
        passwd_hash = do_hash(log, input('Введите пароль: '))
        Logs.create(login=log, password_hash=passwd_hash)
        print('Регистрация прошла успешно! ')


def authorization():
    try:
        log = input('Введите логин: ')
        user = Logs.get(Logs.login == log)
        passwd_hash = do_hash(log, input('Введите пароль: '))
        if passwd_hash == user.password_hash:
            print('Авторизация прошла успешно!')
        else:
            print('Пароль неверен')
    except DoesNotExist:
        print('Пользователь с таким логином не зарегистрирован, попробуйте ещё раз ')


def main(answer):
    if answer == '1':
        registration()
    else:
        authorization()


if __name__ == '__main__':
    cursor = conn.cursor()
    Logs.create_table()
    # query = Logs.delete()
    # query.execute()
    while True:
        answ = input('Регистрация - 1 или авторизация - 2 ?\n'
                     'Для выхода - 0\n')
        if answ == '0':
            break
        main(answ)
    conn.close()
