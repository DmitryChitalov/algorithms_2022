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
import os
import sqlite3


class Person:
    def __init__(self):

        if os.path.isfile('test.db'):
            self.con = sqlite3.connect('test.db')
            self.cursor = self.con.cursor()
        else:
            self.con = sqlite3.connect('test.db')
            self.cursor = self.con.cursor()
            self.con.execute("""CREATE TABLE hash(login text,pass text, finalHash text)""")

    def get_name(self, name, password):
        # hash = hashlib.sha256(str(name).encode('utf-8') + str(password).encode('utf-8'))
        hash = self.__get_hash(name, password)
        print(name, '   ', password)
        print(hash)
        sqlquer = "SELECT finalHash from hash where login = ?"
        ret_hash = self.con.execute(sqlquer, (name,)).fetchone()

        if ret_hash and ret_hash[0] == hash:
            print("Вы уже есть в системе")
        else:
            print("Вас нет в системе введите учетные данны заново")
            name = input("Имя")
            password = input("Введите пароль")
            # hash1 = hashlib.sha256(input("Введите соль").encode('utf-8') + input('Введите пароль').encode('utf-8'))
            hash = self.__get_hash(name, password)
            sqlInsert = """INSERT INTO hash(login,pass,finalHash) values(?,?,?)"""
            data_tuple = (name, password, hash)
            print(data_tuple)
            self.con.execute(sqlInsert, data_tuple)
            self.con.commit()

    def get_data(self):
        rows = self.con.execute("SELECT * FROM hash")
        for row in rows:
            print(row)

    def __get_hash(self, name, password):
        return hashlib.sha256(str(name).encode('utf-8') + str(password).encode('utf-8')).hexdigest()


pers = Person()
pers.get_name("ivan", 'pass')
pers.get_name("ivan1232", 'pass2')

# pers.get_data()
