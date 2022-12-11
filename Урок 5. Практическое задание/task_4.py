"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
import timeit


dict_1 = {}
order_dict = OrderedDict(dict_1)


def func_dict(dictic):
    for i in range(10):
        dictic[i] = 10 * i

print(f'Заполняем простой словарь = {timeit.timeit("func_dict(dict_1)", globals=globals(), number=1000)}')
print(f'Заполняем упорядоченный словарь = {timeit.timeit("func_dict(order_dict)", globals=globals(), number=1000)}')
# Исходя из полученных результатов, я считаю, что OrderedDict в версиях Python 3.6 и позднее вообще не нужен.
# За исключением тех ситуаций, где мне необходимо явно указать о том, что мой словарь - упорядочен.