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


import hashlib
import json
import os
from uuid import uuid4


def add_users(user, password, name_file="base_users.json"):
    try:
        with open(name_file, "r+", encoding="UTF-8") as file_json:
            base = {}
            if os.stat(file_json.name).st_size != 0:
                # file_json.seek(0)
                base = json.loads(file_json.read())
                check_pass = base.get(user, False)
                if check_pass:
                    print(f"Пользователь {user} уже добавлен")
                    return
                else:
                    print(f"Пользователь {user} добавлен")
            salt = uuid4().hex
            hash_ = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
            base.update({user: (hash_, salt)})
            file_json.seek(0)
            json.dump(base, file_json, indent="\t")

    except FileNotFoundError:
        open(name_file, "w", encoding="UTF-8").close()
        add_users(user, password)


def asked_password(user, password):
    with open("base_users.json", "r", encoding="UTF-8") as file_json:

        if os.stat(file_json.name).st_size != 0:
            base = json.load(file_json)
            check_pass = base.get(user, False)
            if not check_pass:
                print(f"Пользователя {user} нет в базе")
                # add_users(user, password)
            else:
                hash_ = hashlib.sha256(password.encode() + check_pass[1].encode()).hexdigest()
                if check_pass[0] == hash_:
                    print(f"Пользователь {user} успешно авторизован")
                else:
                    print(f"Пользователь {user}, введен неверный пароль")
                print(f'Текущий хэш {hash_}, хеш из базы {check_pass[0]}')


for i in range(5):
    add_users(f"user{i}", f"password{i}")


asked_password("user1", "password1")
asked_password("user4", "password4")
asked_password("user6", "password1")
asked_password("user2", "password3")
add_users("user5", "password5")

