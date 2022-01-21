"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет.

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
import os
from pymongo import MongoClient


class Cache:
    cache = {}
    salt = {}

    @classmethod
    def get_hash_from_url(cls, url: str):
        if url not in cls.cache:
            cls.salt[url] = os.urandom(8)
            cls.cache[url] = hashlib.sha512(url.encode('utf-8') + cls.salt[url]).hexdigest()
        return cls.cache[url]

while True:
    command = input('Enter url: ')
    if 'exit' in command:
        break
    hash = Cache.get_hash_from_url(command)
    print(f'{hash=}')
