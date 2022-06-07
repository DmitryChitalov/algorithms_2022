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
import json
from uuid import uuid4

def registration():
    salt = uuid4().hex
    passwd = input('Введите пароль: ')
    hash_passwd = sha256(salt.encode() + passwd.encode()).hexdigest()
    user_data = salt, hash_passwd
    return user_data

def data_writing(w):
    with open('users.json', 'w', encoding='utf-8') as user:
        json.dump(reg_user, user)

def data_reading():
    with open('users.json', 'r', encoding='utf-8') as user:
        user_data_1 = json.load(user)
        return user_data_1

def identity():
    pas = input('Введите пароль еще раз для проверки: ')
    hash_pass = data_reading()
    password_validation  = sha256(hash_pass[0].encode() + pas.encode()).hexdigest()
    if password_validation == reg_user[1]:
        print('Вы ввели правильный пароль')
    else:
        print("Вы ввели не правильный пароль")


reg_user = registration()

# функцию создания хэша пароля вызываем в функции записи
data_writing(reg_user)
data_reading()
identity()

