"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
from collections import OrderedDict


# dc = {x: x for x in range(100)}

def append_dc(n ,val):
    for j in range(n):
        val[j] = j

def get_dc(n, val):
    for j in range(n):
         i = val[j]

def pop_dc(n, val):
    for j in range(n):
        val[j] = j
    for j in range(n):
        val.pop(j)




dc = {}
order_dc = OrderedDict()
print('append     dict', timeit('append_dc(100, dc)', globals=globals(), number=10000))
print('append ord_dict', timeit('append_dc(100, order_dc)', globals=globals(), number=10000))

print('get     dict', timeit('get_dc(100, dc)', globals=globals(), number=10000))
print('get ord_dict', timeit('get_dc(100, order_dc)', globals=globals(), number=10000))

print('pop     dict', timeit('pop_dc(100, dc)', globals=globals(), number=10000))
print('pop ord_dict', timeit('pop_dc(100, order_dc)', globals=globals(), number=10000))

'''
Не значительно выигрывает pop у orderdict
'''