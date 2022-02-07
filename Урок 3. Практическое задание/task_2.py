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
from hashlib import sha256
import json

import password as password


def greeting():
    print('Приветствуем на нашем сайте!')
    user = input('Введите ваш логин для регистрации: ')

    def check_pass():
        while True:
            pswrd = input('Введите пароль для регистрации: ')
            check_pswrd = input('Повторите пароль: ')
            if pswrd == check_pswrd:
                return pswrd
            print('Упс... Вы где-то ошиблись, попробуйте ещё раз!')

    user_password = check_pass()
    salt = 'protection'
    print("Вы успешно зарегистрированы!")
    return user, user_password, salt


user, user_password, salt = greeting()
data, hash_pswrd = {}, (sha256(salt.encode() + user_password.encode()).hexdigest())

data[user] = {
    'login': user,
    'salt': salt,
    'pswrd': hash_pswrd
}

with open('user_db.json', 'w') as users_db:
    json.dump(data, users_db)

with open('user_db.json', 'r') as db:
    u_data = json.load(db)
print('Проверка данных пользователя!')
usr_check = input('Введите свой логин: ')
try:
    if usr_check == u_data[usr_check]['login']:
        pswrd_check = sha256(u_data[usr_check]['salt'].encode() + (input('Введите свой пароль:')).encode()).hexdigest()
        try:
            if pswrd_check == u_data[usr_check]['pswrd']:
                print('Вы успешно прошли проверку!')
        except:
            print('Пароль введён не верно!')
except:
    print('Такого пользователя не существует!')
