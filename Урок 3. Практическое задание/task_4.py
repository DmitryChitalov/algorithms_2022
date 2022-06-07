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
from hashlib import pbkdf2_hmac


class UrlCache:

    def __init__(self):
        self.cache = {}

    def caching(self, url):
        url_in_cache = self.cache.get(url)
        if not url_in_cache:
            salt = uuid4().bytes
            url_hash = pbkdf2_hmac('sha256', url.encode(), salt, 100000)
            self.cache[url] = [url_hash, salt]
            url_in_cache = [url_hash, salt]
        return url_in_cache


if __name__ == '__main__':
    my_cache = UrlCache()
    my_cache.caching('http://google.com')
    my_cache.caching('http://yandex.ru')
    my_cache.caching('http://google.com')
    for i in my_cache.cache:
        print(i, my_cache.cache[i][0].hex())
