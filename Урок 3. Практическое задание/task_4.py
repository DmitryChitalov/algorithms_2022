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
from hashlib import sha512
from uuid import  uuid4

class Main():
    def __init__(self):
        self.hash = {}
        self.salt = 'salt'


    def get_hash_from_url(self, url):
        salt = uuid4().hex
        print(salt)
        hash_url = sha512(salt.encode() + url.encode()).hexdigest()
        return hash_url


    def check_url(self,url):
        new = self.get_hash_from_url(url)
        if url not in self.hash.keys():
            self.hash[url] = new
            print(f'{url} add in hash')
        else:
            print(f'в хеше уже есть {url}')
            print(self.hash[url])

    def print_hash(self):
        print(self.hash)

m = Main()
m.check_url('www.ya.ru')
m.check_url('www.ya.ru')
m.check_url('www.yandex.ru')
m.check_url('www.yandex.ru')
m.print_hash()