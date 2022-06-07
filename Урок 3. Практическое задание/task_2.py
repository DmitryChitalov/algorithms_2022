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


from uuid import uuid4
import hashlib


salt = uuid4().hex
user_pass = input('Введите пароль: ')
pass_hash = hashlib.sha256(salt.encode('utf-8') + user_pass.encode('utf-8')).hexdigest()
with open('pass_hash.csv', 'w', encoding='utf-8') as file:  # не могу вставить сюда чтение из файла
    # (даже с r+, не выводит строку). Поэтому для чтения файла пришлось заново открыть этот файл
    file.write(pass_hash)
with open('pass_hash.csv', 'r', encoding='utf-8') as file:
    str_file = file.read()
    print(f'В базе данных хранится строка: {str_file}.')
check_pass = input('Введите пароль еще раз для проверки: ')
check_hash = hashlib.sha256(salt.encode('utf-8') + check_pass.encode('utf-8')).hexdigest()
with open('pass_hash.csv', 'r', encoding='utf-8') as file:
    if file.read() == check_hash:
        print('Вы ввели правильный пароль.')
    else:
        print('Вы ввели неверный пароль.')
