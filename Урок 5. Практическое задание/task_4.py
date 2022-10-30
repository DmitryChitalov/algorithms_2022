"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

import random
from collections import OrderedDict
from functools import partial
from timeit import timeit

sample_dict = dict({i: random.randint(1, 100) for i in range(500000)})
sample_odict = OrderedDict(sample_dict)
operation_cnt = 1000

operations = ['insert', 'change', 'delete', 'iter']


def dict_op1(in_obj, op: str):
    cur_len = len(in_obj)
    if op == 'insert':
        for i in range(operation_cnt):
            in_obj[cur_len + i] = i
    elif op == 'change':
        for i in range(operation_cnt):
            in_obj[i] = i
    elif op == 'delete':
        keys = list(in_obj.keys())
        for i in keys:
            in_obj.pop(i)
    elif op == 'iter':
        for key, value in in_obj:
            a = key + value
    return in_obj


for op in operations:
    print(f"{op}, standard dict: {timeit(partial(dict_op1,in_obj=sample_dict, op=op), globals=globals(), number=1000)}")
    print(f"{op}, ordered dict: {timeit(partial(dict_op1,in_obj=sample_odict, op=op), globals=globals(), number=1000)}")
# insert, standard dict: 0.13053169600061665
# insert, ordered dict: 0.18888472899925546
# change, standard dict: 0.05378026400012459
# change, ordered dict: 0.07147317199996905
# delete, standard dict: 3.127714836999985
# delete, ordered dict: 0.23673331200006942
# iter, standard dict: 3.0091198780000923
# iter, ordered dict: 0.00026702000013756333
# При сравнимых вариантах использования обычный список работает лучше,
# но по упорядоченному списку почему-то быстрее проходит удаление элемента и итерирование