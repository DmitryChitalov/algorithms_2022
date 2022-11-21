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
        self.session_salt = uuid4().bytes

    def caching(self, url):
        url_in_cache = self.cache.get(url)

        if url_in_cache:
            return url_in_cache

        hashed = pbkdf2_hmac('sha512', url.encode(), self.session_salt, 100000)
        self.cache[url] = hashed
        return hashed


if __name__ == '__main__':
    my_cache = UrlCache()
    my_cache.caching('http://google.com')
    my_cache.caching('http://yandex.ru')
    my_cache.caching('http://google.com')
