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

salt = 'u_salt'


def get_hash(passwd):
    return hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()


passwd = input('Введите пароль: ')
passwd_hash = get_hash(passwd)
print(f'В базе данных хранится строка: {passwd_hash}')
data = {salt: passwd_hash}
with open('task2_data.json', 'w') as f:
    json.dump(data, f)

check_passwd = input('Введите пароль еще раз для проверки: ')
check_passwd_hash = get_hash(check_passwd)
with open('task2_data.json', 'r') as f:
    data = json.load(f)
    if data[salt] == check_passwd_hash:
        print('Вы ввели верный пароль')
    else:
        print('Пароли не совпадают, это не вы')
