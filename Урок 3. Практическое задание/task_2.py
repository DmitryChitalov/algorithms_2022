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

import mysql.connector
import hashlib
from binascii import hexlify

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='******'
)

cursor = db.cursor()
cursor.execute('CREATE DATABASE hash_task3')
cursor.execute('USE hash_task3')
cursor.execute('CREATE TABLE hashes (hash VARCHAR(255), salt VARCHAR(255))')

salt = input('Введите логин')
inp_pswd = input('Введите пароль')

hash_obj = hashlib.pbkdf2_hmac(hash_name='sha256',
                               password=inp_pswd.encode('utf-8'),
                               salt=salt.encode('utf-8'),
                               iterations=100)

result = hexlify(hash_obj)
print(result)

sql = 'INSERT INTO hashes VALUES (%s, %s)'
val = (result, salt)
cursor.execute('USE hash_task3')
cursor.execute(sql, val)

db.commit()

check_pswd = input('Введите пароль повторно')
check_hash_obj = hashlib.pbkdf2_hmac(hash_name='sha256',
                                     password=check_pswd.encode('utf-8'),
                                     salt=salt.encode('utf-8'),
                                     iterations=100)

check_result = hexlify(check_hash_obj).decode('utf-8')

sql = 'SELECT hash FROM hashes WHERE salt = %s'
val = (salt,)
cursor.execute(sql, val)
res = cursor.fetchall()
res = str(res[0][0])

if res == check_result:
    print('Все верно')
else:
    print('Неверно')
