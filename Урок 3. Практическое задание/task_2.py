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

import csv
import os
from binascii import hexlify
from uuid import uuid4
from hashlib import pbkdf2_hmac
from os import stat

def get_key():
    login = input('Введите логин пользователя: ')
    passw = input('Введите пароль: ')
    res_hash = hexlify(
        pbkdf2_hmac(hash_name='sha256',
                    password=passw.encode('utf-8'),
                    salt=login.encode('utf-8'),             # соль вычисляется из логина всегда при выполнении данной функции (при регистрации / проверке и т.д.)
                    iterations=100)
    )
    res_hash.decode('utf-8')
    return login, res_hash

def register():
    login, key = get_key()
    with open("data.csv", 'a+', newline='') as f:                   # не работает чтение в режиме a+
        writer = csv.DictWriter(f, fieldnames=['login', 'key'])
        if stat("data.csv").st_size == 0:
            writer.writeheader()
        is_reg = False

    with open("data.csv", 'r', newline='') as f:
        reader = csv.DictReader(f)
        print(str(login))
        for row in reader:
            if row['login'] == str(login):
                print('Пользователь уже зарегистрирован.')
                is_reg = True

    if is_reg == False:
        with open("data.csv", 'a+', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['login', 'key'])  # дублирование кода изза того , что не работает а+
            writer.writerow({'login': login, 'key': key})
            print('Вы успешно зарегистрированы')

    f.close()


def check():
    login, check_key = get_key()
    with open("data.csv", 'r', newline='') as f:
        reader = csv.DictReader(f)
        is_reg = False
        for row in reader:
            if row['login'] == str(login):
                is_reg = True
                if row['key'] == str(check_key):
                    print('Вы успешно вошли в систему.')
                else:
                    print('Неверный пароль')
        if is_reg == False:
            print('Пользователь не зарегистрирован.')


mod = 1
while mod != 0:
    mod = int(input('Введите - 1  для регистрации или 2 - для входа в систему, для выхода - 0: '))
    if mod == 1:
        register()
    elif mod == 2:
        check()
    elif mod == 0:
        print('Выход')
    else:
        print('Неверный ввод.')