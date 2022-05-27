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
from hashlib import pbkdf2_hmac
from binascii import hexlify
import json


def hash_creator(password, salt):
    return hexlify(pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 1))


"""
Создали файл JSON, пароль pass

data = {
	'salt': 'my_salt',
	'password' : 'c7915718244ceb09c69758bf76260b722a1e29a7f1773c6af45e581babd46fdb' 
}

with open('data_file_json', 'w',) as f:
	json.dump(data, f)
"""

user_pass_attempt_1 = input('Введите пароль: ')

with open('data_file_json', 'r', ) as f:
    my_salt = json.load(f)['salt']

print(f'В базе данных хранится строка: {hash_creator(user_pass_attempt_1, my_salt)}')

user_pass_attempt_2 = input('Введите пароль еще раз для проверки: ')

with open('data_file_json', 'r', ) as f:
    my_pass = json.load(f)['password']

if hash_creator(user_pass_attempt_2, my_salt) == bytes(my_pass, encoding='utf-8'):
    print('Вы ввели правильный пароль')
else:
    print('Пароль не верный')
