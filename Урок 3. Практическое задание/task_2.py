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
import csv
import json
from uuid import uuid4
import hashlib
salt = uuid4().hex


def my_def():
    password = input("Введите пароль: ")
    my_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    print(my_hash)
    with open('password.csv', 'r+', encoding='utf-8') as my_password:
        json.dump(my_hash, my_password, ensure_ascii=False)
    file = open('password.csv', 'r+', encoding='utf-8')
    for i in file:
        password2 = input("Введите пароль еще раз: ")
        my_hash2 = hashlib.sha256(salt.encode() + password2.encode()).hexdigest()
        print(my_hash2)
        test_hash = i.replace('"', '')
        print(test_hash)
        if my_hash2 == test_hash:
            return 'Вы ввели верный пароль'
        else:
            print('Попробуйте еще раз')
            return my_def()
    file.close()

print(my_def())