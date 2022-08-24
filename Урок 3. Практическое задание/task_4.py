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
from hashlib import sha512


class WebPagesCache:
    def __init__(self):
        self.cache = {}

    def append_url(self, url):
        hash_url = sha512('salt'.encode('utf-8') +
                          url.encode('utf-8')).hexdigest()
        self.cache[url] = hash_url
        print(f'Хэш {url} добавлен в кэш')

    def check_url(self, url):
        if self.cache.get(url) is None:
            self.append_url(url)
        else:
            return print(f'{self.cache[url]}')

    def view_cache(self):
        print(self.cache)


url_caching = WebPagesCache()
url_caching.check_url('gb.ru')
url_caching.check_url('yandex.ru')
url_caching.check_url('yandex.ru')
url_caching.check_url('mail.ru')
url_caching.view_cache()
