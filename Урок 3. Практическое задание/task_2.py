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
import csv

def user_hash():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    hash_password = sha256(login.encode() + password.encode()).hexdigest()
    return login, hash_password

def user_data():
    login, hash_password = user_hash()
    print(f'В базе данных хранится строка: {hash_password}')
    with open("users.csv", mode="w") as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow([login, hash_password])

def verification():
    login, verification_hash = user_hash()
    with open("users.csv", mode="r") as r_file:
        file = csv.reader(r_file, delimiter=",")
        f = 0
        for n in file:
            if login == n[0] and verification_hash == n[1]:
                print('Данные верны, вы вошли в систему')
                f = 1
                break
        if f == 0:
            print('Пользователь с такими данными не найден')

user_data()
verification()