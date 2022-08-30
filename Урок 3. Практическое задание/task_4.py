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


class UrlHash:
    def __init__(self):
        self.elems = {}

    def ask_for_url(self, url):
        x = self.elems.get(url, '0')
        if x == '0':
            salt = uuid4().hex
            self.elems[url] = hashlib.sha512(url.encode() + salt.encode()).hexdigest()
        else:
            print(self.elems[url])


def url_append():
    urlhash_obj = UrlHash()
    var = ''
    while var != '-':
        var = input('Введите url или - для выхода: \n')
        urlhash_obj.ask_for_url(var)
    print('Выход')


url_append()
