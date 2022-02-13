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


class UrlCache:

    _salt = b'urls'

    def __init__(self):
        self.cache = {}

    def cache_check(self, url):
        if self.cache.get(url) is None:
            self.cache[url] = hashlib.sha512(self._salt + url.encode('utf-8')).hexdigest()
        else:
            print(f'Хэш {url}\n{self.cache[url]}')


cache = UrlCache()

cache.cache_check('yandex.ru')
cache.cache_check('mail.ru')
cache.cache_check('vk.com')
cache.cache_check('vk.com')
