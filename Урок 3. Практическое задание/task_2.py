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

pw = input('Введите пароль : ')
salt = uuid4().hex
hash_pw = hashlib.sha256(salt.encode() + pw.encode()).hexdigest()
data = (salt, hash_pw)
with open("data_file.json", "w") as file:
    json.dump(data, file)

pw_check = input('Введите пароль еще раз для проверки: ')

with open("data_file.json", "r") as file:
    data_load = json.load(file)
hash_check = hashlib.sha256(data_load[0].encode() + pw_check.encode()).hexdigest()
if hash_check == data_load[1]:
    print('Пароль введен верно')
else:
    print('Пароль введен неверно')
