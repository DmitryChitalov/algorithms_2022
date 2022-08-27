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

import hashlib
from uuid import uuid4

password = input("Введите пароль: ")

salt = uuid4().hex


def hash_pass(data, sal):
    res = hashlib.sha256(sal.encode() + data.encode()).hexdigest()
    print(f'В базе данных хранится строка: {res}')
    pass_2 = input("Введите пароль еще раз для проверки: ")
    exp_res = hashlib.sha256(sal.encode() + pass_2.encode()).hexdigest()
    if exp_res == res:
        return res, print('Вы ввели правильный пароль')
    else:
        return print("Неверный пароль")


hash_password = hash_pass(password, salt)
