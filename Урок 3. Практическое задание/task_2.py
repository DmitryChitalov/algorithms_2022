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
п.с. статья на Хабре - python db-apiс
"""
import hashlib
import json
data = {}

salt = input('Enter your login: ')
password = input('Enter your password: ')
res = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
data[salt] = res
print(f'Hash is: {res}')

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

salt = input('Enter your login and password again. Login: ')
password2 = input('Password: ')
res2 = hashlib.sha256(salt.encode() + password2.encode()).hexdigest()
print(f'Second hash is: {res2}')
with open('data.txt') as json_file:
    data = json.load(json_file)
output = 'Password accepted' if data[salt] == res2 else 'Password denied'
print(output)