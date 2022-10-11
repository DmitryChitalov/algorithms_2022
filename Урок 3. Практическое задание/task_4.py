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
from hashlib import sha256
class Cash:
    def __init__(self):
        self.d = {}
        self.salt = uuid4().hex

    def add(self, url):
        self.d[url] = sha256(self.salt.encode() + url.encode()).hexdigest()

    def check(self, url):
        if url in self.d.keys():
            return self.d[url]
        self.add(url)
        return 'В кеше нет такого URL'


cash = Cash()
a = input('Введите URL или exit для выхода: ')

while a.strip() != 'exit':
    print(cash.check(a))
    a = input('Введите URL или exit для выхода: ')