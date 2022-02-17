"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from cProfile import run


def feeling_dict(input_dict):
    for i in range(10000000):
        input_dict[i] = f'value{i}'
    return input_dict


def get_dict(input_dict):
    for i in range(10000000):
        return input_dict.get(i)


def dict_items(input_dict):
    return input_dict.items


def create_dict():
    simple_dict = {}
    feeling_dict(simple_dict)
    get_dict(simple_dict)
    dict_items(simple_dict)


def create_order_dict():
    ordered_dict = OrderedDict()
    feeling_dict(ordered_dict)
    get_dict(ordered_dict)
    dict_items(ordered_dict)


run('create_dict()')
run('create_order_dict()')


"""
Все функции с обычным словарём выполняются чуть быстрее, чем с OrderedDict! 
Смысла использовать OrderedDict начиная с 3.6 и более поздних версиях нет, если только нет необходимости явно указать
порядок в списке для себя и коллег, работающих с кодом.
"""
