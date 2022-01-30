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


У нас на курсе БД было знакомство с Redis. С тех пор хочется его где-нибудь применить.
Думаю он вполне подойдет для этой задачи.
Идея такая: при старте заружать данные в редис, с целью снижения затрат на процедуры
аутентификации и авторизации, но может так и не делается)

"""

import redis
from random import randint
from hashlib import sha256


def sha256_with_salt(salt, message):
    return sha256(salt.encode('utf-8') + message.encode('utf-8')).hexdigest()


def validate(password, vault):
    pwd_data = vault.lrange(password, 0, 1)
    if pwd_data:
        salt, hash = vault.lindex(password, 0), vault.lindex(password, 1)
        return hash == sha256_with_salt(salt, password)
    else:
        salt = str(randint(1, 100000))
        hash = sha256_with_salt(salt, password)
        vault.rpush(password, salt, hash)

        return hash


if __name__ == '__main__':
    vault = redis.StrictRedis(host='192.168.25.108',
                              port=6379,
                              password='',
                              charset='utf-8',
                              decode_responses=True)

    password = input('Введите пароль: ')
    print(validate(password, vault))
    password = input('Введите пароль еще раз для проверки: ')
    print(f'Вы ввели {"верный" if validate(password, vault) else "неверный"} пароль')