"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях

ВЫВОДЫ:
тестировалось на версии пайтон 3.10
По моим замерам словарь быстрее во всех тестах, кроме перемещения элемента в конец. Полагаю это из-за сохранения порядка.
Перемещение элементов в конец медленнее потому, что оно реализовано на пайтоне

Не вижу смысла его использовать, даже если нужно указать, что порядок следования важен, по моему для этого существует
документация. Раз функции перемещения элемента в конец нет в стандартном словаре, то думаю она не так уж и нужна)
"""

from collections import OrderedDict
from timeit import timeit
from prettytable import PrettyTable
from random import randint


def move_to_end(dct, key):
    value = dct[key]
    del dct[key]
    dct[key] = value


def add_result_row(operation, code_dict, code_odict, result_table):
    print(f'{operation}.....')

    d_time = round(timeit(code_dict, number=number, globals=globals()), 6)
    od_time = round(timeit(code_odict, number=number, globals=globals()), 6)

    percent = round(100 * (d_time - od_time) / d_time if d_time > od_time else 100 * (od_time - d_time) / od_time)
    result = f'Быстрее {"dict" if d_time < od_time else "odict"}'

    result_table.add_row([f'{operation}', d_time, od_time, length, number, result, percent])


length = 10000
number = 1000

dct = dict()
o_dct = OrderedDict()

result_table = PrettyTable()
result_table.field_names = ['Операция (dict/odict)', 'dict', 'odict', 'Элементы', 'Замеры', 'Результат', '%']
result_table.align['Операция (dict/odict)'] = "l"
result_table.align['Результат'] = "l"

add_result_row('append',
               '''for i in range(length):
                      dct[i] = i
               ''',
               '''for i in range(length):
                      o_dct[i] = i
               ''', result_table)

length = 100
number = 100
add_result_row('copy',
               '''for i in range(length):
                      _ = dct.copy()
               ''',
               '''for i in range(length):
                      _ = o_dct.copy()
               ''', result_table)

length = 100
number = 100
add_result_row('update',
               '''for i in range(length):
                     dct.update(dct)
               ''',
               '''for i in range(length):
                      o_dct.update(o_dct)
               ''', result_table)

length = 1000
number = 1000
add_result_row('move_to_end',
               '''for i in range(length):
                     move_to_end(dct, randint(0, length - 1))
               ''',
               '''for i in range(length):
                      o_dct.move_to_end(randint(0, length - 1))
               ''', result_table)

length = 10000000
number = 1

dct = {i: i for i in range(length)}
o_dct = OrderedDict(dct)
add_result_row('popitem',
               '''for i in range(length):
                      dct.popitem()
               ''',
               '''for i in range(length):
                      o_dct.popitem()
               ''', result_table)

length = 10000000
number = 1

dct = {i: i for i in range(length)}
o_dct = OrderedDict(dct)
add_result_row('del',
               '''for i in range(length):
                      del dct[i]
               ''',
               '''for i in range(length):
                      del o_dct[i]
               ''', result_table)


print(result_table)
