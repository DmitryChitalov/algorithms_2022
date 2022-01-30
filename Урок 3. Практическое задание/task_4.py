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

address_lib = {}


def url_adr(url):
    if url in address_lib:
        return f'Хэш url: {address_lib[url]}'
    else:
        address_lib[url] = hashlib.pbkdf2_hmac(hash_name='sha512', password=url.encode('utf-8'),
                                              salt='qwerty'.encode('utf-8'), iterations=100)
        return f'{url} - добавлен в кэш'


print(url_adr('www.google.ru'))
print(url_adr('www.google.ru'))
