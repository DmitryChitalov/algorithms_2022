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

from sqlite3 import connect
from hashlib import sha256
from uuid import uuid4

DB = 'DB.db'


def create_table():
    conn = connect(DB)
    with conn:
        cur = conn.cursor()
        cur.execute(
            f'''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            login VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(64) NOT NULL,
            salt VARCHAR(32) NOT NULL
            );'''
        )


def get_data():
    """Возвращает все записи из бд"""
    conn = connect(DB)
    with conn:
        cur = conn.cursor()
        cur.execute(
            f'''
            SELECT * FROM users;
            '''
        )
    return cur.fetchall()


def add_user(login, hash_pass, salt):
    """
    Добавляет пользователя в бд
    """
    conn = connect(DB)
    with conn:
        cur = conn.cursor()
        cur.execute(
            f'''
            INSERT INTO users (login, password, salt) VALUES (?, ?, ?);
            ''',
            (login, hash_pass, salt)
        )


def get_reg_data(login):
    """
    По логину достает хеш и соль
    Если ничего не найдено вернет None
    """
    conn = connect(DB)
    with conn:
        cur = conn.cursor()
        cur.execute(
            f'''
            SELECT password, salt FROM users WHERE login=?;
            ''',
            (login,)
        )
    return cur.fetchone()


def get_hash(password, salt):
    return sha256(password.encode() + salt.encode()).hexdigest()


def add_user_to_db(login, password):
    salt = uuid4().hex
    hash_psw = get_hash(password, salt)
    add_user(login, hash_psw, salt)
    print(f'Здравствуйте, {login}, Вы зарегистрированы в системе')
    print(f'Хеш нового юзера: {hash_psw}')


def check_data(login, password):
    # Проверяем логин
    try:
        hash_psw_db, salt_db = get_reg_data(login)  # получаем хеш и соль из бд
    except TypeError:  # TypeError: cannot unpack non-iterable NoneType object
        answer = input('Такого пользователя в базе нет. Желаете зарегистрироваться с этими данными? (y/n) ')
        try:
            assert answer == 'y'  # если ответ положительный, то добавляем юзера в базу
            add_user_to_db(login, password)
        except AssertionError:
            # Ответ не 'y'
            print('Всего хорошего!')
        return
    # Проверяем пароль
    try:
        # сверяем хеши
        assert hash_psw_db == get_hash(password, salt_db)
        print(f'{login}, рады видеть Вас снова!')
    except AssertionError:
        # Введен неверный пароль
        print('Введен неверный логин или пароль')


if __name__ == '__main__':
    print(get_data())
    login, password = input('Введите логин: '), input('Введите пароль: ')
    check_data(login, password)
