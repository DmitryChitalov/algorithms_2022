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

import pyodbc
import hashlib


class WorkWithMSSql():

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.cnxn = None

    def connection(self):
        self.cnxn = pyodbc.connect(self.connection_string, autocommit=True)

    def write_hash(self, user_id, str_hash):
        db_cursor = self.cnxn.cursor()
        db_cursor.execute('INSERT INTO user_hash (userID,hash256) VALUES (?,?)', user_id, str_hash)
        db_cursor.close()

    def read_hash(self, user_id):
        db_cursor = self.cnxn.cursor()
        db_cursor.execute('Select userID,hash256 from user_hash where userID = ?', user_id)
        mem_hash = ''
        for row in db_cursor:
            mem_hash = row.hash256
            break
        db_cursor.close()
        return mem_hash.strip()


def get_hash(user_id, password):
    return hashlib.sha256(user_id.encode('utf-8') + password.encode('utf-8')).hexdigest()


if __name__ == '__main__':

    WorkWithMSSql_OBJ = WorkWithMSSql("Driver={SQL Server Native Client 11.0};"
                                      "Server=localhost;"
                                      "Database=algorithms;"
                                      "UID=sa;"
                                      "PWD=indus72;")
    WorkWithMSSql_OBJ.connection()

    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    hash = get_hash(login, password)
    print(f'Получили хэш: {hash}')
    WorkWithMSSql_OBJ.write_hash(login, hash)

    password = input('Введите пароль еще раз: ')

    hash_mem = WorkWithMSSql_OBJ.read_hash(login)
    print(f'Сохраненный хэш: {hash_mem}')

    hash = get_hash(login, password)
    print(f'Расчитанный хэш: {hash}')

    if hash == hash_mem:
        print('Вы ввели верный пароль')
    else:
        print('Введен не верный пароль')

    WorkWithMSSql_OBJ.cnxn.close()
