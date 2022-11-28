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

cash_dict = {}
salt = 'sflpr9fhi2'


def check_url_cash(url):
    if cash_dict.get(url):
        print(f"Кэш данного url: {cash_dict[url]}")
    else:
        url_cash = sha512(salt.encode() + url.encode()).hexdigest()
        cash_dict[url] = url_cash

check_url_cash('yandex.ru')
check_url_cash('yandex.ru')
check_url_cash('rambler.ru')
print(f"Словарь с url: {cash_dict}")

