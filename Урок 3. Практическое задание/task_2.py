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


def write_salt(salt):
    with open('salt.json', 'w') as f:
        f.write(json.dumps(salt))


def write_pswd(pswd):
    with open('hash_file.json', 'w') as f, open('salt.json') as s:
        salt = s.read()
        pswd_hash = hashlib.sha256(salt.encode('utf-8') + pswd.encode('utf-8')).hexdigest()
        f.write(json.dumps(pswd_hash))
        print(f'В базе данных хранится строка: {pswd_hash}')


def check_pswd(pswd):
    with open('hash_file.json') as f, open('salt.json') as s:
        salt = s.read()
        pswd_hash = hashlib.sha256(salt.encode('utf-8') + pswd.encode('utf-8')).hexdigest()
        if pswd_hash in f.read():
            print('Вы ввели правильный пароль')
        else:
            print('Вы ввели неправильный пароль')


if __name__ == '__main__':

    salt = 'skldgfhwleury'
    write_salt(salt)

    pswd = input('Введите пароль: ')
    write_pswd(pswd)

    pswd = input('Введите пароль: ')
    check_pswd(pswd)
