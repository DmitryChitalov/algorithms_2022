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
from uuid import uuid4


def url_cache(cache_in):

    def _url_cache(func):
        def cache_wrapper(url):
            if url not in cache_in:
                cache_in[url] = func(url)
                return
            print(f'хеш url-а {url}: {cache_in[url]}')
        return cache_wrapper

    return _url_cache


cache = {}


@url_cache(cache)
def url_hash(url_in):
    salt = uuid4().hex
    hash_out = sha512(salt.encode() + url_in.encode()).hexdigest()
    return hash_out


if __name__ == '__main__':
    url_hash('https://yandex.ru/')
    url_hash('https://www.google.ru')
    url_hash('https://yandex.ru/')
    print(cache)
