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

# Программа не учитывает что файл базы будет больше объема памяти, для большой базы необходимо выполнять поиск
#   внутри файла, а не как тут целиком вливать файл в память

from uuid import uuid4
import hashlib
import json


class User:
    def __init__(self):
        self.bd = {}
        self.logins = None
        self.passwd = None
        self.salt = None
        self.__load_json()

    def reg(self):
        while self.__login_check() is True:
            print('Пользователь уже существует!')
        while self.__passwd_check(input('Введите пароль: ')) is False:
            print('Пароли не совпадают')
        self.bd.setdefault(self.logins, {'salt': self.salt, 'password': self.passwd})
        self.__save_json()
        print('Регистрация успешна')
        return True

    def login(self):
        while self.__login_check() is False:
            print('Пользователя не существует!')
        self.passwd = self.bd[self.logins]['password']
        self.salt = self.bd[self.logins]['salt']
        while self.__passwd_check(input('Введите пароль: ')) is False:
            print('Пароль не верный')
        print('Вход выполнен')
        return True

    def __save_json(self):
        with open("data_file.json", "w", encoding='UTF-8') as write_file:
            json.dump(self.bd, write_file, indent=4, sort_keys=True)

    def __load_json(self):
        try:
            with open("data_file.json", "r", encoding='UTF-8') as read_file:
                self.bd = json.load(read_file)
        except FileNotFoundError:
            print('С базой что-то не так... её нет!')

    def __login_check(self):
        self.logins = input('Введите логин пользователя: ')
        if self.logins in self.bd.keys():
            return True
        return False

    def __passwd_check(self, in_pass):
        if self.logins in self.bd.keys():
            if self.passwd == hashlib.sha256(self.salt.encode() + in_pass.encode()).hexdigest():
                return True
            else:
                return False
        else:
            if self.salt is None:
                self.salt = uuid4().hex
            passwd1 = hashlib.sha256(self.salt.encode() + in_pass.encode()).hexdigest()
            passwd2 = hashlib.sha256(self.salt.encode() + input('Введите повторно пароль: ').encode()).hexdigest()
            if passwd1 == passwd2:
                self.passwd = passwd1
                return True
            else:
                return False


def menu():
    user = User()
    chose = None
    while chose != 0:
        print(f'Добро пожаловать!\n'
              f'Menu:\n'
              f'1) Регистрация нового пользователя\n'
              f'2) Вход\n'
              f'0) Завершить работу\n')
        try:
            chose = int(input('Введите цифру меню: '))
        except ValueError:
            pass
        if chose == 1:
            user.reg()
        elif chose == 2:
            user.login()
            #  Тут по смыслу логичнее перейти в другое меню или break, но для удобства тестирования не делал break
        elif chose == 0:
            break
        else:
            print('****Введен неправильный номер меню!****')


menu()
