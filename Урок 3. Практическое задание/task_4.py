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


from json import dump, load
from re import match, sub
from requests import get
from hashlib import sha256


class CacheURLClass:

    def __init__(self):
        with open('cache_url.json', 'w', encoding='utf-8') as w_file:
            dump({}, w_file)

    @staticmethod
    def verification_url(url):
        # Проверка наличия http(s) протокола в url (нет на ftp). Остальной части проверки url нет, но можно дописать
        if not match(r'(http)s?://', url):
            url = f'http://{url}'
        else:
            url = sub(r'https', 'http', url)
        if 200 <= get(url).status_code < 400:
            return True, url
        print('Ошибка URL')
        return False

    def add_url(self):
        salt = 'db_url'

        url = input('Введите URL: ')
        url = self.verification_url(url)[1]
        if url[0]:

            with open('cache_url.json', 'r', encoding='utf-8') as r_file:
                url_dict = load(r_file)

            if url_dict.get(url):
                print(url_dict[url])
                return url_dict[url]
            else:
                url_dict.setdefault(url, sha256(salt.encode() + url.encode()).hexdigest())
                print('Добавлен новый URL')

            with open('cache_url.json', 'w', encoding='utf-8') as w_file:
                dump(url_dict, w_file, sort_keys=True, indent=4, ensure_ascii=False)
