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


def cache_webpages(a_url, cache_dict={}, salt='mycache'):
    url_hash = sha512(a_url.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    if a_url in cache_dict.keys():
        return print(cache_dict[a_url])
    else:
        cache_dict[a_url] = url_hash
        return print(cache_dict)


the_cache_dict = {}
url_1 = input('Введите url-адрес: ')
cache_webpages(url_1, the_cache_dict)
url_2 = input('Введите url-адрес: ')
cache_webpages(url_2, the_cache_dict)
url_3 = input('Введите url-адрес: ')
cache_webpages(url_3, the_cache_dict)
