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
import json
import uuid


class Cash:
    cash_file = "cash.json"

    def __init__(self):
        data = {}
        self.salt = uuid.uuid4().hex
        with open(self.cash_file, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def cash_url(self, url):
        with open(self.cash_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if url in data:
            return data[url]
        with open(self.cash_file, 'w', encoding='utf-8') as file:
            hash = hashlib.sha512(url.encode('utf-8') + self.salt.encode("utf-8")).hexdigest()
            data[url] = hash
            json.dump(data, file)
        return "Хеш сохранен"


my_cash = Cash()
print(my_cash.cash_url('qqqq'))
print(my_cash.cash_url('aaaa'))
print(my_cash.cash_url('qqqq'))
