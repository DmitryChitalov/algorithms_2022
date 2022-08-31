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

cache = dict()


def caching_url(cache, url):
    return cache.setdefault(url, hashlib.sha256(url.encode() + 'salt'.encode()).hexdigest())


print(caching_url(cache, 'https://docs.python.org/3.7/'))
print(caching_url(cache, 'https://tretyakov.net/post/hotkeys-phpstorm-i-pycharm/'))
print(caching_url(cache, 'https://docs-python.ru/'))
print(cache)
print(caching_url(cache, 'https://docs-python.ru/'))
