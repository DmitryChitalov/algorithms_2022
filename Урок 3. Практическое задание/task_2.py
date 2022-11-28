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
from os.path import exists
from hashlib import sha256
import json


def get_user_data():
    user_data = {}
    new_login = input("Введите логин: ")
    new_pssw = input("Введите пароль: ")
    hash_pssw = sha256(new_login.encode() + new_pssw.encode()).hexdigest()
    user_data[new_login] = hash_pssw
    return user_data


def fn_add_password():
    user_data = get_user_data()
    user_check = ''
    if exists("passwords.json"):
        with open("passwords.json", "r") as json_file:
            all_data = json.load(json_file)
            for dict_file in all_data:
                for key_file, val_file in dict_file.items():
                    for key_user, val_user in user_data.items():
                        if key_file == key_user:
                            user_check = key_user
                            pass_check = val_user
            if user_check:
                print("Вы уже есть в базе.")
                pass_2check = input("введите пароль еще раз для проверки:")
                pass_2check = sha256(user_check.encode() + pass_2check.encode()).hexdigest()
                if pass_2check == pass_check:
                    print("Вы ввели правильный пароль")
                else:
                    print("Вы ввели неправильный пароль")
            else:
                all_data.append(user_data)
                with open('passwords.json', 'w') as outfile:
                    json.dump(all_data, outfile)
    else:
        all_data = []
        all_data.append(user_data)
        with open('passwords.json', 'w') as outfile:
            json.dump(all_data, outfile)


fn_add_password()



