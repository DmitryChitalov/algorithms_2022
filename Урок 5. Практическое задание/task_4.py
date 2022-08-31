"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict


def make_dict(obj):
    return {x: x for x in obj}


simple_dict = make_dict('12345')
order_dict = OrderedDict(simple_dict)
simple_dict['6'] = '6'
order_dict['6'] = '6'


def del_el(one_dict, el):
    del one_dict[el]


print(timeit("simple_dict['6'] = '6'", globals=globals()))
print(timeit("order_dict['6'] = '6'", globals=globals()))
print(timeit("del_el(simple_dict, '6')", globals=globals(), number=1))
print(timeit("del_el(order_dict, '6')", globals=globals(), number=1))
print(timeit("simple_dict['2']", globals=globals()))
print(timeit("order_dict['2']", globals=globals()))

'''Выводы: использование OrderedDict только ради улучшения скорости кода не 
актуально, по сравнению со стандартными словарем производительность плюс-минус одинаковая. '''

