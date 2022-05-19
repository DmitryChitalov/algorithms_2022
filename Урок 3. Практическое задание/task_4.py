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

import time
import hashlib


def cashing(func):
    cash_url = {}

    def wrapper(url):
        res_hash = cash_url.get(url)
        if res_hash is None:
            res_hash = func(url)
            cash_url[url] = res_hash
        return res_hash
    return wrapper


@cashing
def get_hash_url(url):
    salt = 'qwerty'
    return hashlib.sha512(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()


def test(n):
    for i in range(n):
        print(f'хэш url: {get_hash_url("https://pythonworld.ru/osnovy/indeksy-i-srezy.html")}')
        print(f'хэш url: {get_hash_url("https://snipp.ru/handbk/table-ascii")}')
        print(f'хэш url: {get_hash_url("https://translate.google.com/?hl=ru&sl=ru&tl=en&text=%D0%BA%D1%8D%D1%88&op=translate")}')
        print(f'хэш url: {get_hash_url("https://pythonworld.ru/osnovy/indeksy-i-srezy.html")}')
        print(f'хэш url: {get_hash_url("https://webdevblog.ru/ispolzovanie-functool-wraps-v-dekoratorah-python/")}')
        print(f'хэш url: {get_hash_url("https://realtycalendar.ru/users/sign_in/")}')
        print(f'хэш url: {get_hash_url("https://webdevblog.ru/ispolzovanie-functool-wraps-v-dekoratorah-python/")}')


if __name__ == '__main__':

    test(10)