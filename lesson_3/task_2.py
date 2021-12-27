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
from uuid import uuid4
from hashlib import sha256
import json


class Hashing:
    def __init__(self):
        self.users = {}
        self.salt = None
        self.key = None
        self.user = input('Введите имя пользователя: ')
        self.password = input('Введите пароль: ')
        self.ready_json()
        self.create_keys()
        self.check()

    @staticmethod
    def create_key_with_salt(salt, password):
        result_key = sha256(salt.encode() + password.encode()).hexdigest()
        return result_key

    def ready_json(self):
        try:
            with open('users.json', 'x', encoding='utf-8') as f:
                json.dump(self.users, f)
        except FileExistsError:
            pass
        finally:
            with open('users.json', 'r', encoding='utf-8') as f:
                self.users = json.load(f)
                return self.users

    def create_keys(self):
        if self.user in self.users:
            self.key = self.create_key_with_salt(self.users[self.user][0], self.password)
            return self.key
        else:
            self.salt = uuid4().hex
            key = self.create_key_with_salt(self.salt, self.password)
            print(f'В базе данных хранится строка: {key}')
            self.users[self.user] = [self.salt, key]
            with open('users.json', 'w', encoding='utf-8') as f:
                json.dump(self.users, f)

            check_password = input('Введите пароль еще раз для проверки: ')
            with open('users.json', 'r', encoding='utf-8') as f:
                self.users = json.load(f)

            self.key = self.create_key_with_salt(self.users[self.user][0], check_password)
            return self.key

    def check(self):
        if self.key == self.users[self.user][1]:
            print('Вы ввели правильный пароль')
        else:
            print('Пароль неправильный')


try_hash = Hashing()
