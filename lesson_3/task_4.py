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


url_salt = 'my_salt'
cache_dict = {}


def check_address(url_address):
    if url_address in cache_dict.keys():
        print(f'Хэш страницы: {cache_dict[url_address]}')
    else:
        cache_dict[url_address] = hashlib.sha512(url_address.encode() + url_salt.encode()).hexdigest()
        print(f'Для новой страницы: {url_address} записан хэш: {cache_dict[url_address]}')
    return cache_dict


check_address('gb.ru')
check_address('gb.ru')
check_address('youtube.com')
check_address('youtube.com')
