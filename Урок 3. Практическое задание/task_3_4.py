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


url_cash = {}


def cash_checker(func):
    def hasher(url: str):
        res = url_cash.get(url)
        if res is None:
            res = func(url)
            url_cash[url] = res
            # print('Такая уже есть: ', url_cash[url])
        return res
    return hasher


@cash_checker
def hasher(url: str):
    url_hash = hashlib.sha256(url.encode('utf-8')).hexdigest()
    # url_cash[url] = url_hash
    return url_hash


print(hasher(input('Введите страницу: ')))
print(hasher(input('Введите страницу: ')))
print(hasher(input('Введите страницу: ')))
print(hasher(input('Введите страницу: ')))
print(url_cash)
