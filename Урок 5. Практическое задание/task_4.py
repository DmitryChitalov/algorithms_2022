"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from cProfile import run
import random

random_list = random.sample(range(10000000), 60)


def setdefault(d, l):
    for el in l:
        d.setdefault(el, el * 2)


def check(d, l):
    for el in l:
        if el in d:
            pass


def items(d):
    for k, v in d.items():
        pass


def popitem(d, l):
    for _ in l:
        d.popitem()
    pass


def normal_dict(l):
    test_dict = {}
    setdefault(test_dict, l)
    check(test_dict, l)
    items(test_dict)
    popitem(test_dict, l)
    pass


def ordered_dict(l):
    test_ordered_dict = OrderedDict()
    setdefault(test_ordered_dict, l)
    check(test_ordered_dict, l)
    items(test_ordered_dict)
    popitem(test_ordered_dict, l)
    pass


run('normal_dict(random_list)')
"""
1    0.357    0.357    0.676    0.676 task_4.py:17(setdefault)
1    0.239    0.239    0.239    0.239 task_4.py:22(check)
1    0.054    0.054    0.054    0.054 task_4.py:28(items)
1    0.344    0.344    0.630    0.630 task_4.py:33(popitem)
1    0.000    0.000    1.600    1.600 task_4.py:39(normal_dict)
"""

run('ordered_dict(random_list)')
"""
1    0.362    0.362    0.923    0.923 task_4.py:17(setdefault)
1    0.281    0.281    0.281    0.281 task_4.py:22(check)
1    0.253    0.253    0.253    0.253 task_4.py:28(items)
1    0.335    0.335    0.729    0.729 task_4.py:33(popitem)
1    0.000    0.000    2.187    2.187 task_4.py:48(ordered_dict)
"""
"""
Вывод, по замерам, OrderedDict, выполняет операции чуть медленнее обычного словаря
исходя из замеров можем сделать вывод о том что в актуальной версии применением OrderedDict 
окажутся частные случая к примеру для обработки кэша, когда требуется перемещать элементы 
внутри словаря благодаря move_to_end и popitem  который имеет не обязательный атрибут boolean
который определяет принцип удаления очереди или стека
"""
