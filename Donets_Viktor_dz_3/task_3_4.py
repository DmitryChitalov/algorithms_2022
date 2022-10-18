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

salt = uuid4().hex
cache_webpages = {}


def web_page(url):
    if cache_webpages.get(url):
        print(f'{url} есть в кеше')
    else:
        cache_webpages[url] = hashlib.sha256(salt.encode() +
                                             url.encode()).hexdigest()
        print(cache_webpages)


web_page('https://mail.ru/')
web_page('https://google.ru/')
web_page('https://mail.ru/')