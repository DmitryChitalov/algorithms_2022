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
import  hashlib

def check_url(url_in):
    if url_in not in cache_url.keys():
        salt = uuid4().hex
        res = hashlib.sha512(salt.encode() + url_in.encode()).hexdigest()
        cache_url[url_in] = (res, salt)
        print(f'{url_in}: {res} - записан в кэш')
    else:
        print(f'Хэш {url_in}: {cache_url[url_in][0]} - уже есть в кэше')

cache_url = {}
check_url('https://www.youtube.com')
check_url('https://www.youtube.com')
