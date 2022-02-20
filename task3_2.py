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


import pathlib
import hashlib
import json

filename = 'db.json'


def get_user():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    hash_password = hashlib.sha512(login.encode()+password.encode()).hexdigest()
    return login, hash_password


# Создание файла json
if not pathlib.Path(filename).exists():
    print('-> Регистрация:')
    login, hash_password = get_user()
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump({login: hash_password}, file)
    print('-> Вы зарегистрированы!')


# Авторизация и регистрация
with open(filename, 'r+', encoding='utf-8') as file:
    database = json.load(file)  # метод считывает файл в формате JSON и возвращает объекты Python
    while True:
        try:
            ex = int(input('Для выхода введите ноль, для продолжения 1: '))
            res = 7 / ex
        except ZeroDivisionError:
            break
        login, hash_password = get_user()
        try:  # если login  существует в json-файле, то выводим соот-е сообщение
            if database[login]:
                print('Пользователь с указанным логином уже существует!')
        except KeyError:  # если login  не находится в json-файле, то записываем в него нового пользователя
            database[login] = hash_password
            file.seek(0)  # осуществить смещение. 0 — от начала файла
            json.dump(database, file)
            print('-> Вы зарегистрированы!')
        if database.get(login):
            print(f'\tВ базе данных хранится строка: {database[login]}')
            if database[login] == hashlib.sha512(login.encode()+input('Введите пароль: ').encode()).hexdigest():
                print('\tВы ввели правильный пароль!')
            else:
                print('\tВы ввели неверный пароль!')
