"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

dict_1 = {i: i for i in range(10000)}
dict_2 = OrderedDict(dict_1)


def check_1(dict_check):
    key = [i for i in dict_1]
    dict_check.pop(key[0])
    return dict_check


def check_2(dict_check):
    dict_check.popitem(last=False)
    return dict_check


print('popitem left for dict  ---> ',
      timeit(
          'check_1(dict_1)',
          number=10000,
          globals=globals()))

print('popitem left for OrderedDict  ---> ',
      timeit(
          'check_2(dict_2)',
          number=10000,
          globals=globals()))


# Однозначно Ordered dict работает быстрее при удолении элемента слева,
# особенно в версиях Python 3.6 и более старых версиях
# так как словари неупорядочены