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


class URLCache:

    def __init__(self):
        self.urls = {}

    @property
    def salt(self):
        return uuid4().hex.encode('utf-8')

    def is_cached(self, url):
        return url in self.urls

    def process_the_url(self, url):
        if self.is_cached(url):
            print(self.urls[url])
            return self.urls[url]
        else:
            self.urls[url] = hashlib.sha512(self.salt + url.encode('utf-8')).hexdigest()

    def show_cached(self):
        [print(k, v, sep='\n') for k, v in self.urls.items()]


if __name__ == '__main__':
    url_obj = URLCache()
    url_obj.show_cached()
    url_obj.process_the_url('https://www.google.com')
    url_obj.process_the_url('https://www.google.com')
    url_obj.process_the_url('https://www.yahoo.com')
    print('\n')
    url_obj.show_cached()
