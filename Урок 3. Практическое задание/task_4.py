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

cached_urls = {}

def check_cache(url):
    hashed_url = hashlib.sha512('abracadabra'.encode() + url.encode()).hexdigest()
    if url in cached_urls:
        return hashed_url
    else:
        cached_urls[url] = hashed_url
        return 'url cached'

print(check_cache('www.homework.org'))
print(check_cache('www.homework.org'))
print(check_cache('www.homework.ru'))
print(check_cache('www.homework.ru'))

