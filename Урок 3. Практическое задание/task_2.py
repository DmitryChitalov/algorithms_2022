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


from hashlib import sha256
import modeldb


def user_auth():
    user_name = input('Введите логин: ')
    con = modeldb.sql_connection()
    if modeldb.user_exists(user_name, con):
        print('Введенный логин занят')
        return
    user_pass = input('Введите пароль: ')
    user_pass_hash = sha256(user_name.encode() + user_pass.encode()).hexdigest()
    modeldb.add_user(user_name, user_pass_hash, con)
    print('В базе данных хранится строка:', modeldb.get_user(user_name, con)[1])
    user_pass = input('Введите пароль еще раз для проверки: ')
    user_pass_hash = sha256(user_name.encode() + user_pass.encode()).hexdigest()
    if user_pass_hash != modeldb.get_user(user_name, con)[1]:
        print('Введенный пароль не совпадает')
    else:
        print('Вы ввели правильный пароль')


if __name__ == '__main__':
    user_auth()
