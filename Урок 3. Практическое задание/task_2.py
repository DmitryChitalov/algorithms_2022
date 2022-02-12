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
"""library = {'gogo': '2b3993b869bf9fe5fbf66c62cd3219771d028e1a03787e52d8c8f482cf2e03d7',  # 123
           'wow': '7bde3a244ee3d33225d6df473aba2f539e3f84460bfb78bd6a3e77d31b259218',  # 456
           'qwerty': 'fab6d43655bbca6e71240739f3aad3f9050b5a051924ab3a3bd17a9678525a74'  # 789
           }


def authentication():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    password_two = input('Введите пароль еще раз: ')
    hash_password = sha256(login.encode() + password.encode()).hexdigest()
    return login, hash_password


authentication()"""
import sqlite3
from hashlib import sha256

def database_connection():
    conn = sqlite3.connect('Chinook_Sqlite.sqlite')
    cursor = conn.cursor()
    conn.close()




