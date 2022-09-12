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


def get_hash(salt='111'):
    password = input('')
    p_hash = hashlib.sha256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    return p_hash


salt = 'salt'

print('Введите пароль:')
first_hash = get_hash()
print(first_hash)
with open('key.csv', 'w', encoding='utf-8') as w:
        w.write(first_hash)

print('Введите пароль для проверки:')
second_hash = get_hash()
print(second_hash)
with open('key.csv', 'r', encoding='utf-8') as r:
        try_hash = r.readline()
if second_hash == try_hash:
    print('Password is correct. Welcome on board.')
else:
    print('Wrong password. Try later.')
