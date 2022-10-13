"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

dict_ = {}
o_dict = OrderedDict()

print('*** Добавление элементов в словари: dict vs OrderedDict ***')
print(timeit('for i in range(1000): dict_[i] = i', globals=globals(), number=10000))
print(timeit('for i in range(1000): o_dict[i] = i', globals=globals(), number=10000))

print('*** Получение значений элементов словарей: dict vs OrderedDict ***')
print(timeit('for k in dict_: dict_.get(k)', globals=globals(), number=10000))
print(timeit('for k in o_dict: o_dict.get(k)', globals=globals(), number=10000))

print('*** Перебор словаря по значениям: dict vs OrderedDict ***')
print(timeit('for v in dict_: dict_.values()', globals=globals(), number=10000))
print(timeit('for v in o_dict: o_dict.values()', globals=globals(), number=10000))

"""
Похоже, что преимущества OrderedDict заключены в его методах, которых нет в обычных 
словарях (move_to_end и popitem).
"""