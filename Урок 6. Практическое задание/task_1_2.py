"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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

Это файл для второго скрипта
"""
import hashlib
import string
import random
from uuid import uuid4

import memory_profiler
from pympler import asizeof
from memory_profiler import profile

""" исходное """


class webCaching:
    """
    Задание 4 из урока 3 курса Алгоритмы и структуры данных.
    Задача:
    Реализуйте скрипт "Кэширование веб-страниц"
    Функция должна принимать url-адрес и проверять есть ли в кэше соответствующая страница или нет.
    """
    def __init__(self):
        self._cache = {}

    #@memory_profiler.profile
    def set_cache(self, url: str):
        if url and url not in self._cache:
            salt = uuid4().hex.encode("utf-8")
            self._cache.update({url: hashlib.sha512(salt + url.encode("utf-8")).hexdigest()})
        elif url in self._cache.keys():
            print("already exists: %s" % self.show_cache[url])

    @property
    def show_cache(self):
        return self._cache


""" оптимизированное """

class webCaching_opt:

    __slots__ = "_cache"

    def __init__(self):
        self._cache = {}

    #@memory_profiler.profile
    def set_cache(self, url: str):
        if url and url not in self._cache:
            salt = uuid4().hex.encode("utf-8")
            self._cache.update({url: hashlib.sha512(salt + url.encode("utf-8")).hexdigest()})
        elif url in self._cache.keys():
            print("already exists: %s" % self.show_cache[url])

    @property
    def show_cache(self):
        return self._cache


if __name__ == "__main__":
    obj = webCaching()
    obj_opt = webCaching_opt()
    print(f"Class webCaching instance size (empty): {asizeof.asizeof(obj)}")
    print(f"Class webCaching_opt instance size (empty): {asizeof.asizeof(obj_opt)}")
    obj.set_cache("https://vk.com")
    obj.set_cache("https://vk.ru")
    obj_opt.set_cache("https://vk.com")
    obj_opt.set_cache("https://vk.ru")

    print(f"Class webCaching instance size (after filling): {asizeof.asizeof(obj)}")
    print(f"Class webCaching_opt instance size (after filling): {asizeof.asizeof(obj_opt)}")

"""
Результаты: 
    Class webCaching instance size (empty): 464
    Class webCaching_opt instance size (empty): 48
    Class webCaching instance size (after filling): 960
    Class webCaching_opt instance size (after filling): 48
Вывод: 
    Использование слотов существенно сокращет потребление памяти, с ростом количества записей в словаре, 
    потребление памяти не увеличивалось в оптимизированном Классе.

профилирование памяти метода set_cache(self):

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    75     19.8 MiB     19.8 MiB           1       @memory_profiler.profile
    76                                             def set_cache(self, url: str):
    77     19.8 MiB      0.0 MiB           1           if url and url not in self._cache:
    78     19.8 MiB      0.0 MiB           1               salt = uuid4().hex.encode("utf-8")
    79     19.8 MiB      0.0 MiB           1               self._cache.update({url: hashlib.sha512(salt + url.encode("utf-8")).hexdigest()})
    80                                                 elif url in self._cache.keys():
    81                                                     print("already exists: %s" % self.show_cache[url])
"""