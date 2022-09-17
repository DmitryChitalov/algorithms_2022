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

"""Если пользователь не зарегистрирован, то программа просто проверяет полученные хеши на индентичность 
и вносит данные в базу данных, выводит на экран хеш.
Если пользователь уже есть в базе данных, тогда функция сверяет хеш в базе данных с хешами,
полученным из введенных данных"""


import hashlib, uuid, sqlite3
def passwd_check():
    login = input("Введите логин")
    passwd = input("Введите пароль")
    salt = 'my_salt'
    hashed_passwd = hashlib.sha256(passwd.encode() + salt.encode()).hexdigest()
    passwd_2 = input("Введите пароль еще раз для проверки:")
    hashed_passwd_2 = hashlib.sha256(passwd_2.encode() + salt.encode()).hexdigest()

    conn = sqlite3.connect('Chinook_Sqlite.sqlite')
    cursor = conn.cursor()
    cursor.execute("""create table if not exists users (
        id SERIAL PRIMARY KEY,
        lgn VARCHAR(100),
        password_hash VARCHAR(100)
    ); """)
    cursor.execute("select password_hash from users where lgn =?", (login,))
    res = cursor.fetchall()
    if res:
        if hashed_passwd_2 == str(res[0][0]) and hashed_passwd_2 == hashed_passwd:
            print("Вы ввели правильный пароль")
        else:
            print("Вы ввели неправильный пароль! Попробуйте еще раз")
            conn.close()
            passwd_check()
    else:
        if hashed_passwd == hashed_passwd_2:
            cursor.execute("insert into users(lgn, password_hash) values (?, ?)", (login, hashed_passwd,))
            conn.commit()
            print(f'Пароли совпадают! Регистрация прошла успешно!'
                  f'В базе данных хранится строка: {hashed_passwd}')
            conn.close()
        else:
            print("Пароли не совпадают! Попробуйте еще раз!")
            conn.close()
            passwd_check()
passwd_check()
