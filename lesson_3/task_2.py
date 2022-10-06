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
import sqlite3

# Создаём` файл БД 'example.db'.
conn = sqlite3.connect('example.db')
# Cоздаём объект курсор для направления запросов к БД
cur = conn.cursor()
# Создаём таблицу
cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
        login TEXT,
        password TEXT
        );""")
# Сохраняем изменения
conn.commit()
# Закрываем соединение с БД.
conn.close()


def authorisation():
    login = input('Введите login: ')
    psw = input('Введите пароль: ')
    salt = b'salt'
    hash_psw = hashlib.sha256(salt + psw.encode()).hexdigest()
    return login, hash_psw


def write_data():
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    login, hash_psw = authorisation()
    sqlite_insert_with_param = """
            INSERT INTO users(
            login,
            password)
            VALUES(?, ?);"""
    user_data = (login, hash_psw)
    cur.execute(sqlite_insert_with_param, user_data)
    conn.commit()
    cur.execute("SELECT password FROM users WHERE login = ?", (login,))
    hash_psw = cur.fetchone()
    print(f'В базе данных хранится строка: {hash_psw[0]}')
    conn.close()


def psw_verify():
    login, hash_psw = authorisation()
    salt = b'salt'
    psw_ver = input('Введите пароль еще раз для проверки: ')
    hash_psw_verify = hashlib.sha256(salt + psw_ver.encode()).hexdigest()
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    sql_select_query = """SELECT password FROM users WHERE login = ?;"""
    cur.execute(sql_select_query, (login,))
    hash_psw = cur.fetchone()
    hash_psw = hash_psw[0]
    if hash_psw == hash_psw_verify:
        print(f'Вы ввели правильный пароль')
    else:
        print(f'Введенные пароли не совпадают, повторите ввод')
    conn.close()


if __name__ == "__main__":
    write_data()
    psw_verify()
    