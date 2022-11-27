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


def pass_saver(string):
    pass_file = open('passfile.scv', 'w')
    pass_file.write(string)
    pass_file.close()


def pass_extruder():
    pass_file = open('passfile.scv')
    extracted_hash = pass_file.read()
    pass_file.close()
    return extracted_hash


def register():
    user_login = input('Введите логин: ')
    user_password = input('Введите пароль: ')
    pass_hash = sha256(user_login.encode() + user_password.encode()).hexdigest()
    print(f'Получившийся хеш: {pass_hash}')
    pass_saver(pass_hash)


def login():
    user_login = input('Введите логин еще раз для проверки: ')
    user_password = input('Введите пароль еще раз для проверки: ')
    pass_hash = sha256(user_login.encode() + user_password.encode()).hexdigest()
    print(f'Получившийся хеш при проверке: {pass_hash}')
    if pass_extruder() == pass_hash:
        print('Вы ввели правильный пароль')
    else:
        print('Пароль неверный!')


register()
login()
