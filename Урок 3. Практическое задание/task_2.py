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
import csv
import hashlib
import uuid
import csv


def activation(login, parol):
    salt = uuid.uuid4().hex
    hash = hashlib.sha256(parol.encode("utf-8") + salt.encode("utf-8")).hexdigest()
    print('Хеш вашего пароля ', hash)
    with open("parol.csv", 'a') as file:
        table = csv.writer(file)
        table.writerow([login, salt, hash])


def enter(login, parol):
    with open('parol.csv', 'r') as file:
        data_table = csv.reader(file)
        data = {}
        for i in data_table:
            if not i:
                data[i[0]] = [i[1], i[2]]
        if login not in data:
            return "Вашего логина нет в системе"
        hash = hashlib.sha256(parol.encode("utf-8") + data[login][0].encode("utf-8")).hexdigest()
        if hash == data[login][1]:
            return "Вы ввели правильный пароль"
        return "Вы ввели неправильный пароль"


activation(input("Введите логин: "), input("Введите пароль: "))
activation(input("Введите логин: "), input("Введите пароль: "))
print(enter(input("Введите логин: "), input("Введите пароль: ")))
