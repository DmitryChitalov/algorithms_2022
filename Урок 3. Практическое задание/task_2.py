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
import json

def get_login():
    login = input(f'Enter your login, please: ')
    return login.lower()

def get_password():
    password = input(f'Enter your password, please: ')
    return password

def get_access():
    print('Getting access')
    user_login = get_login()
    with open('passwords.json', 'r') as f:
        dct = json.load(f)
    if user_login in dct:
        user_password = get_password()
        password_hash = hashlib.sha256(user_login.encode() + user_password.encode()).hexdigest()
        if dct[user_login] == password_hash:
            print('access granted')
        else:
            print('access denied')
    else:
        print('user does not exist')



def new_user():
    print('New user registration')
    user_login = get_login()
    try:
        with open('passwords.json', 'r') as f:
            dct = json.load(f)
            if user_login in dct:
                print('User exists. Choose another name')
                return None
    except FileNotFoundError:
        with open('passwords.json', 'w') as f:
            json.dump({}, f)

    user_password = get_password()
    password_hash = hashlib.sha256(user_login.encode() + user_password.encode()).hexdigest()


    with open('passwords.json', 'r') as f:
        dct = json.load(f)
    with open('passwords.json', 'w') as f:
        dct[user_login] = password_hash
        json.dump(dct, f)




new_user()

get_access()





