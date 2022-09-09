from collections import OrderedDict
from timeit import timeit
"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
statements = [
    'dct={i: i for i in range(100000)}',
    'lst = list(dct)',
    """for i in lst:
        dct.pop(i)"""

]
for st in statements:
    print(timeit(globals=globals(), number=1000000))

statements_2 = [
    'dct={i: i for i in range(100000)}'
    'ordered_dct = OrderedDict(dct)',
    'lst = list(ordered_dct)',
    """for key in range(100000):
        ordered_dct.pop(key)"""

]
for st in statements_2:
    print(timeit(globals=globals(), number=1000000))

"""Время создания и удаления (функция pop) больше у OrderedDict"""
#
#
dct = {i: i for i in range(100000)}
ordered_dct = OrderedDict(dct)

def change_dct():
    for key in range(100000):
        dct[key] = '1'

def change_ordered_dct():
    for key in range(100):
        ordered_dct[key] = '1'

print(timeit('change_dct()', globals=globals(), number=100000))
print(timeit('change_ordered_dct()', globals=globals(), number=100000))

"""Время  присвоения значения по ключу также немного больше у OrderedDict"""

"""Начиная с версии Python 3.6 обычный словарь поддерживает запоминание 
порядка добавления пар ключ-значение (также как и OrderedDict), но время выполнения
основных операций немного меньше, чем при использовании OrderedDict. 
Следовательно, логично использовать OrderedDict, когда требуется явно 
обозначить, что нам важен порядок пар ключ-значение или в ситуациях,
когда необходимы функции move_to_end, popitem.
"""