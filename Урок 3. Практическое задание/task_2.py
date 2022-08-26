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

from os.path import join, dirname
from sqlite3 import connect, OperationalError, IntegrityError


class HashClass:
    def __init__(self):
        self.db_obj = join(dirname(__file__), "demo.sqlite")
        self.conn = connect(HashClass.db_obj)
        self.crs = self.conn.cursor()

    def create_table(self):

        create_stmt = "CREATE TABLE user_info (user_login varchar(255) " \
                      "unique, user_password varchar(255));"
        try:
            self.crs.execute(create_stmt)
        except OperationalError:
            print("Таблица уже есть. Не добавляем")
        else:
            self.conn.commit()
            print("Операция прошла успешно, таблица добавлена в БД")

    @staticmethod
    def get_hash():
        login = input('Введите логин: ')
        passwd = input('Введите пароль: ')
        hash_obj = sha256(login.encode() + passwd.encode()).hexdigest()
        return login, hash_obj

    def register(self):

        login, reg_hash = self.get_hash()

        insert_stmt = "INSERT INTO user_info (user_login, user_password)" \
                      " VALUES (?, ?)"

        user_info = (login, reg_hash)
        try:

            self.crs.execute(insert_stmt, user_info)
        except IntegrityError:
            print("Вы уже есть в базе, выполните вход.")
        else:
            self.conn.commit()
            print("Операция прошла успешно, вы зарегистрировались")

    def log_in(self):


        login, check_hash = self.get_hash()

        select_stmt = "SELECT user_password FROM user_info WHERE user_login = ?"

        self.crs.execute(select_stmt, (login,))

        out_hash = self.crs.fetchone()

        if check_hash == out_hash[0]:
            print('это вы!')
        else:
            print("Вы ввели неверный пароль или еще не регались")


network = HashClass()
# network.create_table()
# network.register()
network.log_in()