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


url_hesh_dict = {}


def hash_create(url: str):
    if url_hesh_dict.get(url) == None:
        salt = url
        hash_url = hashlib.sha3_512(url.encode() + salt.encode()).hexdigest()
        url_hesh_dict[url] = hash_url
        return url_hesh_dict[url]
    return url_hesh_dict[url]


hash_create('http://www.obj.ru')
print(url_hesh_dict)