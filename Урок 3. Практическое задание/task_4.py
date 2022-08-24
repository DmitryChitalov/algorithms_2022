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

cache = dict()


def set_url_hash(url2):
    salt = "разная соль"
    url_hash = hashlib.sha256(salt.encode() + url2.encode()).hexdigest()
    return url_hash


def get_url_cache(url3):
    if url3 not in cache:
        cache[url3] = set_url_hash(url3)
    return cache[url3]


url1 = input('Введите url   ')
get_url_cache(url1)
print(cache)
url11 = input('Введите url   ')
get_url_cache(url11)
print(cache)
url111 = input('Введите url   ')
get_url_cache(url111)
print(cache)
