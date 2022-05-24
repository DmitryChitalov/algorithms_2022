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
import binascii
import csv

# salt_bytes = b's'
# passw_bytes = b'123'
salt = 's'
passw = input('Введите пароль ')
passw_bytes = passw.encode(encoding='utf-8')
salt_bytes = salt.encode(encoding='utf-8')
passw_obj = hashlib.pbkdf2_hmac(
    hash_name='sha256',
    password=passw_bytes,
    salt=salt_bytes,
    iterations=100
)
passw_hash = binascii.hexlify(passw_obj).decode('utf-8')
print('Сохранённый пароль:', passw_hash)

with open('passw.csv', mode='w', encoding='utf-8') as passw_csv:
    writer = csv.writer(passw_csv)
    writer.writerow([passw_hash])

passw = input('Введите пароль ещё раз ')
passw_bytes = passw.encode(encoding='utf-8')
salt_bytes = salt.encode(encoding='utf-8')
passw_obj = hashlib.pbkdf2_hmac(
    hash_name='sha256',
    password=passw_bytes,
    salt=salt_bytes,
    iterations=100
)
passw_hash = binascii.hexlify(passw_obj).decode('utf-8')

with open('passw.csv', encoding='utf-8') as passw_csv:
    reader = csv.reader(passw_csv)
    passw_hash_read = [row for row in reader][0][0]

if passw_hash == passw_hash_read:
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели неправильный пароль')
