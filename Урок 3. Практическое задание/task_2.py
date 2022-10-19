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
from mysql.connector import connect, Error

# устанавливаем соединение с сервером MySQL
# создаем БД и таблицу для хранения email и паролей пользователей
def db_create():
    try:
        with connect(
            host = 'localhost',
            user = input('Введите пользователя БД: '),
            password = input('Введите паролья для БД: ')
        ) as connection:
            create_db = "CREATE DATABASE IF NOT EXISTS python_tasks"
            create_tbl = "CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY," \
                         " email VARCHAR(200) NOT NULL UNIQUE, password VARCHAR(300) NOT NULL)"

            with connection.cursor() as cursor:
                cursor.execute(create_db)
                cursor.execute('USE python_tasks')
                cursor.execute(create_tbl)
                for tbl in cursor:
                    print(tbl)
            connection.commit()
    except Error as e:
        print(e)


def user_data():
    login = input('Для регистрации введите Ваш логин: ')
    passw = input('Введите пароль: ')
    salt = 'any_salt'.encode()
    passw_hash = hashlib.sha256(salt + passw.encode()).hexdigest()
    return login, passw_hash


# функция регистрации (занесения в БД) новых пользователей
def user_registration():
    try:
        with connect (
            host = 'localhost',
            user = 'root',
            password = '1201',
            database = 'python_tasks'
        ) as connection:
        #     user_login, user_passw = user_data()
            add_user = "INSERT INTO users (email, password) VALUES (%s, %s)"
            with connection.cursor() as cursor:
                cursor.execute(add_user, user_data())
            connection.commit()

    except Error as e:
        print(e)


# просмотр содержимого таблицы
def users_data_db():
    with connect (host = 'localhost', user = 'root', password = '1201', database = 'python_tasks') as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * from users')
            for line in cursor:
                print(line)

        connection.commit()


# функция получения хэша пароля из БД
def passw_hash_get(login):

    with connect (host = 'localhost', user = 'root', password = '1201', database = 'python_tasks') as connection:
        passw_db_select = "SELECT password FROM users WHERE email = %s;"
        with connection.cursor() as cursor:
            cursor.execute(passw_db_select, (login,))
            passw_hash = cursor.fetchone()
        connection.commit()
    return passw_hash


# Функция входа в аккаунт (проверки пароля)
def login_user():
    login = input('Введите email для авторизации: ')
    passw = input('Введите Ваш пароль для входа в аккаунт: ')
    salt = b'any_salt'
    passw_hash = hashlib.sha256(salt + passw.encode()).hexdigest()
    passw_db = passw_hash_get(login)[0]
    if passw_hash == passw_db:
        return print('Пароль верный!')
    else:
        return print('Неправильный пароль!')


if __name__ == '__main__':
    print(passw_hash_get('sample1'))
    login_user()
