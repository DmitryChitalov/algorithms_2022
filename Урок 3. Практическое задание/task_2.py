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
from hashlib import sha256
import json

with open('result.json', 'w', encoding='utf-8') as f:
    data = {'user_1': {}}
    data['user_1']['login'] = input('Input your login: ')
    data['user_1']['password'] = sha256(data['user_1']['login'].encode() +
                                        input('Input your password. Remember it: ').encode()).hexdigest()
    print(data['user_1']['password'])
    json.dump(data, f)

with open('result.json', 'r', encoding='utf-8') as f:
    data_json = json.load(f)
    user = input('Your login: ')
    password = sha256(user.encode() + input('Your password: ').encode()).hexdigest()
    if data_json['user_1']['login'] == user and data_json['user_1']['password'] == password:
        print('Welcome!')
    else:
        print('Something wrong...')
