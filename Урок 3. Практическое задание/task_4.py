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


def add_dict_hash_url(url, work_dict):
    """
    Добавление в словарь url и его хэш
    :param url: адрес url
    :param work_dict: словарь куда надо добавить
    :return: Добавляеет запись в словарь или сообщает, что такой хэш уже есть
    """
    if work_dict.get(url):
        print(f'Данный адрес - {url} уже есть в словаре с хэшом - {work_dict[url]}')
    else:
        if len(url) > 5:
            salt = url[:5]
        else:
            salt = 'my salt'
        work_dict[url] = hashlib.sha256(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    dict_url_hash = {}
    add_dict_hash_url('https://google.com/', dict_url_hash)
    print(dict_url_hash)
    add_dict_hash_url('https://apple.ru/', dict_url_hash)
    print(dict_url_hash)
    add_dict_hash_url('https://google.com/', dict_url_hash)
    print(dict_url_hash)
    add_dict_hash_url('https://yandex.ru/', dict_url_hash)
    print(dict_url_hash)