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
from hashlib import pbkdf2_hmac
from binascii import hexlify

url_base = {}


def url_check(url):
    if url in url_base:
        print(f'{url} always in base! hash is {url_base[url]}')
    else:
        url_base['url'] = hexlify(pbkdf2_hmac(hash_name='sha256',
                                              password=url.encode('utf-8'),
                                              salt='url'.encode('utf-8'),
                                              iterations=10000))
        print(f'{url} added to base!')


url_check('url')
url_check('url')
url_check('url2')
