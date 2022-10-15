"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

ord_dict = OrderedDict([(elem,elem) for elem in list(range(1000))])
normal_dict = {elem:elem for elem in list(range(1000))}

def get_normal_dict():
    return normal_dict[500]

def get_ord_dict():
    return ord_dict[500]


print("Замеры получения элемента по индексу для normal_dict")
print(timeit("get_normal_dict()", globals=globals(), number=10000000))  # 1.0744209000004048
print("Замеры получения элемента по индексу для ord_dict")
print(timeit("get_ord_dict()", globals=globals(), number=10000000))  # 1.1036278999999922
print('-' * 50)


def del_normal_dict():
    del normal_dict[1]

def del_ord_dict():
    del ord_dict[1]


print("Замеры удаления элемента по индексу для normal_dict")
print(timeit("del_normal_dict()", globals=globals(), number=1))  # 1.2999998943996616e-06
print("Замеры удаления элемента по индексу для ord_dict")
print(timeit("del_ord_dict()", globals=globals(), number=1))  # > 1.3999997463542968e-06
print('-' * 50)

def ch_normal_dict():
    normal_dict[500] = 1

def ch_ord_dict():
    ord_dict[500] = 1


print("Замеры изменения элемента по индексу для normal_dict")
print(timeit("ch_normal_dict()", globals=globals(), number=10000000))  # 1.1898394999998345
print("Замеры изменения элемента по индексу для ord_dict")
print(timeit("ch_ord_dict()", globals=globals(), number=10000000))  # 1.5310966000006374
print('-' * 50)

"""
Выводы: Скорость выполнения операций у OrderedDict ниже чем у обычного словаря. 
Однако есть и плюсы: дополнительный метод move_to_end(), возможность добавлять 
новые атрибуты экземпляра класса ( атрибут __dict__).
"""
