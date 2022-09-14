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
import json

data_for_file = {'salt': 'операция Ы', 'hash': ''}  # создаем файл, в котором будет храниться соль и хеш
with open("secret_file.json", "w") as parole_file:
    json.dump(data_for_file, parole_file)


def get_parole():
    with open("secret_file.json", "r") as parole_file:
        salt_from_file = json.load(parole_file)['salt']  # достаем из файла соль
    parole = input('Введите пароль: ')
    hash_parole = hashlib.sha256(salt_from_file.encode('utf-8') + parole.encode('utf-8')).hexdigest()  # получаем хеш
    with open("secret_file.json", "w") as parole_file:  # записываем в файл хеш
        data_for_file['hash'] = hash_parole
        json.dump(data_for_file, parole_file)
    check_parole = input('Введите пароль повторно для проверки: ')
    with open("secret_file.json", "r") as parole_file:
        data = json.load(parole_file)  # достаем данные из файла
    if hashlib.sha256(data['salt'].encode('utf-8') + check_parole.encode('utf-8')).hexdigest() == data['hash']:
        return 'ok'  # сравниваем хеш пароля введенного второй раз с данными из файла
    else:
        return 'Проверка провалилась'


print(get_parole())
