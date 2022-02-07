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

# Имортирую необходимые модули
from hashlib import sha256
import mysql.connector

# Заранее создал БД и в ней таблицу (в ней три столбца: ID(serial, PK), login, password - в него будем записывать ХЭШ)
# Создал пользователя-админа (через него будем подключаться к БД)
# -u python_pass -p 123


connection = mysql.connector.connect(
    host='localhost',
    user='python_pass',
    password='123',
    database='passwd'
)
mycursor = connection.cursor()


def insert_login_pass():
    """Функция вности Логин и Пароль в БД
    (пароль хэширует + соль Логин)"""
    try:
        login = input('Введите логин: ')
        mycursor.execute(f'INSERT INTO log_pass (login, password) values ("{login}", '
                         f'"{sha256(input("Пароль ").encode("utf-8") + login.encode("utf-8")).hexdigest()}")')
        connection.commit()
    except mysql.connector.Error as e:
        print(e)


def passwd_check():
    """Функция проверяющая верно ли введет пароль"""
    login = input('Логин для проверки ')
    pass_hash = sha256(input('Пароль для проверки ').encode('utf-8') +
                       login.encode('utf-8')).hexdigest()
    mycursor.execute(f'SELECT password FROM log_pass where login = "{login}"')
    try:
        if mycursor.fetchone()[-1] == pass_hash:
            print('Пароли совпадают')
        else:
            print('Пароли не совпадают')
    except TypeError:
        print('Логина не существует')
    _continue = (input('Продолжить? y-да '))
    if _continue == 'y':  # Рекурсия для повторного ввода
        passwd_check()


# insert_login_pass()
passwd_check()
