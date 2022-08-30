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

store_1 = {}


def hash_adress(url, some_dict):
    if url in some_dict:
        return 'адрес уже в кэше.'
    my_hash = hashlib.sha512('salt'.encode('utf-8') + url.encode('utf-8')).hexdigest()
    some_dict[url] = my_hash
    return some_dict


store_1 = hash_adress('https://gb.ru', store_1)
print(store_1)
print(hash_adress('https://gb.ru', store_1))
print(store_1)
store_1 = hash_adress('https://github.com/', store_1)
print(hash_adress('https://github.com/', store_1))
print(store_1)
