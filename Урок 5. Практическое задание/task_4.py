"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict
import time


'''
заполнение словарей
4.622243 dict
5.147885199999999 Orderdict
***************
удаление/изменение элентов словарей
время работы функции deleting_receiving_dict: 3.4810023307800293 dict
время работы функции deleting_receiving_orderdict: 6.34199857711792 Orderdict
 '''



n = 100000
dct = {}
orderdct = OrderedDict()

print('заполнение словарей')

def dict_element(dct, n):
    for i in range(n):
        dct[i] = i
    return dct


def orderdict_element(orderdct, n):
    for i in range(n):
        orderdct[i] = i
    return orderdct

'''заполнение словарей
1.9648250999999999 обычный словарь
2.7753696 Orderdict'''
print(timeit('dict_element(dct, n)', globals=globals(), number=100))
print(timeit('orderdict_element(orderdct, n)', globals=globals(), number=100))
print(15*'*')
print('удаление/изменение элентов словарей')

dict_ = {}
orderdct_2 = OrderedDict()
for i in range(10000000):
    dict_[i] = i
    orderdct_2[i] = i


def completion_element(func):
    def g(*args):
        start = time.time()
        res = func(*args)
        time_res = time.time() - start
        print(f' время работы функции {func.__name__}: {time_res}')
        return res

    return g


@completion_element
def deleting_receiving_dict(dict_):
    for i in range(1500000):
        dict_.pop(i)  # удаление и изменение из словарая происходит быстрее и имеет сложность O(i)
    for j in range(1000001, 2000002):
        dict_[j] = 'hello'
    for k, v in dict_.items():
        dict_[k] = 'world'

deleting_receiving_dict(dict_)


@completion_element
def deleting_receiving_orderdict(orderdct):
    for i in range(1500000):
        orderdct.pop(i)
    for j in range(1000001, 2000002):
        orderdct[j] = 'hello'
    for k, v in orderdct.items():
        orderdct[k] = 'world'


deleting_receiving_orderdict(orderdct_2)

'''удаление/изменение элентов словарей
 время работы функции deleting_receiving_dict: 3.4520087242126465
 время работы функции deleting_receiving_orderdict: 6.37100625038147'''

'''ВЫВОД: начиная с версии Python 3.6 в Orderdict нет необходимости
   либо если использовать отдельные функции например popitem(last=True) или move_to_end('b', last=True)
'''













