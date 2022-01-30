import cProfile
import time


def fast():
    print("Я быстрая функция")


def slow():
    time.sleep(3)
    print("Я очень медленная функция")


def medium():
    time.sleep(0.5)
    print("Я средняя функция...")


def main():
    fast()
    slow()
    medium()


cProfile.run('main()')

"""
Я быстрая функция
Я очень медленная функция
Я средняя функция...
         12 function calls in 3.500 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.500    3.500 <string>:1(<module>)
        1    0.000    0.000    0.500    0.500 task_14.py:14(medium)
        1    0.000    0.000    3.500    3.500 task_14.py:19(main)
        1    0.000    0.000    0.000    0.000 task_14.py:5(fast)
        1    0.000    0.000    3.000    3.000 task_14.py:9(slow)
        1    0.000    0.000    3.500    3.500 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        2    3.500    1.750    3.500    1.750 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
