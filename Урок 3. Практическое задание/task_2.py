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


def hashing_pass(password):
    salt = 'sugar'
    res = hashlib.sha256((password + salt).encode()).hexdigest()
    return res


def save_pass(password):
    salt = 'sugar'
    password = hashing_pass(password)
    print(f'В базе данных хранится строка: {password}')
    with open('hash_log.csv', 'w') as f:
        f.write(password)


def valid_check(password):
    with open('hash_log.csv', 'r') as f:
        saved_hash = f.readline()
    if hashing_pass(password) == saved_hash:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели не правильный пароль')




user_input = input('Введите пароль: ')
save_pass(user_input)
check = input('Введите пароль еще раз для проверки: ')
valid_check(check)
