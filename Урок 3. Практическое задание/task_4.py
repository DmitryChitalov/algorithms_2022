import hashlib
from uuid import uuid4
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


# Реализация через функцию
def url_cash(url, dct):
    """Проверяет наличие хеша в словаре"""
    salt = str(uuid4())
    if url in dct:
        return f'хеш url {url} {dct[url]}'
    else:
        dct[url] = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        return f'url записан в кеш'


# реализация через класс
class UrlCash:
    """Кеш url"""
    def __init__(self):
        self.hash_url = dict()

    def _gen_hash(self, url):
        """Генерирует хеш и записывает в хранилице"""
        self.hash_url[url] = \
            hashlib.sha256(url.encode() + str(uuid4()).encode()).hexdigest()

    def check_hash(self, url):
        """Проверка на наличие хеша"""
        if url in self.hash_url:
            print(f'хеш url {url} {self.hash_url[url]}')
        else:
            self._gen_hash(url)
            print(f'url записан в кеш')


if __name__ == '__main__':
    url_dict = dict()
    print('\nТест для функции')
    print(url_cash('gb.ru', url_dict))
    print(url_cash('yandex.ru', url_dict))
    print(url_cash('4pda.ru', url_dict))
    print(url_cash('4pda.ru', url_dict))
    print(url_cash('gb.ru', url_dict))
    print('\nТест для класса')
    test = UrlCash()
    test.check_hash('gb.ru')
    test.check_hash('yandex.ru')
    test.check_hash('4pda.ru')
    test.check_hash('gb.ru')
    test.check_hash('yandex.ru')
