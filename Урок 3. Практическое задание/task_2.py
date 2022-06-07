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


def hash_pass(password):
    pass_hash = hashlib.sha256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    return pass_hash


def read_file(ch_pass, check):
    with open('pass_hash.csv', 'r', encoding='utf-8') as f:
        if check == 'read_file':
            print(f'В базе данных хранится строка: {f.read()}.')
        else:
            if f.read() == ch_pass:
                print('Вы ввели правильный пароль.')
            else:
                print('Вы ввели неверный пароль.')


salt = uuid4().hex
user_pass = input('Введите пароль: ')
with open('pass_hash.csv', 'w', encoding='utf-8') as file:
    file.write(hash_pass(user_pass))
read_file(hash_pass(user_pass), 'read_file')
check_pass = input('Введите пароль еще раз для проверки: ')
hash_pass(check_pass)
read_file(hash_pass(check_pass), '')
