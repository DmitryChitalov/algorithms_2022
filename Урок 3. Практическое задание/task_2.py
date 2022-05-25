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
import csv

def savePassword(password):
    salt = uuid4().hex
    res = hashlib.sha256(salt.encode('utf8') + password.encode('utf8')).hexdigest()
    print 'В базе данных хранится строка: ' + str(res)

    with open('names.csv', 'w') as csvfile:
        keyResList = [salt, res]
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerows(keyResList)

    checkPassword()


def checkPassword():
    list_ = []
    password = str(raw_input('Введите пароль еще раз для проверки: '))
    with open('names.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            list_.append(''.join(row))

    res = hashlib.sha256(list_[0] + password.encode('utf8')).hexdigest()

    if list_[1] == res:
        print 'Вы ввели правильный пароль'
    else:
        print 'Вы ввели некорректный пароль'

if name == 'main':
    newPassword = str(raw_input('Введите пароль: '))
    savePassword(password=newPassword)
