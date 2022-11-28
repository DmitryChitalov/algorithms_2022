# """
# Задание 2.
#
# Ваша программа должна запрашивать пароль
# Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
# Для генерации хеша обязательно нужно использовать криптографическую соль
# Обязательно выведите созданный хеш
#
# Далее программа должна запросить пароль повторно и вновь вычислить хеш
# Вам нужно проверить, совпадает ли пароль с исходным
# Для проверки необходимо сравнить хеши паролей
#
# ПРИМЕР:
# Введите пароль: 123
# В базе данных хранится строка: 555a3581d37993843efd4eba1921
# f1dcaeeafeb855965535d77c55782349444b
# Введите пароль еще раз для проверки: 123
# Вы ввели правильный пароль
#
# Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
# или, если вы уже знаете, как Python взаимодействует с базами данных,
# воспользуйтесь базой данный sqlite, postgres и т.д.
# п.с. статья на Хабре - python db-api
# """
import hashlib
import sqlite3 as sql
from uuid import uuid4

con = sql.connect('test.sql')

# cur.execute('DROP TABLE IF EXISTS "passwords"')

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS "passwords" ("password" STRING UNIQUE, "cache" STRING)')
    try:
        cur.execute(f'INSERT INTO "passwords" (password, cache) VALUES ("salt", "{str(uuid4())}" )')
    except sql.IntegrityError:
        pass
    finally:
        con.commit()


def get_data(password):
    with con:
        cur = con.cursor()
        cur.execute(f'SELECT "cache" FROM "passwords" WHERE password = "{password}"')
        data = cur.fetchall()
        return str(data[0][0]) if data else None


def get_salt():
    salt = get_data('salt')
    return str(salt[0][0])


def write_data(password: str, cache: str):
    with con:
        cur = con.cursor()
        try:
            cur.execute(f"INSERT INTO passwords VALUES ('{password}','{cache}')")
        except sql.IntegrityError:
            print("Password already in DB")
            return None

        con.commit()


def create_cache(password, salt):
    return hashlib.sha256(password.encode() + salt.encode()).hexdigest()


def main():
    password = input('Введите пароль : ')
    local_cache = create_cache(password, get_salt())
    print(f'В базе данных хранится строка: \n{local_cache}')
    db_cache = get_data(password)
    if not db_cache:
        write_data(password, local_cache)

    password = input("Введите пароль еще раз : ")
    local_cache = create_cache(password, get_salt())
    db_cache = get_data(password)

    if local_cache == db_cache:
        print("Пароль верный")
        return
    print("Пароль не верный")


if __name__ == '__main__':
    main()
