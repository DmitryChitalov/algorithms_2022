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

# Решим задачу с использованием ООП.
class CashWeb:
    def __init__(self):
        self.urls = {}
        self.d_salt = {}


    def get_hash(self,url):
        salt = uuid4().hex
        self.d_salt.setdefault(url, salt)
        url_hash = sha512(salt.encode() + url.encode()).hexdigest()
        return url_hash

    def cash_in(self, url):
        url_hash = self.get_hash(url)
        if url in self.urls:
            print(f'Адрес: {url} уже присутствует в кэше!')
        else:
            self.urls.setdefault(url, url_hash)
            return print(f"Запись HASH для {url} в кэш успешно совершена!")

url1 = 'https://gb.ru/lessons/260927'
url2 = 'https://ya.ru/'
url3 = 'https://github.com/romik1981/algorithms_2242_Belyakov_Roman_27092022/blob/lesson_3/'

lst_urls = CashWeb()

lst_urls.cash_in(url1)
lst_urls.cash_in(url2)
lst_urls.cash_in(url3)

lst_urls.cash_in(url1)

print(f'Словарь кэшей адресов: {lst_urls.urls}')
print(f'Словарь солей адресов: {lst_urls.d_salt}')
