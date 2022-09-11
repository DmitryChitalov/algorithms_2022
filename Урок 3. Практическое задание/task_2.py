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
from sqlite3 import connect
from uuid import uuid4


def hashing(passwd_in, salt_in):
    res_g = sha256(passwd_in.encode() + salt_in.encode()).hexdigest()
    return res_g


login = input('Введите логин: ')
passwd = input('Введите пароль: ')
salt = uuid4().hex
res = hashing(passwd, salt)

conn = connect('db.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS hash_db (login, hash, salt)')
cursor.execute(f'INSERT INTO hash_db (login, hash, salt) VALUES ("{login}", "{res}", "{salt}")')
conn.commit()
print(f'В базе данных хранится строка: {res}')


passwd = input('Введите пароль еще раз для проверки: ')
salt = cursor.execute(f'SELECT salt FROM hash_db WHERE login = "{login}"').fetchall()[0][0]
pass_check = cursor.execute(f'SELECT hash FROM hash_db WHERE login = "{login}"').fetchall()[0][0]
res = hashing(passwd, salt)
print(f'Повторно сгенерированный хеш: {res}')

if res == pass_check:
    print('Пароль верный!')
else:
    print('Пароль не верный')