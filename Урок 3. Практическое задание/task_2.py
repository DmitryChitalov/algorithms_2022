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
import mysql.connector


def to_hash(user_name, user_password):
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=user_password.encode('utf-8'),
                      salt=user_name.encode('utf-8'),
                      iterations=100000)
    return hexlify(obj)


user_name = (input('Введите имя пользователя: '))
user_password = (input('Введите пароль пользователя: '))
result = to_hash(user_name, user_password)
print(result)

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="12345",
                               database="users_access")

mycursor = mydb.cursor()

sql = "INSERT INTO passwords (username, password_hash) VALUES (%s, %s)"
val = (user_name, result)
mycursor.execute(sql, val)

mydb.commit()

prove_password = (input('Введите пароль повторно: '))
result = to_hash(user_name, prove_password)

mycursor.execute(f"SELECT password_hash FROM passwords where username = '{user_name}'")
if result == mycursor.fetchall()[0][0].encode('utf-8'):
    print('Вы ввели правильный пароль')
else:
    print('Пароли не совпадают')
