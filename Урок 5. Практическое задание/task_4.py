"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from random import randint
from timeit import timeit

# print(help(dict))

n = 10 ** 3
number = 10 ** 4
my_dict_1 = dict()
my_dict_2 = OrderedDict()


time_1 = timeit(stmt='for i in range(n):'
                     'my_dict_1[i] = chr(randint(97, 122))',
                number=number,
                globals=globals())
time_2 = timeit(stmt='for i in range(n):'
                     'my_dict_2[i] = chr(randint(97, 122))',
                number=number,
                globals=globals())
# print(my_dict_1)
# print(my_dict_2)
print(f'1. Присвоение. Ordereddict быстрее в {time_2 / time_1:.7f} раз(а)')


time_1 = timeit(stmt='for i in range(n):'
                     'x = my_dict_1[i]',
                number=number,
                globals=globals())
time_2 = timeit(stmt='for i in range(n):'
                     'x = my_dict_2[i]',
                number=number,
                globals=globals())

print(f'2. Получение dict[key] = . dict быстрее в {time_1 / time_2:.7f} раз(а)')


time_1 = timeit(stmt='for i in range(n):'
                     'x = my_dict_1.get(i)',
                number=number,
                globals=globals())
time_2 = timeit(stmt='for i in range(n):'
                     'x = my_dict_2.get(i)',
                number=number,
                globals=globals())

print(f'3. Получение get. Ordereddict быстрее в {time_2 / time_1:.7f} раз(а)')