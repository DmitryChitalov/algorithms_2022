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
import json

flag = True
login_user = input('Введите имя пользователя: ')
psw_user = input('Введите пароль: ')

salt = uuid4().hex
res = hashlib.sha256(salt.encode() + psw_user.encode()).hexdigest()
print(f'В базе данных хранится строка: {res}')
data = dict()
data[login_user] = (res, salt)
with open('password.json', 'w') as f:
    json.dump(data, f)

with open('password.json') as f_r:
    data_rep = json.load(f_r)

while flag:
    login_user_rep = input('Введите имя пользователя еще раз для проверки: ')
    if login_user_rep not in data_rep.keys():
        print('Пользователь с таким именем отсутствует')
    else:
        psw_rep = input('Введите пароль еще раз для проверки: ')
        res_rep = hashlib.sha256(data_rep[login_user_rep][1].encode() + psw_rep.encode()).hexdigest()
        if data_rep[login_user_rep][0] == res_rep:
            print('Вы ввели правильный пароль')
            flag = False
        else:
            print('Вы ввели неверный пароль')
