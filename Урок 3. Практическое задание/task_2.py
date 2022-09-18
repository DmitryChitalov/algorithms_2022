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

salt = '1480rtyu'

def my_hash(salt='111'):
    password = input('')
    new_hash = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
    return new_hash

print('Введите пароль:')
my_hash_one = my_hash()
print(my_hash_one)
with open('fales.JSON', 'w', encoding='utf-8') as w:
        w.write(my_hash_one)
print('Введите пароль для проверки:')
my_hash_two = my_hash()
print(my_hash_two)
with open('fales.JSON', 'r', encoding='utf-8') as r:
        repit_hash = r.readline()
if my_hash_two == repit_hash:
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели ошибочный пароль')