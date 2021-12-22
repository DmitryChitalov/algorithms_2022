"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
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

try:
    with open('users.json', 'x', encoding='utf-8') as f:
        users = {}
        json.dump(users, f)

except FileExistsError:
    pass

finally:
    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)

user = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

if user in users:
    new_key = hashlib.sha256(users[user][0].encode() + password.encode()).hexdigest()

else:
    salt = uuid4().hex
    key = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    print(f'В базе данных хранится строка: {key}')
    users[user] = [salt, key]
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f)

    new_password = input('Введите пароль еще раз для проверки: ')
    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)

    new_key = hashlib.sha256(users[user][0].encode() + new_password.encode()).hexdigest()

if new_key == users[user][1]:
    print('Вы ввели правильный пароль')
else:
    print('Пароль неправильный')
