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

import json
import hashlib

def enter_the_password():
    password = input('Придумайте пароль - ')
    password_2 = input('Повторите пароль - ')
    if password == password_2:
        return password
    else:
        print('Пароли не совпадают')
        return enter_the_password()

def writing_database(data, login, password):
    data[login] = (hashlib.sha256(password.encode() + login.encode())).hexdigest()
    with open('login_password.json', 'w') as f:
        json.dump(data, f)

def password_verification(data, login, count=1):
    password = (hashlib.sha256(input('Введите ваш пароль - ').encode() + login.encode())).hexdigest()
    if count > 6:
        return 'Количество попыток истекло'
    elif data[login] == password:
        return 'Вход разрешен'
    else:
        print(f'Попытка {count}. Повторите попытку')
        return password_verification(data, login, count+1)

login = input('Введите ваш логин - ')
with open('login_password.json', 'r') as f:
    data = json.load(f)
if login not in data:
    writing_database(data, login, enter_the_password())
else:
    print(password_verification(data, login))
