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
from uuid import uuid4
import hashlib


class Hashed:
    def __init__(self, url_adr):
        self.url_adr = url_adr
        self.salt = uuid4().hex
        self.url_hash = hashlib.sha256(self.salt.encode() + self.url_adr.encode()).hexdigest()


def get_url(my_stg):
    new_url = Hashed(my_stg)
    return new_url


def go_to_hash(user_url, dict_hash):
    if user_url not in dict_hash:
        print('добавление url %s в кэш ' % user_url)
        hashed_url = get_url(user_url)
        dict_hash[hashed_url.url_adr] = hashed_url
    else:
        print('URL уже есть в кэше - ', dict_hash[user_url].url_hash)
    return dict_hash


my_hash = {}
url_lst = ['vk.com', 'google.com', 'ya.ru', 'games-workshop.com']

for i in url_lst:
    my_hash = go_to_hash(i, my_hash)

my_url = input('введите url : ')

my_hash = go_to_hash(my_url, my_hash)

# Пытался  реаализовать сохранение кэша в файлах (JSON и YAML) , но столкнулся с проблемой что невозможно стандартными
# средставми сериализовать словарь с объектами пользовательского класса ( ну или я плохо искал), в общем у меня не
# получилось. Если я все таки похо искал, и это возможно, то дайте пожалуйста совет - как ?
