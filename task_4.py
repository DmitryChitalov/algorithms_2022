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

#############################################################################
import hashlib


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r

    return g


@memorize
def cache(i):
    salt = 'salt'
    hash_obj = hashlib.sha256(salt.encode('utf-8') + i.encode('utf-8')).hexdigest()
    new_dict = {'https://gb.ru/education': 'c784fd290ea4717e08995ef180e10c0c29bc54dad25a6a2922f4c4e9417f1338',
                'https://github.com': '7d5c2e41feae0abe3127ecfaea37bf0c075cfc91effef8391f2d9512cdc4de94'}
    for el in new_dict:
        if el in new_dict:
            return hash_obj
        else:
            new_dict.append(f"{i}:{hashlib.sha512(i.encode('utf-8') + salt.encode('utf-8')).hexdigest()}")
    return new_dict


print(cache('https://yandex.ru/'))
print(cache('https://gb.ru/education'))
