from cProfile import run
from sys import setrecursionlimit

setrecursionlimit(10000)


def func_1(n_val):
    if n_val < 2:
        return n_val
    return func_1(n_val - 1) + func_1(n_val - 2)


n = 40
run('func_1(n)')

"""
         331160284 function calls (4 primitive calls) in 72.630 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   72.630   72.630 <string>:1(<module>)
331160281/1   72.630    0.000   72.630   72.630 task_11.py:7(func_1)
        1    0.000    0.000   72.630   72.630 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
