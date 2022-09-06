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

Это файл для четвертого скрипта
"""

"""
В данном задании использовался код с задания:
Урок 3, задание 4
https://github.com/DmitryChitalov/algorithms_2022/pull/804
__slots__
"""

from pympler import asizeof
from uuid import uuid4
import hashlib


class UrlHash:
    def __init__(self):
        self.elems = {}

    def ask_for_url(self, url):
        x = self.elems.get(url, '0')
        if x == '0':
            salt = uuid4().hex
            self.elems[url] = hashlib.sha512(url.encode() + salt.encode()).hexdigest()
        else:
            print(self.elems[url])


def url_append():
    urlhash_obj = UrlHash()
    var = ''
    while var != '-':
        var = input('Введите url или - для выхода: \n')
        urlhash_obj.ask_for_url(var)
    print('Выход')


cls_obj = UrlHash()
print('Размер стандартного объекта класса: ', asizeof.asizeof(cls_obj))


class UrlHashSlots:

    __slots__ = ['elems']

    def __init__(self):
        self.elems = {}

    def ask_for_url(self, url):
        x = self.elems.get(url, '0')
        if x == '0':
            salt = uuid4().hex
            self.elems[url] = hashlib.sha512(url.encode() + salt.encode()).hexdigest()
        else:
            print(self.elems[url])


def url_append_slots():
    urlhash_obj = UrlHashSlots()
    var = ''
    while var != '-':
        var = input('Введите url или - для выхода: \n')
        urlhash_obj.ask_for_url(var)
    print('Выход')


cls_obj_slots = UrlHashSlots()
print('Размер объекта класса с использованием __slots__ : ', asizeof.asizeof(cls_obj_slots))


"""
Для оптимизации памяти при создании класса использовал конструкцию __slots__
Результаты при запуске скрипта

Размер стандартного объекта класса:  272
Размер объекта класса с использованием __slots__ :  104
"""