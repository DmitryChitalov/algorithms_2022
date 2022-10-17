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

def check_pass ():
    salt = 'test'
    password_hash = hashlib.sha256(salt.encode() + input('Введите пароль: ').encode('UTF-8')).hexdigest()
    data ={"salt": salt,
           "hash" : password_hash}
    with open("password.json",'w') as write_pas:
        json.dump(data,write_pas)
    password_hash_check = hashlib.sha256(salt.encode() + input('Повторите пароль: ').encode('UTF-8')).hexdigest()
    with open("password.json", "r") as f:
        pass_hash = json.load(f)['hash']
    if pass_hash in password_hash_check:
        print('Пароли совпадают!')
        print(password_hash)
    else:
        print('Пароли не совпадают!')

if __name__ == '__main__':
    check_pass()