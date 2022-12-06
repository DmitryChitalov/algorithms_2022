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
import hashlib
import json


def get_hash():   #запросил логин и пароль, вычислил хэш(соль логин, пароль password, солёный пароль key
    login = input('Введите логин: ')
    passwd = input('Введите пароль: ')
    key = hashlib.sha256(login.encode() + passwd.encode()).hexdigest()
    return login, key


def create():
    password = {}
    FILENAME = 'password.json'
    login, reg_hash = get_hash()
    with open(FILENAME, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        if data[login]['password'] == reg_hash:
            print("Вы уже есть в базе, выполните вход.")
            check()
        else:
            password[login] = {'password': reg_hash}
            with open(FILENAME, 'r+', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    data[login] = {'password': reg_hash}
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                except json.JSONDecodeError:
                    json.dump(password, file, ensure_ascii=False, indent=4)



def check():
    try:
        login, reg_hash = get_hash()
        FILENAME = 'password.json'
        with open(FILENAME, 'r+', encoding='utf-8') as file:
            data = json.load(file)
        if reg_hash == data[login]['password']:
            print('Вы авторизованы')
        else:
            print('неверный логин или пароль')
    except KeyError:
        print('неверный логин или пароль')



"""логин user1 пароль qwerty, (user2, 123), (user3, 12345)"""

while True:
    choose = input('создать/проверить: ')
    if choose in 'создать':
        create()
        print('создание')
    elif choose in 'проверить':
        print('проверка')
        check()











