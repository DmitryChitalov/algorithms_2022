# from timeit import timeit
from cProfile import run

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    el = sorted([(i, array.count(i)) for i in set(array)], key=lambda t: t[1])[-1]
    return f'Чаще всего встречается число {el[0]}, ' \
           f'оно появилось в массиве {el[1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())

# print(timeit("func_1()", globals=globals(), number=1000))   # 0.0028745000017806888
# print(timeit("func_2()", globals=globals(), number=1000))   # 0.003946799959521741
# print(timeit("func_3()", globals=globals(), number=1000))   # 0.003878000017721206

run('func_1()')
"""
11 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4.py:19(func_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        7    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

run('func_2()')
"""
20 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4.py:31(func_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        7    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
run('func_3()')
"""
14 function calls in 0.000 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4.py:43(func_3)
        4    0.000    0.000    0.000    0.000 task_4.py:44(<lambda>)
        1    0.000    0.000    0.000    0.000 task_4.py:44(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
        4    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

""" Получилось ускорить задачу по сравнению с func_2, но func_1 все таки выполняется быстрее"""