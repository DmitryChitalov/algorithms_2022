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

from hashlib import pbkdf2_hmac
from binascii import hexlify

def password_hash(p):
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=p.encode('utf-8'),
                      salt=b'any_salt_1',
                      iterations=100000)
    return hexlify(obj)


def reg():
    login = input('Введите логин: ')
    p = input('Введите пароль: ')
    return login, password_hash(p)


# Далее программа должна запросить пароль повторно и вновь вычислить хеш
def password_reentry(phash):
    p = input('Введите пароль еще раз для проверки: ')
    if password_hash(p) == phash:
        print(f'Вы ввели правильный пароль.')
        return True
    else:
        return False


# Для проверки необходимо сравнить хеши паролей
def check_db(login, phash):
    from mysql.connector import connect, Error

    try:
        with connect(
                host="localhost",
                user="python",
                password="python",
                database="sample",
        ) as connection:
            with connection.cursor() as cur:
                cur.execute(f'SELECT hash FROM users WHERE name="{login}";')
                result = cur.fetchall()
                for row in result:
                    login_found = True
                    pass_correct = phash.decode() == row[0]
                    return login_found, pass_correct
    except Error as e:
        print(e)

    return False, False


# Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
# или, если вы уже знаете, как Python взаимодействует с базами данных,
def write_db(login, phash):
    from mysql.connector import connect, Error

    try:
        with connect(
                host="localhost",
                user="python",
                password="python",
                database="sample",
        ) as connection:
            with connection.cursor() as cur:
                cur.execute(f'INSERT INTO users (name,hash) VALUES ("{login}","{phash.decode()}")')
                connection.commit()
    except Error as e:
        print(e)


def main():
    login, entered_password_hash = reg()
    login_found, pass_correct = check_db(login, entered_password_hash)
    if not login_found:
        if password_reentry(entered_password_hash):
            write_db(login, entered_password_hash)
            print(f'Хэш пароля: {entered_password_hash.decode()}')
        else:
            print('Пароли не совпадают. Попробуйте снова.')
    else:
        if pass_correct:
            print(f'Авторизация прошла успешно')
        else:
            print('Неверный пароль. Попробуйте снова.')


main()
