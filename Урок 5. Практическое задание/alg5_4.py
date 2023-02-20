"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict

my_dict = {}
ordered_dict = OrderedDict()


def func_my_dict():
    for i in range(1, 10000):
        my_dict[i] = i + 5
    return my_dict


def func_ordered_dict():
    for i in range(1, 10000):
        ordered_dict[i] = i + 5
    return ordered_dict


print(timeit("func_my_dict()", globals=globals(), number=1000))
print(timeit("func_ordered_dict()", globals=globals(), number=1000))

# обычный словарь заполняется быстрее
# использование OrderedDict оправдано, если нужны специальные возможности,
# такие как в move_to_end(перенос элемента в начало или в конец словаря) или чтобы указать значимость элементов по порядку
