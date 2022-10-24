"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit, default_timer
from collections import OrderedDict


dct = {x: x**2 for x in range(0,1000)}
dct_ord = OrderedDict([(x, x**2) for x in range(0, 1000)])


# Добавление элементов в словарь (в конец)
def add_dct(dct):
    for x in range(1000,2000):
        dct[x] = x**2
    return dct

# Удаление элементов из словаря
def del_dct(dct):
    new_dct = dct.copy()
    for x in range(500, 1500):
        del new_dct[x]
    return new_dct

# Изменение значения
def change_dct(dct):
    new_dct = dct.copy()
    for x in range(100, 500):
        new_dct[x] = x**3
    return new_dct

# def change_dct_2(dct):
#     new_dct = dct.copy()
#     for x in range(100, 500):
#         new_dct.update({x : x**3})
#     return new_dct


# # Вывод значений
def get_dct(dct):
    for key in dct.keys():
        dct.get(key)

def get_rev_dct(dct):
    for key in reversed(dct.keys()):
        dct_ord.get(key)


# Замеры
functions = [
    'add_dct',
    'del_dct',
    'change_dct',
    'get_dct',
    'get_rev_dct'
]

for func in functions:
    # statement_dct = f'{func}(dct)'
    statement_ord = f'{func}(dct_ord)'
    setup_dct = f'from __main__ import {func}, dct'
    setup_ord = f'from __main__ import {func}, dct_ord'
    print(f'{func}(dct)', timeit(f'{func}(dct)', f'from __main__ import {func}, dct', default_timer, 1000))
    print(f'{func}(dct_ord)', timeit(f'{func}(dct_ord)', f'from __main__ import {func}, dct_ord', default_timer, 1000))
    print('')


# Выводы:
# Операции с OrderedDict - занимаются больше времени
 # в более поздних версиях Python - есть смысл использовать OrderedDict в случаях когда важен порядок и для операвтивного переупорядочивания элементов
 # в более поздних версиях Python - в обычном словаре dict - также реализовано хранения ключей по порядку

# add_dct(dct) 0.3210204999195412
# add_dct(dct_ord) 0.3871385999955237   -> больше время
#
# del_dct(dct) 0.09024689998477697
# del_dct(dct_ord) 0.2393227000720799   -> больше время
#
# change_dct(dct) 0.11997260001953691
# change_dct(dct_ord) 0.285895699984394 -> больше время
#
# get_dct(dct) 0.11076429998502135
# get_dct(dct_ord) 0.16740749997552484  -> больше время
#
# get_rev_dct(dct) 0.1263459000037983
# get_rev_dct(dct_ord) 0.15418519999366254  -> больше время


