"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
from hashlib import sha512
from pprint import pprint

cache = {}


def url_cache(url):
    salt = url[:5]  # будем солить первыми 5 символами url
    hash_url = sha512(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
    if cache.get(url) is None:
        cache[url] = hash_url
        print(f'Хэш {url} внесён в кэш')
    else:
        print(f'Хэш {url}: {cache[url]}')


url_cache('gb.ru')
url_cache('mail.ru')
url_cache('rambler.ru')
url_cache('gb.ru')
url_cache('docs.python.org')
pprint(cache)
