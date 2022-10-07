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

import sqlite3
import hashlib

# Решееие с использованием базы sqlite.
'''
class DbHash:
    def __init__(self):
        self.conn = sqlite3.connect("test_al.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS users;")
        self.cursor.execute("CREATE TABLE users(u_login varchar(255), password_hash varchar(255))")

    def create_hash(self):
        login = input('Введите логин: ')
        us_pass = input('Введите пароль: ')
        hash_passwd = hashlib.sha256(login.encode() + us_pass.encode()).hexdigest()
        return login, hash_passwd

    def sql_insert(self):

        login, hash_pass = self.create_hash()

        insert_log_hash = 'INSERT INTO users(u_login, password_hash) VALUES(?,?)'
        log_hash = (login, hash_pass)
        try:
            self.cursor.execute(insert_log_hash, log_hash)
        except sqlite3.IntegrityError:
            print('Такой login уже существует. Войдите в систему или введите другой login.')
        else:
            self.conn.commit()
            print('Вы зарегестрированы')

    def log_in(self):

        login, hash_pass = self.create_hash()

        select_log_hash = 'SELECT password_hash FROM users WHERE u_login = ?'

        self.cursor.execute(select_log_hash, (login,))

        db_hash = self.cursor.fetchone()
        db_hash = str(*db_hash)

        if hash_pass == db_hash:
            print('Вы ввели правильный пароль')
        else:
            print('Вы ввели неправильный пароль')

data_base_1 = DbHash()
data_base_1.create_table()
data_base_1.sql_insert()
data_base_1.log_in()
'''


# Решение с хранением логина и хэша-пароля в файле log_pass_hash.csv.
def create_hash():
    login = input('Введите логин: ')
    us_pass = input('Введите пароль: ')
    hash_passwd = hashlib.sha256(login.encode() + us_pass.encode()).hexdigest()
    return login, hash_passwd


def save_hash(login, hash_passwd):
    with open('log_pass_hash.csv', 'a+', encoding='utf-8') as fa:
        fa.writelines(f'{login};{hash_passwd}\n')  # Записывает в файл логин и хэш пароля.


def read_hash():
    dict_hash = {}
    with open('log_pass_hash.csv', 'r+', encoding='utf-8') as fr:
        for _ in fr:
            dict_hash.setdefault(_.strip().split(";")[0], _.strip().split(";")[1])

    return dict_hash


def log_in(dict_hash):
    u_login = input('Введите логин: ')

    if u_login in dict_hash:
        u_password = input('Введите пароль: ')
        hash_u_password = hashlib.sha256(u_login.encode() + u_password.encode()).hexdigest()
        if hash_u_password == dict_hash[u_login]:
            print('Доступ разрешён!')
            return exit(0)
        else:
            print('Неверный пароль!')
            return exit(1)
    else:
        print('Пользователь не зарегестрирован!')
        return exit(1)


login, hash_passwd = create_hash()
print(login, hash_passwd)
save_hash(login, hash_passwd)
log_in(read_hash())
