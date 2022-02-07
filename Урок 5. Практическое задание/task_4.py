"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {x: x**2 + 1 for x in range(5_000)}
my_ord_dict = OrderedDict({x: x**2 + 1 for x in range(5_000)})


def items_dict():
    for k, v in my_dict.items():
        return k, v


def items_ord_dict():
    for k, v in my_ord_dict.items():
        return k, v


def dict_move_to_end():
    items = list(my_dict.items())
    res = {k: v for k, v in reversed(items)}
    return res


def ord_dict_move_to_end():
    for key in sorted(my_ord_dict):
        my_ord_dict.move_to_end(key)


def dict_pop():
    return {k: v for k, v in my_dict.items() if k > 500}


def ord_dict_pop():
    return {k: v for k, v in my_ord_dict.items() if k > 500}


print('По времени выполнения операции items, OrderedDict уступает dict')
print(timeit("items_dict()", globals=globals(), number=1000))
print(timeit("items_ord_dict()", globals=globals(), number=1000))
print('По времени выполнения операции revers, OrderedDict быстрее dict')
print(timeit("dict_move_to_end()", globals=globals(), number=1000))
print(timeit("ord_dict_move_to_end()", globals=globals(), number=1000))
print('По времени выполнения операции (pop c условием) OrderedDict уступает dict')
print(timeit("dict_pop()", globals=globals(), number=1000))
print(timeit("ord_dict_pop()", globals=globals(), number=1000))


"""Python 3.6 представил новую функцию в обычных словарях. Теперь они запоминают порядок вещей. 
С этим дополнением использование OrderedDict теряет смысл. Но OrderedDict так же обладает некоторыми
дополнительными функциями поверх стандартного словаря. Например переупорядочивание 
с помощью метода move_to_end(), OrderedDict быстрее dict. 
В целом у OrderedDict низкая производительность, но высокий
контроль за порядком элементов. Поэтому для реализации определенного алгоритма, нужно учитывать все аспекты."""