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

password = input('Введите пароль: ')
salt = '578'
res = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
print(res)
with open('password.csv', 'w') as file:
    file.write(res)
    file.write('\n')
my_pass = input('Введите пароль еще раз для проверки: ')
res_2 = hashlib.sha256(salt.encode() + my_pass.encode()).hexdigest()
with open('password.csv', 'r') as file:
    pass_lst = [line.strip() for line in file]
    if res_2 in pass_lst:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели не правильный пароль')
