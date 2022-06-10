from cProfile import run

n = 100000


def func_3(n):
    if n < 2:
        return n
    pp = 0
    p = 1
    for i in range(n-1):
        pp, p = p, pp + p

    def func_4(n):
        if n < 2:
            return n
        pp = 0
        p = 1
        for i in range(n - 1):
            pp, p = p, pp + p

    func_4(n)
    return p


run('func_3(n)')


"""
         5 function calls in 0.250 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.250    0.250 <string>:1(<module>)
        1    0.126    0.126    0.126    0.126 task_13.py:14(func_4)
        1    0.123    0.123    0.250    0.250 task_13.py:6(func_3)
        1    0.000    0.000    0.250    0.250 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""