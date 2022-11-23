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

class Сache(object):
    """ Создаёт объект содержащий словарь url адресов и их хэш-значений.

    Atributs:
        salt (str): соль для хэш функции.
        cache (dict): словарь url адресов и их хэш-значений.

    Methods:
        hashed  (solt: str, url: str) -> str: статический метод, вычисляет хэш-значение
        add     (url: str) -> None: метод объекта класса, добавляет url и его хэш-значение в словарь cache
    """

    __slots__ = ('_salt', '_cache')

    def __init__(self, salt: str) -> None:
        self._cache = {}
        self._salt = salt

    @property
    def salt(self):
        # Вернуть значение переменной salt
        return self._salt
        
    @property
    def cache(self):
        # Вернуть значение переменной cash
        return self._cache

    @staticmethod
    def hashed(salt: str, url: str) -> str:
        # Вычислить хэш
        return md5(salt.encode()).hexdigest() + md5(url.encode()).hexdigest()

    def add(self, url: str) -> None:
        # Добавить url в кэш, либо вернуть из кеша если url уже в нём
        if url in self.cache.keys():
            print(f"Получено из кэша: {self.cache[url]}")
        else:
            self.cache[url] = self.hashed(self.salt, url)
            print(f"Добавлено в кэш: {url}")

if __name__ == "__main__":

    cache = Сache('salt')
    for url in ['yandex.ru', 'google.com', 'yahoo.com', 'duckduckgo.com']:
        cache.add(url)
    for key, value in cache.cache.items():
        print(f'url: {key}\nкэш: {value}')
    cache.add('yandex.ru')