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
from uuid import uuid4


class Hash:

    def __init__(self):
        self.data = dict()
        self.salt = uuid4().hex

    def generate(self, url):
        return sha256(url.encode() + self.salt.encode()).hexdigest()

    def write(self, url):
        if self.check(url):
            return f'{self.data[url]} - Хеш уже существует'
        else:
            return self.generate(url)

    def check(self, url):
        if url in self.data.keys():
            return True
        else:
            return False



task = Hash()

print(task.write('https://gb.ru/education'))
print(task.write('https://gb.ru/education'))
print(task.write('https://yandex.ru/'))
print(task.write('https://github.com/'))
