"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


dic1 = {1: 'car', 2: 'bus', 3: 'boat', 4: 'taxi', 5: 'horse'}
notord_dic = {2: 'bus', 1: 'car',  5: 'horse', 3: 'boat', 4: 'taxi'}
order_dic = OrderedDict(dic1)
test = notord_dic.popitem()
test2 = order_dic[1]
print(test, test2)


def get_el(dic):
    for i in range(10):
        for key in dic.keys():
            a = dic[key]
    return a


def items_f1(dic):
    for i in range(100):
        b = dic.items()
    return b


def copy_f1(dic):
    for i in range(100):
        b = dic.copy()
    return b

print(notord_dic.items())
print('Взятие i-го элемента')
print(timeit("get_el(notord_dic)", setup='from __main__ import get_el, notord_dic', number=100000))
print(timeit("get_el(order_dic)", setup='from __main__ import get_el, order_dic', number=100000))
print('Операция items')
print(timeit("items_f1(notord_dic)", setup='from __main__ import items_f1, notord_dic', number=100000))
print(timeit("items_f1(order_dic)", setup='from __main__ import items_f1, order_dic', number=100000))
print('Операция copy')
print(timeit("copy_f1(notord_dic)", setup='from __main__ import copy_f1, notord_dic', number=100000))
print(timeit("copy_f1(order_dic)", setup='from __main__ import copy_f1, order_dic', number=100000))
"""Данные операции выполняются быстрее в обычном словаре, в версия Python выше 3.6 использование
 OrderedDict смысла не имеет"""
