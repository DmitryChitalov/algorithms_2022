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


def page_cache_check(url):
    if cache_dct.get(url):
        print(f'Данный адрес присутствует в кэше, его хеш: {cache_dct[url]}')
    else:
        cache_dct[url] = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        print(f'Страница {url} добанленна в кэш')


salt = 'my_salt'
cache_dct = {}

page_cache_check('https://yandex.ru/')
page_cache_check('https://gb.ru/')
page_cache_check('https://github.com/')
page_cache_check('https://github.com/')
page_cache_check('https://gb.ru/')
page_cache_check('https://yandex.ru/')
