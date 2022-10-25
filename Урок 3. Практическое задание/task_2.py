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
import json
import hashlib
from uuid import uuid4

pw_1 = str(input('enter password: '))
salt = uuid4().hex

# записываем пароль в созданные файл
with open('pass.json', 'w+') as f:
    json.dump(hashlib.sha256(pw_1.encode('utf-8')).hexdigest() + salt, f)

# вытаскиваем пароль из файла
with open('pass.json') as f:
    pw_1_check = f.read()

print(f'String from DataBase: {pw_1_check}')

pw_2 = str(input('enter password again: '))

pw_2_check = json.dumps(hashlib.sha256(pw_2.encode('utf-8')).hexdigest() + salt)

if pw_2_check == pw_1_check:
    print('Password is OK')
else:
    print('Wrong password')
