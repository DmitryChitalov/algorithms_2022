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


class BaseUrl:
    base = {}

    def __init__(self):
        pass

    def put_url(self, url):
        res = self.base.get(url)
        if res is None:
            self.base[url] = hashlib.sha256(str(len(url)).encode() + url.encode()).hexdigest()
            return (self.base[url])
        else:
            return (res)


url1 = 'https://gb.ru/lessons/260926'
url2 = 'https://www.bbc.com/russian'
bs = BaseUrl()
print(bs.put_url(url1))
print(bs.put_url(url2))

print(bs.put_url(url1))
