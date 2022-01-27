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


class CashUrl:
    cash = {}

    def __init__(self, url):
        self.url = url
        self.salt = uuid4().hex

    def __hash__(self):
        return hashlib.sha512(self.url.encode() + self.salt.encode()).hexdigest()

    def check_url(self):
        if self.url in CashUrl.cash:
            return CashUrl.cash[self.url][0]
        else:
            new_hash = CashUrl.__hash__(self)
            CashUrl.cash[self.url] = new_hash, self.salt
            return CashUrl.cash


if __name__ == '__main__':
    from uuid import uuid4
    import hashlib

    obj_1 = CashUrl('https://gb.ru/')
    obj_2 = CashUrl('https://mail.ru/')
    print(obj_1.check_url())
    print(obj_1.check_url())
    print(obj_2.check_url())
