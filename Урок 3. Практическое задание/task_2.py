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


def registration():
    login = input('Придумайте логин: ')
    password = input('Придумайте пароль: ')
    key = hashlib.sha256(password.encode('utf-8') + login.encode('utf-8')).hexdigest()
    with open('passwords.csv', 'a', encoding='utf-8') as file:
        file.write(f'{key} {login}\n')
        print(f'В базе данных хранится строка: {key}')
    with open('passwords.csv', 'r', encoding='utf-8') as file:
        r_password = input('Подтвердите пароль: ')
        r_key = hashlib.sha256(r_password.encode('utf-8') + login.encode('utf-8')).hexdigest()
        for i in [i.split() for i in file.readlines()]:
            if i[0] == r_key:
                return 'Вы ввели правильный пароль'
        return 'Вы ввели неправильный пароль'


print(registration())
