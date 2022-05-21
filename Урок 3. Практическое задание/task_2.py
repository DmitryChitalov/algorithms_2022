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
###################################################

import json
from hashlib import pbkdf2_hmac
from binascii import hexlify


###################################################
# Здесь мы создаем хеш sha256 в пароле при помощи соли со 100,000 итераций.
def hash_gen(hash_name='sha256', password=b'123',
             salt=b'almaz',
             iterations=100000):
    obj = pbkdf2_hmac(hash_name,
                      password,
                      salt,
                      iterations)
    result = hexlify(obj)
    return result


###################################################
# Здесь мы записываем хеш пароля в json файл.
'''
data_users = {}
data_users['almaz'] = hash_gen().decode('utf-8')  # b -> str
with open('data_users.txt', 'w') as outfile:
    json.dump(data_users, outfile)

print(data_users['almaz'])
print(data_users['almaz'].encode('utf-8'))  # str -> b
'''
###################################################
# Здесь мы считываем хеш пароля из json файла.
with open('data_users.txt') as json_file:
    data = json.load(json_file)


###################################################
# Здесь мы вызываем основную программу.
def password_gen():
    user_login = input('Введите логин: ')
    pswd = input('Введите пароль: ')
    user_entrance = hash_gen(password=pswd.encode('utf-8'), salt=user_login.encode('utf-8'))

    try:
        if user_entrance == data[user_login].encode('utf-8'):
            repeat_pswd = input('Введите пароль еще раз для проверки: ')
            user_entrance = hash_gen(password=repeat_pswd.encode('utf-8'), salt=user_login.encode('utf-8'))
            if user_entrance == data[user_login].encode('utf-8'):
                print('Вы ввели правильный пароль.')
            else:
                print('Вы ввели неправильный пароль.')
                password_gen()
        else:
            print('Вы ввели неправильный пароль.')
            password_gen()
    except KeyError as e:
        print(f"Пользователь с логином: {e} не зарегистрирован.")


password_gen()
