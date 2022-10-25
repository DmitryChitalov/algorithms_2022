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


    def hashing(salt, passwd):
        res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
        return res

    salt = 'my_salt'
    result = hashing(salt, pswrd)
    user_hash_dict.setdefault('salt', salt)
    user_hash_dict.setdefault('hash', result)
    with open('data.txt', 'w') as outfile:
        json.dump(user_hash_dict, outfile)

    user_auth = input("Введите пароль еще раз для проверки: ")

    with open('data.txt') as json_file:
        data = json.load(json_file)
        auth_salt = data['salt']
        auth_hash = data['hash']
    result = hashing(auth_salt, user_auth)

    if result == auth_hash:
        return print("Вы ввели правильный пароль.")
    else:
        return print("Вы ввели неправильный пароль.")


hashing_func()



