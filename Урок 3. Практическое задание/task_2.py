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
import sqlite3

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
# conn.cursor().execute('drop table passwd; ')
# conn.cursor().execute('create table passwd (login varchar(255) unique primary key, password varchar(255))')

while True:
    # cursor.execute(f"Select * from passwd")
    # print(cursor.fetchall())

    login = input('Введите Login: ')
    passwd = input('Введите пароль: ')
    hash = hashlib.sha256(login.encode('utf-8') + passwd.encode('utf-8'))
    print(hash.hexdigest())

    passwd2 = input('Введите пароль еще раз: ')
    hash2 = hashlib.sha256(login.encode('utf-8') + passwd2.encode('utf-8'))
    print(hash2.hexdigest())
    if hash2.hexdigest() == hash.hexdigest():

        cursor.execute(f"Select password from passwd where login = ?;", (login,))
        res = cursor.fetchall()
        if not res:
            cursor.execute(f"insert into passwd(login, password) values (?, ?);", (login, hash2.hexdigest()))
            conn.commit()
            print("Пользователь зареган")
        else:
            if res[0][0] == hash.hexdigest():
                print("Пароль введен правильно")
            else:
                print("Пароль введен неправильно")
