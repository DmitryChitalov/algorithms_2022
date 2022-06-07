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
hash_dict = {}


def get_hash():
    login = input('Enter your login to register: ')
    password = input('Enter your password to register: ')
    pass_hash = sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest()
    return login, pass_hash


def register():
    login, reg_hash = get_hash()
    hash_dict[login] = reg_hash
    return f'Registration completed successfully, your hash: {reg_hash}'


def log_in(login, password):
    if login in hash_dict \
            and hash_dict[login] == sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest():
        return 'You are logged in'
    else:
        return "You've entered wrong login or password"


print(register())
print(log_in(input('Enter your login to log-in: '), input('Enter your password to log-in: ')))
