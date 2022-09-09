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
from hashlib import sha256
import csv
log = input('Введите Login: ')
pas = input('Введите Password: ')
pas_ch = sha256(pas.encode() + log.encode()).hexdigest()
print(pas_ch)
with open('verify.csv', mode="w+", encoding='utf-8') as verify:
    fieldnames = ['login', 'pass_h']
    writer = csv.DictWriter(verify, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(dict(login=log, pass_h=pas_ch))
with open('verify.csv', mode="r", encoding='utf-8') as f2:
    pas2 = input('Введите еще раз Password: ')
    pas_ch2 = sha256(pas.encode() + log.encode()).hexdigest()
    reader = csv.DictReader(f2)
    for row in reader:
        if row['login'] == log and row['pass_h'] == pas_ch2:
            print('Вы ввели правильный пароль')
