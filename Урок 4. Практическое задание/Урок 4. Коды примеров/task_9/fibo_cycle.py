"""Фибо через цикл"""

from timeit import timeit


def func(n_val):
    if n_val < 2:
        return n_val
    pp = 0
    p = 1
    for i in range(n_val-1):
        pp, p = p, pp + p
    return p


n = 8

# print(timeit("func(n)", "from __main__ import func, n"))
# print(timeit.timeit("f(n)", "from __main__ import f")) -> вот так не сработает
print(timeit("func(n)", globals=globals()))


"""
0.6502667
0.653676
"""
