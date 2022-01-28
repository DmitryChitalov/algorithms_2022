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
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import sqlite3
import hashlib
from uuid import uuid4

with sqlite3.connect("mydb.sqlite") as conn:
    cursor = conn.cursor()
    cursor.execute("""create table if not exists users 
                        (id integer primary key,
                        name text not null unique,
                        salt text not null unique,
                        password text not null unique,
                        created_at text default current_timestamp )""")


def executeSql(SQL: str, name: str = None, salt: str = None, value: str = None) -> list:
    with sqlite3.connect("mydb.sqlite") as conn:
        cursor = conn.cursor()
        commands = {
            "insert": "insert into users(name, salt, password) values ('%s', '%s','%s')" % (name, salt, value),
            "select": "select name, salt, password from users where name is '%s'" % name
        }
        try:
            cursor.execute(commands[SQL])
        except KeyError:
            print("Provide a right command for executing")
        return cursor.fetchall()


def createHash(password: str, salt: str = None) -> tuple:
    """
    Algorithm sha256 for password hash, with salt generation based on username
    :param password: str
    :param username:str
    :return: tuple (salt, hash)
    """
    salt = uuid4().hex.encode("utf-8") if not salt else salt.encode("utf-8")
    byte_password = str(password).encode("utf-8")
    password_hash_obj = hashlib.sha256(salt + byte_password)
    return salt.decode("utf-8"), password_hash_obj.hexdigest()


def createUser(username: str, salt: str, pass_hash: str):
    SQL = "insert"
    executeSql(SQL, username, salt, pass_hash)


def check_user(username: str, password: str):
    SQL = "select"
    res = executeSql(SQL, username)
    if res:
        for credentials in res:
            username, salt, pass_hash = credentials
            _hash = createHash(salt=salt, password=password)

            if _hash == (salt, pass_hash):
                print("Bingo! \33[33m%s\33[0m with password \33[33m%s\33[0m match with hash: \33[33m%s\33[0m" \
                       % (username, password, _hash[1]))
                return
            else:
                print("Alert different hash \33[31m%s\33[0m != \33[31m%s\33[0m" %(_hash[1], pass_hash))
                return
    else:
        if input("create new user?").lower() in ["y", "yes"]:
            salt, pass_hash = createHash(password)
            createUser(username, salt, pass_hash)
            print("\33[32mWait a moment we'll authorize you...\33[0m")
            check_user(username, password)
        else:
            print("You need to Authorise yourself in system")
            return


if __name__ == "__main__":
    user = input("Username\n").lower()
    password = input("Password\n").lower()
    check_user(user, password)
