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

from uuid import uuid4
import hashlib
salt = uuid4().hex
cache = {}


def cache_url(url):
    hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
    if cache.get(url):
        print(f'Хэш для URL {url}:\n{hash}')
    else:
        cache[url] = hash


cache_url('https://www.ya.ru/')
cache_url('https://www.ya.ru/')
cache_url('https://gb.ru/')
cache_url('https://gb.ru/')
print('\nТекущий кэш:')
print(cache)