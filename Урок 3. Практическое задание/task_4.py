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

dict_url = {}
salt = '1452yfdh789'


def cache_url(url):
    if url in dict_url.keys():
        print(f'хеш {url} - {dict_url[url]}')
    else:
        dict_url[url] = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
        print(dict_url)


cache_url('https://netflix.com')
cache_url('https://netflix.com')
cache_url('https://www.kinopoisk.ru')
cache_url('https://www.kinopoisk.ru')
