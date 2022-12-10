"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
from collections import OrderedDict

def fill_unordered_dict(unordered_dict):
    for i in key_values:
        unordered_dict[i] = i
    return unordered_dict

def fill_ordered_dict(ordered_dict):
    for i in key_values:
        ordered_dict[i] = i
    return ordered_dict

key_values = [i for i in range(10**5)]
unordered_dict = {}
unordered_dict = fill_unordered_dict(unordered_dict)
ordered_dict = OrderedDict()
ordered_dict = fill_ordered_dict(ordered_dict)

print('Fill')

print(timeit('fill_unordered_dict(unordered_dict)', globals=globals(), number=100))    #0.30882095685228705
print(timeit('fill_ordered_dict(ordered_dict)', globals=globals(), number=100))     #0.45288898702710867

def copy_unordered_dict(unordered_dict):
    test_dict = unordered_dict.copy()

def copy_ordered_dict(ordered_dict):
    test_dict = ordered_dict.copy()

print('Copy')

print(timeit('copy_unordered_dict(unordered_dict)', globals=globals(), number=100))    #0.09294576290994883
print(timeit('copy_ordered_dict(ordered_dict)', globals=globals(), number=100))    #0.8983711539767683 

def pop_from_ud(unordered_dict):
    for i in list(unordered_dict.keys()):
        unordered_dict.pop(i)
    return unordered_dict

def pop_from_od(ordered_dict):
    for i in list(ordered_dict.keys()):
        ordered_dict.pop(i)
    return ordered_dict

print('Pop')

print(timeit('pop_from_ud(unordered_dict)', globals=globals(), number=1000))    #0.07241897494532168
print(timeit('pop_from_od(ordered_dict)', globals=globals(), number=1000))    #0.009877482894808054

# OrderedDict в Python 3.6 и более поздних версиях нет смысла использовать.
# Показели у обычного словаря в основном лучше, чем у упорядоченного.
