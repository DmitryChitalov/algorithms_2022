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
from hashlib import sha256


user_password = input("Введите пароль: ")
salt = 'Hello world!'
hash_password = sha256(salt.encode() + user_password.encode('utf-8')).hexdigest()

print(f"В базе данных хранится строка:{hash_password}")
second_password = input("Введите пароль еще раз для проверки: ")

with open('password.csv', 'w', encoding='utf-8')as users_file:
    users_file.write(hash_password)

with open('password.csv', 'r', encoding='utf-8')as users_file:
    cur_pass = users_file.read()
    if sha256(salt.encode() + second_password.encode('utf-8')).hexdigest() == cur_pass:
        print('Вы ввели правильный пароль')
    else:
        print("не правильный")