"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums: int):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums: int):
    new_arr = []
    for i, j in enumerate(nums):
        if i % 2 == 0:
            new_arr.append(j)
    return new_arr


def func_3(nums: int):
    return [i for i, j in enumerate(nums) if i % 2 == 0]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

time_1 = timeit('func_1(arr)', globals=globals(), number=1000)
print(f"Время выполнения func_1: {time_1} секунд")

# Замер времени для func_2
time_2 = timeit('func_2(arr)', globals=globals(), number=1000)
print(f"Время выполнения func_2: {time_2} секунд")

# Замер времени для func_3
time_3 = timeit('func_3(arr)', globals=globals(), number=1000)
print(f"Время выполнения func_3: {time_3} секунд")

# Аналитика
"""
1) func_1(nums) — перебирает все элементы массива и добавляет индексы четных
 чисел в новый массив.
 
2) func_2(nums) — enumerate, который оптимизирует процесс перебора списка, предоставляя и индекс, и значение,
а так же ускоряя процесс.

3) func_3(nums) — оптимизированная версия, которая использует list comprehension вместе с enumerate, 
 для получения индексов с четными значениями значительно ускоряет выполнение.
"""
