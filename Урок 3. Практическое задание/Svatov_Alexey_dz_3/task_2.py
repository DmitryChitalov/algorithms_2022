"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
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
import random
import csv


def input_password():
    raw_password = input('Введите пароль: ').encode()
    return raw_password


def hash_password(raw_password):
    raw_salt = f'test'.encode()
    hash_password = hashlib.sha256(raw_password + raw_salt).hexdigest()
    return {hash_password: raw_salt}


def check_password(file_name):
    with open(file_name, 'r') as csv_pw_salt:
        checking_password = hashlib.sha256(input_password() + b'test').hexdigest()
        for row in csv_pw_salt:
            if checking_password in row[:row.find(',')]:
                return print('Вы ввели правильный пароль')
                break


def add_hash_csv(file_name, new_row):
    with open(file_name, 'a') as csv_pw_salt:
        writer = csv.writer(csv_pw_salt)
        writer.writerow(*new_row.items())


add_hash_csv('pw_salt.csv', hash_password(input_password()))
check_password('pw_salt.csv')
