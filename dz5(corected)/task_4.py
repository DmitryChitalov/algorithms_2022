"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

dct = {}
dct_Ordered = OrderedDict([('a', 1), ('b', 2), ('c', 3)])


def add_el(dicts):
    a = [i for i in 'abcdefgqwzafdszgxhgcnsafdsghhgj,mvhswafsgzdhxfcjk.lkjtdrrwewrghgjhmnbvxzdsEWretyukhjgf']
    for i in range(50):
        dicts[a[i]] = i
    return dicts


# Замер времени вставки 50 элементов в словарь и в упорядоченный словарь.
print('------------------------------------------------')
print(f"Добавление элементов в dict:\t\t {timeit('add_el(dct)', globals=globals(), number=1000)}")
print(f"Добавление элементов в OrderedDict: {timeit('add_el(dct_Ordered)', globals=globals(), number=1000)}")
print('------------------------------------------------')


def del_el(dicts):
    el = [i for i in 'abcdefgqwzafds']
    for i in range(10):
        dicts.pop(el[i])
    return dicts


# Замер времени удаления 50 элементов из словоря и упорядоченного словаря
print(f"Замер удаления 10 элементов dict:\t\t {timeit('del_el(add_el(dct))', globals=globals(), number=100)}")
print(
    f"Замер удаления 10 элементов dct_Ordered: {timeit('del_el(add_el(dct_Ordered))', globals=globals(), number=100)}")
print('------------------------------------------------')


def receiving_dct(dicts):
    n = 0
    for key, val in dicts.items():
        if n < 50:
            return dicts[key]
        else:
            break


# Получение 50 элементов из словаря и упорядоченного словаря
print(
    f"Замер получения 50 элементов из словоря:"
    f"\t\t\t\t {timeit('receiving_dct(add_el(dct))', globals=globals(), number=1)}")
print(
    f"Замер поллучения 50 элементов из упорядоченного словаря: "
    f"{timeit('receiving_dct(add_el(dct_Ordered))', globals=globals(), number=1)}")

'''
Замеры показали, что операциb по вставке, удалению и взятию элементов из словоря и упорядоченного словоря, 
незначительно быстрее в обычном словаре.
Думаю это связано с тем, что упорядоченный словарь запоминает время вставки в упорядоченный словарь.
'''
