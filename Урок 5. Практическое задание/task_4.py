"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


def sep():
    print("_" * 75)


dct = {"10": "1", "20": "2", "30": "3", "40": "4", "50": "5", "60": "6", "70": "7"}
ord_dct = OrderedDict(dct)


def dct_func(dct):
    for i in range(len(dct)):
        dct[i] = i + 1
    return dct


def ord_dct_func(ord_dct):
    for i in range(len(ord_dct)):
        ord_dct[i] = i + 1
    return ord_dct


print(timeit("dct_func", globals=globals()))      # 0.02357510000001639
print(timeit("ord_dct_func", globals=globals()))  # 0.023020099964924157

sep()


def ch_dct_func(dct):
    for i in range(len(dct)):
        dct["20"] = 100
    return dct


def ch_ord_dct_func(ord_dct):
    for i in range(len(ord_dct)):
        ord_dct["20"] = 100
    return ord_dct


print(timeit("ch_dct_func", globals=globals()))      # 0.01967129996046424
print(timeit("ch_ord_dct_func", globals=globals()))  # 0.019687899970449507

sep()


def key_dct_func(dct):
    for i in range(len(dct)):
        return dct["70"]


def key_ord_dct_func(ord_dct):
    for i in range(len(ord_dct)):
        return ord_dct["70"]


print(timeit("key_dct_func", globals=globals()))      # 0.019445599988102913
print(timeit("key_ord_dct_func", globals=globals()))  # 0.01928180002141744

sep()


def pop_dct_func(dct):
    for i in range(len(dct)):
        dct.pop("70")


def pop_ord_dct_func(ord_dct):
    for i in range(len(ord_dct)):
        ord_dct.pop("70")


print(timeit("pop_dct_func", globals=globals()))      # 0.01916330005042255
print(timeit("pop_ord_dct_func", globals=globals()))  # 0.019392699986696243

sep()


def clear_dct_func(dct):
    dct.clear()


def clear_ord_dct_func(ord_dct):
    ord_dct.clear()


print(timeit("clear_dct_func", globals=globals()))      # 0.019521299939602613
print(timeit("clear_ord_dct_func", globals=globals()))  # 0.019347900059074163

"""
Все операции выполняются с примерно одинаковым временем. 
Использовать класс OrderedDict имеет смысл. когда необходимо подчеркнуть особое значение порядка.
В остальных случаях лучше использовать dict, начиная с Python 3.6 он сохраняет упорядоченность.
"""
