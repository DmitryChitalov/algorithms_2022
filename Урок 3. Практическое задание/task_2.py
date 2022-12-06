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
import json


def create():
    password = {}
    FILENAME = 'password.json'
    login = input('введите логин: ')
    pass_input = input('введите пароль: ')
    salt = uuid4().hex
    key = hashlib.sha256(salt.encode() + pass_input.encode()).hexdigest()
    storage = salt + key
    password[login] = {'password': storage}
    with open(FILENAME, 'r+', encoding='utf-8') as file:
        try:
            data = json.load(file)
            data[login] = {'password': storage}
            with open(FILENAME, 'r+', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except json.JSONDecodeError:
            json.dump(password, file, ensure_ascii=False, indent=4)



def check():
    try:
        login = input('введите логин: ')
        FILENAME = 'password.json'
        with open(FILENAME, 'r+', encoding='utf-8') as file:
            data = json.load(file)
        pass_input = input('введите пароль: ')
        salt = data[login]['password'][:32]
        key = hashlib.sha256(salt.encode() + pass_input.encode()).hexdigest()
        if key == data[login]['password'][32:]:
            print('Вы авторизованы')
        else:
            print('неверный логин или пароль')
    except KeyError:
        print('неверный логин или пароль')


"""логин user1 пароль qwerty, (user2, 123), (user3, 12345)"""

while True:
    choose = input('создать/проверить')
    if choose == 'создать':
        create()
    elif choose == 'проверить':
        check()











