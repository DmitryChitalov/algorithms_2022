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

from hashlib import sha512


class CashHashUrls:
    def __init__(self):
        self.__glossary = dict()
        self.salt = 'my_salt'  # Url адреса уникальны, соль может быть не уникальна

    def do_hash(self, url_):
        return sha512(self.salt.encode() + url_.encode()).hexdigest()

    def add_to_cash(self, url):
        if url in self.__glossary.keys():
            return 1
        self.__glossary[url] = self.do_hash(url)
        return 0


def main(url):
    return_from_func = cash_urls.add_to_cash(url)
    if return_from_func == 1:
        print('Url уже находится в кэше')
    else:
        print('Url добавлен в кэш')


if __name__ == '__main__':
    cash_urls = CashHashUrls()
    while True:
        user_answer = input('Введите url для кэширования. Для выхода - 1\n')
        if user_answer == '1':
            break
        main(user_answer)
