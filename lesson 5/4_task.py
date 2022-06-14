"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

std_dict = {}
ord_dict = OrderedDict()


def append_std():
    for i in range(1000):
        std_dict[i] = i


def append_ord():
    for i in range(1000):
        ord_dict[i] = i


def get_std():
    for i in range(1000):
        std_dict.get(i)


def get_ord():
    for i in range(1000):
        ord_dict.get(i)


def pop_std():
    for i in range(1000):
        std_dict.popitem()


def pop_ord():
    for i in range(1000):
        ord_dict.popitem()


print(timeit("append_std()", number=10000, globals=globals()), " - append standard dict")  # 0.682137
print(timeit("append_ord", number=10000, globals=globals()), " - append ordered dict")  # 0.00013639999999992547
print(timeit("get_std()", number=10000, globals=globals()), " - get item standard dict")  # 0.9607574999999999
print(timeit("get_ord()", number=10000, globals=globals()), " - get item ordered dict")  # 0.8019977999999996
print(timeit("pop_std", number=10000, globals=globals()), " - pop item standard dict")  # 0.00018679999999982044
print(timeit("pop_ord", number=10000, globals=globals()), " - pop item ordered dict")  # 0.00016300000000013526

"""
Существенной разницы в скорости выполнения нет, разве что добавление элемента (ord_dict получается в разы быстрее)
Не могу объяснить с чем это связано. Смысла применять OrderDict нет, разве что потребуется функционал метода 
move_to_end или нам надо указать на то, что словарь должен быть упорядочен
"""