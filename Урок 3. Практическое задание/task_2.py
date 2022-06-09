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
import json

class Password:

    def __init__(self):
        self.data = {}
        self.load()

    def load(self):
        with open('task_2.json', mode='r') as file:
            self.data = json.loads(file.readline())
        self.info()

    def info(self):
        print(f"Пользователи: {len(self.data['users'])}")

    def save(self):
        with open('task_2.json', mode='w') as file:
            file.write(json.dumps(self.data))

    @property
    def users(self):
        return self.data['users']

    def check(self, username: str, password: str) -> int:
        return self.users.get(username) \
               and self.users[username]['pass'] == \
               sha256(password.encode() + self.users[username]['salt'].encode()).hexdigest()

    def request(self):
        if self.check_auth(input('Введите логин: '), input('Введите пароль: ')):
            print('Верный пароль')
        else:
            print('Неверный пароль')

        self.request()

Password.request()
