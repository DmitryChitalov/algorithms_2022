"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
import random
from collections import *
from timeit import timeit


dct = {}
o_dct = OrderedDict()

dat = [i for i in range(50)]


def insert_dct(data):
    for i in data:
        dct[i] = i+1


def insert_o_dct(data):
    for i in data:
        o_dct[i] = i+1


def dct_listing():
    for k in dct.keys():
        dct[k] = 'v'


def o_dct_listing():
    for k in o_dct.keys():
        o_dct[k] = 'v'

def dct_moving():
    i = random.choice(list(dct.keys()))
    value = dct[i]
    dct.pop(i)
    dct[i] = value

def o_dct_moving():
    # lst = list(o_dct.keys())
    # print(lst)
    i=random.choice(list(o_dct.keys()))
    #print(i)
    o_dct.move_to_end(i, last=True)


def dct_clear():
    while len(dct) !=0:
        dct.popitem()


def o_dct_clear():
    while len(o_dct) != 0:
        o_dct.popitem()

print("заполнение словаря:")
print(timeit('insert_dct(dat)', globals=globals(), number=1000))
print(timeit('insert_o_dct(dat)', globals=globals(), number=1000))
print("изменение словаря:")
print(timeit('dct_listing()', globals=globals(), number=1000))
print(timeit('o_dct_listing()', globals=globals(), number=1000))
print("перемещение элементов словаря:")
print(timeit('dct_moving()', globals=globals(), number=1000))
print(timeit('o_dct_moving()', globals=globals(), number=1000))
print("очистка словаря:")
print(timeit('dct_clear()', globals=globals(), number=1000))
print(timeit('o_dct_clear()', globals=globals(), number=1000))


"""
 При рассмотрении времени исполнения операций между словарём и упорядоченным
 словарём - преимущество за обычным. 
 На мой взгляд преимущество у ordereddict только в плане перемещения 
 элементов за элегантность написания
"""