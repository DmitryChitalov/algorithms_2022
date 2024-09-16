"""Числа Фибоначчи"""
from sys import setrecursionlimit
setrecursionlimit(10000)


def fib(n, sum_val):
    if n < 1:
        return sum_val
    return fib(n-1, sum_val+n)


c = 1000
print(fib(c, 0))
