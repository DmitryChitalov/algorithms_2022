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
from hashlib import md5

cache = {'https://gb.ru/': 'a783210eb908ec6d9ae5522cc933138998defd6ee70dfb1dea416cecdf391f58',
         'https://www.python.org/': '6bd7e4a1b937bdf1c5f65d1312a4ee9f98defd6ee70dfb1dea416cecdf391f58',
         'https://github.com/': '008ec4453ff31513f43893cba7aa31c898defd6ee70dfb1dea416cecdf391f58'}

salt = md5(b'site').hexdigest()


def add_url(url):
    if url in cache:
        print(cache[url])
    else:
        hashh = md5(url.encode('UTF-8')).hexdigest() + salt
        cache[url] = hashh
        print('Записаны новые данные')
        print(f'URL: {url}\nHash: {hashh}')


if __name__ == '__main__':
    add_url(input('Введите URL: '))
