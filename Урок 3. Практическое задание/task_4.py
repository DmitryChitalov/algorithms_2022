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
from random import randint
from hashlib import pbkdf2_hmac, sha512
from binascii import hexlify


class UrlsCashing:  # Класс для "Кэширование веб-страниц"
    def __init__(self):
        self.urls_cache = {}  # кеш {'url-адрес': 'хеш url-а',}
        self.count_from_cash = 0  # для статистики: кол-во выборок из кеша
        self.count_to_cash = 0  # для статистики: кол-во выборок из кеша

    def __call__(self, fn):  # реализуем декоратор через callable обЪект
        def new_func(link):
            if link in self.urls_cache:
                self.count_from_cash += 1
            else:
                result = fn(link)
                self.urls_cache[link] = result
                self.count_to_cash += 1
            return self.urls_cache[link]

        return new_func

    def __str__(self):
        tmp = [f'Количество вычислений hash: {self.count_to_cash}, выборок из кеша: {self.count_from_cash}. Кеш:']
        for i, item in enumerate(self.urls_cache.items()):
            tmp.append(f'{i}. {item[0]}: {hexlify(item[1])}')
        return '\n'.join(tmp)


@(cashing := UrlsCashing())
def get_hash_url(http_link):  # Вычисление кеша функцией pbkdf2_hmac
    salt = bytes(sha512(bytes(http_link, 'UTF-8')).hexdigest(), 'UTF-8')  # соль : sha512()
    link = bytes(http_link, 'UTF-8')
    return pbkdf2_hmac('sha512', link, salt, 100000)


def get_urls(num):  # Генерируем URL из 3 случайных частей (6x6x6) и передаем в get_hash_url
    for _ in range(num):
        url = f"http://{('google.com', 'yandex.ru', 'gb.ru')[randint(0, 2)]}" \
              f"{('/news/', '/etc/', '/info/')[randint(0, 2)]}p0{randint(0, 2)}.html"
        get_hash_url(url)


# Хорошо видно, как долго выполняется обработка первых 100 адресов (Идет наполнение кеша)
quantity = 100
print(f'Первые {quantity} URLs')
get_urls(100)
print(cashing)
# И насколько быстрее обрабатывается вторая сотня (подавляющая часть хешей достается из словаря)
print(f'Вторые {quantity} URLs')
get_urls(quantity)
print(cashing)
