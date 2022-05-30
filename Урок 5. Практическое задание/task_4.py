"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

import random

from collections import OrderedDict
from timeit import timeit

my_dict = {random.randint(1, 100): random.randint(1, 100) for i in range(100)}
my_ordered_dict = OrderedDict(my_dict)

print('Добавление элемента')
print(timeit('my_dict[1]=1', 'from __main__ import my_dict', number=1000))
print(timeit('my_ordered_dict[1]=1', 'from __main__ import my_ordered_dict', number=1000))
# примерно одинаково

print('Получение элемента')
print(timeit('my_dict[1]', 'from __main__ import my_dict', number=1000))
print(timeit('my_ordered_dict[1]', 'from __main__ import my_ordered_dict', number=1000))
# примерно одинаково

# похоже, смысла использовать OrderedDict уже нет
