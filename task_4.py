"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from collections import OrderedDict
from timeit import repeat, default_timer


def time_test(operations, stmt_dict, stmt_ordict, setup_dict, setup_ordict, repeats, numbers):
    for i in range(len(stmt_dict)):
        res_dict = repeat(stmt_dict[i], setup_dict[i], default_timer, repeats[i], numbers[i], globals=globals())
        res_ordict = repeat(stmt_ordict[i], setup_ordict[i], default_timer, repeats[i], numbers[i], globals=globals())
        print(f'----- {operations[i]} -----')
        # print(f'>Время       {"min":>8} {"mean":>8} {"max":>8}')
        # print(f'Dict:        {min(res_dict):>8.0e} {sum(res_dict) / repeats[i]:>8.0e} {max(res_dict):>8.0e}')
        # print(f'OrderedDict: {min(res_ordict):>8.0e} {sum(res_ordict) / repeats[i]:>8.0e} {max(res_ordict):>8.0e}')
        print(f'             {"Время":>8}')
        print(f'Dict:        {sum(res_dict):>8.3f}')
        print(f'OrderedDict: {sum(res_ordict):>8.3f}')


##############################################################################
"""
----- Операция: добавление эл-та -----
                Время
Dict:           4.962
OrderedDict:    7.158
Вывод: Для обычного словаря отрабатывает быстрее, чем для упорядоченного

----- Метод: pop -----
                Время
Dict:           6.031
OrderedDict:   12.118
Вывод: Для обычного словаря отрабатывает быстрее, чем для упорядоченного

----- Метод: update -----
                Время
Dict:          15.040
OrderedDict:   30.297
Вывод: Для обычного словаря отрабатывает быстрее, чем для упорядоченного

----- Метод: get -----
                Время
Dict:           6.801
OrderedDict:    7.051
Вывод: Для обычного и упорядоченного словарей скорость работы практически
не отличается
 
 
Общий вывод: в плане скорости работы нет смысла исп-ть OrderedDict в
Python 3.6 и более поздних версиях
"""

length = 1000  # количество итераций в рамках запуска

operations = ['Операция: добавление эл-та', 'Метод: pop', 'Метод: update', 'Метод: get']
repeats = [1, 100_000, 1, 1]  # число замеров
numbers = [100000, 1, 100000, 100000]  # число запусков

setup_dict = [
    f'obj=dict()\nelems=range({length})',
    f'elems=range({length})\nobj={{i:i for i in range({length})}}',
    f'obj=dict()\nelems=range({length})',
    f'elems=range({length})\nobj={{i:i for i in range({length})}}'
    ]

setup_ordict = [
    f'obj=OrderedDict()\nelems=range({length})',
    f'elems=range({length})\nobj=OrderedDict({{i:i for i in range({length})}})',
    f'obj=OrderedDict()\nelems=range({length})',
    f'elems=range({length})\nobj=OrderedDict({{i:i for i in range({length})}})'
    ]

stmt = [
    'for i in elems:\n\tobj[i]=i',
    'for i in elems:\n\tobj.popitem()',
    'for i in elems:\n\tobj.update({i:i})',
    'for i in elems:\n\tobj.get(i)'
    ]


time_test(operations, stmt, stmt, setup_dict, setup_ordict, repeats, numbers)