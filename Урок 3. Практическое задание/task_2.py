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

import pickle
import hashlib

SALT = b"w0e_cw03_0e3j_3kcjjaADASC"

def setPass() -> None:
    p = hashlib.sha256(SALT+str.encode(input("Set the password: "))).hexdigest()
    print(f"String stored in DB: {p}")
    with open("hshdpswd.txt", "w") as f:
        f.write(p)


def checkPass():
    p = hashlib.sha256(SALT+str.encode(input("Input the password: "))).hexdigest()
    with open("hshdpswd.txt", "r") as f:
        preal = f.read()
    if preal == p:
        return True
    else:
        return False

setPass()
print(checkPass())

