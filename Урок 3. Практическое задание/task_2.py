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

salt = 'sea_salt'
login = 'user'
password = hashlib.sha256(salt.encode('utf-8') + '123'.encode('utf-8')).hexdigest()
print(password)


data = {login: [password, salt]}
with open("hash_tbl.json", "w") as write_file:
    json.dump(data, write_file)


def pass_checking(n=0):
    with open("hash_tbl.json", "r") as read_file:
        read_data = json.load(read_file)
    check_pass = hashlib.sha256(read_data['user'][1].encode('utf-8') + input('введите пароль: ').encode('utf-8')).hexdigest()
    if check_pass == read_data['user'][0] and n == 1:
        return print('Вы ввели правильный пароль')
    elif check_pass != read_data['user'][0]:
        print('неверный пароль')
        n = 0
        return pass_checking(n)
    else:
        n += 1
        print('Введите пароль еще раз для проверки')
        return pass_checking(n)


pass_checking()





