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

from mysql.connector import connect
from uuid import uuid4
import hashlib

#   Спасибо за информацию о взаимодействии БД с Python, было интересно изучить
#   Вариант ввода пароля от сервера mysql через getpass как-то коряво с idle у меня работал,
#   поэтому ввёл вручную.

"""
    Скрипт создания БД
drop database if exists passwd;
create database passwd;

use passwd;

drop table if exists passwd_hash;
create table passwd_hash(
	id serial primary key,
	login varchar(50) unique,
	salt varchar(64) unique,
	hash varchar(64) unique
);
"""


def add_passwd():
    login = input('Enter your login: ')
    passwd = input('Enter your password: ')
    p_salt = uuid4().hex
    result = hashlib.sha256(p_salt.encode('utf8') + passwd.encode('utf8')).hexdigest()
    with connect(
            host="localhost",
            user='root',
            password='kAzre!47thfbS1') as connection:
        with connection.cursor() as cursor:
            db = 'use passwd;'
            cursor.execute(db)
            l_select = 'select login from passwd_hash'
            cursor.execute(l_select)
            l_result = cursor.fetchall()
            for el in l_result:
                if str(el) == f"('{login}',)":
                    print(f"Hello {login}, you've already added yor hash to DB")
                    exit(0)
            insert = """
            insert into passwd_hash(login, salt, hash)
            values(%s, %s, %s);
            """
            values = [login, p_salt, result]
            cursor.execute(insert, values)
            connection.commit()
            print(f'{login}, your password hash has been added: {result}')


def check_passwd():
    login = input('Enter your login: ')
    passwd = input('Enter your password: ')
    with connect(
            host="localhost",
            user='root',
            password='kAzre!47thfbS1!') as connection:
        with connection.cursor() as cursor:
            db = 'use passwd;'
            cursor.execute(db)
            a_select = 'select * from passwd_hash'
            cursor.execute(a_select)
            a_result = cursor.fetchall()
            for el in a_result:
                if el[1] == login:
                    p_salt = el[2]
                    p_hash = el[3]
                    if p_hash == hashlib.sha256(p_salt.encode('utf8') + passwd.encode('utf8')).hexdigest():
                        print('Correct password!')
                    else:
                        print('Wrong password, try again!')


add_passwd()
# check_passwd()
