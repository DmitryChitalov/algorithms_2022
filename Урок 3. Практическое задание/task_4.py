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

class cash_urls:
    
    def __init__(self):
        self.urls_dict = {}
        
    def create_cash(self, url):
        salt = "!@#$"
        hash_obj = sha256(url.encode() + salt.encode())
        self.urls_dict[url] = hash_obj.hexdigest()
        return self.urls_dict[url]
    
    def get_cash(self, url):
        if url in self.urls_dict.keys():
            return self.urls_dict[url]
        else:
            return self.create_cash(url)
        
if __name__ == '__main__':
    
    url_obj = cash_urls()
    
    print(url_obj.get_cash('https://www.google.com/'))