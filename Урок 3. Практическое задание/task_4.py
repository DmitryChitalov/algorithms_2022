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
from uuid import uuid4
import hashlib

salt = uuid4().hex
cache_url = {}


def url_address(url_add):
    if cache_url.get(url_add):
        print(f'{url_add} есть в кэше.')
    else:
        result = hashlib.sha256(salt.encode() + url_add.encode()).hexdigest()
        cache_url[url_add] = result
        print(f'{url_add}: {result}')


url_address('https://translate.google.com/')
url_address('https://translate.google.com/')