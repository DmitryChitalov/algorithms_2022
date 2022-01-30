"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет.

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""


class Cache:
    def __init__(self, protocol):
        self.protocol = protocol
        self.entries = {}

    def password_hash(self, p):
        from hashlib import pbkdf2_hmac
        from binascii import hexlify

        obj = pbkdf2_hmac(hash_name=self.protocol,
                          password=p.encode('utf-8'),
                          salt=b'whybother',
                          iterations=1)
        return hexlify(obj)

    def add(self, url):
        urlhash = self.password_hash(url)
        if urlhash in self.entries.values():
            return urlhash
        else:
            self.entries.update({url: urlhash})


my_url_cache = Cache('sha512')
my_url_cache.add('https://docs.python.org/3/library/stdtypes.html#typesmapping')
print(my_url_cache.add('https://wikipedia.org/'))
print(my_url_cache.add('https://docs.python.org/3/library/stdtypes.html#typesmapping'))
print(f'Cache contains {len(my_url_cache.entries)} records')

