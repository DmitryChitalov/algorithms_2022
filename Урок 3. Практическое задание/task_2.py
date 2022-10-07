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


def passwd_hashing(password):
    with open("passwd.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        user_hash = hashlib.sha256(password.encode() + data["salt"].encode()).hexdigest()
        data["hash"] = user_hash
        with open("passwd.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    return user_hash


def check_hash(password):
    with open("passwd.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        user_hash = hashlib.sha256(password.encode() + data["salt"].encode()).hexdigest()
        if user_hash == data["hash"]:
            return "Correct password"
        return "Wrong password"


user_pass = input("Your password, please? >>> ")

print(passwd_hashing(user_pass))

user_auth = input("Your password again, please? >>> ")

print(check_hash(user_auth))
