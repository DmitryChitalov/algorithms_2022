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


def gen_pass():
    password_user = input('Введите пароль: ')

    def password_hash(password):
        obj = pbkdf2_hmac(hash_name='sha256',
                          password=password.encode('utf-8'),
                          salt=b'pass',
                          iterations=100)
        return str(hexlify(obj))

    print(fr'СОЗДАН ХЕШ ПАРОЛЯ: {password_hash(password_user)}')
    f = open('passwd.csv', 'w')
    f.write(password_hash(password_user))
    f.close()
    password_2 = input('Введите повтрно пароль для проверки: ')
    f = open('passwd.csv', 'r')
    res = f.readline()
    f.close()
    if res == password_hash(password_2):
        return 'Пароль верный.'
    else:
        return 'Пароль не верный, попробуйте еще раз!'


print(gen_pass())
