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

from hashlib import sha256
import json

salt = input("Введите логин: ")
password = input("Введите пароль: ")


def check_password(password_1, salt_1):
    generation_password = sha256(salt_1.encode() + password_1.encode()).hexdigest()
    print(f"В базе данных храниться строка: {generation_password}")
    salt_2 = input("Введите логин для авторизации: ")
    password_2 = input("Введите пароль еще раз для проверки: ")
    check_password_2 = sha256(salt_2.encode() + password_2.encode()).hexdigest()
    if generation_password == check_password_2:
        return generation_password, print("Вы ввели правильный пароль")
    else:
        return print("Неверный пароль")


hash_password = check_password(password, salt)

with open("password_file.json", "w") as outfile:
    json.dump(hash_password, outfile)
