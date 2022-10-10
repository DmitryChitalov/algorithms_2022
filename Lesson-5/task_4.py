"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

some_dict = {}
some_ord_dict = OrderedDict()


def append_dict():
    for i in range(699):
        some_dict[i] = i
    return some_dict


def append_ord_dict():
    for i in range(699):
        some_ord_dict[i] = i
    return some_ord_dict


print('append')
print('Обычный словарь:', timeit('append_dict()', globals=globals(), number=1000))
print('Упорядоченный словарь:', timeit('append_ord_dict()', globals=globals(), number=1000))

"""
Cоздание обычного словаря быстрее.
"""


def get_dict():
    for key in some_dict:
        some_dict.get(key)
    return some_dict


def get_ord_dict():
    for key in some_ord_dict:
        some_ord_dict.get(key)
    return some_ord_dict


print('get')
print('Обычный словарь:', timeit('get_dict()', globals=globals(), number=1000))
print('Упорядоченный словарь:', timeit('get_ord_dict()', globals=globals(), number=1000))

"""
Возвращения значения ключа у обычного словаря быстрее.
"""


def popitem_dict():
    dict_copy = some_dict.copy()
    for key in range(699):
        dict_copy.popitem()
    return dict_copy


def popitem_ord_dict():
    ord_dict_copy = some_ord_dict.copy()
    for key in range(699):
        ord_dict_copy.popitem()
    return ord_dict_copy


print('popitem')
print('Обычный словарь:', timeit('popitem_dict()', globals=globals(), number=1000))
print('Упорядоченный словарь:', timeit('popitem_ord_dict()', globals=globals(), number=1000))

"""
Удаление последнего элемента у обычного словаря быстрее! """
"""
Выводы:
Использовать ordereddict целесообразно, когда нам важен именно порядок следования элементов или 
важна возможность оперативного переупорядочивания элементов.
В остальных случаях проще обходиться обычным словарём
"""