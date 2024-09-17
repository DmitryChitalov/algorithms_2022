import statistics
from random import randint
from timeit import timeit


def find_med(arr):
    return statistics.median(arr)


m = 10
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "find_med(orig_list[:])",
        globals=globals(),
        number=10000))
m = 100
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "find_med(orig_list[:])",
        globals=globals(),
        number=10000))
m = 1000
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "find_med(orig_list[:])",
        globals=globals(),
        number=10000))

"""
Встроенные функции быстрее всех!
0.014824381999999997
0.12093528
2.278384118 - на 10000 измерений
Выигрыши на порядки величин.
"""

