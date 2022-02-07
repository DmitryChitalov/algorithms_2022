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
from hashlib import pbkdf2_hmac
from binascii import hexlify

cache_base = {}


def check_page_in_cache(url):
    if url in cache_base:
        return (f'{url} уже в кэше, хэш: {cache_base[url]}')
    else:
        cache_base['url'] = hexlify(pbkdf2_hmac(hash_name='sha256',
                                              password=url.encode('utf-8'),
                                              salt='any_salt_1'.encode('utf-8'),
                                              iterations=10000))
        return (f'{url} добавлен в кэш')
print(check_page_in_cache('url'))
print(check_page_in_cache('url'))

