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

passwd = input('Задайте пароль   ')
salt = "простая соль"


def set_pass_hash(pass_1, salt_1):
    passw_hash = hashlib.sha256(salt_1.encode() + pass_1.encode()).hexdigest()
    return passw_hash


pass_hash = set_pass_hash(passwd, salt)

with open("pass_file.json", "w") as pass_file:
    json.dump(pass_hash, pass_file)

print(f'В базе данных хранится строка c хэшем: {pass_hash}')

password_to_check = input('Введите пароль:  ')

with open('pass_file.json', 'r') as openfile:
    pass_stored_hash = json.load(openfile)

pass_to_check_hash = set_pass_hash(password_to_check, salt)

print(f'Хэш пароля для проверки: {pass_to_check_hash}')

if pass_to_check_hash == pass_stored_hash:
    print('Пароль верный')
else:
    print('Пароль неверный')
