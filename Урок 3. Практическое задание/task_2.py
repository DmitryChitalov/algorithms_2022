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
import hashlib
import os
import sqlite3
import json
import csv
from pathlib import Path
from abc import ABC, abstractmethod
from binascii import hexlify

'''
Сразу извиняюсь за длинный код. Захотелось вспомнить работу и с CSV, и с JSON, и попытаться с БД из PYTHON.
И реализовать это через абстрактный класс и наследование.
'''


class UserPassword(ABC):
    def __init__(self, hash_func='sha256', encoding_='utf-8'):
        self.hash_func = hash_func
        self.encoding_ = encoding_
        self.user_data = self.read_data()  # dict: {user: {salt: val, hash: val},}

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, user, salt, hash_num):
        pass

    def registration(self, user, password):  # регистрация нового пользователя
        if user not in self.user_data:
            salt = hexlify(os.urandom(32))
            hash_num = hexlify(hashlib.pbkdf2_hmac(self.hash_func, password.encode(self.encoding_), salt, 100000))
            self.user_data[user] = {'salt': salt.decode(self.encoding_), 'hash': hash_num.decode(self.encoding_)}
            return self.write_data(user, self.user_data[user]['salt'], self.user_data[user]['hash'])
        return False

    def authorization(self, user, password):  # авторизация пользователя
        if user not in self.user_data:
            return False
        data_saved = self.user_data[user]
        salt = data_saved['salt'].encode(self.encoding_)
        hash_num = hexlify(hashlib.pbkdf2_hmac(self.hash_func, password.encode(self.encoding_), salt, 100000))
        if hash_num.decode(self.encoding_) == data_saved['hash']:
            return True
        return False

    def __str__(self):
        tmp = [f'Список пользователей ({len(self.user_data)}):']
        for key, val in self.user_data.items():
            tmp.append(f'{key}: {val["salt"]}, {val["hash"]}')
        return '\n'.join(tmp)


'''
Для создания таблицы users использовался скрипт:
CREATE TABLE users (
   id 		INTEGER PRIMARY KEY AUTOINCREMENT,
   name     TEXT    NOT NULL UNIQUE,
   salt		TEXT	NOT NULL,
   password TEXT    NOT NULL
);
'''


class UserPasswordSqlite(UserPassword):
    def read_data(self):
        conn = sqlite3.connect('test_db.sqlite')  # Создаем соединение с нашей базой данных
        cursor = conn.cursor()  # Создаем курсор
        cursor.execute("SELECT name, salt, password FROM users")
        results = cursor.fetchall()  # выбираем данные пользователя
        conn.close()  # закрыть соединение с базой данных
        if not results:
            return {}
        return {key: {'salt': val1, 'hash': val2} for key, val1, val2 in results}

    def write_data(self, user, salt, hash_num):
        conn = sqlite3.connect('test_db.sqlite')  # Создаем соединение с базой данных
        cursor = conn.cursor()  # Создаем курсор
        try:
            cursor.execute("INSERT INTO users (name, salt, password) VALUES(?, ?, ?)", (user, salt, hash_num))
        except sqlite3.IntegrityError:
            conn.close()
            return False  # пытались создать пользователя с существующим именеи
        conn.commit()
        conn.close()  # закрыть соединение с базой данных
        return True  # пользователь успешно занесен в таблицу `users`


class UserPasswordJson(UserPassword):
    def read_data(self):
        try:
            return json.loads(Path('user_data.json').read_text(self.encoding_))
        except FileNotFoundError:
            return {}

    def write_data(self, user, salt, hash_num):
        Path('user_data.json').write_text(json.dumps(self.user_data), self.encoding_)
        return True


class UserPasswordCsv(UserPassword):
    def read_data(self):
        try:
            with open('user_data.csv') as file:
                return {line[0]: {'salt': line[1], 'hash': line[2]} for line in csv.reader(file)}
        except FileNotFoundError:
            return {}

    def write_data(self, user, salt, hash_num):
        with open('user_data.csv', 'a', newline='') as f_object:
            csv.writer(f_object).writerow([user, salt, hash_num])
        return True


print('\n--------- Данные храним в таблице users СУБД sqlite --------')
ins_sqlite = UserPasswordSqlite()
for i in range(3):
    print(f'Новый пользователь user10{i}: ', ins_sqlite.registration(f'user10{i}', f'10{i}'))
for i in range(3):
    print(f'Проверка пароля пользователя user10{i} пароль "101": ', ins_sqlite.authorization(f'user10{i}', f'101'))
print(ins_sqlite)

print('\n--------- Данные храним в JSON файле "user_data.json" --------')
ins_json = UserPasswordJson()
for i in range(3):
    print(f'Новый пользователь user10{i}: ', ins_json.registration(f'user10{i}', f'10{i}'))
for i in range(3):
    print(f'Проверка пароля пользователя user10{i} пароль "101": ', ins_json.authorization(f'user10{i}', f'101'))
print(ins_json)

print('\n--------- Данные храним в CSV файле "user_data.csv" --------')
ins_csv = UserPasswordCsv()
for i in range(3):
    print(f'Новый пользователь user10{i}: ', ins_csv.registration(f'user10{i}', f'10{i}'))
for i in range(3):
    print(f'Проверка пароля пользователя user10{i} пароль "101": ', ins_csv.authorization(f'user10{i}', f'101'))
print(ins_csv)
