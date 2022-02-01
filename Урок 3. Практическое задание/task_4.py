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

from binascii import hexlify
from hashlib import pbkdf2_hmac
from json import dumps, load, dump
from uuid import uuid4


def get_hash(passwd, salt):
    p_hash = pbkdf2_hmac(hash_name='sha512',
                         password=passwd.encode('utf-8'),
                         salt=salt.encode(),
                         iterations=100_000)
    return hexlify(p_hash)


def cache_url(url):
    try:
        with open('./cache.json') as cache:
            data = load(cache)
    except:
        data = {}
    if url in data:
        return data[url][0]
    else:
        salt = uuid4().hex
        p_hash = get_hash(url, salt)
        with open('./cache.json', 'w+') as cache:
            data[url] = [p_hash.decode(), salt]
            dump(data, cache, indent=2)
            return data[url][0]


print(cache_url('https://pikabu.ru/'))
print(cache_url('https://www.twitch.tv'))