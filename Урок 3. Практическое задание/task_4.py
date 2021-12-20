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

from hashlib import sha256
from random import randint


class Cache:
    def __init__(self):
        self._vault = {}
        self._salt = str(randint(0, 100000)).encode('utf-8')

    def get(self, url):
        cache_page = self._get_from_cache(url)
        if cache_page:
            return cache_page
        self._set_in_cache(url)

    def _get_from_cache(self, url):
        return self._vault.get(url)

    def _set_in_cache(self, url):
        self._vault[url] = sha256(self._salt + url.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    cache = Cache()
    print(cache.get('https://github.com/KTo1'))
    print(cache.get('https://github.com/KTo1'))
    print(cache.get('https://github.com/KTo1'))
    print(cache.get('https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html'))
    print(cache.get('https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html'))
    print(cache.get('https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html'))
    print(cache.get('https://losst.ru/ustanovka-redis-v-ubuntu-18-04'))
    print(cache.get('https://losst.ru/ustanovka-redis-v-ubuntu-18-04'))
