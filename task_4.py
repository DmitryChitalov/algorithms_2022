from collections import OrderedDict
from timeit import timeit

dict_1 = {}
dict_2 = OrderedDict()


def append_1():
    for i in range(1000):
        dict_1[i] = i


def append_2():
    for i in range(1000):
        dict_2[i] = i


def get_1():
    for i in range(1000):
        dict_1.get(i)


def get_2():
    for i in range(1000):
        dict_2.get(i)


def pop_1():
    for i in range(1000):
        dict_1.popitem()


def pop_2():
    for i in range(1000):
        dict_2.popitem()


print(timeit("append_1", globals=globals()))
print(timeit("append_2", globals=globals()))
print(timeit("get_1", globals=globals()))
print(timeit("get_2", globals=globals()))
print(timeit("pop_1", globals=globals()))
print(timeit("pop_2", globals=globals()))

"""
append_1:   0.019396400000000008
append_2:   0.022157700000000002
get_1:      0.019240499999999994
get_2:      0.01905670000000001
pop_1:      0.02259649999999999
pop_2:      0.02592810000000001
Существенной разницы в скорости нет. Соответственно и применять OrderDict тоже не вижу смысла!
"""