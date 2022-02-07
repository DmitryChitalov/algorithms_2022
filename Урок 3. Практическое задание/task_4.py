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

import hashlib


class UrlHasher:

    def __init__(self):
        self.__urls = dict()

    def insert_to_cache(self, url):
        if self.__urls.get(url) is None:
            url_hash = hashlib.sha256(url.encode('utf-8')).hexdigest()
            self.__urls.setdefault(url, url_hash)
            print('Данные внесены в кэш!')
        else:
            print(f'Хеш {url} уже существует {self.__urls.get(url)}')

    def get_cache(self, key=None):
        if len(self.__urls) == 0:
            return 'Кэш очищен '

        if key is None:
            return self.__urls
        return key, self.__urls[key]


test = UrlHasher()
test.insert_to_cache('https://gb.ru/')
test.insert_to_cache('https://gb.ru/')
test.insert_to_cache('https://yandex.ru/')
print(test.get_cache('https://yandex.ru/'))
test2 = UrlHasher()
print(test2.get_cache())
