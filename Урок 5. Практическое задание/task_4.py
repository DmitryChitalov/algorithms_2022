"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from random import randint
from collections import OrderedDict
from timeit import timeit

dct = {x: randint(-10000, 10000) for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'}
ord_dct = OrderedDict(dct)

def empty_values_dct(dct):
    for key, val in dct.items():
        dct[key] = 0



print(ord_dct)

print(timeit("empty_values_dct(dct)", globals=globals(), number=100000)) #Время выполнения 0.349520556
print(timeit("empty_values_dct(ord_dct)", globals=globals(), number=100000)) #Время выполнения 0.569773597 OrderedDict работает медленнее



