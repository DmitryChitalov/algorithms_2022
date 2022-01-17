"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

dict_1 = {}
ord_dict = OrderedDict()


def func_dict_full(dict1):
    for i in range(100000):
        dict1[i] = i


print(timeit(
    "func_dict_full",
    setup='from __main__ import func_dict_full',
    number=1000))
"Время выполнения наполнения dict 1.6399999999999748e-05"


def func_orderdict_full(ord_dict):
    for i in range(100000):
        ord_dict[i] = i


print(timeit(
    "func_orderdict_full",
    setup='from __main__ import func_orderdict_full',
    number=1000))
"Время выполнения наполнения orderdict 1.5899999999999248e-05"
"Orderdict was created for sort elements."


def func_dict_del(dict1):
    for i in range(100000):
        dict1.pop(i)


print(timeit(
    "func_dict_del",
    setup='from __main__ import func_dict_del',
    number=1000))
"Время выполнения delete keys from the dict 1.6900000000000248e-05"


def func_dict_change(dict1):
    for i in range(100000):
        dict1[i] = 'dict'


print(timeit(
    "func_dict_change",
    setup='from __main__ import func_dict_change',
    number=1000))
"Время выполнения change values from the dict 1.6000000000002124e-05"


###############OrderDict###############

def func_orddict_del(ord_dict):
    """Выполняет операции по изменению OrderedDict"""
    for i in range(100000):
        ord_dict.pop(i)


print(timeit(
    "func_orddict_del",
    setup='from __main__ import func_orddict_del',
    number=1000))
"Время выполнения delete keys from the orderdict 2.8799999999995496e-05"


def dunc_orddict_change(ord_dict):
    for i in range(100000):
        ord_dict[i] = 'ord_dict'


print(timeit(
    "dunc_orddict_change",
    setup='from __main__ import dunc_orddict_change',
    number=1000))
"Время выполнения change values from the orderdict 1.6900000000000248e-05"


"Наданный момент, после версии 3.6 достаточно простого словаря, для всех манипуляций"
