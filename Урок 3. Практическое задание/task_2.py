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
    passwd = input('Введите пароль: ')
    hash_pass = sha256(login.encode() + passwd.encode()).hexdigest()
    return login, hash_pass

def new_user():
    login, hash_pass = user_hash()
    print(f'В базе данных есть: {hash_pass}')
    with open("users.csv", mode="w") as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow([login, hash_pass])


def check_hash():
    login, check_pass = user_hash()
    print(check_pass)
    with open("users.csv", mode="r") as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        f = 0
        for n in file_reader:

            if login == n[0] and check_pass == n[1]:
                print('Всё верно, добро пожаловать ')
                f = 1
                break
        if f == 0:
            print('Пользователь не найден')


new_user()
check_hash()

