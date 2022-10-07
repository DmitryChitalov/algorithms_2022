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


def login_pass():
    """
    Создание логина и пароля
    :return: логин и хэш пароля
    """
    res_login = input('Введите логин: ')
    res_pass = input('Введите пароль: ')
    hash_pass = sha256(res_login.encode('utf-8') + res_pass.encode('utf-8')).hexdigest()
    print(f'Хэш вашего пароля - {hash_pass}')
    return res_login, hash_pass


def add_login_pass(my_file):
    """
    Добавление пользователя в json файл
    :param my_file: имя json файла
    :return: добавление пользователя если он есть или сообщение, что такой пользователь есть
    """
    new_login, new_pass = login_pass()
    try:
        json_file = open(my_file, 'r', encoding='utf-8')
    except FileNotFoundError:
        res_dict = {}
        with open(my_file, 'w', encoding='utf-8') as json_file:
            res_dict[new_login] = new_pass
            json.dump(res_dict, json_file)
        return print('Вы добавлены в систему')
    else:
        try:
            res_dict = json.load(json_file)
        except json.decoder.JSONDecodeError:
            json_file.close()
            return print('Не верный файл или формат файла')
        else:
            if res_dict.get(new_login):
                json_file.close()
                return print('Такой пользователь уже существует')
            json_file.close()
            with open(my_file, 'w', encoding='utf-8') as json_file:
                res_dict[new_login] = new_pass
                json.dump(res_dict, json_file)
            return print('Вы добавлены в систему')


def try_login_pass(my_file):
    """
    Проверка логина и пароля
    :param my_file: файл json  с логинами и хэш паролями
    :return: вход в систему или сообщение о не верном логине или пароле
    """
    try_login, try_pass = login_pass()
    with open(my_file, 'r', encoding='utf-8') as json_file:
        try:
            try_dict = json.load(json_file)
        except json.decoder.JSONDecodeError:
            return print('Не верный файл или формат файла')
        else:
            if try_dict.get(try_login):
                if try_pass == try_dict[try_login]:
                    return print(f'Пользователь {try_login} вы успешно вошли в систему')
                return print('Вы ввели не правильный пароль')
            return print('Пользователь не зарегестрирован в системе')


if __name__ == '__main__':
    for i in range(3):
        add_login_pass('login_pass.json')

    for i in range(3):
        try_login_pass('login_pass.json')