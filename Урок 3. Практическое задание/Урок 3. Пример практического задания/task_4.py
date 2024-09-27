from uuid import uuid4
import hashlib

salt = uuid4().hex  # -> 952604f24d9f4cd0b515a39c73657027
cache_obj = {}


def get_page(url):
    if cache_obj.get(url):
        print(f'Данный адрес: {url} присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = res
        print(cache_obj)


get_page('https://geekbrains.ru/')
get_page('https://geekbrains.ru/')
get_page('https://geekbrains.ru/')
