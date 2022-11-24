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

from binascii import hexlify
from hashlib import pbkdf2_hmac
import json


def pass_hash(password):
    with open('data.json', mode='r', encoding='utf-8') as file:
        data_dict = json.load(file)
    salt = data_dict['salt']
    password_bytes = pbkdf2_hmac(hash_name='sha256',
                                 password=password.encode(),
                                 salt=salt.encode(),
                                 iterations=10000)
    return hexlify(password_bytes).decode()


def request_and_check_pass():
    pass_request = input('Введите пароль: ')
    pass_request_hash = pass_hash(pass_request)
    print(f'Хеш пароля: {pass_request_hash}')
    with open('data.json', mode='r', encoding='utf-8') as file:
        data_dict = json.load(file)
    data_dict['user'] = pass_request_hash
    with open('data.json', mode='w', encoding='utf-8') as file:
        json.dump(data_dict, file)
    pass_check = input('Введите пароль ещё раз: ')
    pass_check_hash = pass_hash(pass_check)
    with open('data.json', mode='r', encoding='utf-8') as file:
        data_dict = json.load(file)
    print('Вы ввели верный пароль' if data_dict['user'] == pass_check_hash else 'Вы ввели неверный пароль')


if __name__ == "__main__":
    request_and_check_pass()
