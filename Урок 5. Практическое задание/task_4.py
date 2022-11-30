"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


def create_dict(n=100):
    return {el: el for el in range(n)}


def create_orderdict(n=100):
    return OrderedDict((el, el) for el in range(n))


def dict_func(data, n=50):
    for i in range(n):
        data.pop(i)
    for i in range(n):
        data[i] = 1
    return data


if __name__ == '__main__':
    my_dict = create_dict()
    my_orderdict = create_orderdict()

    print(timeit('dict_func(my_dict)', number=10000, globals=globals()))
    print(timeit('dict_func(my_orderdict)', number=10000, globals=globals()))

"""
Обычный словарь работает быстрее чем orderdict. 
orderdict есть смысл использовать, если нужны такие операции как move_to_end и popitem, 
или если необходимо проверить эквивалентность словарей.
"""