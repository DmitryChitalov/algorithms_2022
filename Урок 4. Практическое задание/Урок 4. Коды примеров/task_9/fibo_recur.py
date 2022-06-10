"""Фибо через рекурсию"""
from timeit import timeit

"""
дерево вызова функции:
1.	2^0 = 1 вызов: f(n)
2.	2^1 = 2 вызова: f(n-1), f(n-2)
3.	2^2 = 4 вызова: f(n-1-1), f(n-1-2), f(n-2-1), f(n-2-2)
4.	2^3 = 8 вызовов: f(n-3), f(n-4), f(n-4), f(n-5), f(n-4), f(n-5), f(n-5), f(n-6)
5.	2^4 = 16 вызовов: f(n-4), f(n-5), f(n-5), f(n-6), f(n-5), f(n-6), f(n-6), f(n-7), f(n-5), f(n-6), f(n-6), f(n-7), f(n-6), f(n-7), f(n-7), f(n-8)
6.	2^5 = 32 вызова: f(n-5), f(n-6), f(n-6), f(n-7), f(n-6), f(n-7), f(n-7), f(n-8), f(n-6), f(n-7), f(n-7), f(n-8), f(n-7), f(n-8), f(n-8), f(n-9), f(n-6), f(n-7), f(n-7), f(n-8), f(n-7), f(n-8), f(n-8), f(n-9), f(n-7), f(n-8), f(n-8), f(n-9), f(n-8), f(n-9), f(n-9), f(n-10)
7.	…
8.	2^k вызовов
9.	…
10.	f(n-m)==f(1), f(n-m)==f(1), ... , f(n-m)==f(1)
"""


def func(n_val):
    if n_val < 2:
        return n_val
    return func(n_val - 1) + func(n_val - 2)


n = 8

print(timeit("func(n)", globals=globals()))

"""8.6776222"""
