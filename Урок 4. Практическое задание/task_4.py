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
from hashlib import sha512
from uuid import uuid4


def read_cache(url_dict, url):
    for i in url_dict.keys():
        if url == i:
            pass_hash, salt = url_dict[i].split(':')
            return pass_hash


def write_cache(url_dict, url):
    salt = uuid4().hex
    url_dict[url] = sha512(salt.encode() + url.encode()).hexdigest() + ':' + salt
    return print('Страница записана в кэш!')


def check_url(url_dict=None):
    if url_dict is None:
        url_dict = {}
    inp_url = input('Введите url-адрес или 0 для выхода: ')
    if inp_url != '0':
        print(f'Кэш страницы: {read_cache(url_dict, inp_url)}') if read_cache(url_dict, inp_url) \
                                                            else write_cache(url_dict, inp_url)
        return check_url(url_dict)


check_url()





