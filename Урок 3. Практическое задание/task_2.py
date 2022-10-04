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


def generate_hash_passwd(salt, passwd):
    hash_passwd = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
    return hash_passwd


def sql_add_data(name, passwd):
    conn = sqlite3.connect('passwd.sqlite')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS PASSWD")
    cursor.execute("""
        CREATE TABLE PASSWD (
            salt TEXT,
            passwd_hash TEXT
        ); 
    """)
    conn.commit()

    # заносим в базу соль и хэш
    hash_passwd = generate_hash_passwd(name, passwd)
    cursor.execute("INSERT INTO PASSWD (salt, passwd_hash) VALUES(?, ?)", (name, hash_passwd))
    conn.commit()

    # проверка
    cursor.execute("SELECT passwd_hash FROM PASSWD")
    passwd_hash = cursor.fetchone()
    print('passwd_hash:', passwd_hash[0])
    conn.close()
    return hash_passwd


def sql_check_hash(name, passwd):
    conn = sqlite3.connect('passwd.sqlite')
    cursor = conn.cursor()

    # генерируем хэш введенного пароля с солью из нашей БД
    test_hash = generate_hash_passwd(name, passwd)

    # получаем эталонный хэш из нашей БД и сравниваем с полученным хешем
    cursor.execute("SELECT passwd_hash FROM PASSWD")
    passwd_hash = cursor.fetchone()
    conn.close()
    if test_hash == passwd_hash[0]:
        return True
    else:
        return False


user_name = input('Введите имя: ')
user_passwd = input('Введите пароль: ')
sql_add_data(user_name, user_passwd)

user_name = input('Введите имя: ')
user_passwd = input('Введите пароль: ')
if sql_check_hash(user_name, user_passwd):
    print('Пароль верный')
else:
    print('Пароль неверный')
