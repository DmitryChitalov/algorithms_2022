"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
from random import randrange
from collections import OrderedDict

dict_noord = dict()
dict_ord = OrderedDict()

def dict_fill(size):
    dict_noord.clear()
    dict_ord.clear()
    for i in range(size):
        k = randrange(10**6)
        v = randrange(10**6)
        dict_noord[k] = v
        dict_ord[k] = v

def noord_pop():        
    dict_noord.pop(list(dict_noord.keys())[index])

def ord_pop():        
    dict_ord.pop(list(dict_ord.keys())[index])
    
def noord_popitem():        
    dict_noord.popitem()

def ord_popitem():        
    dict_ord.popitem()
    
def ord_popitem_first():        
    dict_ord.popitem(last=False)
    
dict_fill(10**5)
index = 100
for func_name in (
    'noord_pop()', 'ord_pop()'
):
    print(f'{func_name}: время = {timeit(func_name, globals=globals(), number=10**2)}')

dict_fill(10**6)
for func_name in (
    'noord_popitem()', 'ord_popitem()', 'ord_popitem_first()'
):
    print(f'{func_name}: время = {timeit(func_name, globals=globals(), number=10**5)}')
    
'''
Извлечение элемента по номеру в OrderedDict выполняется в разы медленнее.
Время извлечения последнего элемента примерно одинаковое.
Для таких операций использование OrderedDict нецелесообразно.
Зато OrderedDict может так же быстро выполнить извлечение первого элемента.
'''    
    