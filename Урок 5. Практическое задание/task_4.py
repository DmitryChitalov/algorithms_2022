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

#-----------------------------------------------------------------------------------------------
# Добавление элементов в словарь (в конец)
def add_dct(dct):
    for x in range(1000,2000):
        dct[x] = x**2
    return dct


# print(timeit('add_dct(dct)', 'from __main__ import add_dct, dct', default_timer, 1000))
# print(timeit('add_dct(dct_ord)', 'from __main__ import add_dct, dct_ord', default_timer, 1000))
#-------------------------------------------------------------------------------------------------

# Удаление элементов из словаря
def del_dct(dct):
    new_dct = dct.copy()
    for x in range(500, 1500):
        del new_dct[x]
    return new_dct


# print('del_dct',timeit('del_dct(dct)', 'from __main__ import del_dct, dct', default_timer, 1000))
# print(timeit('del_dct(dct_ord)', 'from __main__ import del_dct, dct_ord', default_timer, 1000))
#-------------------------------------------------------------------------------------------------

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

# print('change_dct(dct)', timeit('change_dct(dct)', 'from __main__ import change_dct, dct', default_timer, 1000))
#---------------------------------------------------------------------------------------------

# # Вывод значений
def get_dct(dct):
    for key in dct.keys():
        dct.get(key)

def get_rev_dct(dct):
    for key in reversed(dct.keys()):
        dct_ord.get(key)


# print('get_dct', timeit('get_dct(dct)', 'from __main__ import get_dct, dct', default_timer, 1000))
# print('get_dct_ord', timeit('get_dct_ord(dct_ord)', 'from __main__ import get_dct_ord, dct_ord', default_timer, 1000))
#---------------------------------------------------------------------------------------------------------------------------

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



# for func in functions:
#     statement_dct = f'{func}(dct)'
#     statement_ord = f'{func}(dct_ord)'
#     setup_dct = f'from __main__ import {func}, dct'
#     setup_ord = f'from __main__ import {func}, dct_ord'
#     print(statement_dct, timeit(statement_dct, setup_dct, default_timer, 1000))
#     print(statement_ord, timeit(statement_ord, setup_ord, default_timer, 1000))
#     print('')


# dct = {
#     1: 'понедельник',
#     4: 'четверг',
#     2: 'вторник',
#     5: 'пятница',
#     3: 'среда'
# }
#
# dct_ord = OrderedDict([
#     (1, 'понедельник'),
#     (2, 'вторник'),
#     (3, 'среда'),
#     (4, 'четверг'),
#     (5, 'пятница')
# ])
#
#
# print(dct == dct_ord)     # -> словари равны
#
# # добавление элемента в словарь
# dct[6] = 'суббота'
# dct[7] = 'воскресение'
# print(dct)                 # -> вставка в конец
#
#
# dct_ord[6] = 'суббота'
# dct_ord[7] = 'воскресение'
# print(dct_ord)             # -> вставка в конец
#
# print(dct == dct_ord)     # -> словари равны
#
# # удаление элемента словаря
# del dct[7]
# print(dct)
#
# del dct_ord[7]
# print(dct_ord)
#
# print(dct == dct_ord)     # -> словари равны
#
# # изменение значения
# dct[6] = 'saturday'
# dct.update({5 :'friday'})
# print(dct)
#
# dct_ord[5] = 'friday'
# dct_ord[6] = 'saturday'
# print(dct_ord)
#
# print(dct == dct_ord)     # -> словари равны
#
# # вывод значений
# for key, val in dct.items():
#     print (key, val)
#
# for key, val in dct_ord.items():
#     print (key, val)
#
# for key, val in reversed(dct.items()):
#     print (key, val)
#
# for key, val in reversed(dct_ord.items()):
#     print (key, val)
#
# # перемещение элемента
# dct_ord.move_to_end(1, last=True)
# print(dct_ord)
#
# day_1 = dct.pop(1)
# dct[1] = day_1
# print(dct)
#
#
# # удаление элемента и возврат значения
# print(dct.pop(2))
# print(dct)
#
# print(dct_ord.popitem())
# print(dct_ord)
#
# print(dct_ord.popitem(last=False))
# print(dct_ord)
#
# # ВЫВОД:
# # в более поздних версиях Python - есть смысл использовать OrderedDict в случаях когда важен порядок и для операвтивного переупорядочивания элементов