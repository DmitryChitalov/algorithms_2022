"""Фибо через рекурсию с мемоизацией через декоратор"""

from timeit import timeit


def memorize(func):
    def wrapper(n_val, memory={}):
        res = memory.get(n_val)
        if res is None:
            res = func(n_val)
            memory[n_val] = res
        return res
    return wrapper


@memorize
def func(n_val):
    if n_val < 2:
        return n_val
    return func(n_val - 1) + func(n_val - 2)


n = 8

print(timeit("func(n)", globals=globals()))

"""0.19176139999999997"""
