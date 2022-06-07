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
from hashlib import pbkdf2_hmac  # для тренировки (знаю, что для хешироаний паролей)
from binascii import hexlify  # для конвертации результать  pbkdf2_hmac
from uuid import uuid4  # генерирует случайный обьект uuid для соли


class CacheUrl:

    def __init__(self):
        self.cache = {}

    def cache_storage(self, url_add):
        if url_add in self.cache:
            print(f"{url_add} есть в кэше")
        else:
            url_salt = uuid4().hex
            self.cache[url_add] = hexlify(pbkdf2_hmac(hash_name='sha512',
                                                      password=url_add.encode(),
                                                      salt=url_salt.encode(),
                                                      iterations=100)).decode()

        return self.cache


if __name__ == "__main__":
    cache_url_cl = CacheUrl()
    for _ in range(3):
        cache_url_cl.cache_storage(input("Введите url-адрес: "))
    print(cache_url_cl.cache)
