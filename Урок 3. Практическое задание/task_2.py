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

password = input("Input password ")
static_sault = input("some words - ")
hash_object = hashlib.sha256(static_sault.encode('utf-8') + password.encode('utf-8'))
hex_dig = hash_object.hexdigest()
print(hex_dig)

a = hex_dig

with open("myfilepass.csv", "w") as file:
    s = file.write(a)
with open("mysault.csv", "w") as file:
    my_sault = file.write(static_sault)

password2 = input("Input password ")

with open("mysault.csv", "r") as file:
    my_sault_f = file.readline()
sault_num = ''.join(my_sault_f)

hash_object2 = hashlib.sha256(sault_num.encode('utf-8') + password2.encode('utf-8'))
hex_dig2 = hash_object2.hexdigest()
print(hex_dig2)

with open("myfilepass.csv", "r") as file:
    f = file.readline()
num = ''.join(f)

if hex_dig2 == num:
    print('Вы ввели правильный пароль')
else:
    print("Not")
