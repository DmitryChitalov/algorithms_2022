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

class WebPageCaching():
    def __init__(self):
        self.web_caching = {}
        self.salt = 'my_salt'

    def add_check(self, a):
        web = self.web_caching.setdefault(a)
        if web == None:
            url = a
            url_caching = hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()
            self.web_caching[a] = url_caching
            print('в кэше url-адреса не было, уже исправили.')
        else:
            print(f'хеш url-а: {web}, мы его даже посолили.')


test = WebPageCaching()

test.add_check('www.vk.ru')
test.add_check('www.vk.ru')
test.add_check('www.bk.ru')



