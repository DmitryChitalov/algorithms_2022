"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import default_timer
from collections import OrderedDict

d = {}
od = OrderedDict()
n = 1_000_000


def timer(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        print(f'Function: {func.__name__} Timing - {default_timer() - start}')
        return result

    return wrapper


@timer
def dict_fill(d: dict, n: int):
    for i in range(n):
        d[i] = i


@timer
def ordereddict_fill(od: OrderedDict, n: int):
    for i in range(n):
        od[i] = i


@timer
def dict_change(d: dict, n: int):
    for k, v in d.items():
        d[k] = v
    for i in range(n):
        d.pop(i)


@timer
def ordereddict_change(od: dict, n: int):
    for k, v in od.items():
        od[k] = v
    for i in range(n):
        od.pop(i)


if __name__ == '__main__':
    dict_fill(d, n)
    ordereddict_fill(od, n)
    print("""
    Словарь заполняется быстрее, чем OrderedDict. 
    Это связано с тем, что:
    1. OrderedDict реализован на Python, а обычный словарь на С. Язык C быстрее, чем Python.
    2. OrderedDict разработан для быстрого переупорядочивания элементов, скорость в части заполнения на втором плане.
    """)
    dict_change(d, n)
    ordereddict_change(od, n)
    print("""
    Операций изменения и присваивания в словаре работают быстрее, чем в OrderedDict.
    Начиная с версии 3.6 словарь поддерживает запоминание порядка. Использование OrderedDict оправдано, 
    если нужны специфичные для него функции, например, move_to_end(key, last=True), popitem(last=True).
    """)
