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
    def __init__(self):
        self.cache_dict = {}
        self.salt = 'UrlCache'

    def add_url_to_cache(self, new_url: str):
        """Функция принимает в себя url и добавляет его хеш в словарь с другими хешами"""
        new_record = {new_url: hashlib.sha512(new_url.encode() + self.salt.encode()).hexdigest()}
        self.cache_dict.update(new_record)
        return f'Сайт {new_url} добавлен в кеш'

    def check_cache(self, pattern: str):
        """Функция проверяет наличие хеша url в словаре с другими хешами"""
        if pattern in self.cache_dict:
            return f'Хеш {pattern}: {self.cache_dict[pattern]}'
        else:
            return self.add_url_to_cache(pattern)


cache = UrlCache()
print(cache.check_cache('https://www.kinopoisk.ru/'))
print(cache.check_cache('https://www.kinopoisk.ru/'))
print(cache.check_cache('https://www.wink.ru/'))
print(cache.check_cache('https://gb.ru/lessons/'))
print(cache.check_cache('https://gb.ru/lessons/'))
