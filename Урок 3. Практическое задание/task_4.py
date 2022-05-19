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
import time


# Выполним задание с помощью ООП
class UrlTable:
    urls_dict = {}
    user_salt = ''

    def __init__(self):  # Каждый экземпляр класса будем создовать со своей солью
        self.user_salt = input('Введите соль: ')

    def url_add(self, user_url):  # Функция добавления url-адреса в таблицу
        if user_url in self.urls_dict:
            print(self.urls_dict[user_url])  # если адрес есть в словаре, выводим его в консоль
        else:  # если адреса в словаре нет, добавляем его
            self.urls_dict.setdefault(user_url, hashlib.sha512(user_url.encode('utf-8') +
                                                               self.user_salt.encode('utf-8')).hexdigest())

    @property
    def show_urls(self):  # вывод имеющейся таблицы адресов
        print(f'Таблица кешированных адресов на время: {time.ctime()}')
        for key in self.urls_dict:
            print(f'Адресс: {key}, хеш: {self.urls_dict[key]}')

    @property
    def show_salt(self):  # напоминалка введенной соли
        print(f'Пользовательская соль: {self.user_salt}')


a = UrlTable()
a.url_add('http://www.microsoft.com')
a.show_urls
a.url_add('https://www.google.com')
a.url_add('http://www.google.com')
a.url_add('http://www.google.com')
a.url_add('http://yandex.ru')
a.show_urls
a.url_add('http://www.microsoft.com')
a.url_add('http://www.microsoft.com')
a.show_salt
