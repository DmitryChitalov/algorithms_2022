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
import hashlib


def hash_page(url, dct):
    if url in dct.keys():
        return dct[url]
    elif url not in dct.keys():
        hash_object = hashlib.sha256(url.encode('utf-8') + 'slt'.encode('utf-8'))
        hex_dig_res = hash_object.hexdigest()
        dct[url] = hex_dig_res
        return dct


pages = {'github.com': 'f5b3d468fcf48615d45d6104321629d799fc1eddc87b0848d7784f7e3b9c83cf', 'habr.com': '9ef8427b4ddda545f2227a8f45697ca19a3f515b85a9279910fed101761f452f'}
print(hash_page('github.com', pages))
print(hash_page('instagram.com', pages))


class HashUrls:
    def __init__(self):
        self.urls = {}

    def check_url(self, url):
        if url in self.urls.keys():
            print(f'Hash для {url}: {self.urls.get(url)}')
        else:
            print("Нет такого url'a")

    def add_url(self, url):
        if url in self.urls.keys():
            print(self.urls[url])
        elif url not in self.urls.keys():
            hash_object = hashlib.sha256(url.encode('utf-8') + 'slt'.encode('utf-8')).hexdigest()
            self.urls[url] = hash_object
            print(self.urls)


h = HashUrls()
h.add_url('github.com')
h.add_url('instagram.com')
h.add_url('habr.com')
h.check_url('github.com')
h.check_url('telegram.com')