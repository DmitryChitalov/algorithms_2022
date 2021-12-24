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
from uuid import uuid4
from hashlib import sha512


class DataHash:
    hashes = {}
    salt = uuid4().hex

    def __init__(self, address: str):
        self.address = address
        self._hash = sha512(DataHash.salt.encode() + address.encode()).hexdigest()
        DataHash.add(address)

    @classmethod
    def hash(cls, address):
        """
        Get hash by an address.
        If an address doesn't exist return None
        :param address:
        :return: hash or None
        """
        return cls.hashes.get(address)

    @classmethod
    def show_salt(cls):
        """
        Print salt from class
        :return: None
        """
        print(cls.salt)

    def __str__(self):
        return f'URL address: {self.address}'

    @staticmethod
    def add(address):
        """
        Add an address in memory.
        If an address exists, show message
        :param address:
        :return: None
        """
        if not DataHash.hashes.get(address):
            DataHash.hashes[address] = sha512(DataHash.salt.encode() + address.encode()).hexdigest()
        else:
            print('Current URL-address already exists')

    @staticmethod
    def remove(address):
        """
        Remove an address and hash from memory.
        If an address doesn't exist in memory, show message
        :param address:
        :return: None
        """
        if DataHash.hashes.get(address):
            DataHash.hashes.pop(address)
        else:
            print('Current URL-address doesn\'t exists')


if __name__ == '__main__':
    addr = "http://www.yandex.ru//"
    data = DataHash(addr)
    print(data)
    data.add(addr)  # Current URL-address already exists
    data.add('http://www.google.com/')
    print(data.hashes)  # All hashes
    print(data.hash(addr))
    data.remove(addr)
    data.remove('google.com')  # Current URL-address doesn't exists
    print(data.hashes)
    data.show_salt()
