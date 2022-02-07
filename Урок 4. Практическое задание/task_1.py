"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
import random
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, num in enumerate(nums) if num % 2 == 0]


def func_3(nums):
    return {i for i, num in enumerate(nums) if num % 2 == 0}


def func_4(nums):
    return (i for i, num in enumerate(nums) if num % 2 == 0)


array = [random.randint(1, 100) for _ in range(50)]
# запуск функций и вывод результатов (массив из 50 эл-тов, запусков 10000)
[print(f"func_{i}: (индексы четных первых 10 эл-тов ) {eval(f'func_1(array[:10])')}") for i in range(1, 5)]
# профилировка каждого алгоритма через timeit
times = [timeit(f"func_{n}(array)", f"from __main__ import func_{n}, array", number=10000) for n in range(1, 5)]
t_otn = [t / min(times) for t in times]
[print(f'func_{i + 1}:{t:8.3f}') for i, t in enumerate(t_otn)]

'''
На малом количестве элементов массива кузультаты ~ такие (величины относительно лучшего результата):
func_1:  10.858
func_2:   9.364
func_3:   9.736
func_4:   1.000
1 место - func_4: generator на порядок лучше
2,3 место - func_2: LC (list comprehension) и func_2: SC (set comprehension)
4 место - func_1: чуть хуже 2 и 3 из-за, предположительно 'new_arr.append(i)'
'''

array = [random.randint(1, 100) for _ in range(10000)]
# запуск функций и вывод результатов (массив из 10000 эл-тов, запусков 100)
[print(f"func_{i}: (индексы четных первых 10 эл-тов ) {eval(f'func_1(array[:10])')}") for i in range(1, 5)]
# профилировка каждого алгоритма через timeit
times = [timeit(f"func_{n}(array)", f"from __main__ import func_{n}, array", number=100) for n in range(1, 5)]
t_otn = [t / min(times) for t in times]
[print(f'func_{i + 1}:{t:8.3f}') for i, t in enumerate(t_otn)]

'''
На большом количестве элементов массива (10000) результаты ~ такие (величины относительно лучшего результата):
func_1:2044.332
func_2:1732.078
func_3:2700.931
func_4:   1.000
1 место - func_4: GE (generator expression) на уже на 3 порядка лучше
2 место - func_2: LC (list comprehension) увеличивает отрыв
3 место - func_1: посередине между 2 и 4
4 место - func3: SC (set comprehension) показал уже самые худшие рез-ты'

С дальнейшим ростом входного массива (100000) опережение GE ~20000, т.е GE имеет сложность O(1)
Мы не знаем, как дальше воспользуемся результатами, но если просто перебирать входной массив - то только GE
'''