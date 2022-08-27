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


def to_get_hash(login, passwd):
    """Получаем хеш пароля"""
    it_hash = sha256(login.encode() + passwd.encode()).hexdigest()
    print(f'Хеш пароля: {it_hash}')
    return it_hash


def register_user(login, passwd):
    """Регистрация пользователя"""
    log_pswd = authentication_user()  # Получаем данные о пользователях
    if log_pswd.get(login):
        return 'Такой пользователь уже зарегистрирован'

    with open('users_db.json', 'w') as fi:
        log_pswd[login] = to_get_hash(login, passwd)
        json.dump(log_pswd, fi)

    return 'Регистрация прошла успешно'


def authentication_user():
    """ Аутификация пользователя """
    try:
        with open('users_db.json') as fo:
            log_pswd = json.load(fo)
    except FileNotFoundError:
        return {}
    else:
        return log_pswd


def log_in(login, passwd):
    """Вход пользователя"""
    log_pswd = authentication_user()  # Получаем данные о пользователях
    if log_pswd.get(login):
        if log_pswd[login] == to_get_hash(login, passwd):
            return 'Вы ввели правильный пароль'
        else:
            return 'Вы ввели неправильный пароль'
    else:
        return 'Такого пользователя не существует'


def enter_log_paswd():
    login = input('Введите логин: ')  # будет служить нам в качестве соли
    passwd = input('Введите пароль: ')

    return login, passwd


print(register_user(*enter_log_paswd()))
print(log_in(*enter_log_paswd()))
