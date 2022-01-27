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
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import json
from uuid import uuid4
import hashlib


salt = uuid4().hex
password = str(input('Введите пароль: '))
password_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
print(f'В базе данных хранится строка: {password_hash}')

password_data = {'hash': password_hash, 'salt': salt}
password_data_as_str = json.dumps(password_data)
try:
    with open('data.json', 'x', encoding='utf-8') as f:
        f.write(password_data_as_str)
except FileExistsError:
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(password_data_as_str)

# print(password_data_as_str)


with open('data.json', 'r', encoding='utf-8') as f:
    data_as_str = f.read()

temp_data = json.loads(data_as_str)

password_verif = str(input('Введите пароль еще раз для проверки: '))
password_verif_hash = hashlib.sha256(temp_data['salt'].encode() + password_verif.encode()).hexdigest()

if password_verif_hash == password_hash:
    print('Вы ввели правильный пароль')
else:
    print('Пароли не совпадают')
