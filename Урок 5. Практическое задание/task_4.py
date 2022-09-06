"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

dict_test = {}
ord_dict_test = OrderedDict()
test_data = [i for i in range(1000000)]


def add_elem(dct, data):
    """
    Заполнение словаря.
    """
    for elem in data:
        dct[elem] = str(elem)


print(timeit("add_elem(dict_test, test_data)", globals=globals(), number=10))  # быстрее
print(timeit("add_elem(ord_dict_test, test_data)", globals=globals(), number=10))


def pop_dct(dct):
    """
    Удаление элементов словаря
    """
    for i in range(10):
        dct.popitem()


print(timeit("pop_dct(dict_test)", globals=globals(), number=1000))  # быстрее
print(timeit("pop_dct(ord_dict_test)", globals=globals(), number=1000))


def dct_value(dct, test_lst=[]):
    """
    Взятие элемента
    """
    for elem in dct.values():
        test_lst.append(elem)


print(timeit("dct_value(dict_test)", globals=globals(), number=100))  # быстрее
print(timeit("dct_value(ord_dict_test)", globals=globals(), number=100))

"""
Вывод: во всех примерах выше словарь показал более быструю скорость выполнения.
В Python 3.6+ OrderedDict имеет смысл как:
a) Указатель на важность порядков элементов словаря
b) Для операций переупорядочивания(согласно документации модуля collections)
+ до питона 3.8 у OrderedDict присутствовал метод __reversed__(), который отсутсвовал у обычного словаря.
"""
