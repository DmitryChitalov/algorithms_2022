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
import hashlib


class AddUrl:
    def __init__(self):
        self.dict_urlhash = {}
        self. salt = 'salt'

    def input_hash(self, url_adress):
        if url_adress in self.dict_urlhash:
            print('Url- адрес есть в кеше', '\n', url_adress, self.dict_urlhash[url_adress])
        else:
            self.add_dict_urlhash(url_adress)
            print('Url- адрес добавлен в кеш', '\n', url_adress, self.dict_urlhash[url_adress])

    def add_dict_urlhash(self, url_adress):
        self.dict_urlhash[url_adress] = hashlib.sha512(self.salt.encode() + url_adress.encode()).hexdigest()


x = AddUrl()
x.input_hash('https://ya.ru/')
x.input_hash('https://ya.ru/')
x.input_hash('https://mail.google.com')
x.input_hash('https://mail.google.com')
