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
    password = input('Введите пароль: ')
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=password.encode('utf-8'),
                      salt=b'pass',
                      iterations=100)
    result = str(hexlify(obj))
    print(fr'СОЗДАН ХЕШ ПАРОЛЯ: {result}')
    f = open('passwd.csv', 'w')
    f.write(result)
    f.close()
    password_2 = input('Введите повтрно пароль для проверки: ')
    obj_2 = pbkdf2_hmac(hash_name='sha256',
                        password=password_2.encode('utf-8'),
                        salt=b'pass',
                        iterations=100)
    res_2 = str(hexlify(obj_2))
    f = open('passwd.csv', 'r')
    res = f.readline()
    f.close()
    if res == res_2:
        return 'Пароль верный.'
    else:
        return 'Пароль не верный, попробуйте еще раз!'


print(gen_pass())
