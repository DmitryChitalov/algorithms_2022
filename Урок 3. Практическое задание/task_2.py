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
import sqlite3
import hashlib

# Создаём` файл БД 'task_2.db'. За соединение будет отвечать переменная 'conn'.
conn = sqlite3.connect('task_2.db')
# Cоздаём объект курсор для направления запросов к БД
cur = conn.cursor()
# Проверяем, есть ли такая таблица и удаляем её, если есть.
# cur.execute("""DROP TABLE IF EXISTS users;""")
# Создаём таблицу
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   name TEXT,
   login TEXT,
   password TEXT);
""")
# Сохраняем изменения
conn.commit()
# Закрываем соединение с БД.
conn.close()


def registration():
    us_name = input('Введите имя пользователя: ')
    us_login = input('Введите логин: ')
    us_password = input('Введите пароль: ')
    us_password = hashlib.sha256(us_login.encode() + us_password.encode()).hexdigest()
    conn = sqlite3.connect('task_2.db')
    cur = conn.cursor()
    sqlite_insert_with_param = """
    INSERT INTO users(name, login, password) 
           VALUES(?, ?, ?);"""
    us_data = (us_name, us_login, us_password)
    cur.execute(sqlite_insert_with_param, us_data)
    conn.commit()
    sql_select_query = """SELECT password FROM users
                                 WHERE name = ?;"""
    cur.execute(sql_select_query, (us_name,))
    pas = cur.fetchone()
    print(f'В базе данных хранится строка: {pas[0]}')
    conn.close()


def authorization():
    us_login = input('Введите логин: ')
    us_password = input('Введите пароль: ')
    us_password = hashlib.sha256(us_login.encode() + us_password.encode()).hexdigest()
    conn = sqlite3.connect('task_2.db')
    cur = conn.cursor()
    sql_select_query = """SELECT password FROM users
                                WHERE login = ?;"""
    cur.execute(sql_select_query, (us_login,))
    us_password_1 = cur.fetchone()
    us_password_1 = us_password_1[0]
    if us_password_1 == us_password:
        print('Добро пожаловать!')
    else:
        print(f'Введён неверный пароль для пользователя {us_login} '
              f'или пользователь с таким логином не зарегистрирован.')
    conn.close()


if __name__ == "__main__":
    registration()
    authorization()
