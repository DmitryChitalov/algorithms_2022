"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
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
from hashlib import pbkdf2_hmac
from ast import literal_eval
from binascii import hexlify
import json, shelve, sqlite3

login = 'Ivan'
password = 'Testing'
vault = {}


def password_create(login, password):
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=password.encode('utf-8'),
                      salt=login.encode('utf-8'),
                      iterations=10000)
    vault[login] = hexlify(obj)
    return print('Success!')


password_create(login, password)
print(vault)


def password_check(login, password):
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=password.encode('utf-8'),
                      salt=login.encode('utf-8'),
                      iterations=10000)
    result = hexlify(obj)
    print(result)
    return print(True) if vault[login] == result else print(False)


password_check(login, password)

# conn = sqlite3.connect('Chinook_Sqlite.sqlite')
# cursor = conn.cursor()
# cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")
# cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

# Получаем результат сделанного запроса
# results = cursor.fetchall()
# results2 = cursor.fetchall()

# print(results)   # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
# print(results2)

# conn.close()