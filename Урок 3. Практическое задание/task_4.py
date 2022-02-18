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
from uuid import uuid4

salt = uuid4().hex

cashe_obj = {}


def task_4(url):
    if cashe_obj.get(url):
        print(f"Такой {url} есть")
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cashe_obj[url] = res
        print(cashe_obj)


if __name__ == "__main__":
    task_4('https:geekbrains.ru')
    task_4('https:geekbrains.ru')
