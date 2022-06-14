"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

n = 1000
smp_dict = {}
ord_dict = OrderedDict()


def complete_smp_dict(num):
    for i in range(n):
        smp_dict[i] = i


def complete_ord_dict(num):
    for i in range(n):
        ord_dict[i] = i


print(len(smp_dict), len(ord_dict))
print(f'Время выполнения функции complete_smp_dict = {timeit("complete_smp_dict(n)", globals=globals(), number=1000)}')
print(f'Время выполнения функции complete_ord_dict = {timeit("complete_ord_dict(n)", globals=globals(), number=1000)}')
print(len(smp_dict), len(ord_dict))


# Время выполнения функции complete_smp_dict = 0.17909909999999998
# Время выполнения функции complete_ord_dict = 0.22877139999999996


def redesign_smp_dict(num):
    for i in range(n):
        smp_dict[i] = i ** 2


def redesign_ord_dict(num):
    for i in range(n):
        ord_dict[i] = i ** 2


print(f'Время выполнения функции redesign_smp_dict = {timeit("redesign_smp_dict(n)", globals=globals(), number=1000)}')
print(f'Время выполнения функции redesign_ord_dict = {timeit("redesign_ord_dict(n)", globals=globals(), number=1000)}')
print(len(smp_dict), len(ord_dict))


# Время выполнения функции redesign_smp_dict = 0.45360710000000004
# Время выполнения функции redesign_ord_dict = 0.5401092000000001


def pop_smp_dict():
    for i in range(len(smp_dict)):
        smp_dict.pop(i)


def pop_ord_dict():
    for i in range(len(ord_dict)):
        ord_dict.pop(i)


print(f'Время выполнения функции pop_smp_dict = {timeit("pop_smp_dict()", globals=globals(), number=1000)}')
print(f'Время выполнения функции pop_ord_dict = {timeit("pop_ord_dict()", globals=globals(), number=1000)}')
print(len(smp_dict), len(ord_dict))

# Время выполнения функции pop_smp_dict = 0.0008459999999999024
# Время выполнения функции pop_ord_dict = 0.0011996000000000784
# 0 0

# При работе в Python с версией выше 3.6 нет смысла использовать сторонний модуль OrderedDict, так как всторенный
# словарь работает заметно быстрее.