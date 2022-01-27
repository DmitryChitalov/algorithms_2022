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
import json
import hashlib

# salt = 'my_salt'
# dict_hash = {}
while True:
    salt = input('Введите логин: ')
    with open(".data_file.json", "r") as f:
        dict_hash = json.load(f)
    try:
        hash_pas = dict_hash[salt]
    except KeyError:
        print('Не правильный логин')
        break
    passwd = input('Введите пароль: ')
    res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
    print(f'В базе данных хранится строка: {hash_pas}')
    if hash_pas == res:
        print('Вы ввели правильный логин, пароль')
        break
    else:
        print('Не правильный пароль')
        break
# while True:
#     passwd = input('Введите пароль: ')
#     res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
#     print(f'В базе данных хранится строка: {res}')
#     passwd = input('Введите пароль еще раз для проверки: ')
#     res_1 = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
#     if res == res_1:
#         print('Вы ввели правильный пароль')
#         dict_hash[salt] = res
#         break
#     else:
#         break

# load_f = input('Хотите ли вы записать хэш в файл JSON? y/n : ')
# if load_f == 'y':
#     with open(".data_file.json", "w") as f:
#         json.dump(dict_hash, f, indent=4)
#     load_f = input('Хотите ли посмотреть что записалось в файл JSON? y/n : ')
#     if load_f == 'y':
#         with open(".data_file.json", "r") as f:
#             dict_hash = json.load(f)
#             print(dict_hash)
#             print(type(dict_hash))
# else:
#     print('Загрузка не удалась')

