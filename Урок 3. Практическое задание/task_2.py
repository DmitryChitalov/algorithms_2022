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
from os import path
import json


USER_INFO_FILENAME = 'user_info.json'

username = 'user_1'
password = hashlib.sha256((username+'pass123').encode()).hexdigest()
userinfo = {
    'salt': username,
    'password': password
}
with open(USER_INFO_FILENAME, 'w', ) as f:
    json.dump(userinfo, f)

user = input('Введите имя пользователя: ')
password_check_1 = input('Введите пароль: ')

with open(USER_INFO_FILENAME, 'r', ) as f:
    my_salt = json.load(f)['salt']

print(f'В базе данных хранится строка: {hashlib.sha256((user+password_check_1).encode()).hexdigest()}')

password_check_2 = input('Введите пароль еще раз для проверки: ')

with open(USER_INFO_FILENAME, 'r', ) as f:
    my_pass = json.load(f)['password']

if hashlib.sha256((user+password_check_2).encode()).hexdigest() == my_pass:
    print('Вы ввели правильный пароль')
else:
    print('Пароль не верный')
