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
import json


class HashPass:
    def __init__(self):
        self.data = {'login1': 'pass1'}
        self.namejson = 'Hash_passwrd.json'
        self.input_login()

    def input_login(self):
        login = input('Введите логин: ')
        if login not in self.read_json():
            print('Пользователь с логином', login, 'не существует')
            self.registration()
            return
        count = 3
        while count > -1:
            passwrd = input('введите пароль:')
            if count == 0:
                print('Пароль неверный. Попытки кончились.')
                break
            elif self.read_json()[login] == self.hashpass(passwrd, login):
                print('Авторизация пройдена')
                break
            else:
                print('Пароль неверный. У вас осталось попыток', count)
                count -= 1

    def registration(self):
        answer = input('Создать новую учетную запись? Да/Нет: ')
        if answer == 'Да':
            new_login = input('Введите новый логин:')
            if new_login in self.read_json():
                print('Ваш логин неуникальный:')
                return self.registration()
            new_passwrd = input('Введите пароль: ')
            print('вы авторизованы')
            self.write_json(new_login, new_passwrd)
        else:
            print('Вы отказались от регистрации.')
        return

    def write_json(self, login, passwrd):
        with open(self.namejson, encoding='utf-8') as f:
            data = json.load(f)
            data[login] = self.hashpass(passwrd, login)
            with open(self.namejson, 'w', encoding='utf-8') as out_f:
                json.dump(data, out_f)

    def read_json(self):
        with open(self.namejson, 'r', encoding='utf-8') as f_json:
            data = json.load(f_json)
            return data

    def hashpass(self, passwrd, login):
        hash_passwrd = hashlib.sha256(passwrd.encode() + login.encode()).hexdigest()
        return hash_passwrd


x = HashPass()
