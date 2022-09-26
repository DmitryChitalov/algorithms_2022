"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict

my_dict_1 = {i: i for i in range(1, 101)}
my_dict_2 = OrderedDict({i: i for i in range(1, 101)})


def my_def_1(my_dict_1):
    for i in my_dict_1:
        my_dict_1.get(i)


def my_def_2(my_dict_2):
    for i in my_dict_2:
        my_dict_2.get(i)


def my_def_3(my_dict_1):
    for i in range(len(my_dict_1)):
        my_dict_1.popitem()
    return my_dict_1

def my_def_4(my_dict_2):
    for i in range(len(my_dict_2)):
        my_dict_2.popitem()
    return my_dict_2

print(timeit("my_def_1(my_dict_1)", globals=globals(), number=1000))
print(timeit("my_def_2(my_dict_2)", globals=globals(), number=1000))
print(timeit("my_def_3(my_dict_1)", globals=globals(), number=1000))
print(timeit("my_def_4(my_dict_2)", globals=globals(), number=1000))

"""
Смысла использования "OrderedDict" т.к. результаты тестов либо одинаковые, либо отличаются незначительно.


Первый вариант
0.003839900000457419
Второй вариант
0.004587600000377279
Третий вариант
0.00017460000162827782
Четвертый вариант
0.0001754000004439149


"""