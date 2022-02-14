"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {}
my_ordict = OrderedDict()

print('my_dict pop and [i] = i - ', timeit("""
for i in range(100):
    my_dict[i] = i
    my_dict.pop(i)""", globals=globals()))

print('my_ORdict pop and [i] = i - ', timeit("""
for i in range(100):
    my_ordict[i] = i
    my_ordict.pop(i)""", globals=globals()))

# my_dict pop and [i] = i -  7.868406799971126
# my_ORdict pop and [i] = i -  14.149457500025164


print('my_dict[i] = i - ', timeit("""
for i in range(100):
    my_dict[i] = i
    my_dict.popitem()""", globals=globals()))

print('my_ORdict[i] = i - ', timeit("""
for i in range(100):
    my_ordict[i] = i
    my_ordict.popitem()""", globals=globals()))

# my_dict[i] = i -  9.27631519996794
# my_ORdict[i] = i -  15.897510599985253
