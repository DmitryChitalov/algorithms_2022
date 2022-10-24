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


def hashing_func(pswrd=input("Введите пароль: ")):
    user_hash_dict = {}

    salt = 'my_salt'
    res = hashlib.sha256(salt.encode() + pswrd.encode()).hexdigest()
    user_hash_dict.setdefault('salt', salt)
    user_hash_dict.setdefault('hash', res)
    with open('data.txt', 'w') as outfile:
        json.dump(user_hash_dict, outfile)

    user_auth = input("Введите пароль еще раз для проверки: ")

    with open('data.txt') as json_file:
        data = json.load(json_file)
        auth_salt = data['salt']
        auth_hash = data['hash']
    auth_res = hashlib.sha256(auth_salt.encode() + user_auth.encode()).hexdigest()

    if auth_res == auth_hash:
        return print("Вы ввели правильный пароль")
    else:
        return print("Вы ввели неправильный пароль")


hashing_func()



