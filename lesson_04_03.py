from timeit import timeit
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

# Обязательно предложите еще свой вариант решения!


def revers_4(num):
    return "".join(reversed(str(num)))

# Сделайте профилировку каждого алгоритма через cProfile и через timeit
# Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
Согласно замерам через timeit, реализации при помощи среза и через reversed работают практически одинаково, быстрее
цикла while и рекурсии
"""


print(f'Замер времени функции revers: {timeit("revers", "from __main__ import revers", number=1000)}')
print(f'Замер времени функции revers_2: {timeit("revers_2", "from __main__ import revers_2", number=1000)}')
print(f'Замер времени функции revers_3: {timeit("revers_3", "from __main__ import revers_3", number=1000)}')
print(f'Замер времени функции revers_4: {timeit("revers_4", "from __main__ import revers_4", number=1000)}')
"""
Замер времени функции revers: 1.2700000000000905e-05
Замер времени функции revers_2: 1.0999999999997123e-05
Замер времени функции revers_3: 1.0899999999997717e-05
Замер времени функции revers_4: 1.0900000000001187e-05
"""

# n = 1234
# print(run('revers(n)'))
# print(run('revers_2(n)'))
# print(run('revers_3(n)'))
# print(run('revers_4(n)'))
"""
         8 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      5/1    0.000    0.000    0.000    0.000 lesson_04_03.py:5(revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


None
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_04_03.py:15(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


None
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_04_03.py:23(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


None
         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_04_03.py:31(revers_4)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}

"""

print(revers_4(1230))