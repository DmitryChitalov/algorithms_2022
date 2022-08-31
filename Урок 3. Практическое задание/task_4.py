"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
import os

from collections import defaultdict

CACHE_EXAMPLE = defaultdict(int)


def enter_url(url_address):
    old_key = CACHE_EXAMPLE[url_address]
    if old_key:
        print('Ключ уже есть: ')
        key_from_storage = old_key[32:]  # 32 является длиной соли
        return key_from_storage
    else:
        print('Ключ будет добавлен: ')
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha512', url_address.encode('utf-8'), salt, 100000)
        storage = salt + key
        CACHE_EXAMPLE[url_address] = storage
        return key


# определение ключей и значений
print(enter_url('url_address_1'))
print(enter_url('url_address_2'))
print(enter_url('url-address_3'))
print('CACHE_EXAMPLE: ', CACHE_EXAMPLE)
print(enter_url('url_address_1'))
print(enter_url('url_address_2'))
print(enter_url('url-address_3'))
