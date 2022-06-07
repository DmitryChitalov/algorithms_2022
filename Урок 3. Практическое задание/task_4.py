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
    salt = uuid4().hex  # -> 952604f24d9f4cd0b515a39c73657027
    cache_obj = {}
    __url = None

    def set_url (self, url):
        self.__url = url
        if self.cache_obj.get(self.__url):
            print(f'Данный адрес: {self.__url} присутствует в кэше')
        else:
            res = hashlib.sha256(self.salt.encode() + self.__url.encode()).hexdigest()
            self.cache_obj[self.__url] = res
            print(self.cache_obj)
    def get_hash(self, url):
        if url in self.cache_obj:
            return self.cache_obj[url]
        else: print('Данного адреса нет в кеше')

u = UrlHash ()
u.set_url('https://geekbrains.ru/')
u.set_url('https://yandex.ru/')
u.set_url('https://geekbrains.ru/')
print(u.get_hash('https://geekbrains.ru/'))
u.get_hash('https://gekbrains.ru/')