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


def hash_url(url, cache):
    if url in cache:
        print(f'url {url} сть в кэше: {cache[url]}')
    else:
        url_cache = hashlib.sha512(url.encode('utf-8') + url.encode('utf-8')).hexdigest()
        cache[url] = url_cache
        print(f'url {url} добавлен в кэш: {url_cache}')
    return cache


if __name__ == '__main__':
    cache = {
        'mail.ru': '566a51535256fd0bb99468bd329d5afc573cfbec5cf9e5daf5ef52d2263e30c27a4d5aad355be02310ab38e578542fe9a5c799f191c8c1055422b9ed26954078'
        }
    hash_url('mail.ru', cache)
    hash_url('github.com', cache)
    print(cache)
