"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


import collections
from timeit import timeit

test_dict1 = {}
test_dict2 = collections.OrderedDict([])


def app_dict1():
    for i in range(10000000):
        test_dict1[i] = i


def app_dict2():
    for i in range(10000000):
        test_dict2[i] = i


print(timeit('app_dict1', globals=globals()))
print(timeit('app_dict2', globals=globals()))


def el_dict1():
    for i, j in test_dict1.items():
        return i, j


def el_dict2():
    for i, j in test_dict2.items():
        return i, j


print(timeit('el_dict1', globals=globals()))
print(timeit('el_dict2', globals=globals()))

'''
тестовое время показывает, что обычный словарь и OrderedDict примерно равно, и расхождение не велико.
Использование OrderedDict в Python 3.6 и более поздних версиях, зависит от конкретного варианта его использования, 
а также от того, насколько явно необходимо в своем коде использовать OrderedDict, а так же возможность обратной совместимости
с другими версиями кода.(3,6 и выше)
'''
