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
from uuid import uuid4


class Cash:
    def __init__(self):
        self.cash = {}

    def __add_new_hash(self, url):
        salt = uuid4().hex
        hash_url = sha512(url.encode() + salt.encode()).hexdigest()
        self.cash[url] = {'hash': hash_url, 'salt': salt}
        return hash_url

    def __get_hash(self, url):
        return sha512(url.encode() + self.cash.get(url).get('salt').encode())

    def browser(self, url):
        if self.cash.get(url):
            return self.cash[url]['hash'], 'from_cash'  # 'from_cash' для демонстрации
        return self.__add_new_hash(url)

    def show_cash(self):
        return self.cash


if __name__ == '__main__':
    web = Cash()
    print(web.browser('https://some_site_1.ru'))
    print(web.browser('https://some_site_1.ru'))
    print(web.browser('https://some_site_2.ru'))
    print(web.browser('https://some_site_3.ru'))
    print(web.browser('https://some_site_2.ru'))
    print(web.browser('https://some_site_1.ru'))
    print(web.browser('https://some_site_3.ru'))
    for website, d in web.show_cash().items():
        print(website, d)
