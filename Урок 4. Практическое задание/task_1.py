"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from time import perf_counter


def decorator_func(func):
    def wrapper(*args):
        start = perf_counter()
        result = func(*args)
        end = perf_counter()
        print(f'Время выполнения: {end - start}')
        return result

    return wrapper


@decorator_func
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# использование comprehensions уменьшает время работы
@decorator_func
def func_2(nums):
    new_arr = []
    [new_arr.append(i) for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


nums_mass = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(func_1(nums_mass))  # ->Время выполнения: 6.300047971308231e-06 [0, 2, 4, 6, 8]
print(func_2(nums_mass))  # ->Время выполнения: 4.500034265220165e-06 [0, 2, 4, 6, 8]
