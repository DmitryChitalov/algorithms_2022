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
from uuid import uuid4


def check_url_hash(cache=None):

    if not cache:
        cache = dict()

    url = input('Введите url-адрес: ')
    url_hash = cache.get(url, None)

    if url_hash:
        print(f'Взять из кэша: {url_hash}')
    else:
        salt = uuid4().hex
        url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = url_hash
        print(f'Захэширован: {url_hash}')

    return check_url_hash(cache)


if __name__ == '__main__':
    check_url_hash()
