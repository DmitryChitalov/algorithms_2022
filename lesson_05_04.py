"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

simple_dict = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'Estonia': 'Tallinn', 'Hungary': 'Budapest', 'Austria': 'Vienna'}
ord_dict = OrderedDict(simple_dict)


def dict_get(dct=simple_dict):
    for i in range(1000):
        dct.get('Estonia')


def ord_dict_get(dct=ord_dict):
    for i in range(1000):
        dct.get('Estonia')


def dict_values(dct=simple_dict):
    for i in range(1000):
        dct.values()


def ord_dict_values(dct=ord_dict):
    for i in range(1000):
        dct.values()


def dict_keys(dct=simple_dict):
    for i in range(1000):
        dct.keys()


def ord_dict_keys(dct=ord_dict):
    for i in range(1000):
        dct.keys()


def dict_items(dct=simple_dict):
    for i in range(1000):
        dct.items()


def ord_dict_items(dct=ord_dict):
    for i in range(1000):
        dct.items()


def dict_pop(dct=simple_dict):
    for i in range(1000):
        dct.pop()


def ord_dict_pop(dct=ord_dict):
    for i in range(1000):
        dct.pop()


def dict_popitem(dct=simple_dict):
    for i in range(1000):
        dct.popitem(last=True)


def ord_dict_popitem(dct=ord_dict):
    for i in range(1000):
        dct.popitem(last=True)


def dict_move_to_end(item, dct=simple_dict):
    for i in range(1000):
        del_item = dct.pop(item)
        dct[item] = del_item


def ord_dict_move_to_end(itm, dct=ord_dict):
    for i in range(1000):
        dct.move_to_end(itm, last=True)


# get
print(f'Dict get: {timeit("dict_get", "from __main__ import dict_get", number=1000)}')
print(f'Ord dict get: {timeit("ord_dict_get", "from __main__ import ord_dict_get", number=1000)}')
# values
print(f'Dict values: {timeit("dict_values", "from __main__ import dict_values", number=1000)}')
print(f'Ord dict values: {timeit("ord_dict_values", "from __main__ import ord_dict_values", number=1000)}')
# keys
print(f'Dict keys: {timeit("dict_keys", "from __main__ import dict_keys", number=1000)}')
print(f'Ord dict keys: {timeit("ord_dict_keys", "from __main__ import ord_dict_keys", number=1000)}')
# items
print(f'Dict items: {timeit("dict_items", "from __main__ import dict_items", number=1000)}')
print(f'Ord dict items: {timeit("ord_dict_items", "from __main__ import ord_dict_items", number=1000)}')
# pop
print(f'Dict pop: {timeit("dict_pop", "from __main__ import dict_pop", number=1000)}')
print(f'Ord dict pop: {timeit("ord_dict_pop", "from __main__ import ord_dict_pop", number=1000)}')
# popitem
print(f'Dict popitem: {timeit("dict_popitem", "from __main__ import dict_popitem", number=1000)}')
print(f'Ord dict popitem: {timeit("ord_dict_popitem", "from __main__ import ord_dict_popitem", number=1000)}')
# move to end
print(f'Dict move to end: {timeit("dict_move_to_end", "from __main__ import dict_move_to_end", number=1000)}')
print(f'Ord dict move to end: {timeit("ord_dict_move_to_end", "from __main__ import ord_dict_move_to_end", number=1000)}')


"""
OreferedDict оказался быстрее только в случае с get. В остальных случаях результаты замера примерно одинаковые.
Есть смысл использовать OrdereDict, чтобы показать важность порядка, а так же из-за удобного использования move_to_end
Dict get: 1.2800000000000311e-05
Ord dict get: 1.0999999999997123e-05
***
Dict values: 1.0900000000001187e-05
Ord dict values: 1.1000000000000593e-05
***
Dict keys: 1.0999999999997123e-05
Ord dict keys: 1.1000000000000593e-05
***
Dict items: 1.1000000000000593e-05
Ord dict items: 1.1000000000000593e-05
***
Dict pop: 1.1000000000000593e-05
Ord dict pop: 1.0899999999997717e-05
***
Dict popitem: 1.0899999999997717e-05
Ord dict popitem: 1.1000000000000593e-05
***
Dict move to end: 1.0900000000001187e-05
Ord dict move to end: 1.1000000000000593e-05
"""

