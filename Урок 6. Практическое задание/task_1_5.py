"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""
import random
from memory_profiler import profile
import hashlib


def random_url():
    symblos = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    return ''.join([random.choice(symblos) for _ in range(random.randint(5, 15))])


class UrlCache:
    def __init__(self):
        self.cache_dict = {}
        self.salt = 'UrlCache'

    def add_url_to_cache(self, new_url: str):
        """Функция принимает в себя url и добавляет его хеш в словарь с другими хешами"""
        new_record = {new_url: hashlib.sha512(new_url.encode() + self.salt.encode()).hexdigest()}
        self.cache_dict.update(new_record)
        return f'Сайт {new_url} добавлен в кеш'

    def check_cache(self, pattern: str):
        """Функция проверяет наличие хеша url в словаре с другими хешами"""
        if pattern in self.cache_dict:
            return f'Хеш {pattern}: {self.cache_dict[pattern]}'
        else:
            return self.add_url_to_cache(pattern)


@profile
def create_objects():
    cache = UrlCache()
    for i in range(10000):
        cache.check_cache(f'https://www.{random_url()}.ru/')


create_objects()


class UrlSlotCache():
    def __init__(self, new_url: str):
        self.cache_dict = {}
        self.salt = 'UrlCache'
        self.url = new_url

    def add_url_to_cache(self):
        """Функция принимает в себя url и добавляет его хеш в словарь с другими хешами"""
        new_record = {self.url: hashlib.sha512(self.url.encode() + self.salt.encode()).hexdigest()}
        self.cache_dict.update(new_record)
        return f'Сайт {self.url} добавлен в кеш'

    def check_cache(self):
        """Функция проверяет наличие хеша url в словаре с другими хешами"""
        if self.url in self.cache_dict:
            return f'Хеш {self.url}: {self.cache_dict[self.url]}'
        else:
            return self.add_url_to_cache()


@profile
def create_objects_slot():
    for i in range(10000):
        url = UrlSlotCache(f'https://www.{random_url()}.ru/')
        url.check_cache()


create_objects_slot()


"""Кажется я правильно произвел замену существующего образования классов на применение конструкции слотов.
Но это не точно. В прежней редакции Mem usage в ходе работы функции увеличивалась на 2.9 MiB.
В новой редакции Mem usage остался в прежнем объеме
  """