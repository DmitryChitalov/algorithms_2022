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
import hashlib


def get_page(url):
    if cache_page.get(url):
        print(f'Данный адрес: {url} имеется в кэше')
    else:
        page_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_page[url] = page_hash
        print(f'Кэш дополнен адресом: {url}')
        print(cache_page)

salt = uuid4().hex
cache_page = {}

page1 = input('Введите url-адрес страницы 1: ')
get_page(page1)
page2 = input('Введите url-адрес страницы 2: ')
get_page(page2)
page3 = input('Введите url-адрес страницы 3: ')
get_page(page3)
