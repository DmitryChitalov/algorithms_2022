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
from hashlib import pbkdf2_hmac
from binascii import hexlify
import sqlite3


def get_hash_pwd():
    pwd = input('введите пароль ')
    pwd = bytes(pwd.encode('utf-8'))
    slt = b'salt'
    pwd = pbkdf2_hmac(hash_name='sha256', password = pwd, salt=slt, iterations=10000)
    pwd = hexlify(pwd)
    return pwd

def save_in_db(pwd):
    login = 'test_login'
    cursor.execute(f'CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, login text not null, password text);')
    item = (1,login,pwd)
    cursor.execute(f"INSERT INTO users VALUES(?, ?, ?);", item)
    conn.commit()

def get_from_db():
    cursor.execute("SELECT * FROM users")
    res = cursor.fetchone()
    hash = res[2]
    print(f'В базе данных хранится строка: {hash}')
    conn.close()
    return hash





conn = sqlite3.connect(":memory:")  # ('mydatabase.db')
cursor = conn.cursor()

pwd = get_hash_pwd()
save_in_db(pwd)
db_hash = get_from_db()
new_hash = get_hash_pwd()
if db_hash == new_hash:
    print(f'Пароли одинаковые')
else:
    print('Пароли разные')