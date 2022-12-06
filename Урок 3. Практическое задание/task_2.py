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
from hashlib import pbkdf2_hmac
from binascii import hexlify
import json


filename = 'database.json'

# Генерация хеш-пароля
def get_hash_password(login, password):
    hash_password = hexlify(pbkdf2_hmac(hash_name='sha256',
                                        password=password.encode('utf-8'),
                                        salt=login.encode('utf-8'),
                                        iterations=1000)
                            ).decode()
    return hash_password

# Запрос пары логин-пароль и преобразование пароля в хеш
def get_user():
    login = input('\tВведите логин: ')
    password = input('\tВведите пароль: ')
    return login, get_hash_password(login, password)

# Проверка существования базы пользователей
if not pathlib.Path(filename).exists():
    print('-> Регистрация:')
    login, hash_password = get_user()
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump({login : hash_password}, file)
    print('-> Вы зарегистрированы!')

# Основное тестирование
flag_dct = {'yes' : '-> Авторизация:', 'no' : '-> Регистрация:'}
with open(filename, 'r+', encoding='utf-8') as file:
    database = json.load(file)
    while True:
        flag = input('\nАвторизация / регистрация (yes / no) --> ')
        print(flag_dct.get(flag, '-> Выход.'))
        if flag not in ('yes', 'no'):
            break
        login, hash_password = get_user()
        if flag == 'yes':
            if database.get(login):
                print(f'\tВ базе данных хранится строка: {database[login]}')
                if database[login] == get_hash_password(login, input('\tВведите пароль еще раз: ')):
                    print('\tВы ввели правильный пароль!')
                else:
                    print('\tВы ввели НЕправильный пароль!')
            else:
                print('-> Пользователь не зарегистрирован!')
        else:
            if database.get(login):
                print('-> Пользователь с указанным логином уже существует!')
            else:
                database[login] = hash_password
                file.seek(0)
                json.dump(database, file)
                print('-> Вы зарегистрированы!')
