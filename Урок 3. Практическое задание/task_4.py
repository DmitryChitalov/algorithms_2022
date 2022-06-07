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
from hashlib import sha256
import uuid

salt = uuid.uuid4().hex
cache_dct = {'https://gb.ru/lessons/232123': '31a5eb663a4d6b3460fe668535fd7cf0615e373d846c5daba2774c63bf688b66',
             'https://translate.google.com/': 'b92e5dc30e5237b3f47dc96bcfcf23d19b394629b136473789db56762e047c8a'}


def web_page_caching(url):
    cache_dct[url] = cache_dct.get(url, sha256(url.encode('utf-8') + salt.encode('utf-8')).hexdigest())


print(cache_dct)
web_page_caching('https://gb.ru/lessons/232123')
web_page_caching('https://stepik.org/')
print(cache_dct)
