"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

ord_dict = OrderedDict()
reg_dict = dict()


def test_orddict(n):
    for i in range(n):
        ord_dict[i] = True

    for i in range(n):
        ord_dict.pop(i)


def test_dict(n):
    for i in range(n):
        reg_dict[i] = True

    for i in range(n):
        reg_dict.pop(i)


print(timeit('test_dict(1000)', globals=globals(), number=100000))
print(timeit('test_orddict(1000)', globals=globals(), number=100000))

# На операции с обычным словарем ушло 7.7 сек, с ordereddict - 14.9 сек. Учитывая, насколько дольше происходят
# операции, использовать OrderedDict в новых версиях python смысла нет, за исключением надобности операции popitem()
