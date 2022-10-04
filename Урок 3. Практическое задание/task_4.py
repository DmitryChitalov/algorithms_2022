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


from hashlib import sha256


def hash_function(input_string, salt_string):
    hash_obj = sha256(salt_string.encode() + input_string.encode())
    return hash_obj.hexdigest()


class WebUrlCache():

    salt = 'my_salt'

    def __init__(self):
        self.url_cache_dict = {}

    def is_in_cache(self, url):
        if url in self.url_cache_dict.keys():
            return True
        else:
            return False

    def print_is_in_cache(self, url):
        if url in self.url_cache_dict.keys():
            print(f' ulr {url} is in cache')
            return
        else:
            print(f" ulr {url} isn't in cache")
            return

    def hash_push_to_cache(self, url):
        if not self.is_in_cache(url):
            self.url_cache_dict[url] = hash_function(url, WebUrlCache.salt)
            print(f' {url} pushed to cache ' )
        else:
            print(f' {url} is already in cache ')

    def hash_pop_out_cache(self, url):
        if self.is_in_cache(url):
            del self.url_cache_dict[url]
            print(f' {url} pop out from cache ')
        else:
            print(f" {url} isn't in cache")

    def cache_size(self):
        print(f' cache size =  {len(self.url_cache_dict)} records')


if __name__ == '__main__':
    print('')
    my_url_cache = WebUrlCache()
    my_url_cache.cache_size()
    my_url_cache.print_is_in_cache("www.gb.ru")
    my_url_cache.print_is_in_cache("www.stackoverflow.com")

    my_url_cache.hash_push_to_cache("www.gb.ru")
    my_url_cache.hash_push_to_cache("www.stackoverflow.com")

    my_url_cache.print_is_in_cache("www.gb.ru")
    my_url_cache.print_is_in_cache("www.stackoverflow.com")

    my_url_cache.cache_size()

    my_url_cache.hash_pop_out_cache("www.gb.ru")
    my_url_cache.hash_pop_out_cache("www.stackoverflow.com")

    my_url_cache.print_is_in_cache("www.gb.ru")
    my_url_cache.print_is_in_cache("www.stackoverflow.com")
    my_url_cache.cache_size()


# Script listing
#
#  cache size =  0 records
#  ulr www.gb.ru isn't in cache
#  ulr www.stackoverflow.com isn't in cache
#  www.gb.ru pushed to cache
#  www.stackoverflow.com pushed to cache
#  ulr www.gb.ru is in cache
#  ulr www.stackoverflow.com is in cache
#  cache size =  2 records
#  www.gb.ru pop out from cache
#  www.stackoverflow.com pop out from cache
#  ulr www.gb.ru isn't in cache
#  ulr www.stackoverflow.com isn't in cache
#  cache size =  0 records
#
# Process finished with exit code 0
