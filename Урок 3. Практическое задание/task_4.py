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


def get_url_hash(url, salt=b'url_salt'):
	return hexlify(pbkdf2_hmac('sha512', url.encode('utf-8'), salt, 1))


def check_url(url, cache):
	if cache.get(url) != None:
		return cache[url]
	else:
		cache[url] = get_url_hash(url)
		return f'url {url} добавлен в кэш'


if __name__ == '__main__':

	url_cache = {'ya.ru': get_url_hash('ya.ru'), 'vk.com': get_url_hash('vk.com')}

	print(check_url('ya.ru', url_cache))
	print(url_cache)

	print(check_url('google.com', url_cache))
	print(url_cache)