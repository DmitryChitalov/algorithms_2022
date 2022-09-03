"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

print('create :')
print(timeit('default = {x: x ** 2 for x in range(10**5)}', globals=globals(), number=100))
print(timeit('ordered = OrderedDict({x: x ** 2 for x in range(10**5)})', globals=globals(), number=100))


default = {x: x ** 2 for x in range(10**5)}
ordered = OrderedDict({x: x ** 2 for x in range(10**5)})


def dict_get(dict):
    for x in range(10**3):
        dict.get(x)

print('get :')
print(timeit('dict_get(default)', globals=globals(), number=10000))
print(timeit('dict_get(ordered)', globals=globals(), number=10000))


def dict_update(dict):
    for x in range(10**3):
        dict.update(one=1, two=2, three=3)


print('update :')
print(timeit('dict_update(default)', globals=globals(), number=10000))
print(timeit('dict_update(ordered)', globals=globals(), number=10000))


def deftdict_popitem(dict):
    while dict:
        dict.popitem()


print('popitem :')
print(timeit('deftdict_popitem(default)', globals=globals(), number=10000))
print(timeit('deftdict_popitem(ordered)', globals=globals(), number=10000))

"""
В результате замеров, можно обнаружить, что операции получения элемента и удаления элемента (.get() и .popitem() выполняются примерно одинаково по времени.
А операции создания и обновления  выполняются быстрее для стандартного словаря.
Отсюда можно сделать вывод, что в версиях Python старше 3.5 использование OrderedDict необоснованно
"""