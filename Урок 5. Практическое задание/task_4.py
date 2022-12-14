"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from time import perf_counter

n = 10000
new_dict = {}
new_orddict = {}

from time import perf_counter


def perf_time(func):

    def wrapper(*args):
        start = perf_counter()
        data = func(*args)
        print(f'Время выполнения {func.__name__}: {perf_counter() - start}')
        return data

    return wrapper


@perf_time
def fill_dict():
    for i in range(0, n):
        new_dict[i] = i
    return new_dict


@perf_time
def fill_orddict():
    for i in range(0, n):
        new_orddict[i] = i
    return new_orddict


@perf_time
def get_elm_dict():
    for i in range(n):
        new_dict.get(i)
    return None


@perf_time
def get_elm_orddict():
    for i in range(n):
        new_orddict.get(i)
    return None


@perf_time
def pop_elm_dict():
    for i in range(n // 2):
        new_dict.pop(i)
    return new_dict


@perf_time
def pop_elm_orddict():
    for i in range(n // 2):
        new_orddict.pop(i)
    return new_orddict


@perf_time
def popitem_left_elm_dict():
    for i in range(n // 2):
        new_dict.popitem()
    return new_dict


@perf_time
def popitem_left_elm_orddict():
    for i in range(n // 2):
        new_orddict.popitem()
    return new_orddict


fill_dict()
fill_orddict()
get_elm_dict()
get_elm_orddict()
pop_elm_dict()
pop_elm_orddict()
popitem_left_elm_dict()
popitem_left_elm_orddict()

"""
Как видно из результатов , ordereddict выполняются чуть быстрее, но незначительно. Пр иувеличенгии итераций разница во 
времени будет увеличиваться . В Python 3.6+ имеет смысл использовать ordereddict  , в том числе , когда необходимо ,чтобы 
быть точно уверенным , что словарь упорядочен.
"""
