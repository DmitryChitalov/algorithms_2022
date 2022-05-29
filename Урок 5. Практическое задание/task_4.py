"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict


def m_dict():
    dct = {}
    for i in range(10):
        dct[i] = i
    return dct

def ord_dict():
    ord_dct = OrderedDict()
    for i in range(10):
        ord_dct[i] = i
    return ord_dct

print(timeit('m_dict()', globals=globals(), number=1000))
print(timeit('ord_dict()', globals=globals(), number=1000))
'''
0.0024939999999999962
0.003822900000000018
'''

test_dict = m_dict()
test_ord_dict = ord_dict()

def elm_dict(test_dict):
    return test_dict.get(5)

def elm_ord_dict(test_ord_dict):
    return test_ord_dict.get(5)

print(timeit('elm_dict(test_dict)', globals=globals(), number=1000))
print(timeit('elm_ord_dict(test_ord_dict)', globals=globals(), number=1000))
'''
0.00037439999999999696
0.0003771999999999942
'''

'''
Вывод: Заполнение обычного словаря быстрее, но при получении значения по ключу результаты примерно одинаковые.
Думаю использовать OrderedDict в более поздних версиях нет смысла.
'''