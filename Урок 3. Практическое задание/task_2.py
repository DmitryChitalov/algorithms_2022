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
import os.path
from binascii import hexlify
from hashlib import pbkdf2_hmac

CSV = 'password_hash.csv'  # файл в котором находятся данные


def hash_function(login_def, password_def):
    password_hash = hexlify(
        pbkdf2_hmac(hash_name='sha256', salt=login_def.encode('utf-8'), password=password_def.encode('utf-8'),
                    iterations=100000))
    return password_hash


# Проверка пароля
def password_verification(login_def, password_input):
    password_input = str(hash_function(login_def, password_input))
    print(f'Хеш введенного только что пароля: {password_input}')
    with open(CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            password_in_csv = row.get(login_def)
            break
    if password_in_csv == password_input:
        return f'Добро пожаловать, {login_def}'
    else:
        return exit('Неверный пароль!')


# Если файл отсутствует в системе, то создаем его и заполняем шаблонными данными.
def added_password_hash_file():
    users = ['Aleksey', 'Oleg', 'Ivan']
    passwords = ['11111', '22222', '33333']
    for i in range(len(passwords)):
        passwords[i] = hash_function(users[i], passwords[i])
    users_and_password = dict(zip(users, passwords))
    with open(CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=users)
        writer.writeheader()
        writer.writerow(users_and_password)


if not os.path.exists(CSV):
    added_password_hash_file()

login = 'Aleksey'
print(f'Здравствуйте, {login}!')
password = input('Введите пароль: ')
print(password_verification(login, password))
