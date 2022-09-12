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

Это файл для второго скрипта
"""


# Доработанная задача № 4 из 3 урока по курсу "Алгоритмы и структуры данных на Python"

from pympler import asizeof
from os import urandom
from hashlib import pbkdf2_hmac


# ИСХОДНОЕ
class Cash:

    def __init__(self):
        self.urls = {}
        self.salt = urandom(32)

    def check_url(self, url):
        rep_url = self.urls.get(url)
        if rep_url is None:
            self.urls.setdefault(url, pbkdf2_hmac('sha512', url.encode('utf-8'), self.salt, 1000))
            return f'Хэш для {url}'
        else:
            return f'хэш {url} - {rep_url.hex()}'


# ОПТИМИЗИРОВАННОЕ
class CashOptimize:
    __slots__ = ['urls', 'salt']

    def __init__(self):
        self.urls = {}
        self.salt = urandom(32)

    def check_url(self, url):
        rep_url = self.urls.get(url)
        if rep_url is None:
            self.urls.setdefault(url, pbkdf2_hmac('sha512', url.encode('utf-8'), self.salt, 1000))
            return f'Хэш для {url}'
        else:
            return f'хэш {url} - {rep_url.hex()}'


cash_obj = Cash()
cash_obj_optimize = CashOptimize()
print(cash_obj.check_url('www.gb.ru'))
print(cash_obj.check_url('www.gb.ru'))

print(cash_obj.check_url('www.ya.ru'))
print(cash_obj.check_url('www.ya.ru'))

print(cash_obj_optimize.check_url('www.gb.ru'))
print(cash_obj_optimize.check_url('www.gb.ru'))

print(cash_obj_optimize.check_url('www.ya.ru'))
print(cash_obj_optimize.check_url('www.ya.ru'))

print(f'size cash_obj - {asizeof.asizeof(cash_obj)}')
print(f'size cash_obj_optimize - {asizeof.asizeof(cash_obj_optimize)}')


"""
size cash_obj - 904
size cash_obj_optimize - 688

Выводы:
Использование слотов экономнее.
"""