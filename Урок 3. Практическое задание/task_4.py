"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib
from uuid import uuid4


class СacheWebPageClass:
    def __init__(self):
        self.web_cache = {}

    def check_in_cache(self, url):
        if self.web_cache.get(url):
            print(f'hash {url} : {self.web_cache.get(url)}')
        else:
            salt = uuid4().hex
            self.web_cache.setdefault(url, hashlib.sha512(
                url.encode('utf-8') + salt.encode()).hexdigest())
            print("Кеш веб-страниц обновлён")

    def view_cache(self):
        for k, v in self.web_cache.items():
            print(k, ':', v)


if __name__ == '__main__':
    urls = СacheWebPageClass()
    urls.check_in_cache('www.opennet.ru')
    urls.check_in_cache('www.opennet.ru')
    urls.check_in_cache('www.ya.ru')
    urls.check_in_cache('www.ya.ru')
    urls.check_in_cache('www.ya.ru')

    print()
    # вывод значений кеша
    urls.view_cache()

"""
Кеш веб-страниц обновлён
hash www.opennet.ru : d83e1821771566b3726813e0f380dee17f7a79b5515e83bc6
f9bee7227fb994fbb9998d3ab861a35a587830c3152b6df2e2127cec6634ddad1568d02b90c78aa
Кеш веб-страниц обновлён
hash www.ya.ru : f20af5aac9907cc2382bd89cfbd4a54cf0c0ce198c407234d55580
29b1b9baa6960ff64b8851c5ea59d8c24d0840d871856aaaa945e2fb6bf8e450fe43da2379
hash www.ya.ru : f20af5aac9907cc2382bd89cfbd4a54cf0c0ce198c407234d55580
29b1b9baa6960ff64b8851c5ea59d8c24d0840d871856aaaa945e2fb6bf8e450fe43da2379

www.opennet.ru : d83e1821771566b3726813e0f380dee17f7a79b5515e83bc6
f9bee7227fb994fbb9998d3ab861a35a587830c3152b6df2e2127cec6634ddad1568d02b90c78aa
www.ya.ru : f20af5aac9907cc2382bd89cfbd4a54cf0c0ce198c407234d55580
29b1b9baa6960ff64b8851c5ea59d8c24d0840d871856aaaa945e2fb6bf8e450fe43da2379
"""
