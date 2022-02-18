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
from uuid import uuid4
import json


salt = uuid4().hex
inf_dict = {}


def write_password(login=input("Введите логин: "), passwrd=input("Введите пароль: ")):
    res = hashlib.sha256(salt.encode() + passwrd.encode()).hexdigest()
    password_digest = res
    inf_dict[login] = password_digest
    with open("psswrd.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(inf_dict))
    return login


def same_or_not(login=write_password(), passwrd_2=input("Повторите пароль для проверки: ")):
    res_2 = hashlib.sha256(salt.encode() + passwrd_2.encode()).hexdigest()
    passwrd_2_digest = res_2
    with open("psswrd.json", "r", encoding="utf-8") as e:
        str_for_dict = e.read()
    inf_dict_1 = json.loads(str_for_dict)
    if passwrd_2_digest == inf_dict_1.get(login):
        return print("Пароль подходит")
    else:
        return print("Нет совпадения пароля")


if __name__ == "__main__":
    write_password()
    same_or_not()
