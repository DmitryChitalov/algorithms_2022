# from timeit import timeit
from cProfile import run


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    rest_number, numeral = divmod(enter_num, 10)
    if rest_number == 0:
        return str(numeral)
    else:
        return str(numeral) + str(revers_4(rest_number))


my_num = 2130
# print(revers(my_num))       # None
# print(revers_2(my_num))     # 312.0
# print(revers_3(my_num))     # 0312
# print(revers_4(my_num))     # 0312
# print(timeit("revers(my_num)", globals=globals(), number=1000))    # 0.002451399981509894
# print(timeit("revers_2(my_num)", globals=globals(), number=1000))  # 0.0019189000013284385
# print(timeit("revers_3(my_num)", globals=globals(), number=1000))  # 0.0007659000111743808
# print(timeit("revers_4(my_num)", globals=globals(), number=1000))  # 0.005181999993510544

run('revers(my_num)')
"""
8 function calls (4 primitive calls) in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      5/1    0.000    0.000    0.000    0.000 task_3.py:19(revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

run('revers_2(my_num)')
"""
4 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:29(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

run('revers_3(my_num)')
"""
4 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:37(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

run('revers_4(my_num)')
"""
11 function calls (8 primitive calls) in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      4/1    0.000    0.000    0.000    0.000 task_3.py:43(revers_4)
        4    0.000    0.000    0.000    0.000 {built-in method builtins.divmod}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


"""Даже если не брать в расчет то, что первые два алгоритма не корректно выдают результат, эффективней реализация 
 revers_3, так как:
  - revers_2 -  используется цикл while, он гораздо медленнее чем цикл for;
  - revers_3 - метод str() возвращает строку, нет лишних присваиваний как в revers;
  - revers_4 - вызовы методов потребляют больше ресурсов, чем исполнение обычных операторов.
"""