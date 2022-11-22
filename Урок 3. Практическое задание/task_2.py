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

import json
import hashlib
import binascii


def hashing(password):
    object = hashlib.pbkdf2_hmac(hash_name = 'sha256', password = password.encode(), salt = b'what', iterations = 2)
    hashed_password = binascii.hexlify(object)
    hashed_passowrd = str(hashed_password)    
    return hashed_passowrd

def storing(password):
    hashed_password = hashing(password)    
    with open("Урок 3. Практическое задание/task_2_data.json", "w+") as file:
        json.dump(hashed_password, file)
    print(f"Записано. В базе данных хранится строка: {hashed_password}")

def checking(password):
    new_password = hashing(password)
    with open("Урок 3. Практическое задание/task_2_data.json", "r") as read_file:
        hashed_pass = json.load(read_file)
    if hashed_pass == new_password:
        print("Вы ввели правильный пароль.")
    else: 
        print("Вы ввели неверный пароль!")


input_password = input('Введите пароль: ')
storing(input_password)
check_password = input('Введите пароль еще раз для проверки: ')
checking(check_password)