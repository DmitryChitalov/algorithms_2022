"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {}
my_ord_dict = OrderedDict()


def append_dict():
    for i in range(1001):
        my_dict[i] = i
    return my_dict


def append_ord_dict():
    for i in range(1001):
        my_ord_dict[i] = i
    return my_ord_dict


print('1')
print('Обычный словарь:', timeit('append_dict()', globals=globals(), number=1000))
print('Упорядоченный словарь:', timeit('append_ord_dict()', globals=globals(), number=1000))

'''
Cоздание обычного словаря быстрее.
'''


def get_dict():
    for key in my_dict:
        my_dict.get(key)
    return my_dict


def get_ord_dict():
    for key in my_ord_dict:
        my_ord_dict.get(key)
    return my_ord_dict


print('2')
print('Обычный словарь:', timeit('get_dict()', globals=globals(), number=1000))
print('Упорядоченный словарь:', timeit('get_ord_dict()', globals=globals(), number=1000))

'''
Возвращения значения ключа у обычного словаря быстрее.
'''


def popitem_dict():
    dict_copy = my_dict.copy()
    for key in range(1001):
        dict_copy.popitem()
    return dict_copy


def popitem_ord_dict():
    ord_dict_copy = my_ord_dict.copy()
    for key in range(1001):
        ord_dict_copy.popitem()
    return ord_dict_copy


print('3')
print('Обычный словарь:', timeit('popitem_dict()', globals=globals(), number=1000))
print('Упорядоченный словарь:', timeit('popitem_ord_dict()', globals=globals(), number=1000))

'''
Удаление последнего элемента у обычного списка на много быстрее!
'''