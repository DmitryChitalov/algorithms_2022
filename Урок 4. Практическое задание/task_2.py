"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение мемоизацией
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!

П.С. задание не такое простое, как кажется


Листинги работы программы приведены после кода.

Анализ:
при единичном вызове функции мемоизация не нужна,
Мемоизация нужна в том случае, когда в функцию передается один и тот же аргумент несколько раз,
в этом случае функция один раз рассчитает результат,
в остальных случаях для данного аргумента вынет значение функции из кэша.
При единичном запуске функции для данной функции  передается каждый раз разный аргумент :
число без одного знака,
без 2-х знакков,
без 3-х знаков итп
то есть код не использует значения записанные в cache

При использовании Timeit за счет параметра number=10000
функция вызывается несколько раз и начинает читать значения из cache (print at lines 81, 85 )

При Timeit ...  number=4 (lines 110...114) listing использования cache  приведен в строках 167....180,
где видно что функция читает из cache.
"""

from timeit import timeit
from random import randint
from cProfile import run


def recursive_reverse(number):
    # print(number)
    if number == 0:
        s1 = str(number % 10)
        # print (f'str(number % 10) = {s1}')
        return ""
    s1 = str(number % 10)
    s2 = recursive_reverse(number // 10)
    # print (f'return {s1}  {s2}')
    return f'{s1}{s2}'


# num_100 = randint(10000, 1000000)
num_100 = 123456
# num_1000 = randint(1000000, 10000000)
num_1000 = 12345678
# num_10000 = randint(100000000, 10000000000000)
num_10000 = 123456789


print('Не оптимизированная функция recursive_reverse')
run('recursive_reverse(num_10000)')
# print(
#     timeit(
#         "recursive_reverse(num_100)",
#         setup='from __main__ import recursive_reverse, num_100',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_1000)",
#         setup='from __main__ import recursive_reverse, num_1000',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_10000)",
#         setup='from __main__ import recursive_reverse, num_10000',
#         number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            print(f' get from cache  ')
            return cache[args]
        else:
            cache[args] = f(*args)
            print(f'put to cache')
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    # print(f'number = {number}')
    if number == 0:
        return ''
    s1 = str(number % 10)
    s2 = recursive_reverse_mem(number // 10)
    # print (f'return {s1}  {s2}')
    return f'{s1}{s2}'


print('Оптимизированная функция recursive_reverse_mem')
# run('recursive_reverse_mem(num_10000)')
# print(
#     timeit(
#         'recursive_reverse_mem(num_100)',
#         setup='from __main__ import recursive_reverse_mem, num_100',
#         number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=4))
# print(
#     timeit(
#         'recursive_reverse_mem(num_10000)',
#         setup='from __main__ import recursive_reverse_mem, num_10000',
#         number=10000))

# Analitycs  timeit and cProfile:
# Не оптимизированная функция recursive_reverse
#          13 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10/1    0.000    0.000    0.000    0.000 task_2.py:20(recursive_reverse)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# 0.014356899999999999
# 0.018341700000000002
# 0.020870100000000003
# Оптимизированная функция recursive_reverse_mem
#          23 function calls (5 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10/1    0.000    0.000    0.000    0.000 task_2.py:61(decorate)
#      10/1    0.000    0.000    0.000    0.000 task_2.py:72(recursive_reverse_mem)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# 0.0011160000000000059
# 0.0011217000000000033
# 0.0010803000000000063
#
# Process finished with exit code 0
#
# Analitics use cache :
# Не оптимизированная функция recursive_reverse
#          13 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10/1    0.000    0.000    0.000    0.000 task_2.py:38(recursive_reverse)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# Оптимизированная функция recursive_reverse_mem
# put to cache
# put to cache
# put to cache
# put to cache
# put to cache
# put to cache
# put to cache
# put to cache
# put to cache
#  get from cache
#  get from cache
#  get from cache
# 4.9399999999998057e-05
#
# Process finished with exit code 0
