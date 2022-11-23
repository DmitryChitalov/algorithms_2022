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

from hashlib import pbkdf2_hmac
from random import randint
from binascii import hexlify
import json


def password_hash_sha(password: str, salt=str(), algorithm='sha256'):
    """
    Функция для создания хэша введенного пароля по алгоритму sha256.
    Возвращает строку из шестандцатиричных чисел.
    """
    password_hash = pbkdf2_hmac(hash_name=algorithm,
                                password=bytes(password, 'utf-8'),
                                salt=bytes(salt, 'utf-8'),
                                iterations=100)
    return str(hexlify(password_hash))[2:][:-1]


def create_passwords(file_name: str, number=2):
    """
    Функция запрашивает логин, пароль и соль и записывает в файл json.
    В качестве аргументов функции задаются путь до файла и количество записей.
    Примечание. При обращении к функции файл перезаписывается.
    """
    print(f'Заполнение паролями файла {file_name}')
    user_dict = dict()
    for i in range(0, number):
        print(f'Введите {i + 1}-й логин: ', end='')
        login = input()
        print(f'Введите пароль для {i + 1}-го логина: ', end='')
        password = input()
        print(f'Введите соль для {i + 1}-го логина: ', end='')
        salt = input()
        password_hash = password_hash_sha(password, salt)
        user_dict.setdefault(login, (salt, password_hash))
    with open('./passwords.json', 'w') as fp:
        json.dump(user_dict, fp)


def password_check(file_name: str, login=str(), ask_login=True):
    """
    Функция запрашивает логин пользователя и проверяет, есть ли пользователь в файле .json, который указан в
    качестве аргумента. Если пользователь есть в файле, функция запрашивает пароль. Если хэш пароля есть в файле
    .json, пользователю предоставляется доступ. Если нет, функция просит пользователя повторно пройти аутентификацию.
    """
    try:
        if ask_login:
            print('Пожалуйста, введите Ваш логин: ', end='')
            login = input()
        with open(file_name, 'r') as fp:
            users_dict = json.load(fp)
        salt = users_dict[login][0]
        print('Пожалуйста, введите Ваш пароль: ', end='')
        password = input()
        password_hash = password_hash_sha(password, salt)
        print(f'Хэш введенного пароля: {password_hash}')
        if password_hash == users_dict[login][1]:
            print('Пожалуйста, введите Ваш пароль еще раз: ', end='')
            password = input()
            password_hash = password_hash_sha(password, salt)
            print(f'Хэш введенного пароля: {password_hash}')
            if password_hash == users_dict[login][1]:
                print(f'Пароль верный. Добро пожаловать, {login}')
            else:
                print('Произошла ошибка. Попробуйте пройти аутентификацию еще раз: ', end='')
                password_check(file_name)
        else:
            print('Неверный пароль. Попробуйте еще раз: ', end='')
            password_check(file_name, login=login, ask_login=False)
    except KeyError:
        print('Неверный логин. Попробуйте еще раз. ', end='')
        password_check(file_name)


if __name__ == '__main__':
    create_passwords('./passwords.json')
    password_check('./passwords.json')
