"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {}
ord_dict = OrderedDict()

print('_____________________ Добавление элементов в словари: dict vs OrderedDict')
print(timeit('for i in range(1000): my_dict[i] = i', globals=globals(), number=10000))
print(timeit('for i in range(1000): ord_dict[i] = i', globals=globals(), number=10000))
# Стандартный метод впереди.
print('_____________________ Получение значений элементов словарей: dict vs OrderedDict')
print(timeit('for k in my_dict: my_dict.get(k)', globals=globals(), number=10000))
print(timeit('for k in ord_dict: ord_dict.get(k)', globals=globals(), number=10000))
# Стандартный метод впереди.
print('_____________________ Перебор словаря по значениям: dict vs OrderedDict')
print(timeit('for v in my_dict: my_dict.values()', globals=globals(), number=10000))
print(timeit('for v in ord_dict: ord_dict.values()', globals=globals(), number=10000))
# Стандартный метод впереди.
"""
По всей видимости, преимущества OrderedDict на сегодняшний день (после Python 3.6) 
заключены исключительно в его специфических особенностях, которых нет в обычных 
словарях (типа, move_to_end() и popitem()).
"""