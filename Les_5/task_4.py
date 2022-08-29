"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

""""
Заполним dict и ordereddict
0.2003074820004258
0.20586031600032584
поищем по ключу в dict и ordereddict
0.0008408670000790153
0.0007833130002836697

Не вижу никакой разницы в скорости работы.
Имеет смысл использовать упорядоченный словарь,
если нужно перемещать ключи из начала в конец и обратно
или удалять пары ключ-значение в начале или в конце
в остальных случаях заморачиваться с OrderedDict смысла нет
"""

from collections import OrderedDict
from timeit import timeit

dict_dict = {}
order_dict = OrderedDict()


def create_dict():
    for i in range(100):
        dict_dict[i] = i ** 2
    return dict_dict


def create_order_dict():
    for i in range(100):
        order_dict[i] = i ** 2
    return order_dict


dict_dis = create_dict()
dict_ord = create_order_dict()


def find_el_dict(key):
    return dict_dis.get(key)


def find_el_orderdict(key):
    return dict_ord.get(key)


print('Заполним dict и ordereddict')
print(timeit('create_dict()', globals=globals(), number=10000))
print(timeit('create_order_dict()', globals=globals(), number=10000))
print('поищем по ключу в dict и ordereddict')
print(timeit('find_el_dict(100)', globals=globals(), number=10000))
print(timeit('find_el_orderdict(100)', globals=globals(), number=10000))
