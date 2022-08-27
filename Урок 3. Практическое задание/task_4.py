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
from os import urandom
from hashlib import pbkdf2_hmac

 
class Hash:
    def __init__(self):
        self.urls = {}
        self.salt = urandom(32)

    def check_url(self, url):
        rep_url = self.urls.get(url)
        if rep_url is None:
            self.urls.setdefault(url, pbkdf2_hmac('sha512', url.encode('utf-8'), self.salt, 1000))
            return f'Добавлен хэш для {url}'
        else:
            return f'хэш {url} - {rep_url.hex()}'


hash_obj = Hash()

print(hash_obj.check_url('www.yandex.ru'))
print(hash_obj.check_url('www.yandex.ru'))

print(hash_obj.check_url('www.google.ru'))
print(hash_obj.check_url('www.google.ru'))

print(hash_obj.urls)
