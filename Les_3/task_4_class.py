"""
Что должно быть в классе:
    1. инициализация с созданием словаря-кэша
    2. функция check_url, которая будет проверять наличие url в кэше
    3. функция insert_hash, которая будет вызываться из check_url, если не найдётся ключ
    4. метод insert_hash долены быть приватным
    5. должна быть возможность посмотреть кэш словарь-кэш, но нельзя его изменять вне класса
"""

from hashlib import sha512
from pprint import pprint


class UrlCache:
    def __init__(self):
        self.__cache = {}

    def __insert_url(self, url):
        salt = url[:5]  # будем солить первыми 5 символами url
        hash_url = sha512(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
        self.__cache[url] = hash_url
        print(f'Хэш {url} внесён в кэш')

    def check_url(self, check_url):
        if self.__cache.get(check_url) is None:
            self.__insert_url(check_url)
        else:
            return print(f'Хэш {check_url}: {self.__cache[check_url]}')

    def watch_cache(self):
        pprint(self.__cache)


url_hasher = UrlCache()
url_hasher.check_url('gb.ru')
url_hasher.check_url('mail.ru')
url_hasher.check_url('rambler.ru')
url_hasher.check_url('gb.ru')
url_hasher.check_url('docs.python.org')
url_hasher.watch_cache()
