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

from hashlib import pbkdf2_hmac
from binascii import hexlify


def hash_creator(url, salt=b'my_salt'):
	return hexlify(pbkdf2_hmac('sha512', url.encode('utf-8'), salt, 1)) 


def url_check(url, cache):
	if cache.get(url) != None:
		return cache[url]
	else:
		cache[url] = hash_creator(url)
		return 'url добавлен в кэш'


if __name__ == '__main__':
	
	my_cache = {'mail.ru': hash_creator('mail.ru'), 'vk.com': hash_creator('vk.com')}
	
	print(url_check('mail.ru', my_cache))
	print(my_cache)

	print(url_check('gb.ru', my_cache))
	print(my_cache)
